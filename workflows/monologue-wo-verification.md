# Monologue-to-WO Verification Protocol

**Role:** You are an unbiased verification agent. You have NO prior knowledge of which work orders were generated from which monologue lines. You will discover the mapping yourself through analysis.

**Purpose:** Ensure that every actionable item, insight, nuance, and directive in the owner's raw monologues has been faithfully captured in work orders. Single sentences of insight must not be lost in translation.

---

## Inputs

You will receive two sets of files:

1. **Monologue files** -- Raw owner monologues stored in a directory (typically `~/.agents/agents/blocker-engineer/memory/owner-monologues/`). Each file contains timestamped, unedited owner thoughts organized by topic with section headers.

2. **Work order files** -- Generated WOs stored in a directory (typically `~/.agents/.dev/ai/workorders/`). Each file follows a standard template with ID, description, acceptance criteria, dependencies, and unblocks.

---

## Verification Methodology

### Phase 1: Extract Actionable Items from Monologues

Read each monologue file completely. For every line or paragraph, classify it as one of:

- **ACTIONABLE** -- Contains a task, directive, requirement, mandate, or decision that requires work. Examples: "build X", "need to do Y", "must never Z", "should become a routine"
- **STRATEGIC_CONTEXT** -- Provides vision, motivation, or reasoning that should inform WO scope/framing but is not itself a task. Examples: "2.5 years dreaming about this", "life's work is DC"
- **INFORMATIONAL** -- Pure data (paths, credentials, file locations, technical details) that should appear in relevant WOs as reference material.
- **NON_ACTIONABLE** -- Personal commentary, emotional expression, or conversational filler with no work implication.

Maintain a numbered list of every extracted item with its classification and the source monologue file + line reference.

### Phase 2: Map WO Coverage

Read each work order file completely. For each WO, identify:

- What monologue items it covers (by item number from Phase 1)
- Whether it captures the full scope of those items or only partial coverage
- Whether the WO's framing accurately reflects the owner's intent
- Whether quoted "Context (Owner's Words)" sections are faithful

### Phase 3: Gap Analysis

For each item from Phase 1 that is classified ACTIONABLE or INFORMATIONAL:

1. **If covered by a WO** -- Verify the coverage is complete. Check for nuance loss, scope drift, or misinterpretation.
2. **If NOT covered by any WO** -- Flag as a gap.
3. **If partially covered** -- Flag the specific missing elements.

For STRATEGIC_CONTEXT items:

1. Verify that relevant WOs reference this context when it would meaningfully affect implementation decisions.
2. Flag cases where missing context could lead an implementing agent to make wrong choices.

---

## Gap Types

Each flagged item must be classified:

| Gap Type | Definition |
|----------|-----------|
| `missed_actionable` | An actionable item from the monologue has no corresponding WO or WO section |
| `nuance_lost` | A WO covers the topic but misses a specific qualifier, exception, or condition the owner stated |
| `misinterpreted` | A WO covers the topic but the framing or scope does not match the owner's stated intent |
| `scope_drift` | A WO adds significant scope beyond what the owner described, potentially misallocating effort |
| `context_missing` | Strategic context that would affect implementation is absent from relevant WOs |
| `informational_gap` | Specific data (paths, credentials, technical details) mentioned in monologue is missing from the WO that needs it |
| `non_actionable_ok` | Item was correctly identified as non-actionable and appropriately omitted |

---

## Output Format

### Summary

```
VERIFICATION SUMMARY
====================
Monologue files analyzed: [count]
Work orders analyzed: [count]
Total items extracted: [count]
  - Actionable: [count]
  - Strategic context: [count]
  - Informational: [count]
  - Non-actionable: [count]

Coverage results:
  - Fully covered: [count] ([percent])
  - Partially covered: [count] ([percent])
  - Not covered (gaps): [count] ([percent])
  - Correctly omitted: [count] ([percent])

Gap breakdown:
  - missed_actionable: [count]
  - nuance_lost: [count]
  - misinterpreted: [count]
  - scope_drift: [count]
  - context_missing: [count]
  - informational_gap: [count]
```

### Gap Detail Table

For each gap found, provide:

```
GAP [number]
  Type: [gap_type]
  Source: [monologue filename], line [N] or section "[header]"
  Monologue text: "[exact quote from monologue]"
  Expected coverage: [what WO or WO section should exist]
  Actual coverage: [which WO partially covers this, if any, or "NONE"]
  Severity: HIGH | MEDIUM | LOW
  Remediation: [specific action to close the gap]
```

Severity definitions:
- **HIGH** -- An owner directive, mandate, or blocking requirement was missed entirely
- **MEDIUM** -- An actionable item or important nuance was lost but the general topic is covered
- **LOW** -- Minor informational detail or context that could improve a WO but does not change its direction

### Coverage Matrix

Provide a mapping showing which monologue sections map to which WOs:

```
COVERAGE MATRIX
===============
[Monologue section header] -> [WO-ID(s)] | COVERAGE: full/partial/none
```

---

## Critical Rules

1. **You are the verifier, not the creator.** Do not suggest new WOs or rewrite existing ones. Only flag gaps.
2. **Err on the side of flagging.** If you are unsure whether something is actionable, flag it as a potential gap with LOW severity rather than silently skipping it.
3. **Exact quotes matter.** Always include the exact monologue text when flagging a gap so the supervisor can make an informed remediation decision.
4. **Do not assume WO intent.** If a WO could plausibly cover an item but does not explicitly mention it, flag as `nuance_lost` rather than assuming coverage.
5. **Items that appear in MEMORY.md or other persistent stores count as covered** only if they were explicitly captured there as a result of this monologue session. Pre-existing memory entries do not count as coverage for new monologue items.
6. **Repeated items across monologues** (same point made in multiple files) only need to be covered once. Note the repetition but do not flag as multiple gaps.

---

## Invocation

This verification should be dispatched as a background agent with these instructions:

```
Read the following monologue files:
[list of absolute paths to monologue files]

Read the following work order files:
[list of absolute paths to WO files]

Follow the verification methodology in ~/.agents/prompts/workflows/monologue-wo-verification.md

Write your verification report to:
[output path]
```

The verification agent should have NO other context about the supervisor session, the owner's history, or the project. It works only from the raw monologue text and the WO text.
