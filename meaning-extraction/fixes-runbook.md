Fix path: **patch selectively, starting with Universal. Do not reorganize the suite. Do not rewrite all five.**

## 1. Fix the main failure first: Universal is too absorbent

Universal currently covers meaning, doctrine, public messaging, anecdotes, language bank, presentation summary, and vault entries, so it can swallow Adoption and partially Strategy. Its own scope says it extracts “ethical, strategic, emotional, collaboration-related, and public-interest meaning,” and its outputs include public messaging, reusable anecdotes, language bank, and presentation-ready summary. 

### Apply this patch to Universal

#### Replace

```markdown
The goal is to help the author build a reusable knowledge vault by extracting any durable ethics, operating principles, adoption language, movement language, collaboration doctrine, or working hypotheses that the source actually supports.
```

#### With

```markdown
The goal is to help the author build a reusable knowledge vault by extracting durable ethics, operating principles, movement-level language, collaboration doctrine, and working hypotheses that the source actually supports.

Do not perform full adoption, outreach, narrative, strategy, architecture, or execution extraction inside this prompt. If the source strongly supports one of those companion extractions, recommend it as a follow-up instead of importing its category set here.
```

### Why

This prevents Universal from becoming the suite’s hidden mega-prompt.

---

## 2. Demote Universal’s public-output sections

Adoption already owns audience framing, objections, proof points, narrative structure, coalition language, public-safe summaries, and language banks.  Universal should keep only principle-level public language.

### In Universal, rename section 6

#### Replace

```markdown
# 6. Public Messaging Themes
```

#### With

```markdown
# 6. Principle-Level Public Messaging Themes

Use this section only for source-grounded principle-level themes.

Do not create audience strategy, objections, proof points, calls to action, public-safe summaries, coalition language, or full messaging plans here. Route those to the Adoption / Outreach / Narrative prompt.
```

### In Universal, narrow section 11

#### Replace

```markdown
# 11. Presentation-Ready Summary
```

#### With

```markdown
# 11. Optional Principle-Level Presentation Summary

Use this only when the source clearly supports public-facing presentation use. Keep it principle-level. Do not create a talk, deck structure, campaign message, audience-specific pitch, or outreach artifact here.
```

### Why

This keeps Universal useful without letting it duplicate Adoption.

---

## 3. Normalize source-context wording across all five prompts

Four prompts explicitly include uploaded files in Source Context; Universal does not. Product, Strategy, Adoption, and Execution all say the source may be in an “uploaded file.”    

### In Universal, replace

```markdown
Assume the source material is already available in the current conversation, document, transcript, thread, notes, or surrounding context.
```

### With

```markdown
Assume the source material is already available in the current conversation, document, transcript, thread, notes, uploaded file, or surrounding context.
```

### Why

This removes a needless inconsistency.

---

## 4. Standardize conditional-output behavior

Product, Strategy, Adoption, and Execution already treat sections as conditional or omit unsupported sections. Universal still says unsupported sections should say “Not strongly supported by this source,” which encourages full-template output. 

### In Universal, replace

```markdown
If a section is not supported, keep it brief and state: “Not strongly supported by this source.”
```

### With

```markdown
Treat numbered sections as a conditional menu, not a mandatory checklist.

Produce sections only when requested by the user, materially useful for the source, or necessary for the intended output.

Omit unsupported sections by default. If the user requested a full-template output and a section is unsupported, write one brief line: `No strong signal in this source.`
```

### Why

This reduces token cost and prevents forced extraction.

---

## 5. Make prompt-evolution behavior consistent

Universal still forces a “No prompt changes recommended” line when no improvement is justified. Product, Strategy, Adoption, and Execution already omit prompt-evolution notes unless useful or requested.     

### In Universal, replace

```markdown
If no concrete improvement is justified, write:

# Prompt Evolution Notes

No prompt changes recommended from this source material.
```

### With

```markdown
If no concrete improvement is justified, omit this section unless the user explicitly requested prompt-improvement notes.
```

### Why

This removes routine dead output.

---

## 6. Fix Execution’s follow-up inconsistency

Execution still requires:

```markdown
No follow-up extraction recommended.
```

when no follow-up is warranted.  The other specialized prompts omit this section unless useful or requested.

### In Execution, replace

```markdown
If no follow-up extraction is warranted, write:

No follow-up extraction recommended.
```

### With

```markdown
If no follow-up extraction is warranted, omit this section unless the user explicitly requested follow-up status or a complete-template output.
```

### Why

This aligns Execution with the rest of the suite and cuts noise.

---

## 7. Add one routing block to the top of the suite

Add this as a short shared preface before the five prompts, not inside every prompt.

```markdown
# Prompt Suite Routing

Use only the prompt whose extraction role matches the user’s immediate task.

- Use Universal Meaning for durable ethical, emotional, collaboration, public-interest, and worldview meaning.
- Use Product / Architecture / Standards / Idea for buildable concepts, system shape, workflows, data/state, interoperability, standards, and implementation implications.
- Use Strategic Situation / Governance / Risk for power, incentives, governance, leverage, control, risk, assumptions, and decision pressure.
- Use Adoption / Outreach / Narrative for audiences, adoption barriers, objections, proof needs, public-safe messaging, narrative structure, coalition language, and presentation material.
- Use Execution / Decisions / Work Order for decisions, tasks, blockers, dependencies, commitments, missing inputs, acceptance criteria, sequencing, and agent-ready handoff.

Do not combine prompts by default. If the source supports multiple extraction types, run the most relevant prompt first and recommend companion extractions only when strongly supported.
```

### Why

This gives future agents a fast decision path without bloating each prompt.

---

## 8. Add one shared overlap rule to the suite preface

Add this directly after the routing block.

```markdown
# Overlap Routing Rules

When categories overlap, route by function:

- Strategic risks belong in Strategy.
- Implementation risks belong in Product / Architecture.
- Messaging, trust, comprehension, and proof barriers belong in Adoption.
- Work blockers belong in Execution.
- System or technical dependencies belong in Product / Architecture.
- Work dependencies belong in Execution.
- User/system workflows belong in Product / Architecture.
- Operational sequencing belongs in Execution.
- Principle-level public language may appear in Universal.
- Audience-specific public language belongs in Adoption.
```

### Why

This prevents the same source signal from being extracted five ways.

---

## 9. Add one shared vault-provenance rule

Add this to the suite preface, not repeatedly inside every prompt.

```markdown
# Vault Compatibility Rule

For vault-ready outputs, preserve:

- extraction_type
- source_type
- source_scope
- source_date, if known
- confidence
- public_safe status
- tags
- recommended_followup_extractions, if strongly supported

Do not strip uncertainty, source limitations, or public/private status from reusable notes.
```

### Why

The four specialized prompts already have metadata headers. Universal does not. This patch improves interoperability without forcing a heavy metadata block into every Universal run.    

---

## 10. Do not patch everything from the audit

Skip these unless problems recur:

* Do not add a full metadata header to Universal yet.
* Do not create one global tag taxonomy.
* Do not rewrite Product.
* Do not rewrite Strategy.
* Do not rewrite Adoption.
* Do not add new extraction categories.
* Do not merge the suite.
* Do not add more examples.
* Do not add more public/private language unless leakage actually appears.

---

# Minimal Fix Order

Apply in this order:

1. **Universal scope patch**
2. **Universal public-output demotion**
3. **Universal uploaded-file wording**
4. **Universal conditional-output rule**
5. **Universal prompt-evolution omission rule**
6. **Execution follow-up omission rule**
7. **Suite routing preface**
8. **Suite overlap routing rule**
9. **Suite vault compatibility rule**

That is the shortest path to a cleaner suite. The real problem is not the five-prompt architecture. The problem is that Universal is too broad and a few shared behaviors are inconsistent. Patch those; leave the suite mostly intact.
