# CREATE EXEMPLARY PROJECT STATE PACK (LAN)

Use this prompt to create or refresh the LAN holistic documentation pack with concise onboarding and evidence-rich detail.

---

You are creating or updating a **Project State Pack** for Local Artist Network.

## Fixed Project Inputs

- Project root: `/Users/grig/work/lan/lan-platform`
- Project name: `Local Artist Network (lan-platform)`
- Current phase: `Post-Board Demo Reset -> Design + Ingestion Audit -> Phase 2 Execution (Delegated)`
- Canonical state file: `/Users/grig/work/lan/lan-platform/.dev/ai/STATE-OF-THE-PROJECT.md`
- Canonical work-order index: `/Users/grig/work/lan/lan-platform/.dev/ai/workorders/WO-INDEX.md`
- Canonical decision directory: `/Users/grig/work/lan/lan-platform/.dev/ai/decisions/`
- Canonical ingestion ledger: `/Users/grig/work/lan/lan-platform/.dev/ai/ingestion/LEDGER.md`
- Canonical milestone pipeline: `/Users/grig/work/lan/lan-platform/.dev/ai/planning/milestone-pipeline.md`
- Output docs directory: `/Users/grig/work/lan/lan-platform/docs/lan-holistic`

## Non-Negotiables

- Do not invent status or completion claims.
- Anchor important claims to concrete absolute paths.
- Use explicit dates (`YYYY-MM-DD`).
- Keep train-of-logic separation:
  - design/provenance
  - prototype/demo
  - deployment/operations
- Board demo is frozen by default; do not fold hardening into design-provenance tracks.
- Do not run `git commit` or `git push` in this execution context.

## Required Deliverables

Create or update these files:

1. `/Users/grig/work/lan/lan-platform/docs/lan-holistic/00-Start Here.md`
2. `/Users/grig/work/lan/lan-platform/docs/lan-holistic/LAN Holistic Overview.md`
3. `/Users/grig/work/lan/lan-platform/docs/lan-holistic/01-Truth Reconciliation.md`
4. `/Users/grig/work/lan/lan-platform/docs/lan-holistic/02-Source Coverage Audit.md`
5. `/Users/grig/work/lan/lan-platform/docs/lan-holistic/03-Deferred Source Decisions.md`
6. `/Users/grig/work/lan/lan-platform/docs/lan-holistic/04-Milestone Gates.md`
7. `/Users/grig/work/lan/lan-platform/docs/lan-holistic/05-Progress Tracker.md`
8. `/Users/grig/work/lan/lan-platform/docs/README.md`

Use Obsidian wiki-link syntax (`[[...]]`) for internal navigation.

## Writing Standard

- Keep `00-Start Here.md` brief enough to scan in under 90 seconds.
- Keep deep docs explicit, structured, and evidence-linked.
- Clearly separate:
  - verified facts
  - approved constraints/decisions
  - open items and unresolved mismatches

## Quality Gate Before Completion

Before finishing:

- Verify all required files exist.
- Verify wiki-links resolve by filename.
- Verify top-level status matches canonical state/work-order docs.
- Log any mismatch instead of silently normalizing it.

## Final Response Format

Return:

1. Updated file paths (absolute).
2. One-paragraph current-reality summary.
3. Explicit mismatch list requiring decisions.
4. One recommended next action.
