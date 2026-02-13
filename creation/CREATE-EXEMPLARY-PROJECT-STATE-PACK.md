# CREATE EXEMPLARY PROJECT STATE PACK

Use this prompt when you need high-signal project documentation that is concise at entry and deeply auditable in detail.

---

You are creating or updating a **Project State Pack** that leadership can trust.

## Mission

Produce documentation that does two things at once:

1) Gives a fast 60-90 second understanding of current reality.
2) Preserves deep evidence and traceability for decisions, work status, and next gates.

The output must be practical, verifiable, and immediately useful for execution.

## Inputs (fill these before running)

- Project root: `[ABSOLUTE_PROJECT_ROOT]`
- Project name: `[PROJECT_NAME]`
- Current phase: `[CURRENT_PHASE]`
- Canonical state file: `[ABSOLUTE_PATH_TO_STATE_OF_PROJECT]`
- Canonical work-order index: `[ABSOLUTE_PATH_TO_WO_INDEX]`
- Canonical decision directory: `[ABSOLUTE_PATH_TO_DECISIONS_DIR]`
- Canonical ingestion ledger (if used): `[ABSOLUTE_PATH_TO_LEDGER]`
- Canonical milestone pipeline: `[ABSOLUTE_PATH_TO_MILESTONE_PIPELINE]`
- Output docs directory: `[ABSOLUTE_PATH_TO_DOCS_DIRECTORY]`
- Non-negotiables: `[LIST_NON_NEGOTIABLE_RULES]`

## Non-Negotiable Behavior

- Do not invent facts, statuses, or completion claims.
- Every important claim must have a concrete file-path evidence anchor.
- Use absolute paths for references.
- Use explicit dates (YYYY-MM-DD) instead of ambiguous relative dates.
- Separate clearly:
  - Facts (verified)
  - Decisions (approved constraints)
  - Open items (not done yet)
- Preserve train-of-logic separation:
  - Design/provenance
  - Prototype/demo
  - Deployment/operations
- If status docs conflict, call out the mismatch and record the resolution target.
- Do not do git commit or push unless explicitly requested.

## Deliverables (Obsidian-friendly markdown)

Create or update the following files in `[ABSOLUTE_PATH_TO_DOCS_DIRECTORY]`:

1. `00-Start Here.md`
   - Extremely short onboarding.
   - Read order links to all docs.
   - One screen, no fluff.

2. `Project Holistic Overview.md`
   - High-level timeline and current position.
   - What happened, where we are, what is next.
   - Explicitly state frozen artifacts vs active tracks.

3. `01-Truth Reconciliation.md`
   - Reconciliation protocol for state docs, work orders, and decisions.
   - Mismatch log format and resolution checklist.

4. `02-Source Coverage Audit.md`
   - Coverage method and current counts from canonical ledger/manifest.
   - Evidence chain requirements per source.
   - Pass/fail conditions for audit gate.

5. `03-Deferred Source Decisions.md`
   - Decision framework for deferred materials:
     - promote now
     - defer tracked
     - out-of-scope
   - Required rationale and owner/date fields.

6. `04-Milestone Gates.md`
   - Fixed milestone ladder with non-mixing rules.
   - Entry/exit criteria per milestone transition.
   - Clear separation between demo snapshots and prototype hardening.

7. `05-Progress Tracker.md`
   - Gate checklist with current status.
   - Open follow-ups and blockers.
   - Last reviewed timestamp and owner.

8. `README.md` (in docs root)
   - Entry links into the pack.
   - One-line purpose statement.

Use Obsidian wiki-links (`[[...]]`) between these documents.

## Writing Standard

- Entry docs: compact, directive, high signal.
- Deep docs: structured, explicit, evidence-linked.
- Avoid vague words: “mostly”, “kind of”, “probably”, “soon”.
- Prefer concrete language:
  - “Status: IN_PROGRESS”
  - “Evidence: /absolute/path/file.md”
  - “Next gate: Gate 3 closeout”

## Quality Gate Before Completion

Before declaring complete, verify:

- All required docs exist.
- All navigation links resolve by filename.
- No critical claim is missing evidence path.
- Current phase and top priorities match canonical state docs.
- Mismatches are explicitly listed, not silently ignored.

## Final Output Format

Return:

1) What was created/updated (absolute paths).
2) One paragraph “current reality” summary.
3) Open mismatches requiring decisions.
4) Recommended next action in one sentence.

---

If an existing pack already exists, update in place and preserve useful prior context; do not fork competing parallel packs unless explicitly requested.
