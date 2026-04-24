# Contributing

Thanks for your interest in improving Nagram Extera. This file collects the
small set of conventions the project follows so contributions land cleanly.

## Filing issues

- Use the templates under [`.github/ISSUE_TEMPLATE`](../.github/ISSUE_TEMPLATE).
- Always include the **exact** `versionName(versionCode)` from
  Settings → About. CI builds embed the short commit SHA in the version
  name; that string is what we need.
- For crashes, attach the full stack trace. If it occurs only with a
  specific account or chat, say so without disclosing private contents.
- Do **not** file security issues here. See [`SECURITY.md`](SECURITY.md).

## Pull requests

1. Branch off `main`. Keep PRs focused; one feature or fix per PR.
2. Follow existing code style. The project mixes Java and Kotlin; match the
   surrounding file. Indentation is 4 spaces in Java, 4 in Kotlin, no tabs.
3. Gate every fork-specific feature behind a config flag (`NaConfig` or the
   appropriate equivalent) so upstream cherry-picks stay mechanical.
4. Update or add localized strings in `TMessagesProj/src/main/res/values/`.
   English is required; other locales are welcome but optional.
5. If your change has any user-visible effect, add an entry to
   [`CHANGELOG.md`](CHANGELOG.md) under the `Unreleased` section.
6. Run `./gradlew :TMessagesProj:assembleDebug` locally before pushing. CI
   will run the full release build.

## Commit messages

Commit messages should follow the lightweight convention used by the rest of
the lineage:

```
<area>: <short imperative summary>

<optional body explaining the why>
```

`<area>` is typically a directory or feature name (`ui`, `proxy`,
`translation`, `build`, etc.). Keep the summary line under 72 characters.

Special tokens recognised by CI:

- `[skip upload]` — build the APK but do not publish it to the release
  channels.
- `[skip ci]` — do not run CI for this commit at all.

Do **not** include the names of tools, agents, or AI assistants in commit
messages.

## Code review

- Be specific. "This loop allocates per frame" is more useful than
  "looks slow".
- Prefer suggestions over demands; the project has many constraints from
  upstream that reviewers may not be aware of.
- Reviewers should look at the diff *and* the surrounding code; the
  upstream Telegram codebase has many implicit invariants.

## Licensing

By contributing you agree that your changes are licensed under the project's
[GPL-2.0 license](../LICENSE), the same terms as the rest of the codebase
and as upstream Telegram for Android.

