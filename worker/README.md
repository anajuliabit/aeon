# Aeon Telegram Webhook (Cloudflare Worker)

Turns Telegram messages into instant Aeon runs. Without this, the
`messages.yml` workflow polls every 5 minutes. With it, a message
triggers a `repository_dispatch` and Aeon responds in ~1 second.

## How it works

```
Telegram message
  → Cloudflare Worker (this)
    → GitHub repository_dispatch (event_type: telegram-message)
      → .github/workflows/messages.yml runs immediately
```

The Worker also advances the bot's `getUpdates` offset so the 5-minute
poller doesn't reprocess the same message.

## Deploy

```bash
cd worker
npm install
npx wrangler login        # one-time, opens browser
npx wrangler deploy       # prints the *.workers.dev URL
```

## Set secrets

Run once each (Wrangler prompts for the value):

```bash
npx wrangler secret put TELEGRAM_BOT_TOKEN       # from @BotFather
npx wrangler secret put TELEGRAM_CHAT_ID         # your chat ID
npx wrangler secret put GITHUB_REPO              # owner/repo, e.g. aaronjmars/aeon
npx wrangler secret put GITHUB_TOKEN             # GitHub PAT with `repo` scope
npx wrangler secret put TELEGRAM_WEBHOOK_SECRET  # optional — see below
```

## Register the webhook

Point your bot at the deployed Worker URL. If you set
`TELEGRAM_WEBHOOK_SECRET`, pass the same value as `secret_token` so the
Worker can reject forged requests:

```bash
curl "https://api.telegram.org/bot<BOT_TOKEN>/setWebhook" \
  --data-urlencode "url=https://aeon-telegram-webhook.<subdomain>.workers.dev" \
  --data-urlencode "secret_token=<TELEGRAM_WEBHOOK_SECRET>"
```

Verify it stuck:

```bash
curl "https://api.telegram.org/bot<BOT_TOKEN>/getWebhookInfo"
```

Send your bot a message — a run should appear in the Actions tab within
a second or two.

## Local dev

```bash
npx wrangler dev   # runs the Worker locally; needs secrets in .dev.vars
```

`.dev.vars` (gitignored) holds local secrets as `KEY=value` lines.

## Notes

- Only messages from `TELEGRAM_CHAT_ID` are dispatched; everything else
  returns `ignored`.
- A non-OK GitHub dispatch returns HTTP 502 so Telegram retries the
  webhook.
