# Build notes (Replit)

How to build and verify on Replit. Keep env-specific gotchas here.

## Prerequisites

- Telegram API credentials, via `local.properties` or env vars:
  ```
  TELEGRAM_APP_ID=...
  TELEGRAM_APP_HASH=...
  ```
- Android SDK + NDK 27.2.12479018, build-tools 36, JDK 21. The build reads
  SDK/NDK versions from the root `build.gradle`.

## Commands

```
# configure only
./gradlew :TMessagesProj:help

# build one ABI (fast, matches CI)
NATIVE_TARGET=arm64-v8a ./gradlew :TMessagesProj:assembleDebug

# lint
./gradlew :TMessagesProj:lintDebug
```

## Gotchas

- Native builds are heavy; always build a single ABI (`arm64-v8a`) during
  iteration. Build all ABIs only for a real release.
- `google-services.json` package must match `applicationId`
  (`org.nagram.extera`). A mismatch fails the google-services plugin with
  "No matching client found". Keep them in sync.
- If config cache yields stale failures, retry with
  `--no-configuration-cache`.
- Record the first successful build's setup steps here so later sessions skip
  re-discovering them.
