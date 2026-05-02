# Objective Realignment

You are not being asked for a status update.

You are being asked to realign your current work with the project objective, existing project documentation, prior reasoning, accepted vision, and already-defined work orders.

You may have become over-focused on a local implementation problem, a single blocker, a narrow work order, or a technical detail that is no longer proportional to the larger objective.

Your task is to recover the full project context and determine whether your current work still matters.

## 1. Reconstruct the Project Objective

Start by explaining what you understand the project is actually trying to accomplish.

Use the existing project materials, including:

- Vision statements
- Product requirements
- Architecture documents
- Prior reasoning
- Existing work orders
- Acceptance criteria
- User decisions already made
- Relevant implementation notes
- Project memory, state files, planning documents, or recovery files available to you

Do not ask the user to restate context that already exists in the project.

Produce:

```markdown
## Reconstructed Objective

### Primary Objective

### Intended User / Operator Outcome

### Strategic Purpose

### Minimum Viable Completed State

### Ideal Completed State

### Non-Goals / Things We Should Not Over-Optimize
```

## 2. Recover the Existing Reasoning Trail

Before evaluating the current work, recover the reasoning that originally led to the project structure.

Identify:

- The original rationale for the project
- The major design decisions already made
- The constraints already accepted
- The work orders already created
- The assumptions that were explicitly chosen
- The assumptions that are only implied
- The user decisions that should not be re-litigated unless evidence shows they are wrong

Use this format:

| Prior Decision / Rationale | Source | Still Valid? | Why It Matters | Risk if Ignored |
|---|---|---|---|---|

## 3. Identify the Current Work Focus

Explain what you have been spending time on recently.

Be specific.

Include:

- The specific problem or work order you have been focused on
- How long or how much effort has been spent on it
- Why you believed it mattered
- What evidence suggested it was blocking progress
- What assumptions kept you focused on it

Use this format:

| Current Focus | Source Work Order / File | Time or Effort Spent | Assumed Importance | Current Evidence |
|---|---|---|---|---|

## 4. Compare Current Focus to the Larger Objective

Determine whether the current work still has proportional value.

Classify the current focus as one of:

- Core: directly required for the project objective
- Supporting: useful, but not central
- Incidental: nice to have, but not worth major effort
- Misaligned: not meaningfully advancing the project
- Obsolete: previously relevant, but no longer needed
- Unknown: cannot determine from available project materials

Use this format:

| Current Focus | Alignment Classification | Why | Risk of Continuing | Risk of Stopping |
|---|---|---|---|---|

## 5. Detect Local-Optimization Drift

Identify whether you have drifted into solving the wrong problem well.

Answer directly:

- Are you optimizing for closing a narrow technical issue instead of advancing the project?
- Are you treating a local blocker as globally important without evidence?
- Are you spending disproportionate effort on something the user may not care about?
- Are you preserving prior work because effort was already spent on it?
- Are you mistaking implementation activity for meaningful progress?
- Are you ignoring already-defined objectives, constraints, or work orders?
- Are you failing to use project documentation that already answers your uncertainty?
- Are you re-discovering or re-arguing context that already exists?

Produce:

```markdown
## Drift Diagnosis

### Drift Detected
Yes / No / Partial

### Type of Drift

### Evidence

### Consequence if Uncorrected
```

## 6. Re-evaluate Existing Work Orders

Review the existing work orders against the reconstructed project objective.

Do not assume all existing work orders are still equally important.

For each relevant work order, classify it as:

- Keep
- Modify
- Split
- Merge
- Defer
- Cancel
- Needs user decision

Use this format:

| Work Order | Original Purpose | Current Relevance | Recommended Action | Reason |
|---|---|---|---|---|

## 7. Convert Real Gaps Into Corrected Work Orders

If the project is not actually complete, convert the real gaps into corrected work orders.

These work orders must be based on the project objective, not on whatever problem you were most recently stuck on.

Use this format:

```yaml
work_order_id: WO-###
title:
classification: core | supporting | cleanup | validation | documentation | integration
objective_gap:
why_it_matters:
required_output:
acceptance_criteria:
dependencies:
source_material:
recommended_agent_type:
estimated_complexity: low | medium | high
user_input_required: none | specific_decision_required
```

Rules:

- Create work orders only for work that advances the objective.
- Do not create work orders merely to justify previous effort.
- Do not preserve a task just because time has already been spent on it.
- Do not ask the user to clarify anything already defined in available materials.
- Use project files, prior documentation, and existing work orders before declaring uncertainty.
- If a task is not worth continuing, say so directly.
- If the current blocker is real but low-value, downgrade it and move on.
- If the current blocker is real and high-value, explain exactly why it remains central.

## 8. Rebuild the Completion Definition

Create a corrected definition of done for the project.

Include:

- Functional completion criteria
- Documentation completion criteria
- Validation/testing criteria
- Integration criteria
- User handoff criteria
- Evidence required before claiming completion

Use this format:

| Completion Criterion | Required Evidence | Current Status | Remaining Work |
|---|---|---|---|

## 9. Decide What Should Happen Next

Produce a corrected execution plan.

Include:

```markdown
## Corrected Execution Plan

### Stop Doing

### Continue Doing

### Start Doing

### First Priority Work Order

### Work Orders to Defer or Cancel

### Evidence Needed Before Claiming Completion
```

## 10. Final Judgment

End with this exact structure:

```markdown
## Realignment Judgment

### Is the current work still aligned with the project objective?
Yes / No / Partial / Cannot Determine

### Should the current focus continue?
Yes / No / Only after modification / Only if user approves

### Main Reason

### Highest-Value Next Step

### Work Orders Created or Modified

### Work Orders Deferred or Cancelled

### User Decision Required
None / Specific decision:
```

## Constraints

- Do not ask the user to remind you of project details already present in the project.
- Do not summarize effort as progress.
- Do not claim completion unless the project objective is satisfied.
- Do not keep working on a narrow issue merely because it has consumed time.
- Do not treat technical difficulty as proof of importance.
- Do not convert every unresolved detail into a blocker.
- Do not mark work as blocked unless no reasonable assumption or available project material can unblock it.
- Do not protect previous work from cancellation.
- Do not produce generic project-management language.
- Do not re-litigate already accepted decisions unless current evidence invalidates them.
- Treat this as an objective realignment audit.

