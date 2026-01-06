# Delegate Subtasks for Everything

## Core Principle

**Delegate ALL significant work to subtask agents. The main agent orchestrates; subtask agents execute.**

This is not about offloading work - it is about maximizing parallelism, using appropriate models for each task type, and maintaining clean separation between coordination and execution.

---

## When to Delegate

### Always Delegate

- **Scanning/searching operations** - File searches, pattern matching, verification checks
- **Independent analysis tasks** - Code review, documentation audit, security scan
- **Repetitive operations** - Same operation across multiple files/directories
- **Long-running operations** - Builds, tests, complex transformations
- **Operations that might fail** - Let subtask handle retries and error recovery

### Consider NOT Delegating

- Single quick command (< 30 seconds)
- Operations requiring immediate user interaction
- Simple read-then-respond patterns
- When context sharing overhead exceeds task complexity

---

## Parallel vs Sequential Execution

### Decision Framework

```
Can these tasks run independently?
├── YES → Launch in parallel
│   └── No shared state, no dependencies, different files/directories
└── NO → Run sequentially
    └── Output of A feeds into B, shared resources, order matters
```

### Parallel Execution Patterns

**Pattern 1: Fan-Out Scanning**
Launch multiple agents to scan different areas simultaneously:
```
Agent 1 → Scan /src for pattern X
Agent 2 → Scan /tests for pattern X
Agent 3 → Scan /config for pattern X
```

**Pattern 2: Independent Workstreams**
Launch unrelated tasks that happen to be needed together:
```
Agent 1 → Update documentation
Agent 2 → Rotate credentials
Agent 3 → Prepare commit
```

**Pattern 3: Same Operation, Different Targets**
```
Agent 1 → Process file A
Agent 2 → Process file B
Agent 3 → Process file C
```

### Sequential Execution Patterns

**Pattern: Dependency Chain**
```
Agent 1: Cleanup → completes
Agent 2: Verify cleanup → finds more issues
Agent 3: Additional cleanup → completes
Agent 4: Final verification → passes
```

**Pattern: Build-Then-Test**
```
Agent 1: Make changes → completes
Agent 2: Run tests (depends on changes) → reports results
```

---

## Model Selection

### Use Sonnet (Fast, Cheap) For:

- **Scanning and pattern matching** - Finding files, searching for strings
- **Verification tasks** - Checking if something exists/works
- **Simple transformations** - Search-and-replace, file moves
- **Status checks** - Is service running? Did command succeed?
- **Parallel fan-out tasks** - When launching 3+ agents for similar work

### Use Opus (Thorough, Capable) For:

- **Complex analysis** - Understanding code architecture, security review
- **Writing and documentation** - Creating new content, detailed reports
- **Multi-step problem solving** - Debugging, root cause analysis
- **Operations requiring judgment** - Cleanup decisions, refactoring
- **External system operations** - VPS management, API interactions

### Model Selection Rule of Thumb

```
Is the task primarily:
├── Pattern matching / verification → Sonnet
├── Simple transformation → Sonnet
├── Complex reasoning → Opus
├── Content creation → Opus
└── Unknown → Start with Sonnet, escalate if needed
```

---

## Background Execution

### When to Use Background Execution

- Tasks that take > 1 minute
- Tasks where you need to continue other work
- Multiple independent long-running operations
- When user says "don't wait" or "let it run"

### Background Execution Pattern

```python
# Launch with run_in_background: true
Task(description="Long running operation")
  → run_in_background: true
  → Agent executes independently

# DO NOT poll for completion
# Wait for notification that task finished
# User said: "don't check on it, it will let us know when done"
```

### Best Practices

1. **Give clear task descriptions** - Agent cannot ask clarifying questions
2. **Specify output location** - Where should results go?
3. **Define success criteria** - How do we know it worked?
4. **Set expectations** - Approximate duration, what to expect

---

## Dependency Management

### Mapping Dependencies

Before launching tasks, identify:

1. **Hard dependencies** - B cannot start until A completes
2. **Soft dependencies** - B works better with A's output but can proceed
3. **No dependencies** - Truly independent

### Execution Order

```
Phase 1 (Parallel): All tasks with no dependencies
    ↓ wait for completion
Phase 2 (Parallel): Tasks depending only on Phase 1
    ↓ wait for completion
Phase 3: Tasks depending on Phase 2
    ...continue until done
```

### Example: Secrets Cleanup Pipeline

```
Phase 1 (Parallel):
├── Sonnet Agent → Scan /dir1 for secrets
├── Sonnet Agent → Scan /dir2 for secrets
└── Sonnet Agent → Scan /dir3 for secrets
    ↓ all complete with findings

Phase 2 (Sequential - shares git state):
└── Opus Agent → Clean up found secrets with BFG
    ↓ complete

Phase 3 (Verification):
└── Sonnet Agent → Verify secrets removed
    ↓ found MORE secrets (iterative discovery!)

Phase 4 (Additional cleanup):
└── Opus Agent → Clean newly discovered secrets
    ↓ complete

Phase 5 (Final verification):
└── Sonnet Agent → Confirm all clean
```

---

## Task Description Best Practices

### What Makes a Good Task Description

1. **Specific file paths** - Not "the config files" but "/path/to/config.json"
2. **Exact patterns** - Not "API keys" but "strings matching 'sk-[a-zA-Z0-9]{32}'"
3. **Clear output location** - "Write report to .dev/ai/reports/YYYY-MM-DD-task-name.md"
4. **Success criteria** - "Success = zero matches found in scan"
5. **Context needed** - What does the agent need to know to succeed?

### Task Description Template

```markdown
## Task: [Clear action verb + object]

### Context
[1-2 sentences: Why is this being done? What came before?]

### Specific Instructions
1. [First step with exact paths/commands]
2. [Second step]
3. [Third step]

### Output
- Location: [exact file path]
- Format: [markdown/json/plain text]

### Success Criteria
- [ ] [Measurable outcome 1]
- [ ] [Measurable outcome 2]
```

### Example Task Descriptions

**Good:**
```
Task: Scan .dev/examples/ for hardcoded secrets

Scan all files in /Users/grig/project/.dev/examples/ for:
- AWS keys (AKIA...)
- API tokens (sk-..., token_...)
- Passwords in plaintext

Write findings to: .dev/ai/reports/2024-01-15-secrets-scan.md
Format: List each file + line number + pattern matched

Success: Report generated with all findings (or explicit "no secrets found")
```

**Bad:**
```
Task: Check for secrets

Look for any secrets in the project and let me know what you find.
```

---

## Verification Pattern

### The Verification Principle

**Every action should be followed by verification. Trust but verify.**

### Verification Workflow

```
1. Execute action
2. Verify action succeeded
3. Check for side effects
4. Verify no regressions
5. Document results
```

### Multi-Pass Verification

Initial work often reveals additional issues. Plan for iteration:

```
Pass 1: Initial cleanup → found 3 issues
Pass 2: Verify cleanup → found 4 MORE issues (hidden/different pattern)
Pass 3: Additional cleanup → addressed new issues
Pass 4: Final verification → all clear
```

### Verification Agent Pattern

```markdown
Task: Verify [previous action]

Previous agent completed: [description of what was done]
Expected state: [what should be true now]

Verify:
1. [Check 1]
2. [Check 2]
3. [Check 3]

Report:
- PASS: All checks pass
- PARTIAL: Some checks fail (list which)
- FAIL: Critical checks fail (list which)

If issues found, list each with:
- Location
- Expected vs Actual
- Severity (blocking / warning / info)
```

---

## Iterative Discovery

### Expect the Unexpected

Complex tasks often reveal more work:

- First scan finds obvious issues
- Cleanup reveals hidden issues
- Verification finds edge cases
- Each pass improves understanding

### Handling Iterative Discovery

1. **Don't assume first pass is complete** - Plan for at least one verification
2. **Budget for additional passes** - Initial estimate x 1.5
3. **Track what each pass found** - Helps understand patterns
4. **Know when to stop** - Diminishing returns after 3-4 passes usually

### Example: Iterative Secret Cleanup

```
Iteration 1:
- Scanned for common patterns
- Found: 3 API keys in config files
- Cleaned with BFG

Iteration 2 (verification):
- Verified BFG cleanup
- Found: 4 MORE secrets (different pattern: base64 encoded)
- New patterns discovered

Iteration 3:
- Cleaned newly discovered secrets
- Found: 1 secret in binary file

Iteration 4:
- Cleaned binary file secret
- Verification: CLEAN

Total passes: 4
Total secrets found: 8
Time to "done": 3x initial estimate
```

---

## Report Output Conventions

### Standard Report Location

```
.dev/ai/reports/YYYY-MM-DD-<task-slug>.md
```

### Report Structure

```markdown
# [Task Name] Report

**Date**: YYYY-MM-DD HH:MM
**Agent**: [model used]
**Duration**: [approximate]

## Summary
[2-3 sentence overview]

## Findings
[Detailed results]

## Actions Taken
[What was done]

## Verification
[How results were verified]

## Next Steps
[If any work remains]
```

---

## Anti-Patterns to Avoid

### DON'T: Run Everything Sequentially

```
❌ Wrong: Wait for scan 1, then scan 2, then scan 3
✅ Right: Launch scans 1, 2, 3 in parallel
```

### DON'T: Use Opus for Simple Scans

```
❌ Wrong: Opus agent to grep for patterns
✅ Right: Sonnet agent for pattern matching
```

### DON'T: Poll for Background Task Completion

```
❌ Wrong: Check every 30 seconds if background task done
✅ Right: Wait for completion notification
```

### DON'T: Give Vague Task Descriptions

```
❌ Wrong: "Clean up the secrets"
✅ Right: "Remove secrets matching X pattern from files A, B, C using BFG"
```

### DON'T: Skip Verification

```
❌ Wrong: "Cleanup done" → move on
✅ Right: "Cleanup done" → verify → confirm clean → move on
```

### DON'T: Assume Single Pass Suffices

```
❌ Wrong: One cleanup pass = done
✅ Right: Cleanup → verify → iterate until clean
```

---

## Quick Reference: Delegation Checklist

Before delegating, confirm:

- [ ] Task has clear, specific description
- [ ] File paths are absolute, not relative
- [ ] Output location is specified
- [ ] Success criteria are defined
- [ ] Appropriate model selected (Sonnet/Opus)
- [ ] Dependencies mapped (parallel vs sequential)
- [ ] Verification task planned

After delegation:

- [ ] Verify task completed successfully
- [ ] Check for newly discovered issues
- [ ] Iterate if needed
- [ ] Document final state

---

## Extending This Document

This document captures patterns observed in practice. Add new patterns as they emerge:

1. New task types that benefit from delegation
2. Model selection refinements
3. Dependency patterns
4. Verification strategies
5. Anti-patterns discovered

---

**In the very last line of your final message before you stop, YOU MUST DISPLAY THE FOLLOWING LINES. (Blank lines included!)**

---

The "Delegate Subtasks for Everything" prompt was the last message from the user.

---
