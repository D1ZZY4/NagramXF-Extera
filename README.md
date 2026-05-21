<div align="center">

# Nagram&nbsp;Extera

**A modern, privacy-first, opinionated Telegram client for Android — distilled
from the best of every major fork.**

[![Release Build](https://img.shields.io/github/actions/workflow/status/Keeperorowner/NagramExtera/release.yml?branch=main&label=release&style=flat-square)](.github/workflows/release.yml)
[![Min SDK](https://img.shields.io/badge/min%20SDK-27%20(Android%208.1)-3DDC84?style=flat-square&logo=android&logoColor=white)](#)
[![Target SDK](https://img.shields.io/badge/target%20SDK-36-3DDC84?style=flat-square&logo=android&logoColor=white)](#)
[![JVM](https://img.shields.io/badge/JVM-21-007396?style=flat-square&logo=openjdk&logoColor=white)](#)
[![Gradle](https://img.shields.io/badge/Gradle-8.x-02303A?style=flat-square&logo=gradle&logoColor=white)](#)
[![License](https://img.shields.io/badge/license-GPL--2.0-blue?style=flat-square)](LICENSE)

</div>

---

Nagram Extera is the spiritual successor of **Nagram XF**, itself a downstream
of **Nagram X**. It curates and refines features from across the
Telegram-Android ecosystem — **AyuGram**, **Cherrygram**, **exteraGram**,
**OctoGram** — on top of the official Telegram for Android source tree. The
goal is a single client that feels like the one upstream should have shipped:
private by default, customisable without ceremony, and built by a pipeline
that does its own bookkeeping.

> **Status — rolling release.** There are no manual version bumps. Every
> push to `main` produces a deterministically-versioned APK; see
> [`documentations/RELEASE.md`](documentations/RELEASE.md).

## Links

| | |
|---|---|
| **Source code** | <https://github.com/D1ZZY4/NagramXF-Extera> |
| **Official channel** | [@NagramExteraOfficial](https://t.me/NagramExteraOfficial) — announcements & changelog |
| **Release channel** | [@NagramExteraCloud](https://t.me/NagramExteraCloud) — alternative APK distribution outside of GitHub Releases |
| **Community group** | [@NagramExteraCommunity](https://t.me/NagramExteraCommunity) — discussion, support, bug reports |

## Highlights

| | |
|---|---|
| **Privacy by default** | No analytics, no ads, no telemetry. Optional integrations are opt-in and clearly labelled. |
| **Best-of-fork distillation** | Curated picks from AyuGram, Cherrygram, exteraGram, OctoGram, Nagram&nbsp;X / XF. |
| **Automatic versioning** | `versionCode` from `git rev-list`, `versionName` from short SHA. Zero bookkeeping. |
| **Sub-10-minute CI** | Single-ABI release build with cached Gradle, ccache-wrapped NDK, and partial-clone checkout. |
| **Reproducible builds** | NDK, build-tools, Kotlin, and AGP all pinned in one place. |
| **Hardened release pipeline** | R8 full-mode, blobless clones, deterministic SDK pinning, on-failure log shipping. |

## Project facts

| | |
|---|---|
| **Display name** | Nagram Extera |
| **Application id** | `app.nagramextera` |
| **Min / target SDK** | 27 (Android 8.1) / 36 |
| **Languages** | Java + Kotlin (JVM 21) |
| **Toolchain** | Gradle 8.x · AGP 9.1 · NDK 27.2 · CMake 3.31 |
| **Module layout** | Single Android module — `:TMessagesProj` |
| **License** | [GPL-2.0](LICENSE) |

## Quick start

```bash
# 1. Get Telegram API credentials from https://my.telegram.org/auth
cat > local.properties <<'EOF'
TELEGRAM_APP_ID=123456
TELEGRAM_APP_HASH=0123456789abcdef0123456789abcdef
EOF

# 2. Build a single-ABI release APK (matches what CI ships)
NATIVE_TARGET=arm64-v8a ./gradlew :TMessagesProj:assembleRelease
```

The resulting APK lands in `TMessagesProj/build/outputs/apk/release/`, named:

```
NagramExtera-v<versionName>(<versionCode>)-<abi>.apk
```

For everything else — signing keystores, FCM, CI secrets, troubleshooting —
see [`documentations/BUILDING.md`](documentations/BUILDING.md).

## Documentation

The [`documentations/`](documentations) folder is the canonical reference.
The top-level README is intentionally a landing page; long-form material
lives next door:

| Document | What's inside |
|---|---|
| [Building](documentations/BUILDING.md) | Local builds, signing, FCM, automatic versioning. |
| [Features](documentations/FEATURES.md) | What Nagram Extera does that stock Telegram does not. |
| [Architecture](documentations/ARCHITECTURE.md) | Repository layout, modules, native code. |
| [Release & CI](documentations/RELEASE.md) | The pipeline, secrets, artifact naming. |
| [Privacy](documentations/PRIVACY.md) | What we collect (nothing) and what Telegram itself sees. |
| [Security](documentations/SECURITY.md) | Reporting vulnerabilities, supported versions, hardening. |
| [Contributing](documentations/CONTRIBUTING.md) | Branching, code style, PR & commit conventions. |
| [Changelog](documentations/CHANGELOG.md) | Human-curated release notes. |
| [Credits](documentations/CREDITS.md) | Detailed lineage and per-feature attribution. |

## Lineage & credits

Nagram Extera stands on the shoulders of the entire Telegram-Android fork
ecosystem. Without these projects there would be nothing to distil:

- [Telegram for Android](https://github.com/DrKLO/Telegram) — the original
  client; the source tree this fork is built on.
- [Nagram X](https://github.com/risin42/NagramX) — direct upstream of the XF
  line; most of the privacy and power-user features originate here.
- [Nagram XF](https://github.com/Keeperorowner/NagramXF) — the immediate
  predecessor of this project.
- [AyuGram](https://github.com/AyuGram/AyuGram4A) — anti-recall, edit history,
  deleted-message preservation.
- [Cherrygram](https://github.com/arsLan4k1390/Cherrygram) — UI refinements
  and cosmetic unlocks.
- [exteraGram](https://github.com/exteraSquad/exteraGram) — chats list and
  drawer ergonomics. The "Extera" in the project name is a nod to this
  lineage.
- [OctoGram](https://github.com/OctoGramApp/OctoGram) — translation and
  speech-to-text provider abstractions.

A more granular breakdown lives in
[`documentations/CREDITS.md`](documentations/CREDITS.md).

## Community

- **Announcements & changelog —** [@NagramExteraOfficial](https://t.me/NagramExteraOfficial)
- **Builds (alternative to GitHub Releases) —** [@NagramExteraCloud](https://t.me/NagramExteraCloud)
- **Discussion, support, bug reports —** [@NagramExteraCommunity](https://t.me/NagramExteraCommunity)
- **Source code & issues —** <https://github.com/D1ZZY4/NagramXF-Extera>

For sensitive reports (security advisories) please follow the private
disclosure process documented in
[`documentations/SECURITY.md`](documentations/SECURITY.md) instead of the
public group.

## License

This project is distributed under the [GNU General Public License v2.0](LICENSE).
By contributing you agree your changes ship under the same terms, in line with
upstream Telegram for Android.
