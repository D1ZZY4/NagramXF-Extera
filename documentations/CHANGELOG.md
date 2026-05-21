# Changelog

All notable changes to Nagram Extera are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.1] — 2026-05-22

### Fixes & Improvements

#### Force Forward — reduced wait time
The forward process for restricted messages (no-forward chats) now starts
sending immediately for messages whose media is already cached locally.
Previously, the engine downloaded every piece of media in the selected batch
before forwarding anything, causing a long wait when mixing text, already-cached
files, and un-cached files. Now each message is evaluated independently: if the
file is already on device it forwards instantly; if not, only that specific file
is downloaded before it is sent. Text messages and stickers are never delayed.

#### Package name changed
The application package ID has changed from `fork.risin42.nagramx` to
`orang.nagram.extra`. This affects:
- The installed app identifier on Android (a fresh install is required;
  data from the old package is not migrated automatically).
- Account authenticator type, contact provider MIME types, and FCM registration.
- All related XML manifests and `google-services.json`.

Note: users upgrading from Nagram XF or earlier Nagram Extera builds must
uninstall the previous version before installing this build. Telegram will
prompt for re-login on first launch.

#### Settings — old "About" screen removed
The legacy About screen (`NekoAboutActivity`) has been replaced entirely by the
new **Nagram Extera** info screen, which includes upstream channel links, credits,
and source code references in one place. The `nasettings/about` deep link now
opens the new screen.

---

## [1.0.0] — 2026-05-22

### Initial Release — Nagram Extera

This marks the first official release of **Nagram Extera**, a customized Android
Telegram client forked from Nagram XF and further enriched with features from
exteraGram and AyuGram.

---

### Branding & Identity

- **App renamed** from Nagram XF to **Nagram Extera** across all user-facing
  surfaces, resource files, and build outputs.
- **APK output filename** updated to `NagramExtera-v{version}-{abi}.apk`.
- **Default custom title** updated to "Nagram Extera".
- **Version numbering** reset to `1.0.0` to reflect the new project identity.

---

### Settings & About Screen

- **Added "Nagram Extera" info screen** in the main settings menu, containing:
  - **Contents** — official channel (`@NagramExteraOfficial`), release channel
    (`@NagramExteraCloud`), discussion group (`@NagramExteraCommunity`), and
    features tips (`@NagramTips`).
  - **Credits** — Features Tips, Nagram XF, Nagram X, Nagram.
  - **Source Code** — GitHub links for Nagram Extera, Nagram X, Nagram XF,
    and AyuGram.
- **"Ayugram" menu** (previously "AyuMoments") — renamed in all English
  strings for consistency with upstream AyuGram branding.

---

### Upstream Merges & Features

Nagram Extera 1.0.0 integrates all features from Nagram XF at the time of fork:

- **AyuGram** — Ghost Mode, Regex Filters, AyuSpy, deleted message tracking,
  appearance customization (deleted mark style, color, custom text, semi-transparent view).
- **Nagram X** — AI Translator (OpenAI/Gemini/Groq/DeepSeek/xAI/Cerebras),
  deleted and edited message history, custom deleted mark, premium emoji as sticker.
- **exteraGram** — Now Playing (Last.fm & local), Bottom Bar modes, Home Drawer,
  avatar corner customization, force forward, peek online, schedule messages.
- **UI** — Blur options, square floating button, separate headers, sticker size
  control, OneUI style, remove message tail, user avatars in message preview.
- **Camera** — Extended FPS, seamless switching, stabilization, static zoom,
  per-session memory, configurable video message camera (front/rear/ask).

---

### CI/CD & Build System

- GitHub Actions workflows publish APKs to Telegram and GitHub Releases.
  - `release.yaml` — full release on push to `main`; auto-increments
    `APP_VERSION_CODE` after each successful publish.
  - `canary.yaml` — pre-release on push to `canary`.
  - `staging.yaml` — pre-release on push to `dev`.
- Secrets: `BOT_TOKEN`, `REALEASE_UPLOAD_ID`, `CANARY_UPLOAD_ID`.

---

*Nagram Extera is free software, licensed under the GNU General Public License v3.0.*
