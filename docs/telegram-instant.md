# Telegram Instant Mode

Default polling checks for messages every 5 minutes. For ~1s response
time, deploy the Cloudflare Worker in [`worker/`](../worker/) as a
Telegram webhook.

## What it does

```
Telegram message
  → Cloudflare Worker (worker/src/index.js)
    → GitHub repository_dispatch (event_type: telegram-message)
      → .github/workflows/messages.yml runs immediately
```

The Worker also advances the bot's `getUpdates` offset so the 5-minute
poller doesn't reprocess the same message.

## Setup

The Worker is a Wrangler project. Full instructions are in
[`worker/README.md`](../worker/README.md). In short:

```bash
cd worker
npm install
npx wrangler login
npx wrangler deploy
```

Then set the secrets and register the webhook (see `worker/README.md`):

- `TELEGRAM_BOT_TOKEN` — bot token from @BotFather
- `TELEGRAM_CHAT_ID` — your chat ID
- `GITHUB_REPO` — `owner/repo` format (e.g. `aaronjmars/aeon`)
- `GITHUB_TOKEN` — a GitHub PAT with `repo` scope
- `TELEGRAM_WEBHOOK_SECRET` — optional shared secret to reject forged requests

Messages now arrive in ~1 second instead of up to 5 minutes.
