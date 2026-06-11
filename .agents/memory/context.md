# Context

## Current state

- `dev` branch scaffolded with `.agents/` (memory, skills, rules) and `CLAUDE.md`.
- `dev` is in sync with `main` as of the scaffold commit.
- `main` is clean: no `.agents/`, no `CLAUDE.md` (both ignored in `.gitignore`,
  force-added on dev only).

## Branch model

- `main` — clean public branch. Never gets AI tooling.
- `dev` — workspace with all AI scaffolding. Work and build here.
- Promote only the code change to `main`, never `.agents/` or `CLAUDE.md`.

## Communication rule

Talk to the human in Indonesian (professional). All written artifacts (code,
docs, commits, memory) stay in English.

## Next

- Wait for a task in the CURRENT TASK block of the prompt, or run a proactive
  audit if it is empty.
