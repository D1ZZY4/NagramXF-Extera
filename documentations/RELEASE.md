# Release & CI Pipeline

Release builds are produced by GitHub Actions. The pipeline lives at
[`.github/workflows/release.yml`](../.github/workflows/release.yml) and is
designed to run unattended on every push to `main` (with manual
`workflow_dispatch` available for ad-hoc rebuilds).

## Triggers

| Trigger | Behaviour |
|---|---|
| `push` to `main` | Builds, uploads APK artifact, optionally publishes to Telegram. |
| `workflow_dispatch` | Same as above. The `upload` input may be set to `y` to skip the publish step. |
| Commit message contains `[skip upload]` | APK is built and uploaded as an artifact, but the publish job is skipped. |
| Commit message contains `[skip ci]` | Standard GitHub Actions skip token; the workflow is not run at all. |

`paths-ignore` filters skip the run when only documentation or non-release
workflow files change.

## Required secrets

| Name | Purpose |
|---|---|
| `LOCAL_PROPERTIES` | Base64-encoded `local.properties` containing `TELEGRAM_APP_ID`, `TELEGRAM_APP_HASH`, `KEYSTORE_PASS`, `ALIAS_NAME`, `ALIAS_PASS`. |
| `KEYSTORE_BASE64` *(optional)* | Base64 of `release.keystore`. Decoded into place when present. |
| `HELPER_BOT_TOKEN` | Bot token used to publish builds to Telegram. |
| `HELPER_BOT_TARGET` | Chat ID for the release channel. |
| `HELPER_BOT_CANARY_TARGET` | Chat ID for the canary channel. |
| `APP_ID` / `APP_HASH` | Telegram MTProto credentials used by `Tools/scripts/upload.py`. |

Set them in **Settings → Secrets and variables → Actions** in your fork.

## Versioning

Both the `versionCode` and the `versionName` are computed at build time from
git metadata. There is **nothing to bump manually** between releases. The
canonical rules (also documented in [`BUILDING.md`](BUILDING.md)):

- `versionCode = git rev-list --count HEAD`.
- `versionName = ${APP_VERSION_NAME}-${shortSha}` on CI.
- `BUILD_TIMESTAMP` is exported as a Unix epoch second by the workflow and
  baked into `BuildConfig`.

The CI checkout step uses `fetch-depth: 0` so the commit count is accurate.

## Artifact naming

```
NagramExtera-v<versionName>(<versionCode>)-<abi>.apk
```

Artifacts uploaded to GitHub follow the form
`NagramExtera-Release-<unix-timestamp>` so multiple in-flight builds never
collide. Retention is 30 days for the APK and 14 days for the failure log
archive.

## Failure-mode log capture

When the build job fails, the workflow:

1. Collects every `*/build/reports/`, `*/build/logs/`, `*.log` and Gradle
   daemon log it can find.
2. Zips them into `build-logs-<run-id>.zip`.
3. Uploads the archive as an artifact.
4. If `HELPER_BOT_TOKEN` and `HELPER_BOT_TARGET` are configured, sends the
   archive directly to Telegram with a short caption identifying the commit.

This means a failed nightly build is actionable from a phone, without having
to open the GitHub UI.

## Local reproducibility

Every step the CI does can be reproduced locally. The minimal incantation:

```bash
export NATIVE_TARGET=arm64-v8a
export BUILD_TIMESTAMP=$(date +%s)
export COMMIT_ID=$(git rev-parse HEAD)
./gradlew :TMessagesProj:assembleRelease
```

Resulting APKs end up in `TMessagesProj/build/outputs/apk/release/`.

