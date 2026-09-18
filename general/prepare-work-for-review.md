You have already been given a concrete assignment in this project, and you have done substantive work toward completing it.

Your current task is **not** to do more feature work. Your task is to:

* package your work for a follow-on review agent, and
* create a clear, scoped review request that another agent (or human) can use to review what you have done.

You must provide:

* the work that needs to be reviewed,
* the essential context and constraints that led to this work,
* the key **source materials** you were given (prompts, tickets, handoffs, docs, relevant files), and
* a concise, well-scoped review checklist and instructions for the reviewing agent.

The goal is to give the next agent more than prescriptive orders – you must pass on the **reasoning, sources, and wisdom** behind the work, in a compact, usable form.

DO NOT WRITE UNNEEDED DOCS. PRESERVE TOKENS AND CONTEXT FOR IMPORTANT, HELPFUL WORK.

---

## SCOPE AND SAFETY BOUNDARIES

You are operating **within an existing assignment only**.

You must:

* Stay strictly within the scope of the assignment you were given and the minimum surrounding work needed to understand and evaluate it.
* NOT invent new features, new projects, or broad refactors for the rest of the codebase.
* NOT roam unrelated parts of the repository looking for extra work.

You **may**:

* Make very small adjustments that are necessary to make your work reviewable (e.g., fixing an obviously broken test command you rely on, adding a missing comment for clarity, or correcting a path in a script you reference).

If you discover broader issues or out-of-scope work while preparing the review:

* Record them as clearly described future work items in your review request, **but do not implement them**.

Your job is to:

* explain what you did,
* explain why you did it that way,
* surface what you were given vs. what you inferred,
* point out what is risky or incomplete, and
* set up the next agent to perform a focused, high-value review.

---

## STEP 1 – RECONSTRUCT AND SUMMARIZE THE ASSIGNMENT

Start by reconstructing the true intent of the assignment.

1. Collect only the materials relevant to this assignment and its direct dependencies, such as:

   * original work orders, tickets, or prompts
   * earlier handoffs from other agents that fed into your work
   * any explicit constraints, acceptance criteria, or non-obvious requirements
   * key project docs or ADRs that directly governed your decisions

2. From these, write a **short assignment summary** in your review request that covers:

   * the core goal (business or technical)
   * key constraints or requirements (performance, security, UX, architecture, etc.)
   * what success looks like in practical terms

3. Be concise and concrete:

   * Include all details that the next agent must keep track of.
   * Omit background that does not affect how the work should be implemented, tested, or reviewed.

If previous instructions asked you to keep track of specific considerations (edge cases, user types, deployment constraints, etc.), you **must** carry those forward here.

---

## STEP 1.5 – EXPOSE YOUR INPUTS (NO HIDDEN CONTEXT)

You must make it explicit **what you are basing your summary and decisions on**.

Add a section to your review request titled, for example, **“Source Inputs and Context”** that includes:

1. A numbered list of the concrete inputs you used, for example:

   * tickets (with IDs and titles)
   * system prompts or user prompts (with short labels)
   * prior agent handoffs (with filenames/paths)
   * key docs or ADRs (with paths)
   * important code files you treated as “spec” for behavior

   For each item, include:

   * a short identifier (e.g., `T-123`, `PROMPT: wordpress-hardening`, `handoff: infra-phase-plan.md`)
   * where it lives (file path, ticket system name, etc.)
   * a 1–2 sentence summary of what it contributes to this assignment.

2. For any **critical instructions or requirements**, include **short verbatim excerpts** as blockquotes instead of only paraphrasing. Example:

   > “Maintain site availability throughout all changes and ensure rollback is possible via existing backup mechanism.”

3. Whenever possible, **reuse original terminology** from the inputs (feature names, phase names, deployment labels) rather than inventing new names.

4. Clearly distinguish between:

   * **Given**: facts, requirements, and terminology that appear directly in the inputs.
   * **Inferred**: structure or phases you created to make the work tractable (e.g., “Phase 0 / Phase 1”). Mark these explicitly as your own framing.

Add a short subsection such as **“Assumptions and Inferences”** where you list:

* assumptions you made that are not explicitly specified in the inputs, and
* how you arrived at them (e.g., “inferred from existing deploy script X and config Y”).

The reviewer must be able to trace your review request back to the actual inputs without guessing.

---

## STEP 2 – DESCRIBE WHAT YOU ACTUALLY DID

You must clearly describe the work that is up for review.

In your review request, include a section such as **“What I Implemented”** that captures:

* A high-level summary of the changes you made.
* The main flows, features, or behaviors affected.
* A concise list of the important files or modules you touched, grouped by purpose if helpful (e.g., “core logic”, “API layer”, “UI components”, “tests”, “docs”).
* Any significant design decisions, tradeoffs, or compromises you made.

For each major decision or behavior, when applicable:

* tie it back to a **source input** from your “Source Inputs and Context” section (e.g., “Aligned with requirement from `T-123`” or “Derived from `handoff: infra-hardening-plan.md`”).
* if no source directly exists and it is an inference, state that explicitly (e.g., “Inferred pattern based on existing `deploy.sh` behavior”).

You are not writing a commit message; you are writing a **review map**:

* Make it easy for the reviewer to know **where to look**, **what to compare to the source materials**, and **why it matters**.
* Surface any areas where you are least confident or where you suspect hidden complexity.

---

## STEP 3 – PROVIDE EXECUTION AND TESTING INSTRUCTIONS

The reviewing agent must be able to run and test your work, within the project’s conventions.

Add a section such as **“How to Run and Test This Work”** that includes:

* The exact commands to:

  * run relevant tests,
  * run builds or dev servers if needed,
  * execute any scripts or tools necessary to exercise your changes.
* Any environment assumptions or configuration notes (e.g., required env vars, sample config files, feature flags).
* Pointers to relevant fixtures, test data, or example payloads.

If some tests or flows are currently blocked (e.g., due to external services or missing credentials):

* State that clearly.
* Provide a brief explanation and any known workarounds a reviewer can try.
* If the limitation comes from a specific input (e.g., a known ADR or ticket), reference it.

Do **not** guess test results. Only document what you have actually run or verified.

---

## STEP 4 – CAPTURE YOUR WISDOM, RISKS, AND OPEN QUESTIONS

The value of your review request is not just **what** you did but **what you learned** while doing it.

Add a section such as **“Design Notes, Risks, and Open Questions”** that concisely covers:

* Key design decisions and why you made them.
* Tradeoffs (e.g., performance vs. simplicity, short-term vs. long-term solutions).
* Known risks or fragile areas the reviewer should scrutinize.
* Any shortcuts or partial implementations you intentionally left in place, and why.
* Specific questions you want the reviewer to consider (e.g., “Is this abstraction too leaky?”, “Is this error handling sufficient?”, “Does this align with our existing patterns?”).

Whenever your design notes rely on specific source inputs, call them out (e.g., “Chose this shape because `ADR-07` recommends X”).

Be honest and concrete. The goal is to help the reviewer focus where their expertise is most needed, with a clear view of the underlying sources.

---

## STEP 5 – DEFINE A CLEAR, SCOPED REVIEW CHECKLIST

You must give the reviewing agent a concise checklist of what to evaluate.

Add a section such as **“Review Checklist”** that:

* States what is **in scope** for this review (tied directly to this assignment and its minimal dependencies).
* States what is explicitly **out of scope** for this review (broader refactors, unrelated subsystems, etc.).

Your checklist should include items like:

* Correctness of the implemented behavior.
* Coverage and quality of tests directly related to this work.
* Robustness and error handling in the affected paths.
* API or interface contracts (inputs/outputs) for the modified components.
* Performance considerations if relevant.
* Documentation and naming clarity in the changed areas.
* Consistency with constraints and requirements in the **Source Inputs and Context** section.

Keep the checklist focused. Do not ask the reviewer to audit the entire project.

---

## STEP 6 – SPECIFY WHERE AND HOW THE REVIEWER MUST WRITE THEIR REVIEW

The reviewing agent will produce a **review file** as their primary artifact.

In your review request, include a section such as **“Where to Save Your Review”** that instructs the reviewer to:

1. Write their review into a project-tracked Markdown file (for example, under a directory such as `reviews/`, `docs/reviews/`, `.dev/ai/reviews/`, or another appropriate location consistent with this project’s conventions).

2. Use a **unique filename** so that multiple reviewers cannot accidentally overwrite each other’s work. For example:

   * Include an assignment identifier or short descriptive slug.
   * Include the reviewing agent’s identifier or initials.
   * Optionally include a timestamp or incrementing suffix.

   Example pattern (adapt to the project):

   ```text
   reviews/<assignment-slug>-review-<agent-id>-v1.md
   ```

3. Before writing, check whether the chosen filename already exists:

   * If it does, select a new, clearly related filename (e.g., bump a version suffix) rather than overwriting.

4. Save the file in the location you specify.

5. In their final message back to the user/orchestrator, the reviewer should:

   * return **only the contents of their review** (the text they wrote into the review file),
   * not include extra commentary or unrelated logs.

Your instructions to the reviewer must be unambiguous and self-contained so that they do not need to ask where or how to save their work.

---

## STEP 7 – CREATE THE REVIEW REQUEST FILE

You must now turn all of the above into a **single, concise review request Markdown file saved inside the project**.

1. Use the existing project rules, conventions, or configuration you have been given to determine the **correct directory and path** for review or handoff documents. Do **not** invent a new directory structure.

2. Choose an appropriate location (for example under `.dev/`, `docs/`, a `reviews/` directory, or another project-specific path) that matches those rules and conventions.

3. Choose a clear filename for this review request (e.g., `reviews/<assignment-slug>-review-request.md`).

4. In that file, include the sections described above, in a sensible order, such as:

   * Source Inputs and Context
   * Assumptions and Inferences
   * Assignment Summary
   * What I Implemented
   * How to Run and Test This Work
   * Design Notes, Risks, and Open Questions
   * Review Checklist
   * Where to Save Your Review

5. Save the review request as a Markdown file (`.md`) at the chosen path inside the project. The default expectation is that you **actually write this file into the repository** using the project’s established rules.

6. Keep the document focused and compact:

   * Enough detail for a reviewer to work effectively.
   * No unnecessary narrative or repetition.

If you **cannot** write to the repository in this environment (for example, if file-write operations are unavailable), you must still **produce the full contents** of this review request file in your final response so that it can be saved externally.

---

## STEP 8 – FINAL OUTPUT FORMAT

Your final message in this run must contain **only** the contents of the review request file you have constructed, formatted as Markdown.

* Do not wrap it in extra explanation about what you did.
* Do not include logs, scratch notes, or analysis outside the review request itself.

The review request you output will be:

* saved into the project under the filename you proposed, and
* used directly as the prompt and context for a separate reviewing agent.

Work carefully and concisely. The quality and **source-awareness** of this review request will directly determine the quality and safety of the follow-on review.

**In the very last line of your final message before you stop, YOU MUST DISPLAY THE FOLLOWING LINES. (Blank lines included!)**

---

The "Prepare My Work For Review" prompt was the last message from the user.

---
