# Rule: Do Not Break Anything

This is a large, working Android app. Not regressing it is the top priority,
above speed and above cleanliness.

- Make the smallest change that fixes the problem. No drive-by rewrites or
  unrelated refactors in the same commit.
- Before editing or deleting shared code, find every caller and understand the
  contract:
  ```
  grep -rn "SymbolName" TMessagesProj/src/main
  ```
- Never remove a class, method, resource id, or string without checking
  references first. Update all callers before removing.
- Keep the build green and public APIs stable. If a fix can't be done without
  breaking something, stop and reconsider.
- Committed code is clean: no conflict markers, no commented-out dead code, no
  "TODO: fix later", no hardcoded credentials or magic values introduced.
- Prove correctness by tracing the affected flow (activity / fragment / handler
  / config) end to end, not just by a clean build.
