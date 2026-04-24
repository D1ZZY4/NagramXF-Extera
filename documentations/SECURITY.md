# Security Policy

## Supported versions

Only the most recent release on the `main` branch is supported with security
fixes. Older builds — including any APK that has been superseded by a
publicly tagged release — receive **no** backports.

| Version | Status |
|---|---|
| Latest `main` build | **Supported** |
| Previous release | **Best-effort**, no guarantee |
| Anything older | **Unsupported** |

## Reporting a vulnerability

Please report security issues **privately**. Do not open public GitHub
issues for anything you believe is exploitable.

Preferred channels, in order:

1. **GitHub Security Advisory** on the project repository
   ("Security" tab → "Report a vulnerability"). This creates a private
   thread visible only to maintainers.
2. **Telegram DM** to one of the maintainers listed on the project's
   Telegram channel.

Please include, at minimum:

- The affected version (`versionName` and `versionCode` from
  Settings → About).
- A description of the issue, including the security impact and a CVSS
  estimate if you have one.
- Reproduction steps or a proof of concept. Static analysis findings are
  welcome but include enough context to triage.
- Whether the issue exists upstream (in [Telegram for Android] or in any of
  the parent forks listed in [`CREDITS.md`](CREDITS.md)) so we can route the
  report appropriately.

[Telegram for Android]: https://github.com/DrKLO/Telegram

## What to expect

- An initial acknowledgement within **5 working days**.
- A triage decision (accepted / not-a-bug / upstream) within **14 days**.
- For accepted issues, a fix or mitigation in `main` as soon as possible,
  typically within 30 days for high-severity items.
- Public disclosure is coordinated with the reporter. We default to a
  90-day disclosure window from the date of the initial report, shortened
  if the issue is being actively exploited or if a fix has shipped sooner.

## Hardening notes

The app inherits the security posture of upstream Telegram for Android. On
top of that, Nagram Extera:

- Pins the NDK and build-tools versions in `build.gradle` so reproducible
  builds are achievable from a clean checkout.
- Enables R8 full-mode minification and resource shrinking in `release` and
  `staging` build types.
- Ships **without** any third-party analytics, advertising, or attribution
  SDKs.
- Treats Firebase Cloud Messaging and Crashlytics as opt-in surfaces. They
  are wired in but require valid `google-services.json` and explicit user
  consent in Settings before any data leaves the device.
- Stores secrets exclusively through `local.properties` or the
  base64-encoded `LOCAL_PROPERTIES` CI secret. Nothing sensitive is
  committed to the repository.

## Out of scope

The following are **not** considered vulnerabilities for this project:

- Issues that exist in upstream Telegram and reproduce on the official
  Telegram for Android client. Please report those to Telegram directly.
- Self-inflicted misconfiguration when building your own fork (e.g. leaking
  your own API hash by committing `local.properties`).
- Theoretical risks that require a rooted device, a malicious system
  package, or a compromised OS to exploit.
- Vulnerabilities in third-party translation providers, proxies, or other
  optional integrations the user explicitly enables.
  
