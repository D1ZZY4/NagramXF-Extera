# Structure

Snapshot of the repo layout so a new session orients without reading everything.

## Top level

- `build.gradle`, `settings.gradle`, `gradle.properties` — build config. SDK/NDK
  versions and toolchain live in the root `build.gradle`.
- `gradlew`, `gradle/` — Gradle wrapper (9.4).
- `buildSrc/` — build logic helpers.
- `TMessagesProj/` — the single Android module (`:TMessagesProj`).
- `TMessagesProj_AppTests/`, `Tools/` — tests and tooling.
- `documentations/` — only `CREDITS.md` is kept.
- `README.md`, `LICENSE` — public docs.
- `CLAUDE.md`, `.agents/` — agent tooling, **dev branch only**.

## Module: TMessagesProj

- `src/main/java/` — Java sources. Fork code lives mostly under:
  - `tw/nekomimi/nekogram/` — Neko-line settings and helpers
    (e.g. `settings/NekoSettingsActivity.java`,
    `settings/NagramExteraAboutActivity.java`,
    `settings/BaseNekoSettingsActivity.java`).
  - `xyz/nextalone/nagram/` — `NaConfig.kt` and Nagram additions.
  - `org/telegram/` — upstream Telegram for Android source tree.
- `src/main/kotlin/` — Kotlin sources (`ws/...`).
- `src/main/res/values/` — strings: `strings_neko.xml`, `strings_naxf.xml`,
  `strings_na.xml`, etc. Branding strings (Nagram Extera) live in `strings_naxf.xml`.
- `jni/` — vendored native code (ffmpeg, webp, voip/webrtc, etc.).
- `build.gradle` — module build, APK naming, API id/hash wiring.

## Where things tend to break

- Settings rows: declared (field) + init (`addRow`) + click handler + bind +
  divider logic must all agree. Missing one branch = dead row.
- Adapter cell types: header cells use `tw.nekomimi.nekogram.ui.cells.HeaderCell`,
  not `org.telegram.ui.Cells.HeaderCell`. Wrong import = blank screen.
