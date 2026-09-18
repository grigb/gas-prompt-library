## Migration Detection

Check if this project needs AGENTS.md migration to the split model:

1. Does `PROJECT-RULES.md` exist?
   - YES (with or without the migration marker) → Migration not required. Proceed to read it after `AGENTS.md`.
   - NO → Continue to step 2.

2. Does `AGENTS.md` contain project-specific sections?
   - Check for headings like:
     - `## Repository Guidelines`
     - `## Build, Test, and Development Commands`
     - `## Coding Style & Naming Conventions`
     - `## Testing Guidelines`
     - `## Project Overview`
   - If ANY found → Migration needed (offer to run migration).
   - If NONE found → `AGENTS.md` is already a clean global copy. Create `PROJECT-RULES.md` from `~/.agents/templates/PROJECT-RULES-TEMPLATE.md` (leave placeholders).

Integration with onboarding:
- After reading `AGENTS.md`, check migration status.
- If migration needed: inform user and offer to run it (never block work).
- If migrated: read `PROJECT-RULES.md` next.

