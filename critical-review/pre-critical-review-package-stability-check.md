# Pre-Critical Review Package Stability Check

Use this prompt when a project may not actually be ready for Fable/top-model Critical Review because prerequisite WOs, blockers, evidence gaps, stale packets, idle human-in-the-loop waits, or project state drift remain.

This is a stabilization step, not a perfection gate. It should clear safe work and make the review packet genuinely useful before scarce Fable/top-model time is spent. It must not prevent review just because real blockers remain. If the remaining blocker is real owner authority, access, live data, external dependency, production/mainnet/custody risk, or another constraint that cannot be safely resolved by agents, record it clearly in the packet and readiness report, then mark the packet as conditional or blocked according to the actual review question.

## Minimal Paste-In Prompt

```text
Run the Pre-Critical Review Package Stability Check for [project/workstream/issue].

Use: /Users/grig/.agents/prompts/critical-review/pre-critical-review-package-stability-check.md
Report initial and final readiness status, artifact path, owner action yes/no, and next safe action. Do not launch Fable/top-model from this check.
```

## Operational Instructions For The Receiving Agent

If you receive the minimal paste-in prompt above, this file is the complete instruction set. Do not ask the owner to paste the checklist. Do not ask the owner for Fable launch approval. Do the safe readiness work directly, then report the readiness result. Do not broaden into a project-wide audit when a narrow packet/review target exists.

Read first:
/Users/grig/.agents/skills/critical-review/SKILL.md

Then inspect the project-local Critical Review packet/index, WO index, blocker/status files, project rules, project principles/goals, relevant reports, and current source/evidence artifacts.

Your job is to stabilize the project for Critical Review with lighter/policy-selected models and project workers before scarce Fable/top-model time is spent. Clear known safe work first, especially open WOs and idle "waiting for human" states that do not actually need owner authority. Do not ask the owner to approve Fable launch or unblock work that agents can safely continue.

For hard Critical Review/Fable-window work, preserve the owner model directive where the harness supports it: GPT-5.6 Sol Extra High; never Spark unless the owner explicitly overrides.

Return twice when work is needed:

1. Initial status return: after identifying the packet/target and first checker/readiness assessment, before safe fixes. Say whether work is needed and which safe work you will do.
2. Final status return: after safe fixes/dispatches complete, or immediately if no work was needed. Report `READY_FOR_REVIEW`, `READY_FOR_CONDITIONAL_REVIEW`, `BLOCKED_NEEDS_PACKET_FIX`, or `needs more safe churn`.

If this was relayed by Master Steward or GASCR, relay back using the provided return marker, target thread, and durable artifact path. If direct Codex thread relay is unavailable, write the artifact and explicitly state relay was unavailable.

Do this:

1. Identify the exact Critical Review packet or review target. If none exists, create or refresh the packet using the current GASCR skill.
2. Run or prepare the packet checker command, but do not treat a structural pass as enough if evidence is stale or WOs are blocking the review question.
3. Inventory open WOs and blockers that affect Critical Review readiness.
4. Classify each readiness item as:
   - safe worker dispatch now;
   - direct safe remediation;
   - true owner gate;
   - external blocker;
   - not relevant to this review.
5. Dispatch safe workers for relevant WOs that can be completed without owner authority, credentials/access, live data, signing, production, legal/financial/business authority, destructive action, or irreversible action.
6. Update WOs, blocker/status surfaces, Critical Review packet, and Critical Review index according to project-local rules.
7. If Universal Manifest or another project has accumulated old blocked WOs, prioritize the WOs that directly affect the review question and packet evidence first; do not let unrelated backlog hide the readiness-critical path.
8. Preserve project principles/goals and best-posture context in the packet so Fable can directly edit later instead of asking the owner to choose among weak options.
9. If real blockers remain after safe churn, do not manufacture fake readiness and do not over-block the review. Decide whether the packet is still useful for Fable as a conditional review, a review of the blocker itself, or a narrower review scope. Record that decision in the packet.
10. Stop before Fable/top-model dispatch. Do not ask for final launch approval from this check; report readiness status and let the normal Critical Review queue/orchestrator path handle final dispatch.

Return a readiness report with:
- packet path;
- checker command/result;
- safe WOs dispatched;
- WOs/blockers completed or still blocking;
- true owner gates;
- external blockers;
- whether the packet is READY_FOR_REVIEW, READY_FOR_CONDITIONAL_REVIEW, BLOCKED_NEEDS_PACKET_FIX, or needs more safe churn;
- whether any remaining blocker should be part of the Fable review question instead of a reason to delay it;
- initial status return summary if work was needed;
- final status return summary;
- owner action yes/no;
- result artifact path;
- the next safe action.

## Expected Result

The project should either be genuinely ready for Fable/top-model review-and-remediate, ready for a clearly scoped conditional review, or have a readiness-critical WO/blocker list that can churn before Fable is used.
