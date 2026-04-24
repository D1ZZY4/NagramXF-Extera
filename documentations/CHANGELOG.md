# Changelog

All notable changes to Nagram Extera are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and this project
adheres to a rolling release model — version numbers are derived
automatically from git metadata (see [`BUILDING.md`](BUILDING.md)).

## [Unreleased]

### Added

- Rebranded from **Nagram XF** to **Nagram Extera**.
- Comprehensive [`documentations/`](.) folder covering building, release,
  privacy, security, contributing, architecture, features, and credits.
- Fully automatic versioning: `versionCode` is now derived from
  `git rev-list --count HEAD` and `versionName` from the current short SHA.
  No more manual bumps.
- Hardened [`release.yml`](../.github/workflows/release.yml) workflow with
  full-history checkouts, deterministic SDK pinning, ccache, retry-friendly
  caching, build-log capture on failure, and Telegram delivery of failure
  archives.

### Changed

- APK output naming switched from `NagramXF-…` to `NagramExtera-…`.
- App display name (`strings_nax.xml` `NagramX`) is now `Nagram Extera`.
- Top-level `README.md` rewritten as a short landing page; long-form docs
  moved into [`documentations/`](.).

### Removed

- Hard-coded `verCode = 1243` in `TMessagesProj/build.gradle`.

---

For older history, see the upstream [Nagram XF releases page] and the
underlying [Nagram X commit log].

[Nagram XF releases page]: https://github.com/Keeperorowner/NagramXF/releases
[Nagram X commit log]: https://github.com/risin42/NagramX/commits

