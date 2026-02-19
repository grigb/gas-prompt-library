Read AGENTS.md for context. Then read PROJECT-RULES.md for onboarding. Then execute the following.

Context (already done):
- K2B provenance audit repair was completed by Codex authority.
- Do NOT run another K2B provenance audit in this run.

Authority artifacts:
- /Users/grig/work/lan/lan-platform/.dev/ai/reports/k2b-provenance-audits/2026-02-19-05-00-58-lan-platform-k2b-provenance-audit.md
- /Users/grig/work/lan/lan-platform/.dev/ai/reports/k2b-provenance-audits/REPORT-INDEX.md
- /Users/grig/work/lan/lan-platform/.dev/ai/workorders/WO-interface-first-foundation-groups.md
- /Users/grig/work/lan/lan-platform/docs/product/decisions/2026-02-18-interface-first-foundation-gate.md

Primary objective for this run:
- Execute Group A critical-path work with concrete deliverable movement.

Required Group A sequence:
1) WO-lan-screen-onboarding-canvas
2) WO-lan-ember-gallery-navigation
3) WO-lan-tv-native-player-app-kiosk-mode

Mandatory execution requirements:
1) Start with WO-lan-screen-onboarding-canvas and complete at least one concrete acceptance-step delta.
2) Produce real file changes (code and/or specs), not status-only reporting.
3) Update WO progress notes with timestamp and what moved.
4) Keep Group B backend execution on hold (foundation gate not open).

Minimum change bar (anti-stall):
- At least 2 files must be updated under LAN project scope and linked to Group A WOs.
- If WO-lan-screen-onboarding-canvas is blocked, immediately switch to WO-lan-ember-gallery-navigation and complete one concrete delta there in the same run.

Validation command (required):
- /Users/grig/.agents/scripts/validate-k2b-gates.sh /Users/grig/work/lan/lan-platform --artifact-root /Users/grig/work/lan/lan-platform/.dev/ai --strict

Required run report:
- /Users/grig/work/lan/lan-platform/.dev/ai/reports/2026-02-19-interface-first-critical-path-resume.md

Report must include:
- which Group A WO was advanced first and why
- exact files changed
- what acceptance criteria moved
- blockers requiring user/CEO decision
- strict validator command + exit code
- exact next 3 executable shell commands (no bare filenames/paths)

Disallowed output pattern:
- Do not return only a K2B report summary.
- Do not return file names as commands.
- Do not stop without concrete WO-linked file changes unless hard-blocked; if hard-blocked, include exact blocker evidence path and fallback WO executed.

Final chat response format:
- Project root
- Resumed WO
- Files changed
- Acceptance criteria moved
- Strict validator command and exit code
- Blockers
- Exact next 3 commands
