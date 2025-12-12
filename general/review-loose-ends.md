# Role: AI Work Audit & Loose Ends Extraction

**Objective:** Systematically review historical AI work artifacts to identify unfinished tasks, pending actions, and loose ends that require follow-up or completion.

**Context:** After periods of intense AI-assisted development, work artifacts accumulate across multiple subdirectories in `.dev/ai/`. These documents contain scattered references to "next actions", "owner: user", "verify deployment", "TODO", and other indicators of incomplete work. You must extract and consolidate these into a single actionable list.

---

## The Loose Ends Extraction Protocol (7-Phase Process)

You must follow this strict sequential process. Do not skip phases.

### Phase 1: Scope Definition

1. **Determine Time Range**:
   - Default: Last 14 days of work
   - User can specify: "Review last 30 days" or "Review all work since [DATE]"
   - Command: `find .dev/ai -type f -name "*.md" -mtime -14`

2. **Identify All AI Work Directories**:
   Scan AI artifact directories from multiple tools. Do NOT assume you know what subdirectories exist.

   **Primary Directories to Scan:**

   - **Claude Code CLI**: `.dev/ai/` (project-local)
   - **Cursor IDE**: `~/.cursor/projects/[current-project]/`
   - **Antigravity**: `~/.gemini/antigravity/conversations/`, `~/.gemini/antigravity/brain/`

   ```bash
   # Claude Code artifacts (project-local)
   find .dev/ai -type d | sort

   # Cursor project artifacts (if using Cursor)
   project_slug=$(basename $(pwd) | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
   find ~/.cursor/projects -type d -iname "*${project_slug}*" 2>/dev/null

   # Antigravity artifacts (global)
   find ~/.gemini/antigravity/conversations -type f -mtime -14 2>/dev/null
   find ~/.gemini/antigravity/brain -type f -mtime -14 2>/dev/null
   ```

3. **Catalog Document Types by Tool**:

   **Claude Code CLI** (`.dev/ai/`):
   - `handoffs/` - Agent handoff documents
   - `session-summaries/` - Session ending summaries
   - `workorders/` - Work order documents
   - `accomplishments/` - Completed work reports
   - `reminders/` - Pending reminders
   - `fixes/` - Bug fixes and critical issues
   - `research/` - Research findings
   - `audits/` - System audits
   - `plans/` - Implementation plans
   - Root-level files like `STATE-OF-THE-PROJECT.md`

   **Cursor IDE** (`~/.cursor/projects/`):
   - Project-specific composer sessions
   - Chat history (may require export/conversion from internal format)
   - Project rules and context files

   **Antigravity** (`~/.gemini/antigravity/`):
   - `conversations/` - Conversation protobuf files (`.pb`)
   - `brain/` - Project knowledge and context
   - `browser_recordings/` - Recorded browser interactions
   - `implicit/` - Implicit context and learning

   **Note**: Cursor and Antigravity may use binary formats (`.pb`, `.vscdb`). For full extraction, you may need specialized tools or export functionality. Focus on readable artifacts (`.md`, `.json`, `.txt`) unless explicitly asked to process binary formats.

4. **Get Recent Files List**:
   ```bash
   # Claude Code (markdown files)
   find .dev/ai -type f -name "*.md" -mtime -[N] | sort

   # Cursor (readable files only)
   project_slug=$(basename $(pwd) | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
   find ~/.cursor/projects -type d -iname "*${project_slug}*" -exec find {} -type f \( -name "*.md" -o -name "*.txt" -o -name "*.json" \) -mtime -[N] \; 2>/dev/null

   # Antigravity (note: .pb files may need special handling)
   find ~/.gemini/antigravity/conversations -type f -mtime -[N] 2>/dev/null
   find ~/.gemini/antigravity/brain -type f -name "*.json" -o -name "*.md" -mtime -[N] 2>/dev/null
   ```

**Output of Phase 1**: A counted inventory of files to review, organized by subdirectory.

---

### Phase 2: Pattern-Based Extraction (Broad Scan)

**Goal**: Search all in-scope documents for loose end indicators.

**Required Search Patterns** (case-insensitive):

Use `grep` or similar to find these patterns across all files:

```bash
# Core action indicators
NEXT ACTIONS?
NEXT SESSION
TODO:?
ACTION REQUIRED
PENDING

# Ownership indicators
OWNER:\s*(USER|HUMAN|VERIFY)
ASSIGNED TO:.*USER

# Status indicators
REMAINING
INCOMPLETE
BLOCKED
NOT (DONE|COMPLETE|FINISHED)
NEEDS.*REVIEW
NEEDS.*VERIFICATION
VERIFY|VALIDATION NEEDED

# Priority indicators
CRITICAL
IMMEDIATE
URGENT
HIGH PRIORITY

# Deployment indicators
DEPLOYMENT.*PENDING
DEPLOY.*INCOMPLETE
VPS.*VERIFY
PRODUCTION.*TODO

# Recommendation indicators
SUGGESTED:
RECOMMENDED:
SHOULD:
CONSIDER:
FOLLOW.?UP
```

**Extraction Rules**:

1. For each match, capture:
   - Source file path and line number
   - 3 lines of context BEFORE the match
   - 5 lines of context AFTER the match
   - Document timestamp (from filename if available)

2. Preserve exact wording from documents - do not paraphrase

3. Link multiple related items from the same document

**Example grep commands**:
```bash
# Claude Code artifacts
grep -riE "(NEXT ACTIONS?|TODO:|OWNER:.*USER|PENDING|VERIFY)" .dev/ai/ \
  -A 5 -B 3 --include="*.md" > /tmp/loose-ends-claude.txt

# Cursor artifacts (readable files only)
project_slug=$(basename $(pwd) | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9-]/-/g')
cursor_dir=$(find ~/.cursor/projects -type d -iname "*${project_slug}*" 2>/dev/null | head -1)
if [ -n "$cursor_dir" ]; then
  grep -riE "(NEXT ACTIONS?|TODO:|OWNER:.*USER|PENDING|VERIFY)" "$cursor_dir" \
    -A 5 -B 3 --include="*.md" --include="*.txt" --include="*.json" >> /tmp/loose-ends-cursor.txt 2>/dev/null
fi

# Antigravity artifacts (readable files only, .pb files skipped unless converted)
grep -riE "(NEXT ACTIONS?|TODO:|OWNER:.*USER|PENDING|VERIFY)" ~/.gemini/antigravity/brain/ \
  -A 5 -B 3 --include="*.md" --include="*.json" >> /tmp/loose-ends-antigravity.txt 2>/dev/null

# Combine all sources
cat /tmp/loose-ends-claude.txt /tmp/loose-ends-cursor.txt /tmp/loose-ends-antigravity.txt > /tmp/loose-ends-raw.txt
```

**Output of Phase 2**: Raw extraction file containing all matches with context.

---

### Phase 2.5: Deep Review of Recent Documents (Targeted Scan)

**Goal**: Carefully read the most recent documents in each subdirectory to catch small items that pattern matching might miss, especially "suggested next steps" mentioned at the end of completed work.

**Why This Matters**: Documents often follow a standard format where the main work is described, then at the END there are suggestions for follow-up work. Pattern matching catches explicit "TODO" markers but misses subtle recommendations like "it would be good to..." or "future sessions could...". These are exactly the loose ends we're looking for.

#### Step 2.5.1: Identify the 10 Most Recent Files Per Subdirectory

For each subdirectory in `.dev/ai/`, get the 10 most recently modified files:

```bash
# Get subdirectories
for dir in .dev/ai/*/; do
  echo "=== $dir ==="
  ls -t "$dir"*.md 2>/dev/null | head -10
done
```

**Priority Subdirectories** (read these first, they're most likely to have loose ends):
1. `handoffs/` - Session handoffs always end with "Next Steps"
2. `audits/` - Conversation summaries have "Next Actions and Owners" section
3. `accomplishments/` - Completed work often suggests follow-up
4. `workorders/` - May have incomplete checklist items
5. `work-orders/` - Same as above
6. `fixes/` - May have "remaining issues"

#### Step 2.5.2: Read End-of-Document Sections

For each of the 10 most recent files in priority subdirectories, **read the last 100 lines** to find:

**Standard Section Headers to Look For** (these appear at the end of handoffs/audits):
- `## PRIORITY NEXT STEPS`
- `## Next Actions`
- `## Next Actions and Owners`
- `## Remaining Tasks`
- `## Remaining Work`
- `## Follow-up Items`
- `## Gaps and Risks`
- `## Open Questions`
- `## Future Work`
- `## Optional Next Steps`
- `## Recommended (Should Do)`
- `## Nice to Have`

```bash
# Example: Read last 100 lines of most recent handoff
tail -100 "$(ls -t .dev/ai/handoffs/*.md | head -1)"
```

#### Step 2.5.3: Extract Subtle Recommendations

Look for language patterns that suggest incomplete work but aren't explicit TODOs:

- "It would be good to..."
- "A future session could..."
- "This should be verified..."
- "Consider adding..."
- "Once X is done, then Y..."
- "When you have time..."
- "Low priority but..."
- "Nice to have..."
- "Eventually..."
- Checklist items with `- [ ]` (unchecked)
- Items marked with emojis like `⚠️`, `🔜`, `📌`

#### Step 2.5.4: Cross-Reference Accomplishments

Read the `accomplishments/` directory to understand what was marked "complete" - these often contain "Optional Next Steps" or "Future Enhancements" sections that represent loose ends.

**Output of Phase 2.5**: Additional loose ends extracted from careful document reading, especially subtle recommendations and follow-up suggestions.

---

### Phase 3: Categorization & Deduplication

**Goal**: Transform raw extractions into structured, non-redundant action items.

1. **Remove Duplicates**:
   - Same action mentioned in multiple documents (handoff → session summary)
   - Keep the MOST RECENT or MOST DETAILED version
   - Note all source references

2. **Categorize by Priority** (based on keywords and context):

   - **CRITICAL**: Contains "CRITICAL", "BLOCKING", "SECURITY", "DATA LOSS", "PRODUCTION DOWN"
   - **HIGH**: Contains "DEPLOYMENT", "VERIFY", "IMMEDIATE", or explicitly marked "owner: user"
   - **MEDIUM**: Contains "SHOULD", "RECOMMENDED", "ENHANCEMENT"
   - **LOW**: Contains "NICE TO HAVE", "FUTURE", "CONSIDER"

3. **Categorize by Owner**:

   - **USER**: Explicitly says "owner: user" OR requires human decision (strategic, budget, legal)
   - **AGENT**: Can be delegated to AI (refactoring, testing, documentation)
   - **EXTERNAL**: Requires third-party action (DNS, hosting, vendor)
   - **UNCLEAR**: Insufficient context to determine

4. **Categorize by Type**:

   - Deployment & Infrastructure
   - Code & Implementation
   - Testing & Verification
   - Documentation
   - Research & Investigation
   - Configuration & Setup
   - Security & Compliance

**Output of Phase 3**: Structured inventory with categorized, deduplicated items.

---

### Phase 4: Verification Checklist Generation

**Goal**: Create a list of completed work that should be verified, enabling a "trust but verify" second pass.

**Why This Matters**: AI agents mark work as "complete" but the actual system state may differ. This checklist allows the user to audit whether completed items are actually working.

#### Step 4.1: Extract Completed Items

From the documents reviewed, identify items marked as:
- ✅ Complete
- `[x]` Checked
- Status: DONE / FIXED / DEPLOYED / COMPLETE
- "This has been completed"
- Accomplishment entries

#### Step 4.2: Generate Verification Commands

For each completed item, generate a verification command or check:

| Completed Item | Verification Command/Check |
|----------------|---------------------------|
| "SEO deployed to VPS" | `curl -s https://site.com/ \| grep '<meta name="description"'` |
| "Backup cron installed" | `ssh vps 'crontab -l \| grep backup'` |
| "Plugin activated" | Check WP admin or `wp plugin list --status=active` |
| "Cache poisoning fixed" | Test AJAX request doesn't poison cache |
| "CI/CD working" | Push test commit, verify VPS received it |

#### Step 4.3: Cross-Reference with STATE-OF-THE-PROJECT.md

Read `.dev/ai/STATE-OF-THE-PROJECT.md` and compare:

1. **Achievements listed** - Are they actually verified?
2. **Blockers listed as "None"** - Are there hidden blockers in loose ends?
3. **Milestones marked complete** - Do they match accomplishments?
4. **Current Status claims** - Are they accurate?

Note any discrepancies for the report.

**Output of Phase 4**:
- Verification checklist with commands
- STATE-OF-THE-PROJECT discrepancy notes (if any)

---

### Phase 5: Report Generation

**Goal**: Create a single, scannable document that consolidates all loose ends.

**File to Create**: `.dev/ai/LOOSE-ENDS-REVIEW-[YYYY-MM-DD].md`

**Note**: This review consolidates loose ends from ALL AI tools (Claude Code, Cursor, Antigravity). Sources are tagged by tool.

**Required Report Structure**:

```markdown
# Loose Ends Review - [DATE]

Generated from AI work artifacts spanning [START_DATE] to [END_DATE]

---

## Executive Summary

- **Total items found**: [N]
- **Critical items**: [N]
- **High priority**: [N]
- **Owner breakdown**: User [N], Agent [N], External [N], Unclear [N]
- **Files reviewed**: [N]
- **Recent documents deeply read**: [N] (Phase 2.5)

---

## CRITICAL ITEMS (Immediate Attention Required)

### [Item Title]
- **Source**: `path/to/file.md:123`
- **Tool**: Claude Code / Cursor / Antigravity
- **Owner**: USER / AGENT / EXTERNAL
- **Category**: [Type]
- **Context**:
  > [Verbatim excerpt from document]
- **Action Required**: [Clear description]

[Repeat for each critical item]

---

## HIGH PRIORITY ITEMS

[Group by category: Deployment, Code, Testing, etc.]

### Deployment & Infrastructure
1. **[Item]**
   - Source: `file.md:line`
   - Owner: [X]
   - Action: [Y]

[Repeat for each category]

---

## MEDIUM PRIORITY ITEMS

[Same structure, grouped by category]

---

## LOW PRIORITY ITEMS

[Same structure, grouped by category]

---

## SUBTLE RECOMMENDATIONS (From Phase 2.5 Deep Review)

These items weren't explicit TODOs but were mentioned as suggestions or future work:

1. **[Item]**
   - Source: `file.md` (end of document)
   - Context: > "It would be good to..."
   - Priority: LOW / MEDIUM
   - Owner: AGENT / USER

---

## ITEMS NEEDING CLARIFICATION

These items lack sufficient context to determine priority or ownership:

1. **[Item]**
   - Source: `file.md:line`
   - Excerpt: > "..."
   - Question: What is the intended outcome?

---

## VERIFICATION CHECKLIST

Items marked as "complete" that should be verified:

| # | Completed Item | Verification | Status |
|---|---------------|--------------|--------|
| 1 | [Item from accomplishment] | `[command or check]` | ⬜ Not verified |
| 2 | [Item from handoff] | `[command or check]` | ⬜ Not verified |
| ... | ... | ... | ... |

### STATE-OF-THE-PROJECT.md Discrepancies

| Claim in STATE doc | Actual Status | Note |
|--------------------|---------------|------|
| [Milestone X complete] | [Needs verification] | [Why] |
| [No blockers] | [Blocker found: Y] | [Details] |

---

## RECOMMENDED EXECUTION ORDER

Based on dependencies and impact:

1. [CRITICAL item X] - Blocks [Y]
2. [HIGH item Z] - Enables [W]
3. ...

---

## APPENDIX: Source Documents

| File | Loose Ends Count | Last Modified |
|------|------------------|---------------|
| `handoffs/2025-12-07-...md` | 5 | 2025-12-07 |
| ... | ... | ... |

### Documents Deeply Read (Phase 2.5)

| Subdirectory | Files Read | Loose Ends Found |
|--------------|------------|------------------|
| `handoffs/` | 10 | 3 |
| `audits/` | 10 | 5 |
| ... | ... | ... |

---

**Next Steps**:
1. Review CRITICAL items with user
2. Create work orders for AGENT-owned items
3. Schedule USER-owned items
4. Run verification checklist (optional second pass)
5. Update STATE-OF-THE-PROJECT.md if discrepancies found
6. Archive this report to `.dev/ai/loose-ends-archive/`
```

**STOP after generating this report and present it to the user.**

Do NOT automatically create work orders or take other actions unless explicitly requested.

---

### Phase 6: Optional Follow-Up Actions

**Only proceed with these if the user explicitly requests them:**

#### Option A: Create Work Orders

For each AGENT-owned item, generate:
- `.dev/ai/workorders/WO-[N]-[slug].md`
- Follow existing work order format in the project
- Link back to this loose ends review

#### Option B: Update Project State

Update `.dev/ai/STATE-OF-THE-PROJECT.md`:
- Add section for "Pending Loose Ends"
- Link to the loose ends review report
- Update overall completion percentages
- Fix any discrepancies found in Phase 4

#### Option C: Create Backlog Items

For USER-owned items:
- Add to conversation backlog or project backlog
- Tag with priority and category
- Set reminders for time-sensitive items

#### Option D: Run Verification Audit

Execute the verification checklist from Phase 4:
- Run each verification command
- Update the checklist with actual status (✅ Verified / ❌ Failed / ⚠️ Partial)
- Generate a separate `VERIFICATION-AUDIT-[DATE].md` report

---

### Phase 7: Verification Audit (Optional - User Requested)

**Only run if user selects Option D or explicitly requests verification.**

**Goal**: Actually verify that completed items are working as claimed.

#### Step 7.1: Execute Verification Commands

For each item in the verification checklist:

```bash
# Example verifications
curl -s https://site.com/ | grep '<meta name="description"'  # SEO check
ssh deployer@vps 'crontab -l | grep backup'                   # Backup cron
ssh deployer@vps 'docker ps | grep mz_'                       # Containers
# etc.
```

#### Step 7.2: Document Results

Update the checklist with actual results:

| # | Item | Verification | Status | Notes |
|---|------|--------------|--------|-------|
| 1 | SEO deployed | `curl ... | grep meta` | ✅ Verified | Returns description |
| 2 | Backup cron | `crontab -l` | ❌ Failed | No backup job found |
| 3 | Webhook active | `systemctl status` | ⚠️ Partial | Running but 2 commits behind |

#### Step 7.3: Generate Verification Report

Create `.dev/ai/VERIFICATION-AUDIT-[DATE].md` with:
- Summary of pass/fail/partial
- Failed items become new loose ends
- Recommendations for fixes

#### Step 7.4: Update STATE-OF-THE-PROJECT.md

If verification reveals issues:
- Move items from "Completed" to "Needs Attention"
- Update blockers section
- Add verification audit link

**Output of Phase 7**: Verification audit report and updated project state.

---

## Constraints & Guardrails

1. **Stay Read-Only**: Do NOT modify source documents during extraction (Phases 1-5)
2. **No Scope Creep**: Review ONLY AI tool artifact directories, not the entire codebase
3. **No Interpretation**: Extract verbatim text; don't rewrite or "improve" loose ends
4. **No Execution**: Do NOT start working on loose ends; only catalog them
5. **Preserve Context**: Always include source file paths, line numbers, and tool name
6. **Binary Files**: Skip binary formats (`.pb`, `.vscdb`) unless user provides conversion tools
7. **Tool-Specific Handling**:
   - Claude Code: Full `.dev/ai/` scan
   - Cursor: Only readable files in project-specific directories
   - Antigravity: Focus on `brain/` and converted conversation exports

---

## Quality Checks

Before finalizing the report, verify:

- [ ] All subdirectories of `.dev/ai/` were scanned
- [ ] Search patterns covered all common loose end indicators
- [ ] **10 most recent files in priority subdirectories were deeply read (Phase 2.5)**
- [ ] End-of-document sections were checked for subtle recommendations
- [ ] Each item includes source file + line number
- [ ] Critical items are genuinely critical (not mislabeled)
- [ ] Duplicates across multiple documents are consolidated
- [ ] Verification checklist generated with runnable commands
- [ ] STATE-OF-THE-PROJECT.md cross-referenced for discrepancies
- [ ] Report is saved to `.dev/ai/LOOSE-ENDS-REVIEW-[DATE].md`

---

## Expected User Workflow

1. User invokes this prompt: "Review loose ends from the last 14 days"
2. You execute Phases 1-5
3. You present the report and ASK: "I found [N] items. Would you like me to:
   - (A) Create work orders for AGENT-owned items?
   - (B) Update STATE-OF-THE-PROJECT.md?
   - (C) Create backlog entries for USER-owned items?
   - (D) Run verification audit on completed items?
   - (E) None - I'll handle these manually"
4. You proceed with Phase 6/7 only if requested

---

**In the very last line of your final message before you stop, YOU MUST DISPLAY THE FOLLOWING LINES. (Blank lines included!)**

---

The "Review Loose Ends" prompt was the last message from the user.

---
