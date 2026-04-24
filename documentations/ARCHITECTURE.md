# Architecture

A high-level map of the repository for newcomers. This is **not** an
exhaustive code tour; the official Telegram source is large and well
commented, and the Nagram lineage has its own conventions on top.

## Repository layout

```
.
├── build.gradle                Root Gradle config, AGP/Kotlin/SDK pinning.
├── settings.gradle             Plugin management, single included module.
├── gradle.properties           App version baseline, JVM args, AndroidX flags.
├── buildSrc/                   Custom Gradle logic shared across modules.
├── gradle/                     Gradle wrapper distribution.
├── gradlew, gradlew.bat        Wrapper entry points.
│
├── TMessagesProj/              The one and only application module.
│   ├── build.gradle            App-level config, automatic versioning, ABI splits.
│   ├── google-services.json    Firebase config (placeholder by default).
│   ├── release.keystore        Placeholder signing key (replace for real builds).
│   ├── proguard-rules.pro      R8/ProGuard rules.
│   ├── schemas/                Room schema export directory.
│   ├── jni/                    Native (C/C++) sources, CMakeLists.txt.
│   └── src/main/
│       ├── AndroidManifest.xml
│       ├── java/               Java + Kotlin sources.
│       └── res/                Resources, including localized strings_*.xml.
│
├── Tools/                      Build-time and CI helper scripts (e.g. upload.py).
├── TMessagesProj_AppTests/     Instrumentation/unit test scaffolding.
├── documentations/             This folder.
└── .github/                    Issue templates and CI workflows.
```

## Module boundaries

There is a single Gradle module — `:TMessagesProj`. Upstream Telegram has
historically resisted multi-module splits because the codebase predates
Gradle's good multi-module ergonomics, and the fork ecosystem has followed
suit to keep cherry-picks straightforward.

Logical layers inside the module, by package prefix:

| Package root | Responsibility |
|---|---|
| `org.telegram.tgnet` | MTProto framing and the wire-level API. |
| `org.telegram.messenger` | Data layer: account state, controllers, storage. |
| `org.telegram.ui` | UI layer: activities, fragments, components. |
| `org.telegram.ui.Components` | Reusable views and widgets. |
| `org.telegram.ui.ActionBar` | The custom theming/action-bar framework. |
| `org.telegram.SQLite` | Thin JNI wrapper around bundled SQLite. |
| `tw.nekomimi.nekogram` *(historical)* | Nekogram/Nagram extensions. |
| `xyz.nextalone.nagram` | Nagram X additions. |

Fork-specific code is **always** behind a `NaConfig` (or equivalent) flag so
upstream merges stay mechanical. New features should follow the same
pattern.

## Native code

`TMessagesProj/jni/` builds a single shared library (`libtmessages.<ver>.so`)
that wraps:

- A vendored ffmpeg for media decoding.
- Bundled SQLite (with custom encryption hooks).
- TgVoip / WebRTC for calls and video calls.
- Various image-decoding shims (libwebp, libjxl helpers).

The native build is driven by `CMakeLists.txt` and respects the standard
Android NDK toolchain. `ccache` is auto-detected and wired in via
`-DANDROID_CCACHE=...` when present on `PATH`.

ABI splits are configured in `TMessagesProj/build.gradle`:

- Default: `armeabi-v7a`, `arm64-v8a`, `x86_64` plus a universal APK.
- CI: `NATIVE_TARGET=arm64-v8a` to ship a single APK per release.
- `NATIVE_TARGET=SKIP` disables all CMake/JNI tasks for faster Java-only
  iteration.

## Build flavours

Three build types are defined: `debug`, `staging`, `release`. `staging` is
what CI builds for canary channels — release packaging with R8 minification
enabled, but signed with the same keystore as `release` to keep the install
path stable on testers' devices.

## Signing & secrets

All secrets enter the build through one of two channels:

1. **Local development**: `local.properties` (git-ignored).
2. **CI**: a single base64-encoded `LOCAL_PROPERTIES` GitHub Actions secret
   that the Gradle build decodes at configuration time. See
   [`RELEASE.md`](RELEASE.md) for the full secret list.
   
