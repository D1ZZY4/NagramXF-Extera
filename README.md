# Nagram Extera

> A community-maintained Telegram client for Android, distilled from the best
> of every major fork. Privacy-first, opinionated defaults, and a build pipeline
> that takes care of itself.

Nagram Extera is the successor of **Nagram XF**, itself a fork of
**Nagram X**. It pulls features and ideas from across the Telegram-Android
ecosystem (AyuGram, Cherrygram, exteraGram, OctoGram) and ships them on top of
the official Telegram for Android source tree.

| | |
|---|---|
| **Package** | `fork.risin42.nagramx` |
| **Min SDK** | 27 (Android 8.1) |
| **Target SDK** | 36 |
| **Language** | Java + Kotlin (JVM 21) |
| **Build** | Gradle 8.x · AGP 9.1 · NDK 27.2 |
| **License** | GPL-2.0 (see [`LICENSE`](LICENSE)) |

## Quick start

```bash
# 1. Get Telegram API credentials at https://my.telegram.org/auth
# 2. Drop them into local.properties at the repo root:
cat > local.properties <<EOF
TELEGRAM_APP_ID=123456
TELEGRAM_APP_HASH=0123456789abcdef0123456789abcdef
EOF

# 3. Build a universal release APK
./gradlew :TMessagesProj:assembleRelease
```

Output APKs land in `TMessagesProj/build/outputs/apk/`, named
`NagramExtera-v<version>-<short-sha>(<versionCode>)-<abi>.apk`.

The `versionCode` is derived from the git commit count and the `versionName`
suffix from the current short SHA — there are **no manual version bumps**.
See [`documentations/BUILDING.md`](documentations/BUILDING.md) for the long
form, including signing, FCM, and CI setup.

## Documentation

Full documentation lives in the [`documentations/`](documentations) folder:

- [Overview & index](documentations/README.md)
- [Building from source](documentations/BUILDING.md)
- [Features](documentations/FEATURES.md)
- [Architecture](documentations/ARCHITECTURE.md)
- [Release & CI pipeline](documentations/RELEASE.md)
- [Privacy policy](documentations/PRIVACY.md)
- [Security policy](documentations/SECURITY.md)
- [Contributing](documentations/CONTRIBUTING.md)
- [Changelog](documentations/CHANGELOG.md)
- [Credits](documentations/CREDITS.md)

## Credits

Nagram Extera would not exist without the upstream work of:

- [Telegram for Android](https://github.com/DrKLO/Telegram) — the original
  client and the source tree this project is built on.
- [Nagram X](https://github.com/risin42/NagramX) — direct upstream of the XF
  line.
- [Nagram XF](https://github.com/Keeperorowner/NagramXF) — predecessor of this
  project.
- [AyuGram](https://github.com/AyuGram/AyuGram4A)
- [Cherrygram](https://github.com/arsLan4k1390/Cherrygram)
- [exteraGram](https://github.com/exteraSquad/exteraGram)
- [OctoGram](https://github.com/OctoGramApp/OctoGram)

A more detailed acknowledgements list, including individual feature
attributions, is in [`documentations/CREDITS.md`](documentations/CREDITS.md).

## License

This project is licensed under the GNU General Public License v2.0. See the
[`LICENSE`](LICENSE) file for the full text. By contributing you agree that
your contributions are licensed under the same terms.
