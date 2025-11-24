# Claude Code Agent Prompt Style Guide

**Purpose**: Guide for writing optimized agent prompts that work seamlessly with Claude Code's agent system.

**Last Updated**: 2025-11-13

---

## Overview

Claude Code agents are specialized AI assistants invoked via the Task tool. Well-crafted agent prompts enable:
- **Agent-to-agent coordination**: Other agents know when to invoke your specialist
- **Token efficiency**: Smaller prompts = faster processing, lower cost
- **Action-oriented focus**: Clear directives over lengthy explanations
- **Metadata-driven discovery**: YAML front matter enables systematic agent selection

---

## File Structure

### 1. YAML Front Matter (REQUIRED)

Every agent prompt MUST start with YAML front matter:

```yaml
---
name: agent-name-in-kebab-case
description: When to use this agent, with 3-5 invocation examples
model: sonnet|opus|haiku
color: blue|red|green|yellow|purple|orange
---
```

#### Field Specifications:

**`name`** (required):
- Format: `kebab-case` (lowercase, hyphens for spaces)
- Examples: `network-diagnostics-specialist`, `dev-worker`, `research-analyst`
- Must be unique across all agents
- Used for agent identification and invocation

**`description`** (required):
- **Purpose**: Tell other agents WHEN and HOW to invoke this specialist
- **Format**: 1-2 sentence overview + 3-5 invocation examples
- **Critical**: This is how agents discover and invoke each other

**Example Structure**:
```yaml
description: Use this agent when [triggering conditions]. This agent should be invoked proactively when you detect symptoms like:\n\n<example>\nContext: [Situation]\nuser: "[User's request]"\nassistant: "[Invocation statement]"\n<task>[Task description passed to agent]</task>\n<commentary>[Optional: Why this agent was chosen]</commentary>\n</example>\n\n[Repeat for 3-5 different scenarios]
```

**`model`** (required):
- Options: `sonnet`, `opus`, `haiku`
- Choose based on task complexity:
  - `haiku`: Fast, simple, deterministic tasks (file operations, basic analysis)
  - `sonnet`: Default choice - balanced speed/capability (most agents)
  - `opus`: Complex reasoning, critical decisions, high-stakes operations
- Default to `sonnet` unless you have specific reasons

**`color`** (optional but recommended):
- Options: `blue`, `red`, `green`, `yellow`, `purple`, `orange`
- Visual identification in UI
- Suggested mapping:
  - `red`: Diagnostics, debugging, critical analysis
  - `blue`: Research, documentation, analysis
  - `green`: Building, implementation, creation
  - `yellow`: Testing, validation, quality assurance
  - `purple`: Strategic, planning, coordination
  - `orange`: Optimization, refactoring, improvement

### 2. Agent Identity & Core Configuration

Immediately after front matter, establish identity:

```markdown
You are **[Agent Name]**, a [Role/Title] with [X]+ years of experience specializing in [domain].

## Core Identity & Expertise

You excel at [key strengths]. Your core competencies include:
- [Competency 1]
- [Competency 2]
- [Competency 3]
- [Competency 4]

You operate with [HIGH/MEDIUM] autonomy and can [capabilities list].
```

**Guidelines**:
- Lead with expertise level (Senior, Expert, Specialist)
- Specify years of experience for credibility (10+, 15+, 20+)
- List 4-6 core competencies (specific, actionable)
- State autonomy level and decision-making scope

### 3. Fundamental Operating Principles

List 4-8 core principles that govern behavior:

```markdown
## Fundamental Operating Principles

1. **[Principle Name]**: [One-line directive]
2. **[Principle Name]**: [One-line directive]
3. **[Principle Name]**: [One-line directive]
...
```

**Examples**:
- **Evidence-Based Diagnosis**: Never assume - always gather concrete data before conclusions
- **Parallel Efficiency**: Execute independent operations simultaneously for 4-5x speed
- **Surgical Precision**: Target only affected components with minimal intervention

**Guidelines**:
- Make them actionable, not abstract
- Bold the principle name
- One clear directive per principle
- Order by importance

### 4. Methodology/Protocol Section

Define the agent's systematic approach:

```markdown
## [X]-Phase [Process Name]

For EVERY [task type], execute this exact sequence:

### Phase 1: [PHASE NAME]
- [Step 1 with specific action]
- [Step 2 with specific action]
- **[CRITICAL DIRECTIVE]** in bold
- Example command or pattern if applicable

### Phase 2: [PHASE NAME]
...
```

**Guidelines**:
- Number phases clearly (3-6 phases typical)
- Use imperative verbs (Understand, Diagnose, Execute, Verify)
- Include code examples inline where they clarify
- Bold critical steps or constraints
- Keep descriptions concise (1-3 bullets per sub-step)

### 5. Tool Usage & Patterns

Specify how to use available tools:

```markdown
## [Critical Strategy Name] (CRITICAL)

For maximum efficiency, ALWAYS [directive]:

```xml
<function_calls>
<invoke name="ToolName"><parameter name="param">[example]</parameter></invoke>
<invoke name="ToolName"><parameter name="param">[example]</parameter></invoke>
</function_calls>
```

Use [strategy] for:
- [Scenario 1]
- [Scenario 2]
- [Scenario 3]
```

**Guidelines**:
- Show actual function call syntax when helpful
- Emphasize parallel execution where applicable
- Provide concrete examples, not just descriptions
- List specific scenarios for tool selection

### 6. Pattern Library (If Applicable)

For domain specialists, include common patterns:

```markdown
## [Domain] Patterns Library

### Pattern 1: [Pattern Name]
**Symptoms**: [Observable indicators]

**Investigation**:
```bash
# [Description]
command-1
command-2
```

**Common Root Causes**:
- [Cause 1]
- [Cause 2]

**Surgical Fix**: `[exact command or approach]`

**Verification**: [How to confirm fix worked]
```

**Guidelines**:
- 3-5 patterns typical
- Focus on common, high-value scenarios
- Include commands/code when applicable
- Keep explanations brief

### 7. Communication Protocol

Define output formats:

```markdown
## Communication Protocol

### [Response Type] Pattern
```markdown
[STAGE] [What you're doing]

<show relevant output>

[FINDING] [Discovery with data]
- [Specific evidence]

[NEXT] [Next step]
```
```

**Guidelines**:
- Show exact formatting with markdown blocks
- Use stage markers like [INVESTIGATING], [FINDING], [ROOT CAUSE], [FIX], [VERIFIED]
- Include examples of good/bad communication
- Specify when to use AskUserQuestion tool

### 8. Constraints Section

Define hard limits:

```markdown
## Hard Constraints (NEVER Violate)

1. **[Constraint name]** - [Why this is critical]
2. **[Constraint name]** - [Why this is critical]
...
```

**Guidelines**:
- 5-8 constraints typical
- Bold constraint name
- State as absolute directive (NEVER/ALWAYS)
- Brief rationale improves compliance

### 9. Anti-Patterns Section

Show what NOT to do:

```markdown
## Anti-Patterns (What NOT to Do)

❌ **[Bad Pattern Name]**: "[Bad example]"
✅ **Correct**: "[Good example]"

❌ **[Bad Pattern Name]**: "[Bad example]"
✅ **Correct**: "[Good example]"
```

**Guidelines**:
- 3-5 anti-patterns
- Use ❌ and ✅ for visual clarity
- Show actual examples, not descriptions
- Pair each anti-pattern with correct approach

### 10. Platform/Domain-Specific Details (Optional)

For specialists, include reference info:

```markdown
## Platform-Specific Commands

**macOS**: `command1`, `command2`, `command3`
**Linux**: `command1`, `command2`, `command3`
**Windows**: `command1`, `command2`, `command3`
```

**Guidelines**:
- Keep concise (commands only, not explanations)
- Group by platform, framework, or domain
- Use inline code formatting

### 11. Initialization Sequence

Define startup behavior:

```markdown
## Initialization Sequence

Upon activation:
1. [First action with specific directive]
2. [Second action]
3. [Third action]
4. State readiness: "[Exact message to user]"
```

**Guidelines**:
- 3-5 steps typical
- Concrete actions (create file, check tools, run diagnostics)
- End with specific readiness message
- No lengthy explanations

### 12. Remember Statement (Optional)

Final reminder of core identity:

```markdown
**Remember**: You are [identity summary]. Your goal is to [primary objective]. Always prefer [value 1] over [alternative 1], [value 2] over [alternative 2], and [value 3] over [alternative 3].
```

---

## Writing Style Guidelines

### DO:
✅ Use **bold** for critical directives and phase names
✅ Use `inline code` for commands, file paths, technical terms
✅ Use code blocks for multi-line commands or examples
✅ Use bullet points for lists (not numbered unless sequence matters)
✅ Use "ALWAYS", "NEVER", "CRITICAL" sparingly but emphatically
✅ Show examples inline (don't defer to separate sections)
✅ Use stage markers: [INVESTIGATING], [FINDING], [ROOT CAUSE]
✅ Include actual commands and code patterns
✅ Specify tool invocation syntax when non-obvious

### DON'T:
❌ Write long explanatory paragraphs
❌ Include "nice to know" background information
❌ Repeat the same concept in multiple sections
❌ Use passive voice ("should be done" vs "do this")
❌ Include hypothetical examples
❌ Write "you may" or "you might" (use "you will" or "you must")
❌ Add motivational language or cheerleading
❌ Explain WHY unless it's critical to correct action

---

## Token Efficiency Principles

**Target**: 300-400 lines for most agents (not including front matter examples)

### Condensation Strategies:

1. **Merge Sections**: Combine related concepts
   - Before: "Tool Usage" + "Tool Selection Logic" + "Available Tools" (3 sections)
   - After: "Tool Usage & Patterns" (1 section)

2. **Inline Examples**: Don't separate examples from instructions
   - Before: Instruction in one section, examples in another
   - After: Example immediately follows instruction

3. **Remove Scaffolding**: Cut structural text that doesn't add value
   - Before: "This section describes how to..."
   - After: [Just start with the content]

4. **Command Over Explanation**:
   - Before: "You should check the network connectivity by using the ping command to test..."
   - After: "Check connectivity: `ping -c 3 8.8.8.8`"

5. **Tables for Comparisons**: More efficient than prose
   - Before: "For macOS use X, for Linux use Y, for Windows use Z..."
   - After:
     ```
     **macOS**: `command-x`
     **Linux**: `command-y`
     **Windows**: `command-z`
     ```

6. **Bullet Points Over Paragraphs**: Always
   - Before: "The agent should first analyze the request, then break it down into components, and finally execute each step systematically."
   - After:
     ```
     1. Analyze request
     2. Break into components
     3. Execute systematically
     ```

---

## Front Matter Description Best Practices

The `description` field is CRITICAL for agent discoverability. Follow this template:

```yaml
description: Use this agent when [trigger conditions]. This agent should be invoked proactively when you detect symptoms like:\n\n<example>\nContext: [Setup]\nuser: "[User quote]"\nassistant: "[Invocation statement with Task tool]"\n<task>[Task description]</task>\n<commentary>[Optional: Why this agent]</commentary>\n</example>
```

### Invocation Example Template:

```yaml
<example>
Context: [One-line scenario setup]
user: "[Direct quote of user's request]"
assistant: "[Statement invoking the agent via Task tool]"
<task>[Specific task description passed to agent]</task>
<commentary>[Optional: Agent selection reasoning]</commentary>
</example>
```

### Example Categories:

Include 3-5 examples covering:
1. **Direct Request**: User explicitly asks for the service
2. **Implicit Need**: User's request implies the need (without naming it)
3. **Proactive Detection**: Agent notices the need from context/symptoms
4. **Error Response**: User encounters specific error that triggers agent
5. **Optimization Opportunity**: After completing other work, agent identifies improvement

### Real Examples from Network Diagnostics Specialist:

```yaml
description: Use this agent when the user reports network connectivity issues, slow responses, timeouts, application offline errors, or requests network troubleshooting. This agent should be invoked proactively when you detect symptoms like:\n\n<example>\nContext: User is experiencing slow application responses and mentions timeouts\nuser: "My application keeps timing out when trying to connect to the API"\nassistant: "I'm going to use the Task tool to launch the network-diagnostics-specialist agent to investigate this connectivity issue systematically."\n<task>Diagnose API connection timeout - application experiencing repeated timeouts when connecting to API endpoint</task>\n</example>\n\n<example>\nContext: After completing other work, you notice network-related warnings in logs\nuser: "Can you help me refactor this API client?"\nassistant: "I'll help with the refactoring. However, I notice connection warnings in the logs - after we finish this refactoring, I should use the network-diagnostics-specialist agent to check for potential connection leaks."\n<commentary>Proactively identifying network issues for later investigation</commentary>\n</example>
```

---

## Conversion Checklist

When converting an existing agent prompt to Claude Code format:

### Phase 1: Front Matter
- [ ] Create YAML front matter section
- [ ] Choose agent name in kebab-case
- [ ] Write 1-2 sentence overview
- [ ] Create 3-5 invocation examples
- [ ] Select model (default: sonnet)
- [ ] Choose color (recommended for UX)

### Phase 2: Core Content Review
- [ ] Identify agent's core identity and expertise
- [ ] Extract 4-8 fundamental principles
- [ ] Define methodology/protocol (3-6 phases typical)
- [ ] List critical tool usage patterns
- [ ] Include pattern library if domain specialist
- [ ] Define communication protocol
- [ ] Specify hard constraints (5-8 typical)
- [ ] Create anti-patterns section (3-5 examples)

### Phase 3: Condensation
- [ ] Remove explanatory prose
- [ ] Inline examples with instructions
- [ ] Convert paragraphs to bullet points
- [ ] Merge related sections
- [ ] Cut "nice to know" background info
- [ ] Use tables/lists for comparisons
- [ ] Verify all code examples are inline

### Phase 4: Formatting
- [ ] Bold all critical directives
- [ ] Use `inline code` for commands and paths
- [ ] Use code blocks for multi-line examples
- [ ] Add stage markers ([INVESTIGATING], [FINDING], etc.)
- [ ] Ensure consistent heading hierarchy
- [ ] Remove unnecessary whitespace

### Phase 5: Quality Check
- [ ] Target: 300-400 lines (excluding front matter examples)
- [ ] Every section has clear, actionable directives
- [ ] No redundancy across sections
- [ ] Examples are concrete, not hypothetical
- [ ] All critical behaviors are specified
- [ ] Constraints are clear and absolute
- [ ] Initialization sequence is specific

### Phase 6: Validation
- [ ] Read through as if you were the AI
- [ ] Verify all tool invocations have syntax
- [ ] Check that phase sequence is logical
- [ ] Ensure front matter examples cover key scenarios
- [ ] Confirm no ambiguous directives
- [ ] Test file naming: `agent-name-in-kebab-case.md`

---

## Example Conversion: Before & After

### BEFORE (Traditional Template - 663 lines):

```markdown
# Agent Identity & Core Configuration

You are Network Diagnostics Specialist...

## Fundamental Operating Principles
- You operate with HIGH autonomy and can diagnose complex network issues...
- Your primary objective is to identify and resolve...
- You maintain persistent context...

[15 major sections with extensive explanations]
[Multiple subsections with detailed examples]
[Lengthy pattern library with full explanations]
[Communication examples in separate section]
[Anti-patterns scattered throughout]

Total: 663 lines, 23KB
```

### AFTER (Claude Code Format - 335 lines):

```yaml
---
name: network-diagnostics-specialist
description: Use this agent when user reports network issues...\n\n<example>...[5 examples]...</example>
model: sonnet
color: red
---

You are **Network Diagnostics Specialist**, a Senior Systems/Network Engineer with 15+ years...

## Core Identity & Expertise
You excel at methodical diagnosis... Your core competencies include:
- Network architecture and protocol-level debugging
- Connection pool management and performance optimization
- [concise list continues]

## Fundamental Operating Principles
1. **Evidence-Based Diagnosis**: Never assume - gather concrete data
2. **Surgical Precision**: Target only affected components
[6 principles, one line each]

## Six-Phase Diagnostic Protocol
### Phase 1: UNDERSTAND
- Use AskUserQuestion to clarify symptoms
- Identify scope: all apps? specific services?

[Phases with inline examples, commands shown immediately]

## Pattern Library
### Pattern 1: Connection Pool Exhaustion
**Symptoms**: Timeouts, "too many open files"
**Investigation**: `netstat -an | grep ESTABLISHED | wc -l`
**Surgical Fix**: `pkill -f "pattern"`

[5 patterns, condensed format]

Total: 335 lines, 11KB (50% reduction, full functionality preserved)
```

---

## Special Cases

### Research Agents
- Include parallel execution strategy prominently
- Specify progress tracking requirements
- Define research output formats
- Include source quality criteria

### Development Agents
- Define working memory structure (files to maintain)
- Specify evidence requirements (show full outputs)
- Include rollback/safety protocols
- Define handover requirements if context limits approached

### Coordination/Orchestrator Agents
- Define agent selection logic
- Specify handoff protocols
- Include delegation patterns
- Define escalation triggers

### Diagnostic/Analysis Agents
- Include pattern library (3-5 common patterns)
- Define investigation protocols
- Specify evidence collection requirements
- Include verification procedures

---

## Quick Reference Template

```yaml
---
name: agent-name
description: Use when [conditions].\n\n<example>...[3-5 examples]...</example>
model: sonnet
color: blue
---

You are **[Name]**, a [Role] with [X]+ years specializing in [domain].

## Core Identity & Expertise
You excel at [strengths]. Core competencies:
- [Competency 1]
- [Competency 2-4]

## Fundamental Operating Principles
1. **[Principle]**: [One-line directive]
2-6. [More principles]

## [X]-Phase [Process Name]
### Phase 1: [NAME]
- [Steps with inline examples]
### Phase 2-X: [Continue]

## [Tool/Pattern] Strategy (CRITICAL)
[Key patterns with code examples inline]

## Communication Protocol
### [Response Type]
[Show exact format with examples]

## Hard Constraints (NEVER Violate)
1. **[Constraint]** - [Brief why]
2-8. [More constraints]

## Anti-Patterns
❌ **[Bad]**: "[Example]"
✅ **Correct**: "[Example]"

## Initialization Sequence
1. [Specific action]
2-4. [More actions]
4. State: "[Exact message]"

**Remember**: [Identity + goal + key values].
```

---

## Maintenance

When updating agents:
- Keep changes minimal and focused
- Test that invocation examples still make sense
- Verify token count stays reasonable (300-400 lines)
- Update version comment if significant changes
- Consider if examples need updating for new use cases

---

**End of Style Guide**

For questions or examples, refer to:
- `/Users/grig/.claude/agents/network-diagnostics-specialist.md` (reference implementation)
- `/Users/grig/.agents/prompts/agents/NETWORK-DIAGNOSTICS-SPECIALIST.md` (detailed version for comparison)
