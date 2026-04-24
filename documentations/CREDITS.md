# Credits

Nagram Extera is the product of years of work by many people across many
forks of Telegram for Android. This file makes the lineage explicit.

## Direct lineage

- **[Telegram for Android](https://github.com/DrKLO/Telegram)** — the
  original client. Nagram Extera is a soft fork of this codebase and
  inherits all of its functionality, MTProto stack, native libraries, and
  UI framework. Maintained by Telegram FZ-LLC and contributors.
- **[Nagram X](https://github.com/risin42/NagramX)** — the direct upstream
  of the XF line. Most of the privacy- and power-user features in this app
  originated here.
- **[Nagram XF](https://github.com/Keeperorowner/NagramXF)** — the
  immediate predecessor of this project. Nagram Extera continues from
  exactly where Nagram XF left off.

## Sister forks we draw from

Features, bug fixes, and ideas have been ported (with attribution in source
where possible) from:

- **[AyuGram](https://github.com/AyuGram/AyuGram4A)** — anti-recall, deleted
  message preservation, edit history visibility, server-time spoofing
  protections.
- **[Cherrygram](https://github.com/arsLan4k1390/Cherrygram)** — UI
  refinements, additional bubble/icon styles, premium-style cosmetics
  unlocked locally.
- **[exteraGram](https://github.com/exteraSquad/exteraGram)** — chats list
  ergonomics, folder tab refinements, and several drawer/menu cleanups.
  The "Extera" in the project name is a nod to this lineage.
- **[OctoGram](https://github.com/OctoGramApp/OctoGram)** — translation
  provider abstraction, additional speech-to-text providers, and chat
  utilities.

## Libraries

The native and Java/Kotlin sides depend on (a non-exhaustive list):

- AndroidX, Material Components, ExoPlayer, Firebase Messaging /
  Crashlytics, Google ML Kit, Room, OkHttp.
- ffmpeg, libwebp, libjxl, libvpx, libopus, SQLite — all vendored under
  `TMessagesProj/jni/` per upstream Telegram's bundling.
- TgVoip / WebRTC for voice and video calls.

Each has its own license; see the individual source trees for the canonical
notices.

## Special thanks

To everyone who has filed issues, contributed translations, or maintained
any of the upstream forks above — this project would not exist without you.

## How to be added here

If your code, design, or icon set has been ported into Nagram Extera and
you are not credited, please open a pull request against this file (or an
issue with the relevant link) and we will add you.
