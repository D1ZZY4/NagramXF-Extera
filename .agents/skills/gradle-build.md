# Skill: gradle-build

Build and verify the app on Replit.

## When to use

Any change to Java/Kotlin code, resources, Gradle files, or native code — i.e.
almost every task. Verification is not optional.

## Steps

1. Ensure API credentials exist (`local.properties` or env):
   ```
   TELEGRAM_APP_ID=...
   TELEGRAM_APP_HASH=...
   ```
2. Configure:
   ```
   ./gradlew :TMessagesProj:help
   ```
3. Assemble a single ABI (matches CI, far faster than all ABIs):
   ```
   NATIVE_TARGET=arm64-v8a ./gradlew :TMessagesProj:assembleDebug
   ```
4. Lint the touched area when feasible:
   ```
   ./gradlew :TMessagesProj:lintDebug
   ```

## Notes

- Native (NDK) builds are heavy. Build one ABI; don't build all four unless
  shipping a release.
- The output APK name pattern is `NagramExtera-v<versionName>(<versionCode>)-<abi>.apk`.
- Record slow-build workarounds and env setup in `.agents/memory/build.md`.
- If Gradle config caching causes stale failures, retry with
  `--no-configuration-cache` before assuming a real error.
