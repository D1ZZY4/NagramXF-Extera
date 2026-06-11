# CLAUDE.md — Nagram Extera (dev branch)

Agent rules for this repository. This file and `.agents/` exist on **dev only**.
`main` is the clean public branch and must never contain them.

## Project

- Android Telegram client. Soft fork of Telegram for Android, downstream of
  Nagram X / Nagram XF, with ports from AyuGram, Cherrygram, exteraGram, OctoGram.
- Java + Kotlin (JVM 21), single Gradle module `:TMessagesProj`, native under
  `TMessagesProj/jni/`.
- AGP 9.1, NDK 27.2, build-tools 36, min SDK 27 / target 36.
- Application id `org.nagram.extera`. Version is manual in `gradle.properties`.

## Start every session with context recovery

Read these before touching code, in order:
`.agents/memory/MEMORY.md` → `context.md` → `progress.md` → `decisions.md` →
`structure.md` → `build.md`. Then read `.agents/skills/find-skills.md` and apply
matching skills.

## Hard rules

1. **Do not break the build or regress features.** Smallest change that fixes
   the problem. Check all callers before editing or deleting shared code.
2. **Verify after every change:** configure → `assembleDebug` (single ABI is
   fine) → trace the affected flow. Build must be green.
3. **Use Context7 first** for any library/SDK/Gradle/AndroidX API. Never guess
   signatures. See `.agents/rules/context7.md`.
4. **Branch discipline:** all AI tooling stays on `dev`. When promoting a fix to
   `main`, move only the code change — never `.agents/` or `CLAUDE.md`.
5. **Memory is exactly 6 files** under `.agents/memory/`. Update affected ones
   before each commit.
6. **Commit trailers** (every commit):
   ```
   Author-by: D1ZZY4 <176969112+D1ZZY4@users.noreply.github.com>
   Signed-off-by: D1ZZY4 <176969112+D1ZZY4@users.noreply.github.com>
   ```
   Do not push unless asked.

## Communication

Talk to the human in Indonesian (professional). Keep all written artifacts —
code, comments, docs, commit messages, memory files — in English.
