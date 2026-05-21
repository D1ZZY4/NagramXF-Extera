# Nagram XF

## Project Overview

Nagram XF is a customized Android client for Telegram, forked from Nagram X. It integrates additional features from other Telegram forks including exteraGram and AyuGram.

- **Platform:** Android (minSdk 27, targetSdk 36)
- **Build System:** Gradle (with Kotlin DSL in buildSrc)
- **Languages:** Java, Kotlin, C/C++ (JNI for native libs)
- **Protocol:** Telegram MTProto (via tgnet JNI component)

## Project Structure

- `TMessagesProj/` - Main Android application module (Java/Kotlin sources, resources, JNI)
- `buildSrc/` - Custom Gradle plugins and code generation tasks (TL schema → Java/Kotlin)
- `Tools/` - Helper scripts for uploading builds
- `gradle/` - Gradle wrapper files

## Building the App

### Prerequisites

1. Create `local.properties` in the project root with your Telegram API credentials:
   ```properties
   TELEGRAM_APP_ID=<your_telegram_app_id>
   TELEGRAM_APP_HASH=<your_telegram_app_hash>
   ```

2. Optionally add APK signing config to `local.properties`:
   ```properties
   KEYSTORE_PASS=<keystore_password>
   ALIAS_NAME=<alias_name>
   ALIAS_PASS=<alias_password>
   ```

3. Optionally replace `TMessagesProj/google-services.json` with your own for FCM support.

### Build Commands

```bash
# Debug build
./gradlew :TMessagesProj:assembleDebug

# Release build
./gradlew :TMessagesProj:assembleRelease
```

## Notes

- This is a native Android app — it does not run a web server.
- The app is intended to be built and deployed to Android devices via APK.
- Android SDK tools (aapt, adb, etc.) are typically required for a full build; use Android Studio for the best experience.

## User Preferences

- Follow existing Gradle/Android project conventions.
