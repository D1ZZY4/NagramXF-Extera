# Credits

Nagram Extera is a distillation, not an invention. The features, fixes, and
ideas in this client come from years of work by many people across many
forks of Telegram for Android. This file makes that lineage explicit and
keeps every upstream project one click away.

> If you authored code, an icon set, a translation, or a setting that ended
> up in this fork and you are not credited here, please open a pull request
> against this file (or an issue with the relevant link) and we will fix it.

## Direct lineage

The chain that this project is a continuation of, in order:

| Project | Role | Repository |
|---|---|---|
| **Telegram for Android** | Original client. Nagram Extera is a soft fork of this codebase and inherits its MTProto stack, native libraries, and UI framework. | <https://github.com/DrKLO/Telegram> |
| **Nagram X** | Direct upstream of the XF line. Most of the privacy and power-user features in this app originated here. | <https://github.com/risin42/NagramX> |
| **Nagram XF** | Immediate predecessor of this project. Nagram Extera continues from where Nagram XF left off, hence the working name **Nagram XF Extera**. | <https://github.com/Keeperorowner/NagramXF> |

## Sister forks we draw from

Each of these projects has shipped features or design ideas that have been
ported, adapted, or reworked into Nagram Extera. Source-level attribution
lives next to each port; this is the high-level summary.

| Project | What we picked up | Repository |
|---|---|---|
| **AyuGram** | Anti-recall, deleted-message preservation, edit-history visibility, server-time spoofing protections. | <https://github.com/AyuGram/AyuGram4A> |
| **Cherrygram** | UI refinements, additional bubble/icon styles, premium-style cosmetics unlocked locally. | <https://github.com/arsLan4k1390/Cherrygram> |
| **exteraGram** | Chats list ergonomics, folder tab refinements, drawer/menu cleanups. The "Extera" in the project name is a nod to this lineage. | <https://github.com/exteraSquad/exteraGram> |
| **OctoGram** | Translation provider abstraction, additional speech-to-text providers, chat utilities. | <https://github.com/OctoGramApp/OctoGram> |

## Bundled libraries

The native and JVM sides depend on, among others:

- **AndroidX**, **Material Components**, **ExoPlayer**, **Firebase
  Messaging**, **Firebase Crashlytics**, **Google ML Kit**, **Room**,
  **OkHttp** — pulled from Maven Central / Google Maven.
- **ffmpeg**, **libwebp**, **libjxl**, **libvpx**, **libopus**, **SQLite**
  — vendored under [`TMessagesProj/jni/`](../TMessagesProj/jni) per the
  upstream Telegram bundling convention.
- **TgVoip / WebRTC** — voice and video calls.

Each dependency carries its own license; consult the canonical project for
the authoritative notice.

## Translations & community

Translations, issue triage, and field-testing on the long tail of Android
devices come from the wider Nagram and Telegram-fork community. Localised
strings live under
[`TMessagesProj/src/main/res/values-*/`](../TMessagesProj/src/main/res). If
you contributed a translation and want explicit credit here, please open a
PR.

## Special thanks

To everyone who filed an issue, sent a patch, ported a feature, maintained
an upstream fork, kept a localisation alive, or just hammered on a beta
build until it stopped crashing — this project would not exist without you.
