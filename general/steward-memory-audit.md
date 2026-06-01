# Steward Memory Audit

Run this prompt to verify the steward memory system is actually working.
Produces a markdown report the prompt-improvement agent can act on.

## Two Modes

**Cold audit** (any agent, no conversation context): examine memory directories
for freshness, coverage, and quality. Answers: "Is anything being written? Is
it sparse? Are there obvious gaps?"

**Hot audit** (steward mid-session or at session close): compare what happened
in THIS conversation to what was actually recorded. Answers: "Did the steward
capture the corrections, decisions, and lessons from this session?"

Detect mode automatically: if you have conversation context with owner
corrections, decisions, or lessons, run hot audit. If you're a fresh agent
with no prior conversation, run cold audit.

## Cold Audit Steps

### 1. Scan memory directories

Check these locations and report what exists:

```
# Universal role memory
ls -lt ~/.agents/agents/project-steward/memory/*.md 2>/dev/null | head -20

# Project-local steward memories (check each project that has a steward home)
find ~/work -path "*/.dev/ai/roles/project-steward/memory/*.md" -type f 2>/dev/null | head -30

# Private owner context
ls -lt ~/.agents-private/project-steward/projects/*/  2>/dev/null | head -20

# MS knowledge tree
ls -lt ~/.agents-private/project-steward/master-steward/knowledge/projects/*.md 2>/dev/null | head -20
```

### 2. Freshness check

For each directory with files, report:
- Most recent file modification date
- Oldest file modification date
- Total file count
- Any file not modified in >14 days (stale)

### 3. Content quality spot-check

Read the 3 most recent memory files. For each, check:
- Does it have proper frontmatter (name, description, metadata.type)?
- Is the content specific and actionable, or vague ("remember to be better")?
- Does it reference a concrete event, correction, or decision?
- Is it >3 lines of actual content (not just frontmatter)?

### 4. Coverage scan

Check for obvious gaps:
- Does MEMORY.md index exist and have entries? Count them.
- Are there memories tagged `scope: global-candidate` that haven't been reviewed?
- Are there memories tagged `scope: promoted-to-prompt` — how many?
- Is the MS MASTER-INDEX.md `last_updated` for T1 projects within 14 days?

### 5. Session record chain

Check the last 3 session records in `~/.agents/.dev/ai/sessions/`:
- Do they mention owner corrections? If so, do matching memory files exist?
- Do they mention decisions? If so, are those decisions captured anywhere durable?
- Are there "lessons learned" in BACKWARD sections that have no corresponding memory?

## Hot Audit Steps (in addition to cold audit)

### 6. This-session capture check

Scan the current conversation for:
- **Owner corrections** ("don't do X", "stop doing Y", "that's wrong"): was a memory file created for each?
- **Owner decisions** ("use X", "we're going with Y", "approved"): was the decision recorded in the appropriate artifact (decision log, memory, active constraint, knowledge file)?
- **Behavioral lessons** (something went wrong and was corrected): was it logged to the tuning log?
- **New facts** (credentials, paths, people, relationships): were they stored in the right layer (project-local, universal, or private)?

For each missed capture, report:
- What happened (quote or paraphrase the owner)
- What should have been created
- Where it should have been saved
- Why it matters for future sessions

### 7. Knowledge maintenance check (MS only)

If this was a Master Steward session:
- Were any T1 project phases discussed? If so, was `knowledge/projects/{slug}.md` updated?
- Were any new cross-project relationships discovered? If so, was `cross-project-map.md` updated?
- Was MASTER-INDEX Section 0 (top priorities) still accurate at session close?

## Report Format

Write the report to `.dev/ai/reports/{timestamp}-steward-memory-audit.md` using:

```markdown
---
type: steward-memory-audit
mode: cold | hot
created: YYYY-MM-DD-HH-MM-SSZ
auditor: [agent role]
project: [project or "portfolio" for MS]
---

# Steward Memory Audit — [date]

## Summary
- Mode: [cold|hot]
- Memory directories scanned: [count]
- Total memory files found: [count]
- Freshness: [newest file date] to [oldest file date]
- Quality: [good|sparse|problematic]
- Missed captures this session: [count or N/A for cold]

## Freshness Report
[per-directory breakdown]

## Quality Spot-Check
[3 most recent files assessed]

## Coverage Gaps
[missing memories, stale indexes, unreviewed global-candidates]

## Missed Captures (hot audit only)
[each missed item with what/where/why]

## Recommendations for Prompt Improvement
[specific, actionable items the PI agent should address]
```

## How to Use the Report

Hand the report path to the prompt-improvement agent:
```
You are the prompt-improvement agent. Read the steward memory audit at:
[path to report]
Address the recommendations. If the gaps are systemic (same type of capture
missed repeatedly), add or strengthen the relevant prompt rule.
```
