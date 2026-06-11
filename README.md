# Nagram Extera

A Telegram client for Android, forked from Nagram XF (a downstream of Nagram X).
It carries the privacy and power-user features of that line and ports selected
features from other Telegram-Android forks on top of the official Telegram
source tree.

[![License](https://img.shields.io/badge/license-GPL--3.0-blue?style=flat-square)](LICENSE)
[![Min SDK](https://img.shields.io/badge/min%20SDK-27-3DDC84?style=flat-square&logo=android&logoColor=white)](#)
[![Target SDK](https://img.shields.io/badge/target%20SDK-36-3DDC84?style=flat-square&logo=android&logoColor=white)](#)

## Build

You need Telegram API credentials from <https://my.telegram.org/auth>.

```bash
cat > local.properties <<'EOF'
TELEGRAM_APP_ID=123456
TELEGRAM_APP_HASH=0123456789abcdef0123456789abcdef
EOF

NATIVE_TARGET=arm64-v8a ./gradlew :TMessagesProj:assembleRelease
```

The APK is written to `TMessagesProj/build/outputs/apk/release/` and named
`NagramExtera-v<versionName>(<versionCode>)-<abi>.apk`.

`TELEGRAM_APP_ID` and `TELEGRAM_APP_HASH` can be supplied through
`local.properties` or as environment variables. The version code and name are
set manually in `gradle.properties` (`APP_VERSION_CODE`, `APP_VERSION_NAME`).

## Project facts

| | |
|---|---|
| Application id | `org.nagram.extera` |
| Min / target SDK | 27 / 36 |
| Languages | Java + Kotlin, JVM 21 |
| Toolchain | Gradle 9.4 · AGP 9.1 · NDK 27.2 · build-tools 36 |
| Module | `:TMessagesProj` |
| License | [GPL-3.0](LICENSE) |

## Links

- Source: <https://github.com/D1ZZY4/NagramXF-Extera>
- Announcements: [@NagramExteraOfficial](https://t.me/NagramExteraOfficial)
- Builds: [@NagramExteraCloud](https://t.me/NagramExteraCloud)
- Community and bug reports: [@NagramExteraCommunity](https://t.me/NagramExteraCommunity)

## Credits

Built on [Telegram for Android](https://github.com/DrKLO/Telegram) and the
Nagram line ([Nagram X](https://github.com/risin42/NagramX),
[Nagram XF](https://github.com/Keeperorowner/NagramXF)), with features ported
from AyuGram, Cherrygram, exteraGram, and OctoGram. Full attribution is in
[documentations/CREDITS.md](documentations/CREDITS.md).

## License

[GNU General Public License v3.0](LICENSE). Contributions ship under the same
terms as upstream Telegram for Android.
