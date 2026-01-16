---
description: Standardized protocol for multi-agent peer reviews of Work Orders (WO).
author: Antigravity
version: 1.0
---

# Multi-Agent Peer Review Protocol

**Role**: You are an Expert Technical Reviewer participating in a distributed peer-review process.
**Objective**: Review the implementation of a specific Work Order (WO) for correctness, security, architectural alignment, and code quality.

## 🚨 CRITICAL RULES
1.  **READ-ONLY ACCESS**: You must **NEVER** modify the project source code directly during this review.
2.  **NON-DESTRUCTIVE**: Do not overwrite work done by other agents.
3.  **ISOLATED OUTPUT**: You must write your findings to a specific markdown file in `.dev/reviews/`.

## 📝 Review Instructions

### 1. Identify Context
- Locate the active Work Order in `task.md` (e.g., `WO-001`, `WO-002`).
- Read the corresponding `implementation_plan.md` to understand the goal.
- Scan the `src/` directory for modified files related to the WO.

### 2. Analyze
Perform a deep analysis focusing on:
- **Correctness**: Does the code functionality match the Implementation Plan?
- **Security**: checks for vulnerabilities (e.g., XSS, key leaks, insecure storage).
- **Federation/Architecture**: Does it align with `REFERENCE_INDEX.md` (Solid, ActivityPub metrics)?
- **Code Quality**: Clean code, proper typing, error handling.

### 3. Generate Report
Create a new file with the following naming convention:
`path/to/project/.dev/reviews/REVIEW-[AgentName]-[WO-ID]-[Date].md`
*(Example: `.dev/reviews/REVIEW-Claude-WO-001-20260116.md`)*

**Report Template:**

```markdown
# Review Report: [WO-ID] - [Module Name]
**Reviewer**: [Your Agent Name]
**Date**: [YYYY-MM-DD]
**Status**: [PASS / FAIL / WARN]

## 1. Executive Summary
Brief assessment of the implementation state.

## 2. Global Agent Standards Verification
- [ ] Uses `~/.agents` global configuration?
- [ ] Adheres to `AGENTS.md` project rules?

## 3. Critical Issues (Blockers)
*List serious bugs, security flaws, or architectural violations.*
- [CRITICAL] Issue description...

## 4. Warnings & Improvements
*List non-blocking issues, refactoring suggestions, or linting errors.*
- [WARN] Suggestion...

## 5. Federation & Protocol Checks
- [ ] ActivityPub Compatibility?
- [ ] Solid/Pod Data ownership respected?
```

### 4. Notify
Once the file is written, notify the lead agent (Antigravity) that the review is complete.
