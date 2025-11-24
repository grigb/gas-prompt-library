# Prompts Directory

This directory contains all prompt templates and agent instructions organized by category.

## Directory Structure

### `agents/`
Agent-specific prompts for agent-to-agent communication, orchestration, and coordination.

### `creation/`
Prompts for creating new artifacts:
- `CREATE-AUDITABLE-RECORD.md` - Create comprehensive audit trails
- `CREATE-FEATURE-REQUEST.md` - Capture feature requirements
- `CREATE-WORK-PROPOSAL.md` - Generate work proposals

### `general/`
General-purpose prompts for common agent workflows:
- `autonomous-mode-now.md` - Autonomous engineering agent mode for isolated branch work with time/credit constraints, emphasizing documentation-first approach and continuous high-impact work
- `check-the-work.md` - Verification prompt for skeptically reviewing prior work, testing claims, and ensuring quality with concrete evidence
- `do-you-know-what-to-do-next.md` - Branch workflow prompt for determining current state, preparing merge handoffs, and identifying next tasks on feature branches 


### `handoffs/`
Handoff prompts for transferring work between agents:
- `HANDOFF.md` - Standard handoff prompt
- `HANDOFF-MINIMAL.md` - Minimal handoff for quick transfers
- `HANDOFF-DETAILED.md` - Comprehensive handoff with full context

### `modes/`
Mode-specific prompts that define agent behavior:
- `DISCUSSION-MODE.md` - Read-only analysis mode

### `research/`
Research-related prompts:
- `DEEP-RESEARCH-CURSOR-MCP-PLAYWRIGHT.md` - Deep research workflows

### `work-orders/`
Work order lifecycle prompts:
- `CREATE-WORK-ORDER.md` - Create executable work orders
- `EXECUTE-WORK-ORDER.md` - Execute existing work orders
- `WORK-ORDER-INDEX.md` - Work order index template

### `archive/`
Backup files and migration artifacts (not actively used).

## Usage

Prompts in this directory are referenced by:
- AGENTS.md (main configuration file)
- Mode definitions in `~/.agents/modes/`
- Agent orchestration scripts
- Work order execution workflows

## Adding New Prompts

1. Choose the appropriate subdirectory based on purpose
2. Follow naming convention: `ACTION-OBJECT.md` or `MODE-NAME.md`
3. Update this README if adding a new category
4. Update AGENTS.md if the prompt is referenced there

