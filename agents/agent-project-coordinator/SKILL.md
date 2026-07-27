---
name: project-coordinator
description: >
  DEPRECATED - folded into the Project Manager on 2026-07-12. Do not activate this
  role. Task decomposition, dependency mapping, progress tracking, coordination
  structure, and actionable project plans are owned by the Project Manager at
  /Users/grig/.agents/prompts/agents/agent-project-manager/SKILL.md.
metadata:
  author: gas-system
  version: "2.0"
  category: business-operations
  scope: single-project
  status: deprecated
  deprecated_on: 2026-07-12
  superseded_by: agent-project-manager
  tiers: [1, 2, 3]
  harnesses: [claude]
  tags: [deprecated, superseded]
---

After the required startup read of
`/Users/grig/.agents/style-guides/writing/OWNER-FACING-AGENT-MESSAGE-STYLE-GUIDE.md`,
apply `/Users/grig/.agents/style-guides/writing/OWNER-FACING-AGENT-MESSAGE-RUNTIME-CONTRACT.md`
before every owner-facing message as the short pre-send check. The runtime
card does not replace the full guide or this role's existing choice/`go`,
first-turn/re-entry, `AGENT-STATE`, gate, absolute-path, and closeout rules.

# PROJECT COORDINATOR - RETIRED

Folded into the **Project Manager** on 2026-07-12 per the owner-accepted Project
Manager design review (findings F-11, F-14, F-15; target state TS-2.1). Two roles
claiming the project-manager charter was the defect; there is now exactly one.

- `/Users/grig/.agents/.dev/ai/audits/2026-07-12-21-54-09Z-project-manager-design-review-findings.md`
- `/Users/grig/.agents/docs/standards/PROJECT-MANAGER-TARGET-STATE-STANDARD.md`

**Do not activate this role. Use the Project Manager:**
`/Users/grig/.agents/prompts/agents/agent-project-manager/SKILL.md`

It owns everything this prompt claimed - task decomposition, dependency mapping,
progress tracking, and actionable project plans - plus proposal-to-WO coverage,
workstream drift, gate control, and execution-readiness routing. If it is not the
right fit: raw context capture and strategy go to `agent-project-steward`;
execution orchestration to `agent-orchestrator`; new-project registration to
`/Users/grig/.agents/prompts/general/PROJECT-INCEPTION.md`.
</content>
</invoke>
