# Migrate AGENTS.md to Split Model (AGENTS.md + PROJECT-RULES.md)

This migration is non-destructive: it creates a backup before any changes.

## Step 1: Create Backup

```bash
cp ./AGENTS.md "./AGENTS.md.backup-$(date +%Y-%m-%d-%H-%M-%S)"
```

## Step 2: Identify Project-Specific Sections

Read the current `./AGENTS.md` and locate project-specific sections from the Sync Merge Protocol list:

- `## Repository Guidelines`
- `## Project Structure & Module Organization`
- `## Build, Test, and Development Commands`
- `## Coding Style & Naming Conventions`
- `## Testing Guidelines`
- `## Project Overview`
- `## Project Phase & Current Status`
- `## Architecture Overview`
- `## Repository Structure`
- `## Key Documentation`
- `## Development Commands`
- `## Future Development`
- `## Module Integration Points`
- `## Research Methodology`
- `## Team Workflow`
- `## Important Notes`
- `## Agent-Specific Instructions`
- `## AI Document Migration Status`

Helper (optional):
```bash
~/.agents/scripts/extract-project-sections.sh .
```

## Step 3: Create PROJECT-RULES.md From Template

Start from:
- Template: `~/.agents/templates/PROJECT-RULES-TEMPLATE.md`

Create `./PROJECT-RULES.md` and:
- Copy the template as the base.
- For each project-specific section found in the legacy `./AGENTS.md`:
  - Copy the full content into the matching section in `./PROJECT-RULES.md`.
  - Replace the placeholder text with the actual project content.
- For sections not found:
  - Keep the placeholder content from the template.
- Fill frontmatter:
  - `migration_date`: current timestamp
  - `project_name`: best available value from the legacy file or repo name
  - Keep `format_version: 1.0`

## Step 4: Verify Extraction Completeness

For each extracted section, verify:
- Content appears in `PROJECT-RULES.md`
- No truncation or unintended edits
- Headings match expected format

If you find custom project-specific sections (not in the list), place them under:
- `## Important Notes`, or
- `## Agent-Specific Instructions`, or
- the "Discovered Patterns / Known Issues" sections in `PROJECT-RULES.md`

## Step 5: Report Extraction Results

Provide a short report:

```
Extracted N sections to PROJECT-RULES.md:
  - Repository Guidelines (X lines)
  - Build, Test, and Development Commands (Y lines)
  - ...

Sections still placeholders (no project content found):
  - ...

Backup: AGENTS.md.backup-YYYY-MM-DD-HH-MM-SS
```

## Step 6: Replace AGENTS.md With Global Copy

```bash
cp ~/.agents/AGENTS.md ./AGENTS.md
```

## Step 7: Verify Replacement

```bash
diff ~/.agents/AGENTS.md ./AGENTS.md
# Expected: no differences
```

## Step 8: Validate Migration

```bash
~/.agents/scripts/validate-migration.sh .
```

If validation fails, fix issues before proceeding.

## Step 9: Rollback (If Needed)

```bash
cp "./AGENTS.md.backup-"* ./AGENTS.md
rm -f PROJECT-RULES.md
echo "Rollback complete. Original AGENTS.md restored."
```

## References

- `~/.agents/docs/MIGRATION-GUIDE.md`
- `~/.agents/docs/SYNC-MERGE-PROTOCOL.md` (legacy classification reference)

