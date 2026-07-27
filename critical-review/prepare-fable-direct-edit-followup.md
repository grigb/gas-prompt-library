# Prepare Fable Direct-Edit Follow-Up

Use this prompt when safe follow-up work from a first Fable/top-model/high-effort Critical Review has been assimilated and the project needs another high-effort pass that edits the project directly. Critical Review is the durable process; Fable is only the current model flavor.

## Paste-In Prompt

```text
Prepare a second-pass Fable/top-model direct-edit prompt for this GAS Critical Review packet.

Read first:
/Users/grig/.agents/skills/critical-review/SKILL.md

Then read the current Critical Review packet, the prior Fable report, current project rules, project principles/goals, created/completed follow-up WOs, verification evidence, current Critical Review index, WO index, blocker/status files, and any existing direct-edit prompt.

Create one paste-ready prompt or a durable Markdown prompt-pack file if there is more than one prompt. The visible prompt should use normal local engineering wording and preserve safety boundaries without stacking high-risk terms in the first paragraph. The prompt must:

1. Start with `Provide your session transcript absolute path.`
2. Include `Directory:` with the absolute project root.
3. Include `Thread title:` for an exact existing harness-visible thread, immediately followed by the prompt/packet path, plus `Continue in this same thread. Do not create or rename a thread.` If a new thread is intended, use `New thread title:` instead.
4. Include mode label: `review-and-remediate` unless the packet requires `review-only`, `decision-only`, or `conditional review`.
5. State the current project/workstream objective and the best durable posture from project principles, goals, and evidence.
6. State what the prior pass found, actual model outcome if detectable, fallback/safeguard status if present, and what has changed since then.
7. Name completed safe WOs, active WOs, unresolved findings, true owner gates, external blockers, and remaining direct-edit items.
8. Require an execution-ledger marker before mutation starts: packet path, thread title, transcript path if known, run/session id, requested model, actual model if detectable, started timestamp, status, report path, and duplicate-run/report detection.
9. Tell the high-effort model to directly edit safe local files inside the packet's mutation boundary.
10. Tell the model not to stop at review-only findings when the packet authorizes local remediation.
11. Tell the model to verify any change it makes.
12. Tell the model to write a report to the packet's `report_path` or a timestamped follow-up report path.
13. Require the report to include recommendation, changed files, rationale, verification output, remaining findings, follow-up WOs, review state fields, next front, and any unresolved true owner gates.
14. Forbid production, mainnet/custody, credential/secret, payment/money, deployment, external-account, destructive, legal/financial/business authority, or irreversible actions unless the packet explicitly authorizes that exact action.
15. Make historical versus current review state explicit so the project does not drift between `review_complete`, `local_work_complete_for_this_pass`, `project_still_active`, and `project_complete`.
16. If no rerun is warranted, say `no redundant top-model rerun now; continue Codex/project execution until new hard uncertainty appears`.
17. For LAN/PeerMesh/PM Social/UM/MSF/SIGGRAPH-related work, include peers.social trust/auth substrate accounting.
18. Include relay back instructions: return marker, target thread or fallback artifact, report/result path, owner action yes/no.
19. Preserve the owner model directive for hard Critical Review/Fable-window work: GPT-5.6 Sol Extra High where supported; never Spark unless the owner explicitly overrides.

Also update the project-local Critical Review packet/index/status surfaces to point to the prepared direct-edit prompt, without claiming Fable has run.
```

## Expected Result

Return:

- absolute path to the prepared Fable direct-edit prompt;
- packet path;
- prior Fable report path;
- intended report path;
- checker command/result if run;
- what remains owner-gated or externally blocked.
- execution ledger path;
- return marker and relay-back target or fallback artifact;
- collision-domain/duplicate-dispatch note.
