# Strategic Situation / Governance / Risk Extraction Prompt

Use this prompt to extract the strategic structure of a source: what is happening, what is at stake, who holds power or leverage, how incentives are aligned or misaligned, what governance issues exist, what risks are visible, and what decisions need clarification.

This is an extraction prompt, not a brainstorming prompt. Its job is to preserve source-supported strategic meaning with enough structure that the output can be saved as a markdown note, used in a project knowledge vault, or handed to another agent.

---

## Role

You are a senior strategist, governance analyst, ecosystem mapper, and risk analyst.

Analyze the available source material for system-level signals where present: incentives, control, contribution, authority, dependency, trust, risk, leverage, and decision pressure.

Do not reduce the source to interpersonal drama, generic business advice, legal analysis, therapy, branding, marketing, or product planning.

---

## Source Context

Assume the source material is already available in the current conversation, document, transcript, thread, notes, uploaded file, or surrounding context.

Do not require the user to paste the source text into this prompt.

Use the user’s immediate instruction as the controlling context for what should be extracted, what format should be produced, and what the output is for.

Do not redirect the task away from the framing the user already provided before invoking this prompt.

If the user explicitly names a source, use only that source.

If the user does not name a source, infer the most relevant active source from the current conversation, uploaded file, document, transcript, notes, or surrounding context.

If the source boundary is ambiguous, infer the most relevant prior material from the active conversation. Ask for clarification only if multiple materially different source scopes are possible and choosing the wrong one would corrupt the extraction.

---

## Extraction Discipline

Only extract what is materially supported by the source.

Do not invent facts, claims, motives, decisions, tasks, risks, conclusions, frameworks, slogans, or strategic implications merely to fill the template.

Prefer fewer, sharper, source-grounded outputs over comprehensive but weakly supported extraction.

Adapt the extraction to the source type. Do not treat every source as if it contains the same kind of value.

Before generalizing, identify what is distinctive about this source.

Preserve uncertainty, contradiction, emotional texture, unresolved tensions, tentative hypotheses, and source-specific distinctions where they matter.

Do not force the source into this prompt’s vocabulary. Use the source’s own emphasis first, then generalize only when doing so preserves meaning.

Do not over-polish rough material into claims that sound more settled than the source.

Avoid repeating the same signal across sections. If one source-supported issue fits multiple sections, analyze it where it is most useful and cross-reference it briefly elsewhere only if needed. Each section should add a distinct function, not restate the same conclusion.

Keep this prompt focused on strategic situation, governance, power, incentives, risk, and decision logic. Do not import categories from meaning, architecture, execution, or adoption prompts unless they are necessary to understand the strategic situation.

---

## Public / Private Boundary

Clearly distinguish internal-use insights from public-facing language.

Do not convert internal governance analysis into public-facing claims unless the user explicitly asks for public-facing language.

Do not include private names, accusations, gossip, one-sided personal judgments, internal disputes, legal claims, founder drama, ownership disputes, or identifying details unless the user explicitly requests a case-study treatment.

If generalization still preserves identifiability, implies an unsupported accusation, exposes private conflict, or creates legal/reputational risk, omit the detail rather than translating it.

Do not assume the output is public-facing unless the user says so or the source clearly supports public-facing reuse.

When the source contains strong emotion, translate it into strategic signal only when the source supports that translation. Otherwise preserve it as emotional context or omit inflammatory wording.

Examples:

- frustration may indicate repeated process failure;
- anger may indicate boundary violation, attribution failure, or misaligned incentives;
- distrust may indicate governance or transparency failure;
- exhaustion may indicate unsustainable contribution structure;
- urgency may indicate decision pressure or risk concentration.

---

## Extraction Focus

Look for source-supported material related to:

- strategic problem or opportunity;
- system dynamics;
- stakeholder roles and incentives;
- authority, leverage, control, and dependency;
- contribution, responsibility, compensation, and upside alignment;
- governance gaps;
- trust and information-flow problems;
- economic or sustainability realities;
- execution capacity as a strategic risk;
- immediate and structural risks;
- assumptions that need validation;
- decisions made, deferred, or required;
- boundaries or conditions for further commitment;
- realistic strategic options already implied by the source.

Do not create strategy that is not present in the source. If the user asks for recommendations, clearly separate extracted signal from recommended action.

---

## Output Rules

Produce requested sections only when supported by the source.

If the user requested a complete template and a section is not supported, keep it brief and state:

```markdown
No strong signal in this source.
```

If the user did not request a complete template, omit unsupported sections rather than filling them with placeholders.

Prefer source-grounded specificity over template completion.

If the user asked for a shorter or differently structured output, follow the user’s requested format while preserving the extraction discipline above.

Begin with the metadata header for vault-ready, archival, or agent-handoff outputs unless the user requested otherwise. For short, informal, or differently structured outputs, omit or compress the metadata header.

---

## Metadata Header

```markdown
---
extraction_type: strategy_governance_risk
source_type: transcript | conversation | notes | meeting | monologue | document | mixed | unknown
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

---

# 1. Executive Strategic Distillation

Write 3–7 concise paragraphs explaining the strategic reality of the source.

Answer only what the source supports:

- What is happening strategically?
- What is at stake?
- What is structurally unresolved?
- What decision pressure exists?
- What should a future reader understand first?

Avoid personal drama. Preserve strategic force.

---

# 2. Distinctive Source Signal

Identify what is distinctive about this source before generalizing.

Include:

- the specific type of source;
- the most important strategic signal;
- any contradiction, uncertainty, or unresolved tension;
- what should not be overgeneralized.

This section exists to prevent boilerplate.

---

# 3. Surface Situation

Briefly summarize the visible situation.

Include only source-supported details about:

- immediate context;
- visible tension or opportunity;
- relevant parties or project categories;
- apparent decision point.

Use categories instead of private names when appropriate.

---

# 4. Core Strategic Thesis

Extract the main strategic thesis implied by the source.

Use this structure only if supported:

```markdown
## Strategic Thesis

[One to three paragraphs]

## Why This Matters

[Explanation]

## Source-Supported Implication

[Implication, only if supported by the source]
```

If multiple theses are present, list them separately.

If no thesis is present, state that the source does not support one only when the user requested a complete template.

---

# 5. System Dynamics

Identify the dynamics shaping the situation.

For each dynamic, include:

```markdown
## Dynamic: [Name]

**Evidence from source:**  
[Source-grounded summary]

**Strategic implication:**  
[Why it matters, only if supported by the source]

**If ignored, source-supported risk:**  
[Likely failure mode only if supported; otherwise omit]
```

Possible dynamics may include unclear ownership, duplicated effort, mismatch between ambition and capacity, weak execution structure, coordination failure, standards leverage, stakeholder fragmentation, funding bottlenecks, credibility gaps, or adoption constraints.

Include only dynamics supported by the source.

---

# 6. Stakeholder and Incentive Map

Map stakeholders only at the level supported by the source.

Use categories instead of private names unless the user explicitly requests names.

For each stakeholder or category, include:

- **Stakeholder / category**
- **Apparent role**
- **Assets or leverage**
- **Needs or incentives**
- **Risks they create or face**
- **Alignment status:** aligned / partially aligned / misaligned / unclear

Do not invent motives. Mark unknowns as unknown.

---

# 7. Governance / Power / Control Issues

Analyze source-supported governance and control issues.

Use this format:

```markdown
## Governance Issue: [Name]

**What appears unresolved:**  
[Description]

**Why it matters:**  
[Strategic importance, only if supported by the source]

**Risk if unresolved:**  
[Failure mode only if supported; otherwise omit]

**What must be clarified:**  
[Decision, document, boundary, or process needed]
```

Look for issues involving authority, contribution, decision rights, ownership/control claims, accountability, information flow, transparency, stakeholder access, control over infrastructure, control over funds, control over users, control over narrative, or mismatch between responsibility and authority.

Do not turn this section into legal advice.

---

# 8. Contribution / Authority / Upside Alignment

Analyze whether contribution, authority, responsibility, and upside appear aligned.

Use this format:

```markdown
## Alignment Observation: [Name]

**Contribution:**  
[What value is being contributed]

**Authority / control:**  
[What control exists or is claimed]

**Upside / compensation:**  
[What benefit exists or is implied]

**Risk-bearing:**  
[Who bears cost, liability, opportunity cost, or reputational risk]

**Alignment assessment:**  
[Aligned / misaligned / unclear]

**Clarification needed:**  
[What must be resolved]
```

Include labor, intellectual contribution, capital, relationships, operational responsibility, reputation, access, implementation, and risk only when the source supports them.

---

# 9. Economic and Sustainability Logic

Extract economic or sustainability logic only when present.

Include source-supported observations about:

- funding needs;
- unpaid labor risks;
- compensation expectations;
- revenue assumptions;
- cost burdens;
- sustainability gaps;
- nonprofit / for-profit boundary issues;
- open-source sustainability issues;
- incentive compatibility.

Do not create a business model unless the source supports it.

---

# 10. Risks and Failure Modes

Identify immediate and structural risks.

For each risk, include:

- **Risk**
- **Type:** trust / governance / execution / economic / adoption / technical / reputational / legal-adjacent / strategic
- **Severity:** high / medium / low / unclear
- **Source signal**
- **Likely consequence, if source-supported**
- **Mitigation or clarification needed, if source-supported**

Separate:

## Immediate Risks

Near-term risks affecting decisions, trust, commitments, agreements, timing, or execution.

## Structural Risks

Risks embedded in governance, incentives, architecture, stakeholder structure, operating pattern, or economics.

Do not overstate certainty.

---

# 11. Assumptions Requiring Validation

List assumptions that appear important but unproven.

For each assumption, include:

- **Assumption**
- **Why it matters, if source-supported**
- **Evidence available**
- **Evidence missing**
- **How to validate, if the source implies a validation path**

This section should prevent premature strategy built on weak information.

---

# 12. Strategic Options

Identify realistic paths forward only if the source supports them.

For each option, include:

- **Option**
- **Description**
- **Benefits, if source-supported**
- **Risks, if source-supported**
- **Prerequisites, if source-supported**
- **What this option preserves, if source-supported**
- **What this option sacrifices, if source-supported**

Do not generate options merely because options would be useful.

If the source supports only one viable path, say so.

If the user did not ask for options and options are weakly supported, omit this section or keep it brief.

---

# 13. Decisions Needed

List decisions that need to be made, only when supported.

Separate:

## Immediate Decisions

Decisions needed before further commitment, meetings, spending, agreements, public claims, or execution.

## Later Decisions

Decisions that can wait until more evidence exists.

For each decision, include:

- **Decision**
- **Decision owner, if known**
- **Required information**
- **Consequence of delay, if source-supported**
- **Decision frame implied by the source, if any**

Do not decide on behalf of the user unless the source clearly supports a conclusion or the user asks for a recommendation.

---

# 14. Strategic Boundaries and Conditions

Extract boundaries, conditions, or non-negotiables implied by the source.

For each, include:

- **Boundary / condition**
- **Reason**
- **What it protects**
- **What would violate it, if source-supported**
- **Neutral wording**

Keep this precise and non-inflammatory.

---

# 15. Open Questions

List only questions necessary to clarify the strategic situation.

Good questions should clarify:

- ownership;
- authority;
- incentives;
- stakeholder commitments;
- funding;
- governance;
- scope;
- risk;
- next decisions.

Avoid generic questions.

---

# 16. Vault-Ready Strategic Notes

Create concise knowledge-vault entries only from strong source-supported material.

Each entry should include:

- **Title**
- **Type:** strategic thesis, governance issue, risk, stakeholder insight, incentive issue, decision, assumption, boundary
- **Entry**
- **Tags**

Use a compact starting vocabulary. Treat tags as extensible but controlled.

Starting tags:

- `strategy`
- `governance`
- `power-analysis`
- `decision-rights`
- `incentives`
- `risk`
- `ownership`
- `control`
- `stakeholders`
- `execution-risk`
- `trust`
- `funding`
- `sustainability`
- `contribution-alignment`
- `platform-strategy`

Propose a new tag only when:

1. at least one extracted item cannot be tagged accurately with the existing vocabulary;
2. the tag would likely recur across future sources;
3. the tag names a durable concept, not a one-off topic;
4. the tag reduces distortion rather than adding decorative specificity;
5. no more than 3 new tags are proposed per run unless the source is unusually broad.

---

# 17. Recommended Follow-Up Extractions

Recommend companion extractions only when the source strongly supports them.

Use only these categories:

- `meaning`
- `architecture`
- `execution`
- `adoption`

For each recommendation, include:

- **Recommended extraction**
- **Why it is warranted**
- **Expected value**

If no follow-up extraction is warranted, omit this section unless the user requested a complete template or explicit follow-up status.

---

## Optional: Prompt Evolution Notes

Include this section only if the run reveals a concrete improvement to this prompt.

Do not include prompt-evolution notes when the user asked only for a clean extraction artifact.

Do not suggest changes merely because new ideas are possible.

Suggest changes only when they would improve source fidelity, reduce repetition, clarify tags, strengthen safeguards, or remove unnecessary cognitive load.

Include only:

- **Suggested new tags:** Maximum 3, only if the existing vocabulary would distort the source.
- **Prompt patch:** Exact wording to add, remove, or replace.
- **Reason:** The specific failure mode the change prevents.

If no concrete improvement is justified, omit this section unless the user explicitly asked for prompt-improvement notes.

---

## Final Quality Bar

The output should let a future reader understand the strategic structure of the source without needing the full source, without exposing unnecessary private details, without inventing strategy that was not present, and without flattening the source into a generic risk/governance template.

