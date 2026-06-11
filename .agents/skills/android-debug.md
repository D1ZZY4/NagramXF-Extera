# Skill: android-debug

Reproduce and root-cause a reported bug or broken feature.

## When to use

A complaint in the task block (e.g. "Local Premium doesn't work"), a crash, or
a feature that does nothing.

## Steps

1. **Locate the feature.** Search by the user-facing string, the setting key, or
   the class name:
   ```
   grep -rn "Premium" TMessagesProj/src/main
   grep -rn "name=\"...\"" TMessagesProj/src/main/res/values
   ```
2. **Trace the path** from entry point (menu row, toggle, handler) to the code
   that should act on it. Read each hop; do not assume.
3. **Find the break:** missing wiring, a config flag never read, a wrong import
   or cast, a row added to the list but not handled, a string/resource mismatch.
4. **Fix the root cause**, not the symptom. Keep the change minimal.
5. **Verify** with the `gradle-build` skill, then re-trace the flow to confirm
   the feature now behaves.
6. Record the cause and fix in `.agents/memory/decisions.md`.

## Common Android-fork pitfalls

- A settings row declared and rendered but missing its `onItemClick` branch.
- Wrong cell/view class imported, causing a `ClassCastException` and a blank
  screen (real example seen in this repo's About activity).
- A `NekoConfig` / config flag added but never checked at the use site.
- Resource exists in one `values-*` locale but not the default, or duplicate
  string keys after a merge.
