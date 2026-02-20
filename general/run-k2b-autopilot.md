Read `AGENTS.md` and `PROJECT-RULES.md` first, then execute.

Goal:
Run Knowledge-to-Build in zero-touch autopilot mode for this project:
- establish or repair K2B baseline,
- verify provenance quality,
- and resume critical-path execution in the same run.

Do not stop at report-only output unless hard-blocked.

Context resolution:
- `PROJECT_SOURCE_ROOT`: current working directory (`pwd`)
- `PROJECT_NAME`: from `PROJECT-ID.md` (`project:`, `id:`, or `Project Name`), else repo basename
- `K2B_ARTIFACT_ROOT` precedence:
  1. explicit policy in `PROJECT-RULES.md`/`AGENTS.md`/project governance docs
  2. existing `PROJECT_SOURCE_ROOT/.dev/ai`
  3. fallback `PROJECT_SOURCE_ROOT/.dev/ai`

Autopilot flow (mandatory sequence):
1. Baseline detection:
   - If Stage -1/0 artifacts are missing/stale, execute:
     - `/Users/grig/.agents-gas-prompt-library/general/integrate-Knowledge-to-Build-system.md`
2. Provenance quality pass:
   - Execute:
     - `/Users/grig/.agents-gas-prompt-library/general/run-k2b-provenance-audit.md`
3. Auto-repair if audit is incomplete:
   - If invalid next commands, missing lens evidence, or missing pivot mapping:
     - `/Users/grig/.agents-gas-prompt-library/general/repair-k2b-provenance-audit-report.md`
4. Triage decision:
   - Execute:
     - `/Users/grig/.agents-gas-prompt-library/general/respond-to-k2b-agent-report.md`
5. Critical-path movement:
   - If the bottleneck is design synthesis (IA/UX/UI/structured design data), execute:
     - `/Users/grig/.agents-gas-prompt-library/general/run-k2b-ia-ux-ui-design-pipeline.md`
   - Then continue triage/resume logic from this autopilot flow.
   - If strict clean + mandatory artifacts exist, resume first unblocked active/open WO and move acceptance criteria in this run.
   - If no executable WO exists, create one for highest-priority K2B gap and start first acceptance step.

Hard constraints:
- Use absolute paths only.
- Next 3 commands must be executable shell commands (no bare filenames/paths).
- Run strict validator with explicit artifact root:
  - `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT" --strict`
- If validator requires Bash 4+, use explicit runtime path and record it.

Mandatory run report:
- `K2B_ARTIFACT_ROOT/reports/K2B-AUTOPILOT-RUN-<YYYY-MM-DD-HH-MM-SS>.md`

Report must include:
- resolved roots and policy decision
- which autopilot steps executed (1-5) and outcomes
- strict validator command/exit code/log path
- files changed
- WO resumed (or created) and acceptance criteria moved
- blockers requiring user decision
- exact next 3 executable shell commands

Final chat response format:
- Resolved project source root
- Resolved K2B artifact root
- Autopilot steps executed
- Strict validator command and exit code
- Files changed
- WO resumed/created and acceptance criteria moved
- Blockers
- Exact next 3 commands
