# Post-Review Gap Capture Follow-Up

Use this prompt as the second message to a Fable/top-model/high-effort Critical Review agent after it has produced, or is close to producing, its main report. It captures gaps the reviewer noticed but the original packet did not explicitly ask for, and makes those gaps easy for Master Steward or a project steward to assimilate later. Critical Review is the durable process; Fable is only the current model flavor.

## Paste-In Prompt

```text
You have already reviewed, or are currently reviewing, this GAS Critical Review packet. Before this session closes, produce a durable gap-capture addendum for things you noticed that the original prompt or packet did not explicitly ask you to cover.

Do not start a new broad review. Use your current context, the packet, the report you wrote or are writing, and any evidence you already inspected.

Write two outputs:

1. If you can still edit the main report, append a section titled:
   `Gap Capture Addendum - Unasked Findings And Patch Targets`

2. Always write a standalone addendum file so the handoff can be found later. Put it next to the main report when possible:
   - If the packet has `report_path`, use the same directory and filename base with `-gap-capture-addendum.md`.
   - If the packet is project-local and the report path is unclear, use:
     `<project_root>/.dev/ai/critical-review/reports/<critical_review_id>-gap-capture-addendum.md`
   - If this is a cross-project/GAS packet and the report path is unclear, use:
     `/Users/grig/.agents/.dev/ai/critical-review-queue/reports/<critical_review_id>-gap-capture-addendum.md`

The standalone addendum must include:

- Main packet path and main report path if known.
- Your transcript path if known.
- Whether the main report already exists, was updated, or could not be updated.
- `Unasked gaps noticed`: things that looked important but were not in the original review question.
- `Report patch targets`: exact sections of the main report that should be amended, clarified, or caveated.
- `Packet/process gaps`: missing evidence, stale evidence, overly narrow scope, bad mutation boundary, or prompt/process defects.
- `Patch queue`: concrete files, docs, tests, work orders, or status surfaces that should be patched next.
- For each gap: severity, why it matters, whether it is safe agent work, a true owner gate, an external blocker, or a future Critical Review trigger.
- `Do not do now`: any tempting work that should not be started from this session.
- `Handoff line`: one plain sentence the user can paste back to Master Steward, including the absolute addendum path.

Do not perform production, credential, secret, account, deploy, mainnet/custody, money, destructive, irreversible, or live-data actions. Do not invent gaps for completeness. If nothing material was noticed beyond the main report, write a short addendum that says that clearly and still includes the addendum path.

When finished, reply only with:

Completed.
Main report: <absolute path or unknown>
Gap addendum: <absolute path>
Owner action needed: yes/no - <one sentence>
```

## What This Prompt Is For

This prompt is for reviewer context recovery. It should be used while the high-effort session still has its review context, especially when the owner only needs to tell Master Steward that the work is done.

Good uses:

- The reviewer found packet-scope defects that should become process improvements.
- The reviewer noticed safe follow-up work outside the explicit review question.
- The report answers the formal question but does not capture adjacent risks.
- A live Fable window is expensive, and we want the reviewer's remaining context before the thread goes cold.

Bad uses:

- Reopening a completed review without new uncertainty.
- Asking for another broad architecture essay.
- Starting implementation that belongs in Codex/project lanes.
- Asking the reviewer to poll other sessions or wait for external work.

## Assimilation Rule

When a project steward or Master Steward receives the addendum path, treat the addendum as a supplement to the main report, not as a separate final review. Assimilate it by classifying each gap as:

- direct safe remediation;
- safe WO dispatch;
- true owner gate;
- external blocker;
- future Critical Review trigger;
- process/prompt improvement;
- no-action/parked.

Do not mark the project complete merely because the gap addendum was written.

