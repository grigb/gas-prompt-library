Read AGENTS.md and PROJECT-RULES.md for context first, then execute.

Goal:
Run a full K2B provenance audit for this project and produce one timestamped markdown report that is comprehensive enough for iterative gap closure.

Authority references (follow these if any conflict exists):
- /Users/grig/.agents/docs/methodologies/k2b-provenance-audit-process.md
- /Users/grig/.agents/docs/methodologies/knowledge-to-build-method.md
- /Users/grig/.agents/modes/KNOWLEDGE-TO-BUILD-MODE.md
- /Users/grig/.agents/docs/vision/VISION-ADDENDUM-knowledge-index-to-build-mandate.md
- /Users/grig/.agents/scripts/validate-k2b-gates.sh
- /Users/grig/.agents/templates/k2b/K2B-PROVENANCE-AUDIT-REPORT-TEMPLATE.md

Context resolution (do not ask user for placeholders):
- PROJECT_SOURCE_ROOT: current working directory (`pwd`)
- PROJECT_NAME: resolve from PROJECT-ID.md (`project:`, `id:`, or `Project Name`), else repo basename
- K2B_ARTIFACT_ROOT precedence:
  1. explicit `K2B_ARTIFACT_ROOT:` in project rules/docs
  2. existing `PROJECT_SOURCE_ROOT/.dev/ai`
  3. fallback `PROJECT_SOURCE_ROOT/.dev/ai`

Output location and naming (mandatory):
- Create directory if missing:
  - `K2B_ARTIFACT_ROOT/reports/k2b-provenance-audits/`
- Create main report file:
  - `K2B_ARTIFACT_ROOT/reports/k2b-provenance-audits/<YYYY-MM-DD-HH-MM-SS>-<project-name>-k2b-provenance-audit.md`
- Update or create index:
  - `K2B_ARTIFACT_ROOT/reports/k2b-provenance-audits/REPORT-INDEX.md`

Mandatory audit tasks:
1. List all files actually read (absolute path + why each file was read).
2. Compute Stage -1, Stage 0, and G1-G7 status with evidence file paths.
3. Run validator:
   - `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT"`
   - `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT" --strict`
   - Record both commands, both exit codes, summaries, and strict-log path.
4. Build complete ingestion inventory:
   - selected/deferred/excluded counts
   - internal/external source counts
   - selected-source adequacy mapping against active/open work orders and active decision files
5. For every selected source, produce a provenance chain:
   - source -> disposition -> ingestion -> extraction -> synthesis/spec -> gate evidence -> build/workorder -> implementation evidence (if any)
   - classify status: implemented / partially-implemented / not-implemented
6. Provide dedicated external-source provenance section showing where outside-project knowledge changed design or implementation.
   - If external source count is `0`, include explicit adjudication with evidence paths proving this was intentional and complete.
7. Create gap backlog entries with IDs (`GAP-K2B-###`) and concrete remediation targets.
8. Add iteration delta against latest prior provenance audit report (if one exists).
9. End with exact next 3 executable shell commands for highest-impact closure.
   - Command 1 must be `cd "$PROJECT_SOURCE_ROOT"`.
   - Command 2 must run the highest-priority evidence/gap-closure check.
   - Command 3 must run strict validator and write output to `reports/k2b-provenance-audits/<timestamp>-strict-validator.log`.
   - Bare paths/filenames are invalid command entries.

Quality constraints:
- Use absolute paths only.
- No markdown tables.
- Every claim must cite evidence path(s).
- If evidence is missing, explicitly state: `not provable with current artifacts`.
- If external source count is `0`, external adjudication is mandatory.
- If selected-source adequacy mapping is missing, the audit is incomplete.
- If any of the 3 next-action entries is not an executable shell command, the audit is incomplete.

Final response format in chat:
- Resolved project source root
- Resolved K2B artifact root
- Report path
- Report index path
- Validator baseline command and exit code
- Validator strict command and exit code
- Strict validator log path
- Total files reviewed
- Source counts (selected/deferred/excluded; internal/external)
- Gap count by priority (P1/P2/P3)
- Exact next 3 commands
