# Decisions

Format: `YYYY-MM-DD` — decision — reason.

- 2026-06-12 — Keep AI tooling (`.agents/`, `CLAUDE.md`) on `dev` only; ignore
  it in `.gitignore` and force-add on dev. Reason: `main` must look like a pure,
  human-authored repo with no AI indicators, while dev keeps full agent context.
- 2026-06-12 — Application id is `org.nagram.extera` (fixed from the earlier
  typo `orang.nagram.extra`). Reason: correct package naming for the fork.
- 2026-06-12 — Version is set manually in `gradle.properties`
  (`APP_VERSION_CODE`, `APP_VERSION_NAME`), not derived from git. Reason: matches
  the actual build config; earlier README claim of auto-versioning was wrong.
