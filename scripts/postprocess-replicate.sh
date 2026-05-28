#!/usr/bin/env bash
# Post-process Replicate API requests left by Claude (sandbox blocks outbound curl).
# Reads .pending-replicate/*.json, makes the API call, downloads the image.
set -euo pipefail

PENDING_DIR=".pending-replicate"

if [ ! -d "$PENDING_DIR" ] || [ -z "$(ls -A "$PENDING_DIR"/*.json 2>/dev/null)" ]; then
  echo "replicate-postprocess: no pending requests"
  exit 0
fi

if [ -z "${REPLICATE_API_TOKEN:-}" ]; then
  echo "replicate-postprocess: REPLICATE_API_TOKEN not set, skipping"
  exit 0
fi

for req_file in "$PENDING_DIR"/*.json; do
  [ -f "$req_file" ] || continue
  echo "replicate-postprocess: processing $(basename "$req_file")..."

  # Accept both flat and nested {input: {...}} shapes. The skill spec defines flat
  # as canonical, but Claude sometimes mirrors the curl example into pending files.
  PROMPT=$(jq -r '.prompt // .input.prompt // empty' "$req_file")
  ASPECT=$(jq -r '.aspect_ratio // .input.aspect_ratio // "16:9"' "$req_file")
  OUTPUT_PATH=$(jq -r '.output_path // empty' "$req_file")
  MODEL=$(jq -r '.model // "google/nano-banana-pro"' "$req_file")

  if [ -z "$PROMPT" ] || [ -z "$OUTPUT_PATH" ]; then
    echo "replicate-postprocess: invalid request for $(basename "$req_file") — prompt=$([ -n "$PROMPT" ] && echo set || echo MISSING) output_path=$([ -n "$OUTPUT_PATH" ] && echo "$OUTPUT_PATH" || echo MISSING)"
    echo "replicate-postprocess: pending file keys: $(jq -r 'keys | join(",")' "$req_file")"
    continue
  fi

  # Capture both stdout (body) and HTTP status so we can log the actual API error
  # instead of swallowing it. Replace -sf (silent-fail) with -s + manual status check.
  call_replicate() {
    local body="$1"
    curl -s --max-time 60 -X POST \
      -w '\n__HTTP_STATUS__:%{http_code}' \
      -H "Authorization: Bearer $REPLICATE_API_TOKEN" \
      -H "Content-Type: application/json" \
      -H "Prefer: wait" \
      -d "$body" \
      "https://api.replicate.com/v1/models/${MODEL}/predictions"
  }

  REQ_BODY=$(jq -n --arg prompt "$PROMPT" --arg aspect "$ASPECT" \
    '{input: {prompt: $prompt, aspect_ratio: $aspect, number_of_images: 1, safety_tolerance: 5}}')

  RAW=$(call_replicate "$REQ_BODY") || RAW="${RAW}__HTTP_STATUS__:CURL_ERR"
  HTTP=$(printf '%s' "$RAW" | sed -n 's/.*__HTTP_STATUS__:\([^[:space:]]*\).*/\1/p' | tail -1)
  RESPONSE=$(printf '%s' "$RAW" | sed 's/__HTTP_STATUS__:.*//')

  if [ "$HTTP" != "200" ] && [ "$HTTP" != "201" ]; then
    echo "replicate-postprocess: API call failed for $(basename "$req_file") (HTTP $HTTP)"
    echo "replicate-postprocess: response body: $(printf '%s' "$RESPONSE" | jq -c '.' 2>/dev/null || printf '%s' "$RESPONSE" | head -c 500)"

    echo "replicate-postprocess: retrying with allow_fallback_model..."
    REQ_BODY=$(jq -n --arg prompt "$PROMPT" --arg aspect "$ASPECT" \
      '{input: {prompt: $prompt, aspect_ratio: $aspect, number_of_images: 1, safety_tolerance: 5, allow_fallback_model: true}}')
    RAW=$(call_replicate "$REQ_BODY") || RAW="${RAW}__HTTP_STATUS__:CURL_ERR"
    HTTP=$(printf '%s' "$RAW" | sed -n 's/.*__HTTP_STATUS__:\([^[:space:]]*\).*/\1/p' | tail -1)
    RESPONSE=$(printf '%s' "$RAW" | sed 's/__HTTP_STATUS__:.*//')

    if [ "$HTTP" != "200" ] && [ "$HTTP" != "201" ]; then
      echo "replicate-postprocess: retry failed (HTTP $HTTP)"
      echo "replicate-postprocess: response body: $(printf '%s' "$RESPONSE" | jq -c '.' 2>/dev/null || printf '%s' "$RESPONSE" | head -c 500)"
      continue
    fi
  fi

  # Extract image URL from response
  IMAGE_URL=$(echo "$RESPONSE" | jq -r '.output // empty | if type == "array" then .[0] else . end // empty')

  if [ -z "$IMAGE_URL" ]; then
    # Check if prediction is still processing (no "Prefer: wait" support)
    PRED_URL=$(echo "$RESPONSE" | jq -r '.urls.get // empty')
    if [ -n "$PRED_URL" ]; then
      echo "replicate-postprocess: polling for result..."
      for i in $(seq 1 12); do
        sleep 5
        POLL=$(curl -sf -H "Authorization: Bearer $REPLICATE_API_TOKEN" "$PRED_URL" 2>&1) || continue
        STATUS=$(echo "$POLL" | jq -r '.status // empty')
        if [ "$STATUS" = "succeeded" ]; then
          IMAGE_URL=$(echo "$POLL" | jq -r '.output // empty | if type == "array" then .[0] else . end // empty')
          break
        elif [ "$STATUS" = "failed" ] || [ "$STATUS" = "canceled" ]; then
          echo "replicate-postprocess: prediction $STATUS"
          break
        fi
      done
    fi
  fi

  if [ -z "$IMAGE_URL" ]; then
    echo "replicate-postprocess: no image URL in response, skipping"
    continue
  fi

  # Download the image
  mkdir -p "$(dirname "$OUTPUT_PATH")"
  if curl -sfL --max-time 30 "$IMAGE_URL" -o "$OUTPUT_PATH"; then
    echo "replicate-postprocess: saved $OUTPUT_PATH ($(wc -c < "$OUTPUT_PATH") bytes)"
    # Write a marker so Claude's skill output can reference the path
    echo "$OUTPUT_PATH" > "$PENDING_DIR/$(basename "$req_file" .json).done"
  else
    echo "replicate-postprocess: failed to download image from $IMAGE_URL"
  fi
done

echo "replicate-postprocess: done"
