You have already been given a concrete assignment in this project. You have begun to understand the system and may have done some initial exploration or preliminary work.

Your current task is **not** to implement more changes.

Your task is to:

* construct a clear, realistic plan to complete the assignment,
* package that plan together with the essential project context and current state, and
* create a **review request** that another agent (or human) can use to review and improve your plan **before** further implementation happens.

The reviewing agent must understand:

* what the project and assignment are about,
* what has already been done,
* what you are proposing to do next, and
* how all of this aligns with the original user goals and constraints.

DO NOT WRITE UNNEEDED DOCS. PRESERVE TOKENS AND CONTEXT FOR IMPORTANT, HELPFUL WORK.

---

## SCOPE AND SAFETY BOUNDARIES

You are operating **within an existing assignment only**.

You must:

* Stay strictly within the scope of the assignment you were given and the minimum surrounding work needed to plan and validate it.
* NOT invent new features, projects, or broad refactors for the rest of the codebase.
* NOT roam unrelated parts of the repository looking for extra work or “nice to have” initiatives.

You **may**:

* Read whatever is necessary (within project rules) to understand the assignment, existing implementation, and constraints.
* Propose a plan that covers all work required to satisfy the assignment and its minimal dependencies.

If you discover broader issues or out-of-scope initiatives while preparing the plan:

* Record them in a short **Future Opportunities / Out-of-Scope** section,
* but do **not** roll them into this plan as in-scope tasks.

Your job is to:

* make the goals and constraints explicit,
* show what has already been done vs. what remains,
* design a realistic, phased plan to reach the goals, and
* set up the next agent to review and refine that plan before major execution.

---

## STEP 1 – SOURCE INPUTS AND CONTEXT (NO HIDDEN SPEC)

You must expose the concrete inputs you are basing your plan on.

Add a section to your review request titled **“Source Inputs and Context”** that includes:

1. A numbered list of the primary inputs for this assignment, for example:

   * original user prompts or tickets
   * system / project instructions
   * prior agent handoffs and reports
   * relevant docs or ADRs
   * key code files that effectively act as current behavior spec

   For each item, include:

   * a short identifier (e.g., `T-123`, `PROMPT: wordpress-hardening`, `handoff: infra-phase-plan.md`),
   * where it lives (file path, ticket system, doc name), and
   * a 1–2 sentence summary of what it contributes.

2. For any **critical requirements, constraints, or goals**, include short verbatim excerpts as blockquotes rather than only paraphrasing, for example:

   > “Maintain site availability throughout all changes and ensure rollback is possible via existing backup mechanism.”

3. Clearly distinguish between:

   * **GIVEN** – things explicitly stated in inputs (requirements, constraints, terminology).
   * **INFERRED** – structure or phases you introduced to reason about the work (e.g., “Phase 0 quick wins, Phase 1 hardening”). Mark these as your own framing.

Add a small subsection **“Assumptions and Inferences”** where you list:

* assumptions that are not explicitly stated in the sources but that your plan relies on,
* and how you derived them (e.g., inferred from a pattern in existing deploy scripts).

The reviewer must be able to see how your plan traces back to real inputs, not guess.

---

## STEP 2 – CURRENT STATE: WHAT IS ALREADY DONE VS. NOT DONE

The reviewing agent needs to know the **starting point**.

Add a section **“Current State of the Work”** that concisely describes:

1. What is already implemented or configured that is relevant to this assignment:

   * existing services, components, scripts, or infrastructure in play,
   * prior phases that have been completed (if any),
   * any prior “quick wins” or partial implementations.

2. What remains **clearly incomplete or unstarted**:

   * major areas where no work has been done,
   * half-implemented paths or features,
   * “claimed” work that you cannot verify or that is obviously partial.

3. Any known problems, risks, or fragilities in the current state that your plan must address.

If some “completed” work is uncertain, mark it explicitly as **“claimed complete but unverified”** rather than treating it as a firm foundation.

---

## STEP 3 – EXPLICIT GOALS AND SUCCESS CRITERIA

Before proposing steps, you must clarify **what success means**.

Add a section **“Goals and Success Criteria”** that:

1. States the **core goal** of this assignment in practical terms (business or technical).
2. Lists the **key constraints** that your plan must respect (e.g., uptime, rollback ability, security posture, compatibility requirements, performance SLOs).
3. Defines **success criteria** that are observable and verifiable, for example:

   * “X endpoint supports Y throughput under condition Z,”
   * “WordPress site remains available during all maintenance operations,”
   * “Restore from Golden State backup recreates a functioning environment without manual patching.”

Whenever possible, tie each goal or criterion back to a **source input** in your “Source Inputs and Context” section.

---

## STEP 4 – PRESENT YOUR PLAN

Now describe the plan you want reviewed.

Add a section **“Proposed Plan”** that:

1. Organizes the work into a small number of clearly named phases or stages (only if helpful), for example:

   * Phase 0 – Stabilize and verify existing state
   * Phase 1 – Implement host-level security
   * Phase 2 – Hardening, monitoring, and backup validation

2. For each phase or stage, list:

   * Objectives: what the phase is supposed to achieve and how it relates to the overarching goals.
   * Tasks: concrete steps, in order, that you expect to perform.
   * Inputs/Dependencies: configs, tools, credentials, environments, or approvals required.
   * Outputs: what should exist or be true when the phase is complete.

3. Mark for each task whether it is:

   * **Required** to meet the assignment’s goals and constraints, or
   * **Optional / follow-up** and thus **not** part of the minimum viable plan, even if it may be valuable later.

If your plan assumes certain work is already complete (e.g., “Phase 0 is done”), state that explicitly and reference the **Current State** description instead of silently assuming it.

---

## STEP 5 – RISKS, TRADEOFFS, AND OPEN QUESTIONS ABOUT THE PLAN

The reviewer needs to see where the plan might be weak or risky.

Add a section **“Plan Risks, Tradeoffs, and Open Questions”** that:

1. Lists key **risks** in your plan, such as:

   * areas of high uncertainty,
   * dependencies on unstable systems or manual processes,
   * security or reliability concerns,
   * things that could easily go wrong during execution.

2. Summarizes important **tradeoffs**, e.g.:

   * “Chose simpler but less efficient strategy X over more complex Y due to time constraints.”
   * “Deferring deeper hardening to a later phase to avoid production risk during initial rollout.”

3. Enumerates **specific questions** you want the reviewer to answer, for example:

   * “Is this phase ordering safe given our uptime constraints?”
   * “Are there security or compliance requirements I missed?”
   * “Is this backup and rollback strategy sufficient for disaster recovery?”
   * “Does this plan respect the original user’s goals as you read them in the Source Inputs?”

The goal is to direct the reviewer’s attention to the parts of the plan where their judgment and experience are most valuable.

---

## STEP 6 – DEFINE A CLEAR, SCOPED PLAN REVIEW CHECKLIST

You must give the reviewing agent a checklist that is clearly about **the plan**, not implementation details.

Add a section **“Plan Review Checklist”** that:

1. Defines what is **in scope** for this review:

   * alignment of the plan with goals, constraints, and inputs,
   * completeness of tasks needed to meet success criteria,
   * correctness of dependencies and sequencing,
   * reasonableness of risk management and rollback strategy,
   * whether the plan is realistic given known constraints.

2. Defines what is **out of scope** for this review:

   * detailed line-by-line code review of existing implementation,
   * review of unrelated systems or future-phase features,
   * re-architecting the entire project.

3. Lists concrete review prompts, for example:

   * “Does this plan clearly and faithfully reflect the original user request and constraints?”
   * “Are there critical gaps in the phases or tasks?”
   * “Are any tasks dangerous or likely to break key guarantees (availability, security, data integrity)?”
   * “Is the rollback and backup strategy sound?”
   * “Are there simpler, safer ways to reach the same goals?”

Keep the checklist focused and explicitly about **plan quality**, not execution status.

---

## STEP 7 – WHERE AND HOW THE REVIEWER MUST WRITE THEIR REVIEW

The reviewing agent will produce a **review file** as their primary artifact.

Add a section **“Where to Save Your Review”** that instructs the reviewer to:

1. Write their review into a project-tracked Markdown file (for example, under `reviews/`, `docs/reviews/`, `.dev/ai/reviews/`, or another location defined by the project rules).

2. Use a **unique filename** so multiple reviewers cannot overwrite each other. For example, include:

   * an assignment slug,
   * the reviewing agent’s identifier, and
   * a version suffix.

   Example pattern (adapt to the project):

   ```text
   reviews/<assignment-slug>-plan-review-<agent-id>-v1.md
   ```

3. Before writing, check whether the chosen filename already exists:

   * If it exists, choose a new related name (e.g., bump version) instead of overwriting.

4. Save the file at the chosen path inside the project.

5. In their final message back to the orchestrator, the reviewer should:

   * return **only the contents of their review file** (the text they wrote),
   * not include extra commentary or logs outside the review.

---

## STEP 8 – CREATE AND SAVE THE PLAN REVIEW REQUEST FILE

You must now turn all of the above into a **single, concise plan review request Markdown file saved inside the project**.

1. Use the project’s existing rules and configuration to determine the correct directory for review / handoff documents. Do **not** invent a new directory structure.

2. Choose a clear filename for this **plan review request**, for example:

   ```text
   reviews/<assignment-slug>-plan-review-request.md
   ```

3. In that file, include the sections described above, in a sensible order, such as:

   * Source Inputs and Context
   * Assumptions and Inferences
   * Current State of the Work
   * Goals and Success Criteria
   * Proposed Plan
   * Plan Risks, Tradeoffs, and Open Questions
   * Plan Review Checklist
   * Where to Save Your Review

4. Save the plan review request as a Markdown file (`.md`) at the chosen path inside the project. The default expectation is that you **actually write this file into the repository** using the project’s established rules.

5. Keep the document focused and compact:

   * Enough detail for a reviewer to fully understand the project, what’s been done, and the plan forward.
   * No unnecessary narrative or repetition.

If you **cannot** write to the repository in this environment, you must still **produce the full contents** of this plan review request file in your final response so it can be saved externally.

---

## STEP 9 – FINAL OUTPUT FORMAT

Your final message in this run must contain **only** the contents of the plan review request file you have constructed, formatted as Markdown.

* Do not wrap it in extra explanation about what you did.
* Do not include logs, scratch notes, or analysis outside the review request itself.

The plan review request you output will be:

* saved into the project under the filename you proposed, and
* used directly as the prompt and context for a separate **plan-review** agent.

Work carefully and concisely. The quality and **source-alignment** of this plan review request will directly determine whether the follow-on agents execute the right work, in the right order, for the right reasons.


**In the very last line of your final message before you stop, YOU MUST DISPLAY THE FOLLOWING LINES. (Blank lines included!)**

---

The "Review My Plan" prompt was the last message from the user.

---
