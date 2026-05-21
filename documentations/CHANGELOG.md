# Changelog

All notable changes to Nagram Extera are documented in this file.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.0] — 2025-05-21

### Initial Release — Nagram Extera

This marks the first official release of **Nagram Extera**, a customized Android Telegram client forked from Nagram XF and further enriched with features from exteraGram and AyuGram.

---

### Branding & Identity

- **App renamed** from Nagram XF to **Nagram Extera** across all user-facing surfaces, resource files, and build outputs.
- **APK output filename** updated to `NagramExtera-v{version}-{abi}.apk`.
- **Default custom title** updated to "Nagram Extera".
- **Version numbering** reset to `1.0.0` to reflect the new project identity.

---

### Settings & About Screen

- **Added "Nagram Extera" info screen** in the main settings menu — a dedicated screen (similar in structure to the Ayugram settings screen) containing:
  - **Contents** — links to the official Nagram Extera Channel (`@NagramExteraOfficial`), Release Channel (`@NagramExteraCloud`), Discussion Group (`@NagramExteraCommunity`), and Features Tips (`@NagramTips`).
  - **Credits** — attribution to upstream projects: Features Tips (`@NagramTips`), Nagram XF (`@NagramX_Fork`), Nagram X (`@NagramX`), and Nagram (`@nagram_channel`).
  - **Source Code** — direct links to the GitHub repositories of Nagram Extera, Nagram X, Nagram XF, and AyuGram.
- **"Ayugram" settings menu** (previously named "AyuMoments") — renamed across all English strings, settings entries, and the About section for accuracy and consistency with upstream AyuGram branding.

---

### Upstream Merges & Features

Nagram Extera 1.0.0 integrates all features available in Nagram XF at the time of fork, including:

- **AyuGram integration** — Ghost Mode, Regex Filters, AyuSpy Settings, deleted message tracking and appearance customization (deleted mark style, color, custom text, semi-transparent view).
- **Nagram X features** — AI Translator (LLM-based, supports OpenAI/Gemini/Groq/DeepSeek/xAI/Cerebras), deleted and edited message history, custom deleted mark, premium emoji as sticker, and all upstream Nagram-specific settings.
- **exteraGram additions** — Now Playing (Last.fm & local integration), Bottom Bar display modes, Home Drawer, avatar corner customization, force forward, peek online, and schedule messages.
- **UI enhancements** — Blur options, square floating button, separate headers, sticker size control, OneUI style support, remove message tail, user avatars in message preview, recent chats sidebar.
- **Camera improvements** — Extended FPS range, seamless switching, stabilization, static zoom, per-session camera memory, and configurable video message camera (front/rear/ask).
- **Message filters** — Regex-based filters with mask mode, shadow ban list, import/export via URL or clipboard, per-chat exclusions, and reversed expression support.

---

### CI/CD & Build System

- **GitHub Actions workflows** updated to publish APKs to both Telegram channels and GitHub Releases on every build:
  - `release.yaml` — Creates a full GitHub Release for every push to `main`.
  - `canary.yaml` — Creates a GitHub pre-release for every push to `canary`.
  - `staging.yaml` — Creates a GitHub pre-release for every push to `dev`.
- **Secret naming convention** standardized: `BOT_TOKEN`, `REALEASE_UPLOAD_ID`, `CANARY_UPLOAD_ID`.
- **Workflow file extensions** corrected to `.yaml` throughout all internal references.
- All GitHub Actions pinned to latest stable versions.

---

### Known Limitations

- Package name remains `fork.risin42.nagramx` for compatibility with existing installations. A package rename is planned for a future release.
- Some strings in non-English language files may still reference legacy "AyuMoments" labels; these will be updated as translations are contributed.

---

*Nagram Extera is free software, licensed under the GNU General Public License v3.0.*
