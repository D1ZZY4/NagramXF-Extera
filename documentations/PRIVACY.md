# Privacy Policy

_Last updated: 2026-04-24_

Nagram Extera ("the app") is a third-party client for the
[Telegram messaging service](https://telegram.org). This document explains
exactly what the app does and does not do with your data.

## TL;DR

- The app **does not collect, transmit, or sell** any personal data to its
  developers or any third party.
- All chat data is exchanged directly between your device and Telegram's
  servers using the official MTProto protocol.
- Optional integrations (translation providers, FCM push, voice-to-text) are
  **off by default** and clearly labelled in settings before they are used.
- The app contains **no advertising, analytics SDKs, or tracking pixels.**

## What the app does **not** do

- No telemetry beacons, no "anonymous usage statistics", no crash reports
  sent to the developers without your explicit opt-in.
- No third-party advertising, marketing, or attribution SDKs.
- No automatic transmission of your contact list, message history, media, or
  device identifiers to anyone other than Telegram itself.
- No background uploading of files, logs, or diagnostics.

## What Telegram itself collects

Because the app talks to Telegram's servers, Telegram's own privacy policy
applies to all data exchanged through the service (accounts, messages,
media, contacts you choose to sync, etc.). Please read it:

- <https://telegram.org/privacy>

The app's developers have no access to that data and no special relationship
with Telegram.

## Optional integrations

The following features are **off by default**. When you enable them you
explicitly send the relevant data to the listed third party. Disabling them
again immediately stops any further requests.

| Feature | Endpoint contacted | Data sent |
|---|---|---|
| Google Translate (default provider) | `translate.googleapis.com` | The text you choose to translate. |
| DeepL / Yandex / LibreTranslate translators | The provider you select | The text you choose to translate, plus any API key you configured. |
| On-device ML Kit translation / speech-to-text | None (runs locally) | None. |
| Firebase Cloud Messaging (push) | Google FCM | A device push token. Required for push notifications on Google-services devices. |
| Crashlytics | Firebase Crashlytics | Stack traces of crashes, **only if you opt in** in Settings → Nagram → Privacy. |
| Custom proxies (MTProto, SOCKS, Trojan, Shadowsocks, V2Ray) | The proxy you configure | Your Telegram traffic, encrypted as MTProto. |

If you build the app yourself with your own `TELEGRAM_APP_ID` /
`TELEGRAM_APP_HASH` and your own Firebase project, even those Google
endpoints can be substituted or removed.

## Local data

All chats, media, drafts, and settings are stored locally on your device in
the app's private storage area, encrypted at rest by Android. Removing the
app removes all of it. The app supports a local "passcode" lock; enabling it
prevents the app from being opened without the passcode and, optionally,
hides the app from the recents screen.

## Children

The app has no separate experience for children and Telegram's own minimum
age requirements apply. Refer to Telegram's privacy policy for details.

## Changes to this policy

If this policy changes, the new version will appear in this file with an
updated "Last updated" date. Material changes will be summarised in
[`CHANGELOG.md`](CHANGELOG.md).

## Contact

Privacy questions about Nagram Extera itself can be filed as a GitHub issue
on the project repository. For questions about Telegram's own data handling,
contact Telegram directly via <https://telegram.org/support>.

