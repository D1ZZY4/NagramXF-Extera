# Nagram Extera — Documentation

This directory is the canonical home for all long-form documentation about
Nagram Extera. The top-level [`README.md`](../README.md) is intentionally a
short landing page; everything that needs more than a few paragraphs lives
here.

## Index

| Document | What it covers |
|---|---|
| [`BUILDING.md`](BUILDING.md) | Building the APK locally, signing, FCM, troubleshooting. |
| [`FEATURES.md`](FEATURES.md) | The headline features that distinguish Nagram Extera from upstream. |
| [`ARCHITECTURE.md`](ARCHITECTURE.md) | High-level repository layout, module boundaries, native code. |
| [`RELEASE.md`](RELEASE.md) | The CI pipeline, automatic versioning, artifact naming, secrets. |
| [`PRIVACY.md`](PRIVACY.md) | Privacy policy. What we collect (nothing) and what Telegram itself collects. |
| [`SECURITY.md`](SECURITY.md) | Reporting vulnerabilities, supported versions, hardening notes. |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to file issues, propose changes, code style, commit conventions. |
| [`CHANGELOG.md`](CHANGELOG.md) | Human-curated release notes. |
| [`CREDITS.md`](CREDITS.md) | Detailed upstream and per-feature attribution. |

## Conventions used in this folder

- All documents are GitHub-flavoured Markdown and wrapped at ~80 columns.
- File names are `SCREAMING_SNAKE_CASE.md` to match the existing top-level
  `LICENSE`/`README.md` style.
- Code examples assume a POSIX shell unless noted.
- Anything time-sensitive (release dates, signing fingerprints, etc.) lives in
  [`CHANGELOG.md`](CHANGELOG.md) so the rest of the docs stay evergreen.

