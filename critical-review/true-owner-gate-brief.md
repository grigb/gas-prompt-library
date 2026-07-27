# True Owner Gate Brief

Use this prompt only when a Critical Review finding leaves a real owner-authority decision after safe work has been separated, dispatched, or explicitly recorded as impossible without the owner. Do not use owner gates as a substitute for project execution.

## Paste-In Prompt

```text
Create a true owner-gate brief for the remaining GAS Critical Review issue.

Read first:
/Users/grig/.agents/skills/critical-review/SKILL.md

Before writing the brief, separate safe follow-up work from the owner gate. If any safe WO dispatch or direct safe remediation remains, create/update/dispatch that work first unless it conflicts with the owner gate.

The brief must:

1. State the recommended best posture first.
2. Ask only for the owner authority actually required.
3. Avoid presenting weak or bad-but-possible options as peers.
4. Explain why the gate cannot be resolved by agents from existing evidence.
5. Name what safe work is already complete, running, or queued.
6. State consequences of approving, declining, or holding.
7. Use stable reply handles if a decision is unavoidable.
8. Preserve project safety boundaries: no production, mainnet/custody, credential/secret, payment/money, deployment, external-account, destructive, or irreversible actions without explicit owner authorization.
9. State the next front that continues regardless of the owner gate when safe: Codex/project lane, blocker-supervisor lane, evidence loop, future Critical Review trigger, or direct safe edits already complete.
10. If the high-effort rerun is held, use project-motion language: `no redundant top-model rerun now; continue Codex/project execution until new hard uncertainty appears`.

Return the brief path and the exact owner reply handles. Do not ask for generic `go` unless it approves only the explicitly recommended owner action.
```

## Expected Result

The owner sees a narrow authority gate, not a broad menu or a backlog disguised as a decision.
