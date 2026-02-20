Read AGENTS.md for context. Then read PROJECT-RULES.md for onboarding. Then execute the following.

Context (already done):
- K2B provenance audit is complete for this project.
- Do NOT run another provenance audit in this run.
- Do NOT stop at K2B-only status reporting.

Authority artifacts:
- /Users/grig/work/repo/universalmanifest/.dev/ai/reports/k2b-provenance-audits/2026-02-19-04-28-33-universalmanifest-k2b-provenance-audit.md
- /Users/grig/work/repo/universalmanifest/.dev/ai/reports/k2b-provenance-audits/REPORT-INDEX.md
- /Users/grig/work/repo/universalmanifest/docs/CRITICAL-PATH.md
- /Users/grig/work/repo/universalmanifest/docs/STATE-OF-THE-PROJECT.md
- /Users/grig/work/repo/universalmanifest/docs/workorders/WO-0017-corpus-to-ia-and-journey-synthesis.md
- /Users/grig/work/repo/universalmanifest/docs/workorders/WO-0015-first-time-overview-and-visual-onboarding.md
- /Users/grig/work/repo/universalmanifest/docs/workorders/WO-0014-interactive-manifest-workbench.md

Primary objective for this run:
- Execute WO-0017 forward with concrete implementation deltas that close P1 backlog gaps.

Required WO sequence:
1) WO-0017-corpus-to-ia-and-journey-synthesis.md
2) WO-0015-first-time-overview-and-visual-onboarding.md
3) WO-0014-interactive-manifest-workbench.md

Mandatory execution requirements:
1) Start with WO-0017 and address at least one P1 gap from the audit backlog.
2) Produce real file changes in this run (minimum 3 files), including all of:
   - /Users/grig/work/repo/universalmanifest/.dev/ai/specs/2026-02-19-ia-delta-from-full-corpus.md
   - /Users/grig/work/repo/universalmanifest/docs/workorders/WO-0017-corpus-to-ia-and-journey-synthesis.md
   - At least one downstream materialization file:
     - /Users/grig/work/repo/universalmanifest/docs/journeys/README.md
     - /Users/grig/work/repo/universalmanifest/docs/workorders/WO-0012-user-journeys-and-e2e-test-suite.md
     - /Users/grig/work/repo/universalmanifest/docs/DECISIONS.md
     - /Users/grig/work/repo/universalmanifest/docs/STATE-OF-THE-PROJECT.md
3) Update WO-0017 acceptance-criteria progress with timestamped evidence links.
4) Run strict validator with explicit artifact root:
   - /Users/grig/.agents/scripts/validate-k2b-gates.sh /Users/grig/work/repo/universalmanifest --artifact-root /Users/grig/work/repo/universalmanifest/.dev/ai --strict
5) Save strict validator output to:
   - /Users/grig/work/repo/universalmanifest/.dev/ai/reports/2026-02-19-um-strict-validator.log

Momentum rule (anti-stall):
- If WO-0017 movement is blocked, immediately advance WO-0015 criterion (reader-testing evidence) in the same run.
- Do not end the run without concrete WO-linked file edits unless hard-blocked by missing authority input.

Disallowed output pattern:
- Do not end with only "applied/report created."
- Do not return file names or paths as commands.
- Do not repeat the prior provenance-audit summary as the main output.

Mandatory report for this run:
- /Users/grig/work/repo/universalmanifest/.dev/ai/reports/2026-02-19-wo-0017-execution-progress.md

Report must include:
- which gap IDs were addressed (`GAP-K2B-001` to `GAP-K2B-005`) and status changes
- exact files changed
- WO acceptance criteria moved (WO-0017/0015/0014 where applicable)
- strict validator command + exit code
- blockers (if any) with evidence path
- exact next 3 executable shell commands (full commands only)

Final chat response format:
- Project root
- Resumed WO
- Gap IDs addressed
- Files changed
- Acceptance criteria moved
- Strict validator command and exit code
- Blockers
- Exact next 3 commands
