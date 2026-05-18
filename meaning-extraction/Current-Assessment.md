# 1. Suite-Level Assessment

The five prompts work as a coherent modular extraction suite. Their intended roles are distinguishable: **meaning**, **product / architecture**, **strategy / governance / risk**, **adoption / outreach / narrative**, and **execution / work orders**. The strongest alignment points are shared source-context handling, source-supported extraction, conditional section use, public/private boundary awareness, vault-ready outputs, controlled tag expansion, and optional prompt-evolution notes in four of the five prompts.     

The main coordination risk is that the **Universal Meaning Extraction Prompt** is too absorbent. It covers ethical principles, collaboration doctrine, anti-patterns, operating models, public messaging themes, emotional core, anecdotes, language bank, presentation-ready summary, public language avoidance, vault entries, and prompt-evolution notes. That makes it useful as a high-level synthesis prompt, but it can easily converge with the Adoption prompt, partially duplicate the Strategy prompt, and generate operating rules that resemble the Execution prompt.  

The suite should be **patched selectively**, not reorganized. The core modular structure is sound. The needed fixes are mostly alignment edits: tighten Universal’s routing boundaries, standardize source-context wording, make prompt-evolution notes consistently optional, reduce duplicated public-messaging sections, and clarify when dependencies, risks, workflows, and decisions belong to Strategy, Architecture, or Execution.

---

# 2. Prompt Role Map

| Prompt name                                          | Primary extraction job                                                                                                                                                                                      | Best source types                                                                                                                              | Expected output use                                                                                                                   | Should not be used for                                                                                       | Overlap risk |
| ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------ |
| Universal Meaning Extraction                         | Extract durable ethical, emotional, collaboration, public-interest, worldview, and operating-principle meaning.                                                                                             | Reflective conversations, monologues, messy notes, conflict-adjacent material, public-interest ecosystem reflections.                          | Knowledge-vault principles, ethical framing, collaboration doctrine, generalized anecdotes, source-grounded public-interest language. | Detailed architecture, task extraction, full adoption strategy, governance-risk mapping, ticket creation.    | High         |
| Product / Architecture / Standards / Idea Extraction | Extract buildable product concepts, architecture notes, components, workflows, standards implications, interoperability requirements, data/state objects, technical constraints, and implementation risks.  | Technical notes, product discussions, standards conversations, architecture meetings, workflow descriptions, implementation-heavy transcripts. | Builder handoff, architecture vault notes, standards analysis, implementation planning inputs.                                        | General strategy, public messaging, ethical doctrine, task planning unless architecture-relevant.            | Medium       |
| Strategic Situation / Governance / Risk Extraction   | Extract strategic structure, incentives, authority, leverage, governance gaps, risks, assumptions, decisions needed, and strategic boundaries.                                                              | Governance discussions, partnership ambiguity, stakeholder conflicts, funding/control questions, risk-heavy project conversations.             | Strategic notes, governance review, risk register inputs, decision framing, stakeholder/incentive mapping.                            | Product specification, public messaging, task tickets, therapy, legal analysis.                              | Medium       |
| Adoption / Outreach / Narrative Extraction           | Extract audience framing, adoption barriers, objections, proof needs, narrative structure, coalition language, reusable lines, claims needing evidence, and public-safe summaries.                          | Presentation prep, outreach notes, coalition discussions, adoption conversations, public/semi-public narrative material.                       | Deck/essay/talk preparation, outreach planning, public-safe messaging, narrative vault notes.                                         | Architecture, execution planning, governance analysis, generic marketing generation.                         | High         |
| Execution / Decisions / Work Order Extraction        | Extract decisions, deferred decisions, commitments, tasks, blockers, dependencies, missing inputs, work packages, acceptance criteria, sequencing, and agent-ready next actions.                            | Meeting notes, planning calls, project updates, task discussions, handoff notes, operational transcripts.                                      | Decision logs, work orders, tickets, agent handoffs, project archives.                                                                | Ethical synthesis, public narrative, strategy generation, architecture design unless required for execution. | Medium       |

---

# 3. Overlap Matrix

| Prompt pair           | Overlap area                                                                                           | Necessary shared rule or redundant duplication                                           | Risk created                                                                                                                                 | Recommended fix                                                                                                                                                        |
| --------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Universal × Adoption  | Public messaging, language bank, presentation summary, audience-like themes, what not to say publicly. | Partly necessary; mostly redundant at output-category level.                             | Universal may produce adoption/narrative output without Adoption’s stronger evidence, public-safety, and claims-requiring-evidence controls. | Keep Universal’s public-language extraction as “principle-level language only.” Route audience, objections, proof points, CTAs, and public-safe summaries to Adoption. |
| Universal × Strategy  | Governance, strategic thesis, risk-adjacent anti-patterns, contribution/authority concerns.            | Necessary as shared ethical context; redundant when Universal produces strategic theses. | Universal may turn ethical signal into strategic implication too early.                                                                      | In Universal, frame governance as ethical/collaboration meaning, not strategy unless the user asks for strategy or the source strongly supports it.                    |
| Universal × Execution | Operating rules, open questions, collaboration implications.                                           | Limited useful overlap.                                                                  | Universal may create process rules or implied tasks from emotional/ethical material.                                                         | In Universal, rename “operating rules” type to “collaboration principle” unless source clearly states a reusable rule. Route tasks/work orders to Execution.           |
| Universal × Product   | Interoperability, open standards, shared protocols, local-first, identity/social graph themes.         | Necessary as worldview overlap.                                                          | Universal may imply architecture from values language.                                                                                       | Add boundary: “Do not convert values about openness/interoperability into product architecture unless the source contains buildable system detail.”                    |
| Product × Strategy    | Governance-adjacent implementation risks, authority boundaries, dependencies, standards leverage.      | Necessary.                                                                               | Product may duplicate broad strategic risks; Strategy may duplicate technical constraints.                                                   | Product handles implementation consequences; Strategy handles power, incentives, decision rights, and governance risk.                                                 |
| Product × Execution   | Workflows, dependencies, acceptance-like criteria, implementation risks, handoff notes.                | Necessary.                                                                               | Product may become ticket planning; Execution may become architecture design.                                                                | Product extracts system structure and technical dependencies. Execution extracts tasks, blockers, owners, readiness, and acceptance criteria.                          |
| Product × Adoption    | UX, onboarding, public-facing product language, adoption risks, proof via prototype.                   | Necessary but narrow.                                                                    | Product may create pitch language; Adoption may invent product details.                                                                      | Product may include UX/interaction implications only when system-relevant. Adoption may mention product concepts only as source-supported explanation/proof.           |
| Strategy × Adoption   | Stakeholders/audiences, credibility gaps, trust, adoption barriers, public claims.                     | Necessary.                                                                               | Stakeholder analysis can collapse into audience messaging; adoption barriers can become strategic risks.                                     | Strategy maps incentives/leverage/risk. Adoption maps comprehension, trust, proof, objection, and public framing.                                                      |
| Strategy × Execution  | Decisions needed, blockers, execution capacity, dependencies, commitments.                             | Necessary.                                                                               | Strategy may produce implied tasks; Execution may decide strategy.                                                                           | Strategy identifies decision pressure and consequences. Execution extracts actual decisions, tasks, blockers, dependencies, and next actions.                          |
| Adoption × Execution  | Calls to action, follow-up actions, presentation deliverables, proof-gathering tasks.                  | Necessary only when outreach execution is explicit.                                      | Adoption may generate CTAs as tasks; Execution may generate messaging.                                                                       | Adoption extracts CTAs and proof needs. Execution converts them into tasks only if source-supported or user-requested.                                                 |

---

# 4. Coverage Gap Review

| Gap                                                         | Why it matters                                                                                                                                 |             Covered by existing prompt with a small patch? | New prompt needed? |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------: | -----------------: |
| Suite-level routing preamble                                | Fresh agents need a quick way to choose among five prompts without reading every prompt.                                                       |                                                        Yes |                 No |
| Provenance consistency across vault entries                 | Outputs will be more interoperable if vault entries preserve source scope, confidence, public-safety status, and extraction type consistently. |                                                        Yes |                 No |
| Universal lacks uploaded-file wording in Source Context     | Other prompts explicitly include uploaded files; Universal omits that term, creating minor source-context inconsistency.                       |                                                        Yes |                 No |
| Prompt-evolution consistency                                | Universal currently forces a “No prompt changes recommended” line; the others omit prompt-evolution notes unless justified or requested.       |                                                        Yes |                 No |
| Cross-prompt deduplication rule                             | Product, Strategy, Adoption, and Execution contain deduplication controls; Universal is less explicit.                                         |                                                        Yes |                 No |
| Internal-only vs public-safe output labels in Universal     | Universal has strong exclusions but can still produce public-facing sections; it should label public-safety status more clearly.               |                                                        Yes |                 No |
| “Evidence gap / claims requiring evidence” outside Adoption | Useful for public claims, but not every prompt needs this as a section.                                                                        |                                Yes, by routing to Adoption |                 No |
| Legal/reputational review flag for public-facing outputs    | Adoption handles this more explicitly than the others.                                                                                         | Yes, add concise shared safeguard to public-facing prompts |                 No |

No new prompt is needed. The gaps are alignment and routing issues, not missing extraction categories.

---

# 5. Boundary and Routing Rules

## Universal Meaning Extraction

**Use this prompt when...** the source contains durable ethical, emotional, collaboration, public-interest, worldview, or principle-level meaning.

**Do not use this prompt when...** the user needs tasks, tickets, architecture, standards analysis, adoption strategy, public copy, stakeholder risk mapping, or decision logs as the primary output.

**If confused with Adoption, choose based on...** whether the target output is principle/worldview extraction or audience-facing communication. Use Adoption for audiences, objections, proof, CTAs, public-safe summaries, and language banks.

**If confused with Strategy, choose based on...** whether the source is primarily about values/collaboration meaning or power/incentives/control/risk/decision pressure.

**If confused with Execution, choose based on...** whether the source asks what something means or what must be done.

---

## Product / Architecture / Standards / Idea Extraction

**Use this prompt when...** the source implies systems, modules, workflows, data/state, identity, permissions, standards, interoperability, UX control surfaces, or buildable ideas.

**Do not use this prompt when...** the source only contains values, public narrative, interpersonal conflict, governance strategy, or tasks without system implications.

**If confused with Execution, choose based on...** whether the output should describe a system or produce actionable work items.

**If confused with Strategy, choose based on...** whether the issue is technical/system structure or control/incentives/governance.

**If confused with Adoption, choose based on...** whether the need is product comprehension/proof for audiences or architecture itself.

---

## Strategic Situation / Governance / Risk Extraction

**Use this prompt when...** the source contains power, control, incentives, governance, stakeholder alignment, risk concentration, leverage, contribution/upside mismatch, or decision pressure.

**Do not use this prompt when...** the user needs a build spec, work order, public-facing narrative, or values doctrine.

**If confused with Universal, choose based on...** whether the analysis must map strategic structure rather than extract enduring ethical meaning.

**If confused with Execution, choose based on...** whether decisions and blockers are being analyzed strategically or converted into tasks and handoffs.

**If confused with Adoption, choose based on...** whether “trust” is a governance/incentive issue or an audience/proof/messaging issue.

---

## Adoption / Outreach / Narrative Extraction

**Use this prompt when...** the source contains audience needs, public/semi-public framing, adoption barriers, objections, proof needs, coalition language, narrative structure, public-safe summaries, or presentation material.

**Do not use this prompt when...** the primary need is strategy, architecture, task extraction, or internal ethical synthesis.

**If confused with Universal, choose based on...** whether the user needs public-facing communication artifacts rather than durable meaning.

**If confused with Strategy, choose based on...** whether stakeholders are being analyzed as audiences or as power/incentive actors.

**If confused with Execution, choose based on...** whether calls to action are being extracted as messaging or converted into operational tasks.

---

## Execution / Decisions / Work Order Extraction

**Use this prompt when...** the source contains decisions, deferred decisions, commitments, tasks, blockers, dependencies, missing inputs, acceptance criteria, sequencing, work packages, or agent-ready actions.

**Do not use this prompt when...** the source is mainly reflective, strategic, architectural, or public-facing and does not support concrete work extraction.

**If confused with Strategy, choose based on...** whether the output should clarify strategic decision pressure or produce an executable work order.

**If confused with Product, choose based on...** whether the artifact should describe system shape or assign/structure work.

**If confused with Adoption, choose based on...** whether outreach language is being extracted or outreach work is being operationalized.

---

# 6. Shared Rule Consistency Review

| Issue                                                                                                               | Prompts affected                       | Failure mode                                                                                             | Smallest effective fix                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Universal Source Context omits “uploaded file.”                                                                     | Universal                              | Agent may think uploaded files are outside scope for Universal while included in the other four prompts. | Add “uploaded file” to Universal Source Context.                                                                                     |
| Universal prompt-evolution notes are not fully optional.                                                            | Universal                              | Routine “No prompt changes recommended” output adds noise and contradicts suite norm.                    | Replace forced no-change line with omission unless user requests status.                                                             |
| Universal treats numbered sections more like a full template.                                                       | Universal                              | Unsupported sections get placeholder text, bloating output and encouraging template completion.          | Add conditional menu wording used in Product/Strategy/Adoption/Execution.                                                            |
| Universal public-facing sections lack status labels.                                                                | Universal                              | Private material may become presentation language without explicit public-safe status.                   | Add “public-safe / partial / internal-only / needs evidence” labels for public messaging, language bank, and presentation summary.   |
| Follow-up extraction behavior differs.                                                                              | Execution vs Product/Strategy/Adoption | Execution forces “No follow-up extraction recommended,” while others usually omit.                       | Make “no follow-up” status optional unless requested or required by output format.                                                   |
| Metadata header behavior differs.                                                                                   | Universal vs other four                | Vault interoperability is weaker for Universal outputs.                                                  | Add optional metadata header to Universal for vault-ready outputs only.                                                              |
| “Risks” appear in Strategy, Product, Adoption, and Execution.                                                       | Product, Strategy, Adoption, Execution | Same issue may appear as implementation risk, strategic risk, adoption barrier, and blocker.             | Add routing distinction: strategic risk vs implementation risk vs adoption barrier vs execution blocker.                             |
| “Dependencies” appear in Product and Execution.                                                                     | Product, Execution                     | Product may produce project dependencies; Execution may produce architecture dependencies.               | Add distinction: Product dependencies are system/technical; Execution dependencies block work.                                       |
| “Workflows” appear in Product and Execution.                                                                        | Product, Execution                     | Product may turn workflows into task sequences.                                                          | Product handles user/system flows; Execution handles operational order and handoff.                                                  |
| Public/private safeguards are stronger in Adoption and Execution than Universal.                                    | Universal mainly                       | Public sections can leak generalized but still identifiable conflict.                                    | Apply shared public-facing safeguard patch to Universal and Adoption; add concise compatibility line to Product/Strategy/Execution.  |
| “Do not import categories” appears in four role-specific prompts, but Universal lacks equivalent boundary language. | Universal                              | Universal becomes a catch-all mega-prompt.                                                               | Add “Do not import architecture, strategy, adoption, or execution categories unless the user asks or source strongly supports them.” |
| Tag vocabularies are compatible but not namespaced.                                                                 | All prompts                            | Same tag, such as `trust` or `governance`, may mean different things across outputs.                     | Add optional `extraction_type` or namespace in metadata; do not force a single taxonomy.                                             |

---

# 7. Output Compatibility Review

The outputs can work together in a shared knowledge vault, markdown folder, project archive, or agent handoff workflow if the suite adds a small amount of metadata and routing discipline.

**Section names mostly do not conflict.** The four role-specific prompts use distinct executive distillation names: Architecture, Strategic, Adoption, and Execution. Universal uses “Executive Distillation,” which is acceptable but should be treated as a meaning-level synthesis, not the canonical executive summary for every extraction.

**Tags are compatible but should remain prompt-local.** The tag vocabularies are compact and controlled in each prompt, and each uses a similar rule for proposing no more than three durable new tags when existing tags would distort the source.     The fix is not one universal taxonomy; it is consistent metadata: `extraction_type`, `source_scope`, `confidence`, `public_safe`, and `tags`.

**Outputs can feed one another.** Strategy can recommend Architecture, Execution, Adoption, or Meaning follow-up extractions; Product can recommend Meaning, Strategy, Execution, or Adoption; Adoption can recommend Meaning, Strategy, Architecture, or Execution; Execution can recommend known companion extraction categories.     This is a strong suite feature. Standardize “recommend only when strongly supported” and omit no-op status by default.

**Public-facing and internal outputs are mostly separated.** Adoption and Execution are strongest here; Product and Strategy are adequate; Universal needs the most tightening because it contains public messaging, anecdotes, language bank, and presentation summary sections.   

**Later synthesis is supported but provenance could improve.** Add optional vault metadata to Universal and add a one-line rule across all prompts: “For vault entries, preserve extraction type, source scope, confidence, and public-safety status when known.”

---

# 8. Redundancy and Token-Cost Reduction

| Redundant material                        | Where it appears                                            | Keep, shorten, merge, or remove                              | Value to preserve                                                                                            |
| ----------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Long Source Context blocks                | All prompts                                                 | Shorten via shared block                                     | Active context, no paste requirement, user framing controls, clarify only when source ambiguity is material. |
| Extraction Discipline wording             | Product, Strategy, Adoption, Execution; partially Universal | Merge into shared rule block                                 | Source fidelity, no invention, conditional output, source-type sensitivity.                                  |
| Public/private boundary lists             | All prompts                                                 | Keep but standardize; shorten repeated prohibited-item lists | No leakage of private names, accusations, disputes, legal/reputational risk.                                 |
| Prompt Evolution Notes                    | All prompts                                                 | Standardize; remove Universal forced no-change output        | Only emit when concrete failure-mode-based prompt improvement exists.                                        |
| Tag proposal rules                        | All prompts                                                 | Keep as shared rule reference                                | Durable controlled tags; max 3 new tags; no decorative specificity.                                          |
| “Distinctive Source Signal”               | Product, Strategy, Adoption, Execution                      | Keep                                                         | Prevents boilerplate and output convergence. Consider adding to Universal if not already implicit.           |
| Metadata header                           | Product, Strategy, Adoption, Execution                      | Keep; add optional version to Universal                      | Vault interoperability and agent handoff.                                                                    |
| Public messaging / language bank sections | Universal and Adoption                                      | Narrow Universal; keep Adoption as canonical                 | Universal preserves principle-level language; Adoption handles audience-tested communication artifacts.      |
| Risks                                     | Product, Strategy, Adoption, Execution                      | Keep with routing labels                                     | Distinguish implementation risk, strategic risk, messaging risk, blocker.                                    |
| Dependencies                              | Product and Execution                                       | Keep with routing labels                                     | Distinguish system dependency from work dependency.                                                          |
| Workflows                                 | Product and Execution                                       | Keep with routing labels                                     | Distinguish user/system workflow from operational sequence.                                                  |
| Follow-up extraction recommendations      | Product, Strategy, Adoption, Execution                      | Keep; standardize omission of unsupported status             | Cross-prompt modular workflow.                                                                               |

---

# 9. False Creativity and Over-Extraction Review

| Prompt affected                    | Risky wording or structure                                                                                                          | Failure mode                                                                                | Minimal fix                                                                                                                     |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Universal Meaning                  | “Collaboration Doctrine / Working Hypotheses,” “Positive Operating Model,” “Public Messaging Themes,” “Presentation-Ready Summary.” | Agent may invent doctrine, operating model, or public thesis from thin reflective material. | Add: “Use these sections only when the source contains more than isolated preference, frustration, or aspiration.”              |
| Universal Meaning                  | “Look for durable meaning related to...” followed by many preferred themes.                                                         | Agent may force every source into open-systems/public-good worldview.                       | Add: “Treat these as possible signals, not expected findings.”                                                                  |
| Universal Meaning                  | “Language Bank” and “Presentation-Ready Summary.”                                                                                   | Agent may generate slogans or polished claims unsupported by source.                        | Add public-safety and support-status labels; route audience-specific language to Adoption.                                      |
| Product / Architecture             | “Buildable Ideas,” “Modules / Components / Services,” “Data / State Object.”                                                        | Agent may infer product specs, interfaces, schemas, or modules from vague pain points.      | Already mostly guarded; add: “If only a pain point is present, record it as an open architecture question, not a component.”    |
| Product / Architecture             | “What could be built” in Buildable Ideas.                                                                                           | Agent may brainstorm MVPs.                                                                  | Add: “Describe only the minimum expression directly implied by the source; do not optimize or expand.”                          |
| Strategy / Governance / Risk       | “Core Strategic Thesis,” “Strategic Options,” “Source-Supported Implication.”                                                       | Agent may invent strategy or options because strategy output feels incomplete without them. | Add: “If the source supports only a constraint, risk, or question, do not elevate it into a thesis or option.”                  |
| Strategy / Governance / Risk       | “Who holds power or leverage.”                                                                                                      | Agent may infer motives or hidden power structures.                                         | Add: “Separate observed leverage from inferred leverage; mark inferred leverage as low confidence or omit.”                     |
| Adoption / Outreach / Narrative    | “Narrative Arc,” “Presentation / Essay / Talk Building Blocks,” “Coalition-Building Language,” “Calls to Action.”                   | Agent may generate marketing copy, CTAs, or coalition asks not present in source.           | Already guarded; add: “When drafting is requested, label drafted material separately from extracted material.”                  |
| Adoption / Outreach / Narrative    | “Likely objections.”                                                                                                                | Agent may invent straw-man objections.                                                      | Existing “Do not invent straw-man objections” is sufficient.                                                                    |
| Execution / Decisions / Work Order | “Agent-Ready Next Actions,” “Work Packages,” “Suggested Sequence.”                                                                  | Agent may convert weak implications into tasks, owners, priorities, or acceptance criteria. | Already strong; remove forced no-follow-up line and add “Do not convert recommendations into extracted tasks unless requested.” |
| Execution / Decisions / Work Order | “Operating Rules Learned.”                                                                                                          | Agent may create universal process doctrine from one bad meeting.                           | Existing “Do not turn every frustration into a universal rule” is sufficient; keep.                                             |

---

# 10. Public / Private Safety Review

| Prompt affected                    | Risk                                                                                                                                                           | Failure mode                                                                                                    | Minimal safeguard                                                                                                               |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Universal Meaning                  | High public/private leakage risk because it creates public messaging, anecdotes, presentation summaries, and language banks from potentially private material. | Generalized language may still reveal private conflict, accusations, or ownership disputes.                     | Add public-safety status labels and route detailed public messaging to Adoption.                                                |
| Product / Architecture             | Medium risk. Architecture notes may encode private disputes as requirements.                                                                                   | Interpersonal conflict becomes permission systems, audit trails, or attribution infrastructure without support. | Existing “Do not convert every human problem into a product requirement” is strong; keep.                                       |
| Strategy / Governance / Risk       | Medium-high risk. Governance analysis can contain sensitive power, control, and incentive claims.                                                              | Internal strategic analysis may be repurposed as public claims.                                                 | Existing rule “Do not convert internal governance analysis into public-facing claims unless explicitly asked” is strong; keep.  |
| Adoption / Outreach / Narrative    | High risk by domain, but best protected.                                                                                                                       | Private grievance becomes public narrative, coalition language, or claims needing evidence.                     | Existing public/private and claims-evidence controls are strong; keep.                                                          |
| Execution / Decisions / Work Order | Medium risk. Internal work orders may expose disputes, ownership, legal-adjacent issues, or private participants.                                              | Details move from internal notes into public-safe summaries by paraphrase.                                      | Existing “label internal and public-safe separately” and “do not move details by paraphrase if still risky” are strong; keep.   |

Strictly internal prompts do still need public/private safeguards because extracted vault notes can later be reused. None should remove safeguards.

---

# 11. Recommended Shared Patch Set

## Shared Patch 1: Source Context Alignment

### Apply To

All prompts; required for Universal, optional wording normalization for the other four.

### Add / Replace

```markdown
Assume the source material is already available in the current conversation, document, transcript, thread, notes, uploaded file, or surrounding context.

Do not require the user to paste the source material into this prompt.

Use the user’s immediate instruction as the controlling context for source scope, extraction purpose, output format, level of detail, intended use, and whether the output is internal or public-facing.

If the source boundary is ambiguous, infer the most relevant active source. Ask for clarification only if multiple materially different source scopes are possible and choosing the wrong scope would corrupt the extraction.
```

### Failure Mode Prevented

Agents asking for pasted source text, ignoring uploaded files, or overriding the user’s immediate task framing.

---

## Shared Patch 2: Conditional Output Rule

### Apply To

All prompts; especially Universal.

### Add / Replace

```markdown
Treat numbered sections as a conditional menu, not a mandatory checklist.

Produce sections only when requested by the user, materially useful for the source, or necessary for the intended output.

Omit unsupported sections by default. If the user requested a full-template output and a section is unsupported, write one brief line: `No strong signal in this source.`
```

### Failure Mode Prevented

Template completion, bloated outputs, weak placeholder sections, and forced convergence across different source types.

---

## Shared Patch 3: Role Boundary Rule

### Apply To

All prompts.

### Add / Replace

```markdown
Keep this prompt within its extraction role. Do not import categories from companion prompts unless the user explicitly asks for them or they are necessary to preserve the source’s meaning.

When companion extraction would be useful, recommend it as a follow-up instead of performing it inside this prompt.
```

### Failure Mode Prevented

Mega-prompt behavior, duplicated outputs, and cross-prompt category drift.

---

## Shared Patch 4: Public / Private Output Separation

### Apply To

All prompts; strongest need in Universal and Adoption.

### Add / Replace

```markdown
When producing public-facing, semi-public, or presentation-adaptable material, label or separate it from internal-use analysis.

Do not move private names, accusations, identifying details, internal disputes, legal/reputational claims, ownership disputes, founder drama, interpersonal criticism, or one-sided judgments into public-facing output by paraphrase. If safe generalization still preserves identifiability or implies an unsupported accusation, omit it.
```

### Failure Mode Prevented

Private conflict leakage through polished public-facing language.

---

## Shared Patch 5: Risk / Dependency / Workflow Routing

### Apply To

Product, Strategy, Adoption, Execution.

### Add / Replace

```markdown
Route overlapping categories by function:

- Strategic risks belong in Strategy.
- Implementation risks belong in Product / Architecture.
- Messaging or trust barriers belong in Adoption.
- Blockers that stop concrete work belong in Execution.
- System or technical dependencies belong in Product / Architecture.
- Work dependencies belong in Execution.
- User/system workflows belong in Product / Architecture.
- Operational sequencing belongs in Execution.
```

### Failure Mode Prevented

The same issue being duplicated as a risk, blocker, barrier, dependency, workflow, and task.

---

## Shared Patch 6: Prompt Evolution Standard

### Apply To

All prompts; required for Universal and Execution.

### Add / Replace

```markdown
## Optional: Prompt Evolution Notes

Include this section only if the run reveals a concrete, reusable improvement to this prompt.

Do not suggest changes merely because new ideas are possible. Do not include a routine “no changes recommended” line unless the user explicitly requests prompt-improvement status.

Include only:

- **Suggested new tags:** Maximum 3, only if existing tags would distort the source.
- **Prompt patch:** Exact wording to add, remove, or replace.
- **Reason:** The specific failure mode the change prevents.
```

### Failure Mode Prevented

Routine prompt-maintenance noise and inconsistent prompt-evolution behavior across the suite.

---

## Shared Patch 7: Vault Entry Provenance

### Apply To

All prompts with vault-ready outputs.

### Add / Replace

```markdown
For vault-ready entries, preserve provenance fields when known:

- extraction_type
- source_type
- source_scope
- source_date
- confidence
- public_safe
- tags

Do not strip uncertainty, source limitations, or public/private status from reusable notes.
```

### Failure Mode Prevented

Knowledge-vault entries becoming detached from source scope, confidence, and reuse safety.

---

# 12. Prompt-Specific Patch List

## Universal Meaning Extraction Prompt

### Patch 1: Source Context Uploaded Files

#### Replace This

```markdown
Assume the source material is already available in the current conversation, document, transcript, thread, notes, or surrounding context.
```

#### With This

```markdown
Assume the source material is already available in the current conversation, document, transcript, thread, notes, uploaded file, or surrounding context.
```

#### Failure Mode Prevented

Universal becomes less file-aware than the other four prompts.

---

### Patch 2: Bound Universal Against Companion-Prompt Drift

#### Replace This

```markdown
The goal is to help the author build a reusable knowledge vault by extracting any durable ethics, operating principles, adoption language, movement language, collaboration doctrine, or working hypotheses that the source actually supports.
```

#### With This

```markdown
The goal is to help the author build a reusable knowledge vault by extracting durable ethics, operating principles, movement-level language, collaboration doctrine, or working hypotheses that the source actually supports.

Do not perform full adoption, strategy, architecture, or execution extraction inside this prompt. If the source strongly supports one of those companion extractions, recommend it rather than importing its full category set here.
```

#### Failure Mode Prevented

Universal absorbing Adoption, Strategy, Product, and Execution outputs.

---

### Patch 3: Public Messaging Narrowing

#### Replace This

```markdown
# 6. Public Messaging Themes
```

#### With This

```markdown
# 6. Principle-Level Public Messaging Themes

Use this section only for source-grounded principle-level themes. Do not create audience strategy, objections, proof points, calls to action, or full public messaging plans here; route those to the Adoption / Outreach / Narrative prompt.
```

#### Failure Mode Prevented

Universal duplicating Adoption’s core function.

---

### Patch 4: Prompt Evolution Notes Optional

#### Replace This

```markdown
If no concrete improvement is justified, write:

# Prompt Evolution Notes

No prompt changes recommended from this source material.
```

#### With This

```markdown
If no concrete improvement is justified, omit this section unless the user explicitly requested prompt-improvement status.
```

#### Failure Mode Prevented

Routine no-op prompt-evolution noise.

---

### Patch 5: Optional Metadata Header

#### Replace This

No existing metadata header.

#### With This

```markdown
## Optional Metadata Header

Use this header only for vault-ready, archival, or agent-handoff outputs unless the user requested otherwise.

---
extraction_type: meaning
source_type: transcript | conversation | notes | meeting | monologue | interview | document | uploaded_file | mixed | unknown
source_scope: inferred | user-specified | ambiguous
source_date:
projects:
private_entities_redacted: true | false | not_applicable
public_safe: true | false | partial | unknown
confidence: high | medium | low
recommended_followup_extractions:
tags:
---
```

#### Failure Mode Prevented

Universal outputs being less interoperable in a knowledge vault than the other four prompts.

---

## Product / Architecture / Standards / Idea Extraction Prompt

### Patch 1: Pain Point to Architecture Boundary

#### Replace This

```markdown
Do not convert every human problem into a product requirement.
```

#### With This

```markdown
Do not convert every human problem into a product requirement. If the source contains only a pain point, record it as an open architecture question or omit it; do not invent a module, feature, schema, interface, or implementation plan.
```

#### Failure Mode Prevented

Vague interpersonal or workflow pain becoming false architecture.

---

### Patch 2: Product vs Execution Dependencies

#### Replace This

```markdown
## Dependencies

Systems, people, decisions, APIs, standards, data, infrastructure, or prior work required before implementation can proceed.
```

#### With This

```markdown
## Dependencies

Systems, APIs, standards, data, infrastructure, technical decisions, or prior technical work required before implementation can proceed.

For work-blocking dependencies, owners, deadlines, or task readiness, route to the Execution / Decisions / Work Order prompt unless the user requested execution extraction.
```

#### Failure Mode Prevented

Product extraction becoming project-management extraction.

---

## Strategic Situation / Governance / Risk Extraction Prompt

### Patch 1: Strategy Options Constraint

#### Replace This

```markdown
Identify realistic paths forward only if the source supports them.
```

#### With This

```markdown
Identify realistic paths forward only if the source directly supports them. If the source supports only a constraint, unresolved question, risk, or decision pressure, do not elevate it into a strategic option.
```

#### Failure Mode Prevented

Invented strategy options from weak source signal.

---

### Patch 2: Stakeholder Inference Control

#### Replace This

```markdown
Map stakeholders only at the level supported by the source.
```

#### With This

```markdown
Map stakeholders only at the level supported by the source. Separate observed roles, incentives, and leverage from inferred ones. Mark inferred items as low confidence or omit them when the source is thin.
```

#### Failure Mode Prevented

Unsupported motive or power analysis.

---

## Adoption / Outreach / Narrative Extraction Prompt

### Patch 1: Extracted vs Drafted Language Separation

#### Replace This

```markdown
Do not create messaging that is not present in the source. If the user asks for new messaging, clearly separate extracted language from newly drafted language.
```

#### With This

```markdown
Do not create messaging that is not present in the source. If the user asks for new messaging, clearly separate:

- **Extracted language**
- **Lightly rewritten source-grounded language**
- **Newly drafted language requested by the user**

Do not present drafted language as if it came from the source.
```

#### Failure Mode Prevented

Public copy appearing more source-supported than it is.

---

## Execution / Decisions / Work Order Extraction Prompt

### Patch 1: Follow-Up Extraction No-Op

#### Replace This

```markdown
If no follow-up extraction is warranted, write:

No follow-up extraction recommended.
```

#### With This

```markdown
If no follow-up extraction is warranted, omit this section unless the user explicitly requested follow-up status or a full-template output.
```

#### Failure Mode Prevented

Unnecessary routine status lines and inconsistency with the other prompts.

---

### Patch 2: Recommendations vs Extracted Tasks

#### Replace This

```markdown
Do not create tasks or priorities that are not present in the source. If the user asks for recommendations, clearly separate extracted work from recommended next actions.
```

#### With This

```markdown
Do not create tasks or priorities that are not present in the source. If the user asks for recommendations, clearly separate:

- **Extracted work**
- **Recommended next actions**
- **Assumptions required before execution**

Do not convert recommendations into extracted tasks.
```

#### Failure Mode Prevented

Recommended work being mistaken for source-supported commitments.

---

# 13. Recommended Final Suite Structure

```markdown
# Final Prompt Suite Map

## 1. Universal Meaning Extraction

**Purpose:** Extract durable ethical, emotional, collaboration, public-interest, and worldview meaning from source material.
**Primary outputs:** Executive meaning distillation, ethical principles, collaboration doctrine, anti-patterns, emotional core, generalized anecdotes, principle-level language, vault entries.
**Use when:** The source is primarily about what a situation means, what values it reveals, or what collaboration/public-good principles it supports.

## 2. Product / Architecture / Standards / Idea Extraction

**Purpose:** Extract source-supported product, architecture, standards, interoperability, workflow, data, and implementation implications.
**Primary outputs:** Product concepts, architecture notes, components, workflows, data/state objects, interoperability requirements, UX implications, technical constraints, implementation risks, reusable architecture notes.
**Use when:** The source contains buildable system detail, technical structure, product concepts, standards implications, or implementation-relevant requirements.

## 3. Strategic Situation / Governance / Risk Extraction

**Purpose:** Extract strategic structure, governance issues, incentives, authority, leverage, risk, assumptions, decision pressure, and boundaries.
**Primary outputs:** Strategic distillation, system dynamics, stakeholder/incentive map, governance issues, risk/failure modes, assumptions, decisions needed, strategic boundaries, vault-ready strategic notes.
**Use when:** The source contains power, control, incentives, contribution/upside mismatch, governance ambiguity, risk concentration, or strategic decision pressure.

## 4. Adoption / Outreach / Narrative Extraction

**Purpose:** Extract audience framing, adoption barriers, objections, proof needs, public/private-safe narrative, coalition language, and presentation-ready building blocks.
**Primary outputs:** Adoption distillation, audience map, audience-specific framing, barriers, objections, proof points, narrative structure, language bank, language to avoid, claims requiring evidence, public-safe summary, vault-ready adoption notes.
**Use when:** The source needs to be translated into public/semi-public communication, outreach, coalition-building, deck, essay, talk, or adoption strategy.

## 5. Execution / Decisions / Work Order Extraction

**Purpose:** Extract decisions, commitments, tasks, blockers, dependencies, missing inputs, sequencing, work packages, and agent-ready next actions.
**Primary outputs:** Decision log, deferred decisions, commitments/non-commitments, tasks, blockers, dependencies, missing inputs, work packages, acceptance criteria, sequence, operating rules, agent-ready next actions, vault-ready execution notes.
**Use when:** The source needs to become actionable work, a decision log, project handoff, ticket input, or agent-ready execution package.
```

---

# 14. Final Recommendation

**Patch selectively** — the suite is basically sound but needs targeted consistency and overlap fixes.

The five-prompt architecture should remain intact. The role separation is useful, and the four specialized prompts already contain strong source-fidelity, public/private, conditional-output, and prompt-evolution controls. The main weakness is not structural failure; it is role bleed, especially from Universal Meaning into Adoption and Strategy. Apply small shared-rule patches, narrow Universal’s public-messaging role, standardize prompt-evolution behavior, add optional Universal metadata, and clarify routing for risks, dependencies, workflows, and decisions. This will preserve modularity while reducing redundant outputs, false creativity, public/private leakage, and token cost.
