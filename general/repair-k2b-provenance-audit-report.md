Read AGENTS.md and PROJECT-RULES.md for context first, then execute.

Goal:
Repair the latest K2B provenance audit output so it conforms to the canonical report contract and quality gates.

Authority references (follow these if any conflict exists):
- /Users/grig/.agents/docs/methodologies/k2b-provenance-audit-process.md
- /Users/grig/.agents/templates/k2b/K2B-PROVENANCE-AUDIT-REPORT-TEMPLATE.md
- /Users/grig/.agents/scripts/validate-k2b-gates.sh

Context resolution:
- PROJECT_SOURCE_ROOT: current working directory (`pwd`)
- PROJECT_NAME: resolve from PROJECT-ID.md (`project:`, `id:`, or `Project Name`), else repo basename
- K2B_ARTIFACT_ROOT precedence:
  1. explicit `K2B_ARTIFACT_ROOT:` in project rules/docs
  2. existing `PROJECT_SOURCE_ROOT/.dev/ai`
  3. fallback `PROJECT_SOURCE_ROOT/.dev/ai`

Repair protocol:
1. Locate latest report under `K2B_ARTIFACT_ROOT/reports/k2b-provenance-audits/`.
2. Validate it against the current report template and process contract.
3. If malformed sections exist, generate a corrected replacement report with a new timestamped filename.
4. Keep the original report; add a supersession note in the new report intro (`supersedes: <old_report_path>`).
5. Update `REPORT-INDEX.md` to include the new report and note supersession.

Mandatory corrections:
1. Run both validators and record both:
   - `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT"`
   - `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT" --strict`
2. Persist strict output log to:
   - `K2B_ARTIFACT_ROOT/reports/k2b-provenance-audits/<timestamp>-strict-validator.log`
3. Add selected-source adequacy check:
   - map selected sources to active/open work orders and active decision files
   - create gaps for uncovered work items
4. Handle external coverage correctly:
   - if external count > 0, provide external provenance chains
   - if external count = 0, provide explicit adjudication and evidence proving intentional zero
5. Fix Next Actions section:
   - exactly 3 entries
   - each entry must be an executable shell command
   - command 1 must be `cd "$PROJECT_SOURCE_ROOT"`
   - command 3 must run strict validator and tee/write log
   - bare filenames/paths are invalid and must be removed

Quality constraints:
- Use absolute paths only.
- No markdown tables.
- Every claim must cite evidence path(s).
- If evidence is missing, explicitly state: `not provable with current artifacts`.

Final response format in chat:
- Resolved project source root
- Resolved K2B artifact root
- Old report path
- New report path
- Report index path
- Validator baseline command and exit code
- Validator strict command and exit code
- Strict log path
- Total files reviewed
- Source counts (selected/deferred/excluded; internal/external)
- Gap count by priority (P1/P2/P3)
- Exact next 3 commands
