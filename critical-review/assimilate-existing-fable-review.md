# Assimilate Existing Fable Review

Use this prompt when a project already has a Fable/top-model/high-effort Critical Review report or transcript and the project steward or agent needs to turn it into executable project state. Critical Review is the durable process; Fable is only the current model flavor.

## Paste-In Prompt

```text
Consume the existing Fable/top-model/high-effort review for this GAS Critical Review packet using the current GAS Critical Review skill.

Read first:
/Users/grig/.agents/skills/critical-review/SKILL.md

Then read the project packet, report, transcript path if supplied, project rules, current WO index, blocker/status files, and any existing Critical Review index.

Your job is not to ask me for broad permission or to summarize a review as if the project is done. Assimilate the report into project state and keep the project moving:

1. If a transcript path is available, inspect it before counting the run complete. Search for safeguard text such as `Fable 5's safeguards flagged this message`, fallback records such as `fallback claude-fable-5 -> claude-opus-4-8`, model counts, and actual model names. Classify the run as clean top-model result, fallback-supported result, partial/still-running result, or retry-needed result.
2. Record separate state fields: `review_complete`, `local_work_complete_for_this_pass`, `project_still_active`, and `project_complete`. A completed review is not project completion.
3. Classify every finding as exactly one of:
   - direct safe remediation;
   - safe WO dispatch;
   - true owner gate;
   - external blocker;
   - Fable/top-model direct-edit follow-up;
   - no-action/parked because already resolved or explicitly out of scope.
4. Derive the best durable posture from project principles, goals, and evidence.
5. Do not present weaker or bad-but-possible choices as owner options unless a real owner authority decision remains.
6. If the best posture is not knowable, say exactly what evidence is missing and create/dispatch safe evidence-gathering work.
7. Create or update WOs for safe work.
8. Dispatch safe workers for work that does not require owner authority, credentials/access, live data, signing, production, legal/financial/business authority, destructive action, or irreversible action.
9. Isolate true owner gates so they do not block unrelated safe follow-up work.
10. Name the next front: direct safe edits already made, Codex/project lane, blocker-supervisor lane, owner live/production gate, evidence loop, or future Critical Review trigger.
11. If no rerun is warranted, state: `no redundant top-model rerun now; continue Codex/project execution until new hard uncertainty appears`.
12. For LAN, PeerMesh, PM Social, UM, or MSF/SIGGRAPH-related work, include peers.social trust/auth substrate accounting: identity/lifecycle authority, tenant SSO, follow/unfollow proof, authenticated tenant-health proof, UM selective-disclosure adoption, or presentation/story proof.
13. Update the Critical Review packet, Critical Review index, WO index, project status, and steward/orchestration state according to project-local rules.
14. Prepare a second-pass Fable/top-model direct-edit prompt only if a new hard uncertainty or safe top-model-worthy direct-edit need remains.
15. Write a concise assimilation report with run classification, changed state, created/updated WOs, dispatched workers, true owner gates, external blockers, next front, owner action yes/no, and next direct-edit prompt path if created.

Do not run Fable/top-model yourself unless explicitly authorized in this session. Do not perform production, mainnet/custody, credential/secret, payment/money, deployment, external-account, destructive, or irreversible actions unless the packet explicitly authorizes that exact action.
```

## Expected Result

The project should end with either:

- a classified review result, safe follow-up work created/dispatched, and true owner gates isolated;
- a second-pass Fable direct-edit prompt ready for the owner to paste;
- or a specific blocker/missing-evidence statement explaining why the project cannot proceed.
