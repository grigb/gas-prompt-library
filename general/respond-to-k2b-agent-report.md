Read AGENTS.md for context. Then read PROJECT-RULES.md for onboarding. Then execute the following.

Goal:
Given the latest K2B status report from this project agent, decide whether to:
1) keep the agent in K2B remediation, or
2) return it to project critical-path execution.

Required inputs:
- latest K2B report path (or paste report body)
- latest validator command and exit code
- current WO index path
- project state/critical-path path

Decision logic:
1. If validator exit is non-zero OR strict warnings/fails exist:
   - stay in K2B remediation mode
   - output exact remediation steps with file targets and commands
2. If next-3-commands output contains any bare filename/path instead of executable shell commands:
   - treat report as incomplete
   - stay in K2B remediation mode
   - require corrected report with command-validity check
3. If report lacks keyword/query-lens evidence path or lacks external-pivot mapping:
   - treat report as incomplete
   - stay in K2B remediation mode
   - require a repair pass that adds missing evidence sections
4. If validator strict is clean and mandatory K2B artifacts exist:
   - switch to critical-path mode
   - output WO sequence to resume and explicitly mark K2B follow-ups as non-blocking

Mandatory output file:
- <K2B_ARTIFACT_ROOT>/reports/<YYYY-MM-DD>-k2b-report-triage-and-next-directive.md

Report must include:
- project root and artifact root
- report reviewed (path)
- validator baseline/strict commands and exit codes
- decision: `k2b_remediation` or `critical_path_resume`
- rationale with evidence paths
- exact files to touch next
- command-validity check result for next 3 commands
- exact next 3 executable shell commands

Final chat response format:
- Project root
- Decision mode
- Why
- Files to update next
- Exact next 3 commands
