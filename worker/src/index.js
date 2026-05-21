/**
 * Aeon — Telegram → GitHub Actions webhook.
 *
 * Receives Telegram webhook updates and fires a `repository_dispatch`
 * event so the Messages workflow (.github/workflows/messages.yml) runs
 * in ~1s instead of waiting up to 5 minutes for the cron poller.
 *
 * Secrets (set with `wrangler secret put <NAME>`):
 *   TELEGRAM_BOT_TOKEN       bot token from @BotFather
 *   TELEGRAM_CHAT_ID         the chat allowed to trigger runs
 *   GITHUB_REPO              "owner/repo"
 *   GITHUB_TOKEN             GitHub PAT with `repo` scope
 *   TELEGRAM_WEBHOOK_SECRET  (optional) shared secret passed to setWebhook
 */

const GITHUB_API = "https://api.github.com";
const TELEGRAM_API = "https://api.telegram.org";

export default {
  async fetch(request, env) {
    if (request.method !== "POST") {
      return new Response("method not allowed", { status: 405 });
    }

    // If a webhook secret is configured, reject updates that don't carry it.
    // Telegram echoes the secret in this header when setWebhook was called
    // with `secret_token`. This stops anyone from POSTing fake updates.
    if (
      env.TELEGRAM_WEBHOOK_SECRET &&
      request.headers.get("X-Telegram-Bot-Api-Secret-Token") !==
        env.TELEGRAM_WEBHOOK_SECRET
    ) {
      return new Response("forbidden", { status: 403 });
    }

    let update;
    try {
      update = await request.json();
    } catch {
      return new Response("bad request", { status: 400 });
    }

    // Telegram sends an Update object: { update_id, message }.
    // `update_id` lives at the top level, NOT inside `message`.
    const { update_id, message } = update;
    if (!message?.text || String(message.chat?.id) !== env.TELEGRAM_CHAT_ID) {
      return new Response("ignored");
    }

    // Advance the polling offset so the 5-min poller doesn't reprocess this.
    await fetch(
      `${TELEGRAM_API}/bot${env.TELEGRAM_BOT_TOKEN}/getUpdates?offset=${
        update_id + 1
      }`,
    );

    // Trigger the Messages workflow immediately.
    const dispatch = await fetch(
      `${GITHUB_API}/repos/${env.GITHUB_REPO}/dispatches`,
      {
        method: "POST",
        headers: {
          Authorization: `Bearer ${env.GITHUB_TOKEN}`,
          Accept: "application/vnd.github+json",
          "X-GitHub-Api-Version": "2022-11-28",
          "User-Agent": "aeon-telegram-webhook",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          event_type: "telegram-message",
          client_payload: { message: message.text },
        }),
      },
    );

    if (!dispatch.ok) {
      const detail = await dispatch.text();
      console.error(`github dispatch failed: ${dispatch.status} ${detail}`);
      return new Response(`dispatch failed: ${dispatch.status}`, {
        status: 502,
      });
    }

    return new Response("ok");
  },
};
