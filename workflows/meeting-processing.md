# Meeting Processing Prompt

## Purpose

Process a work session meeting transcript or notes into the 4 standard DC extracts. This is the same distillation methodology used for WhatsApp chat processing (WO-SUP-005), adapted for longer-form meeting content.

## Input

A markdown file from `~/work/obsidian-vault/distributed-creatives-vault/general/meetings/work-sessions/`. Meeting files may be:

- Raw transcripts (conversational, speaker-attributed)
- Agent briefs (already structured by an LLM from a transcript)
- Action item lists with discussion summaries
- Mixed format (some structured, some raw)

Read the entire meeting file before producing any extracts. Understand context, participants, projects discussed, and the meeting's temporal position (what came before, what's being planned).

## Output

Produce exactly 4 extract files in the companion `-extracts/` directory alongside the meeting file. Each file follows a specific format described below.

### Output File Naming

```
<meeting-filename-without-ext>-extracts/
  Advocacy Vision.md
  Core Signals.md
  Broad-Signal Digest (Frivolity Filter).md
  Project-Segmented Summary.md
```

---

## Extract 1: Advocacy Vision

**File:** `Advocacy Vision.md`

**Purpose:** Synthesize the meeting into the ongoing advocacy narrative. What does this meeting contribute to the larger story of Distributed Creatives, SaveTheCreators, and the creator economy movement?

**Format:**

```markdown
<date range or meeting date>

## 1. **<Pillar Title>: <Subtitle>**

| Pillar | Core Idea | Why It's Strong |
|--------|-----------|-----------------|
| **<Name>** | <Concise description> | <Why this matters strategically> |
| ... | ... | ... |

### How This Period Advances the Advocacy Framework
1. **<Headline>:** <Detail>
2. ...

---

## 2. **Visionary Statements & Calls to Action**

| Source | Vision / CTA | Key Takeaway |
|--------|--------------|--------------|
| **<Speaker> -- <Context>** | "<Quote or paraphrase>" | <Why it matters> |
| ... | ... | ... |

### Actionable Ideas from This Period
- **<Idea Name>**: <Description>
- ...

---

## 3. **Operational Tactics & Community Building**

| Tactic | Description | How It Supports the Vision |
|--------|-------------|---------------------------|
| **<Name>** | <What it is> | <How it connects to the larger mission> |
| ... | ... | ... |

---

## 4. **Suggested Next Steps**

1. **<Step>**
   - <Detail>
2. ...
```

**Guidelines:**
- Extract genuine vision and advocacy material, not operational minutiae
- Attribute statements to speakers when known
- Connect dots to the DC advocacy framework pillars: Technology in Service of Creativity, Community Ownership, Creator Rights, Open Infrastructure
- Include concrete evidence (numbers, dates, names) that strengthen the narrative
- Keep the tone professional and suitable for grant applications or board presentations

---

## Extract 2: Core Signals

**File:** `Core Signals.md`

**Purpose:** Capture the individual important signals from the meeting -- decisions, announcements, capability reveals, strategic shifts, partnership developments, and other concrete events that an agent or team member needs to know about.

**Format:**

```markdown
<date range or meeting date>

## <Project or Topic Area>

### <Signal Headline>
**<Speaker> <verb>s <what happened>.**
*<Project tags> -- <Signal type: Capability/Scope, Vision, Evidence/Result, Decision, Risk, Dependency>*
*<Speaker> -- <Date and timezone>*

> <Key quote or paraphrase from the discussion>

### <Next Signal>
...
```

**Guidelines:**
- Each signal is a discrete, quotable fact or decision
- Include the project/topic tags (e.g., `peers.social, LAN -- Capability/Scope`)
- Include speaker attribution and approximate timestamp/date when available
- Include a direct quote or close paraphrase in a blockquote
- Group signals by project or topic area
- Signal types: `Capability/Scope`, `Vision`, `Evidence/Result`, `Decision`, `Risk`, `Dependency`, `Realization`, `Request`
- Bias toward specificity -- numbers, names, URLs, versions, amounts

---

## Extract 3: Broad-Signal Digest (Frivolity Filter)

**File:** `Broad-Signal Digest (Frivolity Filter).md`

**Purpose:** A high-level narrative digest that filters out noise and captures only the signals that move the organization forward. This is the "executive summary for someone who wasn't there."

**Format:**

```markdown
<date range or meeting date>

# <Period Title: A short thematic summary>

**<1-3 sentence overview paragraph.>**

*<Attribution -- Signal type>*
*<Speaker -- Date>*

> <Supporting quote>

### <Signal Headline>
**<Description sentence.>**
*<Project tags -- Signal type>*
*<Speaker -- Date>*

> <Supporting quote>

### <Next signal>
...
```

**Guidelines:**
- Apply a frivolity filter: skip social chatter, jokes, off-topic tangents, and anything that doesn't represent a real development or strategic insight
- Lead with the most impactful development
- The opening paragraph should capture the period's theme in 1-3 sentences
- Each signal gets a headline, a description, attribution, and a supporting quote
- Fewer signals is better -- aim for 8-15 signals, not 50
- This is the document a busy board member reads to stay informed

---

## Extract 4: Project-Segmented Summary

**File:** `Project-Segmented Summary.md`

**Purpose:** Organize everything discussed by project, creating a clean reference of what was said about each active initiative.

**Format:**

```markdown
<date range or meeting date>

# Project-Segmented Summary

## <Project Name>
- <Bullet point summary of what was discussed/decided>
- <Another point>
- <Speaker attribution where relevant: "Grig: '<quote>'">

## <Next Project>
- ...
```

**Standard project segments (use when relevant, skip when nothing was discussed):**

- **peers.social** -- The social network/platform
- **Local Artist Network (LAN)** -- Digital signage, venue network, local infrastructure
- **Save The Creators (STC) / CAFI** -- Advocacy, policy, campaigns
- **PeerMesh / Universal Manifest** -- Protocol, standards, federation
- **EverArchive** -- Permanent storage, provenance, proof-of-ownership
- **DC (Organization)** -- Organizational matters, team, legal, governance
- **Distributed Studios** -- Creator-economy studio concept
- **GAS (Global Agents System)** -- AI infrastructure, automation
- **Fund Raising** -- Grants, sponsorships, fundraising campaigns
- **Rivr / External Partners** -- External collaborators and their projects

**Non-project categories (use for items that don't fit a project):**

- **Vision Statements** -- Big-picture directional statements not tied to one project
- **New Project Ideas** -- Concepts raised but not yet formalized into a project
- **People** -- New contacts, team changes, relationship developments
- **Someday/Maybe** -- Ideas explicitly deferred or marked as future possibilities
- **Personal / Creative Practice** -- Individual creative work by team members (e.g., poetry, art)

**Guidelines:**
- Every substantive point from the meeting should appear in exactly one segment
- Use bullet points, not paragraphs
- Include speaker attributions for key statements
- Include specific details: amounts, dates, names, URLs
- If a topic spans multiple projects, place it under the primary project and cross-reference

---

## General Rules for All Extracts

1. **No hallucination.** Every fact, quote, and detail must come from the source meeting file. Do not infer or assume.
2. **Preserve voice.** When quoting speakers, use their actual words. Clean up speech disfluencies but don't rewrite meaning.
3. **Date header.** Every extract file starts with the meeting date or date range on line 1.
4. **No meta-commentary.** Do not include notes about the processing methodology or explain what the extract is. Just produce the extract.
5. **Meeting-specific adaptation.** Unlike WhatsApp (many short messages over days/weeks), meetings are dense single sessions. Expect deeper discussion on fewer topics. Adjust signal density accordingly.
6. **Existing extract quality.** Reference existing WhatsApp extracts in the `WhatsApp/` sibling directory for tone and format calibration if needed.

---

## Agent Dispatch Instructions

When dispatching an LLM agent to process a meeting, provide:

```
Read the processing prompt:
  ~/.agents/prompts/workflows/meeting-processing.md

Read the meeting source:
  <path to meeting file>

Write 4 extract files to:
  <path to extracts directory>

Expected outputs:
  1. <extracts-dir>/Advocacy Vision.md
  2. <extracts-dir>/Core Signals.md
  3. <extracts-dir>/Broad-Signal Digest (Frivolity Filter).md
  4. <extracts-dir>/Project-Segmented Summary.md
```
