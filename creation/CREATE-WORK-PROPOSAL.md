# Work Proposal Creation Protocol

## 🚨 AUTOMATIC TRIGGERING RULES (MANDATORY)

**READ THIS FIRST:** Proposal creation is now MANDATORY for large/complex work.

### When Proposals Are REQUIRED (Agent MUST suggest)

**You MUST suggest creating a proposal (before work orders) when ANY of these indicators are present:**

1. **Major Task Threshold**
   - Work involves **5+ major tasks** (not subtasks)
   - Action: STOP and suggest proposal creation

2. **Timeline Threshold**
   - Estimated timeline is **3+ weeks**
   - Action: STOP and suggest proposal creation

3. **Architectural Decision Threshold**
   - Multiple architecture alternatives need evaluation
   - System design decisions required
   - Technology stack choices needed
   - Action: STOP and suggest proposal creation

4. **Complexity Threshold**
   - Solution approach is unclear or multiple approaches exist
   - Research phase needed before implementation
   - Proof-of-concept required
   - Action: STOP and suggest proposal creation

5. **Cross-System Impact Threshold**
   - Changes affect multiple modules/systems
   - Integration points unclear
   - Coordination between teams needed
   - Action: STOP and suggest proposal creation

### Agent Response Template (When Proposal Needed)

```
🚨 PROPOSAL REQUIRED

This appears to be a complex initiative that requires a proposal:
- [x] 5+ major tasks identified
- [x] Multi-week timeline (estimated 3-4 weeks)
- [ ] Architectural decisions needed
- [ ] Multiple alternatives to evaluate
- [x] Cross-system impact

Creating a proposal will:
✅ Evaluate all viable approaches
✅ Break work into coordinated phases
✅ Generate work orders with proper dependencies
✅ Provide clear decision rationale
✅ Enable higher-level project tracking

I will create a proposal that generates work orders for execution.

User can override with: "skip proposal, create work orders directly"
```

### Proposal vs Work Order Decision

**Use PROPOSAL when:**
- Problem has multiple solution approaches
- Need to evaluate trade-offs before committing
- Work spans multiple sprints/phases
- Requires architectural design phase
- Multiple teams/agents will collaborate

**Use WORK ORDER directly when:**
- Solution approach is clear and agreed
- Task is well-defined and scoped
- Can be completed in <1 week
- <5 major tasks
- No architectural decisions needed

**Visual Decision Tree:**
```
User requests work
    │
    ├─ Solution unclear OR multiple approaches? → PROPOSAL
    ├─ 5+ tasks AND 3+ weeks? → PROPOSAL
    ├─ Architectural decisions needed? → PROPOSAL
    ├─ Cross-system impact unclear? → PROPOSAL
    │
    └─ Well-defined, <5 tasks, <1 week? → WORK ORDER
```

### User Override Protocol

**Users CAN choose to skip proposal** by explicitly saying:
- "skip proposal, create work orders directly"
- "no proposal needed"
- "we know the approach, just create work orders"

**When user overrides, you MUST:**
1. Acknowledge the override
2. Confirm they want to proceed directly to work orders
3. Create work orders with the implied approach
4. Document that no proposal phase occurred

**Override response template:**
```
⚠️ Proposal skipped by user request

Creating work orders directly with the following approach:
[Brief summary of assumed approach]

Note: No formal proposal document will be created.
Alternative approaches have not been formally evaluated.

Proceeding to create work orders...
```

### Integration with Work Order System

**When proposal is created, it MUST include:**
1. Work Order Generation Plan section
2. Suggested work order breakdown
3. Dependency graph between work orders
4. Priority mapping for each work order

**Workflow:**
```
1. Create Proposal → 2. Review & Approve → 3. Generate Work Orders → 4. Execute WOs
```

Each generated work order will reference the parent proposal for full context.

---

## Standard Proposal Generation

Generate a comprehensive work proposal for the identified problem or task. Execute all steps sequentially without pausing for review. **ALWAYS save the proposal to disk and track it in the project tracking system.**

# Control Triggers
- **Standard proposal:** Default behavior - generate full proposal with all sections, save, and track
- **Quick proposal:** If message includes "quick" → produce condensed 5-section version, save, and track
- **With code samples:** If message includes "with samples" → include code snippets in implementation approach
- **Skip tracking:** If message includes "no track" → save proposal but skip tracking system (rare)

# Proposal Requirements

## PHASE 1 - PROBLEM ANALYSIS
1. **Identify:** State the exact problem or requirement being addressed
2. **Context:** Analyze current state and why it needs changing
3. **Impact:** Define what's broken, inefficient, or missing
4. **Root cause:** Explain underlying reasons for the issue

## PHASE 2 - SOLUTION DESIGN
Generate a structured proposal containing:

### 1. Executive Summary
- **Problem statement:** One sentence describing the core issue
- **Proposed solution:** One sentence describing your approach
- **Expected outcome:** Measurable result after implementation

### 2. Rationale
- **Why this approach:** Technical justification for chosen solution
- **Alternatives considered:** Other approaches and why they were rejected
- **Risk assessment:** Potential issues and mitigation strategies

### 3. Implementation Approach
- **Core changes:** List of specific modifications required
- **Technical details:** How each change addresses the problem
- **Integration points:** Where changes connect with existing system

### 4. Task Breakdown
**Order tasks by dependencies. Each task must include:**

- Task ID (e.g., T1, T2)
- Description
- Dependencies (which tasks must complete first)
- Estimated complexity (Simple/Medium/Complex)
- Success criteria

Example format:
```
T1: [Description]
   Dependencies: None
   Complexity: Simple
   Success: [Specific measurable outcome]

T2: [Description]
   Dependencies: T1
   Complexity: Medium
   Success: [Specific measurable outcome]
```

### 5. Validation Strategy
- **Testing approach:** How to verify each change works
- **Success metrics:** Quantifiable measures of completion
- **Rollback plan:** Steps to revert if issues arise

### 6. Timeline & Resources
- **Critical path:** Sequence of dependent tasks
- **Parallel work:** Tasks that can proceed simultaneously
- **Blockers:** External dependencies or prerequisites

### 7. Work Order Generation Plan
**How this proposal converts to work orders:**
```yaml
work_order_generation:
  auto_create: [true/false]  # Should WOs be created on approval
  split_strategy: [by_task/by_milestone/by_complexity]
  priority_mapping:
    T1-T3: critical
    T4-T6: high
    T7+: medium
  estimated_wo_count: [number]
```

**Suggested Work Order Breakdown:**

- WO-1: [Tasks T1-T2] - [Title]
- WO-2: [Tasks T3-T4] - [Title]
- WO-3: [Tasks T5+] - [Title]

## PHASE 3 - SAVE AND TRACK

### File Management
1. **Generate timestamp:** Get current timestamp in format `YYYY-MM-DD-HH-MM-SS` using utility script
   ```bash
   TIMESTAMP=$(~/.agents/scripts/get-filename-prefix.sh)
   ```
2. **Determine project:** Infer project name from context or use "general" if unclear
3. **Create directory:** `mkdir -p .dev/ai/proposals/`
4. **Save location:** `.dev/ai/proposals/${TIMESTAMP}-[project]-proposal.md`
5. **Write file:** Save complete proposal to disk
6. **Confirm save:** Explicitly verify file was written successfully

### Tracking Integration
After saving, execute tracking command:
```bash
~/.agents/scripts/track-project.sh "[project-name]" "Proposal created" "[problem summary]" "[agent-name]" "create proposal" "" "file://[absolute-path-to-proposal]"
```

Parameters:

- Project name: From context or "general"
- Action: "Proposal created"
- Details: One-line problem summary
- Agent: Current agent name
- Prompt: "create proposal"
- Related files: Leave empty
- Reference URI: Absolute path to saved proposal with `file://` prefix

## PHASE 4 - FINAL OUTPUT

Present the complete proposal wrapped in markers:

```
** WORK PROPOSAL START **

# Work Proposal: [Problem/Feature Name]
**Generated:** [Timestamp]
**Status:** Ready for Review
**Saved to:** [Full path to saved file]
**Tracked in:** [Project name]

[All sections from Phase 2]

## Review Checklist
- [ ] Problem clearly defined
- [ ] Solution addresses root cause
- [ ] Tasks properly sequenced
- [ ] Success criteria measurable
- [ ] Risks identified and mitigated

** WORK PROPOSAL END **
```

# Output Rules
- Be explicit and specific - no vague descriptions
- Include concrete examples where helpful
- Mark unknowns as "TBD: [what needs determining]"
- Use active voice and present tense
- Each task must be independently verifiable
- Dependencies must form a valid directed acyclic graph
- **ALWAYS confirm file was written and tracked successfully**
- Include file path and tracking confirmation in output

# Review Prompt
After presenting the proposal, confirm:
"✅ Proposal saved to: [path]
✅ Tracked in project: [project-name]

Options:

- 'approve' to proceed with implementation
- 'revise [section]' to modify specific parts
- 'expand [task ID]' for more detail on a task"
