# Zentik Notifier

<p align="center">
  <img src="https://raw.githubusercontent.com/Zentik-notifier/zentik-notifier/main/docs/static/logos/brand-logo.png" alt="Zentik" width="200" />
</p>

**Zentik** is a notification hub: one place to receive alerts from all your systems and send them to your devices with rich push. Custom actions, attachments, buckets, webhooks, and a bunch of integrations — self-host it or use the hosted app.

---

## What is it?

- **Mobile-first** — Especially iOS: rich notifications, multiple attachments, custom actions (snooze, postpone, mark read, open URL, webhooks…).
- **Flexible** — Send from anything: webhooks, APIs, integrations. Use buckets and tokens to route messages. Transform payloads with parsers and templates.
- **Self-hostable** — Run the backend (and optionally the frontend) on your infra; apps can talk to your instance or to the main Zentik server via passthrough.

---

## Quick links

| Section | Description |
|--------|-------------|
| [**Docs**](https://notifier-docs.zentik.app/) | Full documentation (intro, buckets, notifications, self-hosted) |
| [**First steps**](https://notifier-docs.zentik.app/docs/intro#first-steps) | Register, create a bucket, send your first notification |
| [**Buckets**](https://notifier-docs.zentik.app/docs/notifications/buckets/creation) | Create buckets, tokens, and magic codes |
| [**Webhooks**](https://notifier-docs.zentik.app/docs/webhooks) | Send notifications via HTTP |
| [**Self-hosted**](https://notifier-docs.zentik.app/docs/self-hosted/installation) | Install and run Zentik on your server |

---

## Integrations

Connect your stack and get notifications in Zentik:

| Integration | What it does |
|-------------|----------------|
| [**NTFY**](https://notifier-docs.zentik.app/docs/integrations/ntfy) | Proxy NTFY topics to Zentik (subscribe + publish), with supported parameters |
| [**Home Assistant**](https://notifier-docs.zentik.app/docs/integrations/homeassistant) | HACS integration: `notify` service to send to Zentik from automations |
| [**Uptime Kuma**](https://notifier-docs.zentik.app/docs/integrations/uptime-kuma) | Webhook for monitoring alerts (up/down, status) |
| [**Scrypted**](https://notifier-docs.zentik.app/docs/integrations/scrypted) | Push notifications from Scrypted (cameras, NVR, etc.) |
| [**Servarr**](https://notifier-docs.zentik.app/docs/integrations/servarr) | Notifications from Sonarr, Radarr, and the rest of the *arr stack |
| [**Authentik**](https://notifier-docs.zentik.app/docs/integrations/authentik) | Alerts and events from Authentik (SSO, events) |
| [**Unraid**](https://notifier-docs.zentik.app/docs/integrations/unraid) | Notifications from Unraid (plugins, system events) |

---

## Try it

- **Web (PWA):** [notifier.zentik.app](https://notifier.zentik.app)
- **iOS:** [App Store](https://apps.apple.com/de/app/zentik-notifier/id6749312723) · [TestFlight](https://testflight.apple.com/join/dFqETQEm)

Need a feature or want to contribute? Open a discussion or a PR — [Discord](https://discord.gg/DzhJ4s7N).
