# Rule: Context7 First

Before writing any code that calls a library, SDK, Gradle DSL, AndroidX, or
Telegram-Android API, fetch current documentation with the Context7 MCP tool.
Do not rely on memory for signatures, configuration keys, or behavior that
changes between versions.

## Steps

1. `resolve-library-id` with the library name (e.g. "AndroidX", "Gradle",
   "Firebase", "ExoPlayer"), unless an exact `/org/project` id is already known.
2. `get-library-docs` with the resolved id and a specific topic (the class,
   method, or concept you need).
3. Implement from the fetched docs.

## When it is mandatory

- Gradle build script / AGP DSL changes.
- AndroidX, Material, ExoPlayer, Firebase, ML Kit, Room, OkHttp APIs.
- Any `NoSuchMethodError`, `NoClassDefFoundError`, or resource-linking failure
  tied to a library version.
- Whenever you are not 100% sure of the exact signature in the installed version.

## Fallback when Context7 returns nothing

Read the actual source in the repo (`TMessagesProj/src`, `jni/`, Gradle files)
or inspect the dependency. Reading real source always beats guessing.

Priority: Context7 docs > repo source > guessing. Never guess an API signature.
Record reusable findings in `.agents/memory/decisions.md`.
