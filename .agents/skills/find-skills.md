# Skill: find-skills (entry skill)

This is the default skill. Run it at the start of every task to decide which
other skills apply, then apply them automatically without being told.

## Procedure

1. List the skills folder:
   ```
   ls .agents/skills/
   ```
2. Read the title and first lines of each skill file.
3. Match skills to the current task. A skill matches if the task touches its
   area (build, debugging, a subsystem, docs, git, etc.).
4. Apply every matching skill. Compose multiple when the work spans areas.
5. If the task needs a reusable procedure that no skill covers yet, write a new
   skill file here so future sessions reuse it. Keep each skill focused and
   short.

## Writing a new skill

- File name: short, kebab-case, ends in `.md` (e.g. `gradle-build.md`).
- Start with `# Skill: <name>` and a one-line purpose.
- Describe when to use it and the concrete steps. No fluff.
- Mention it in `.agents/memory/structure.md` if it changes how work is done.

## Always-on skills

- `find-skills` (this file) — run first, every task.
- Context7 lookups are governed by `.agents/rules/context7.md`; treat doc
  fetching as an always-on habit, not an optional skill.
