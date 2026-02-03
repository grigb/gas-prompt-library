# Prompt File Path Index

**Purpose**: Fast lookup index for all prompt files. Agents should check this file FIRST before searching.

## Quick Lookup Table

| Logical Name | Actual Path |
|-------------|-------------|
| CREATE-WORK-PROPOSAL | `~/.agents/prompts/creation/CREATE-WORK-PROPOSAL.md` |
| CREATE-AUDITABLE-RECORD | `~/.agents/prompts/creation/CREATE-AUDITABLE-RECORD.md` |
| CREATE-FEATURE-REQUEST | `~/.agents/prompts/creation/CREATE-FEATURE-REQUEST.md` |
| CREATE-WORK-ORDER | `~/.agents/prompts/work-orders/CREATE-WORK-ORDER.md` |
| EXECUTE-WORK-ORDER | `~/.agents/prompts/work-orders/EXECUTE-WORK-ORDER.md` |
| WORK-ORDER-INDEX | `~/.agents/prompts/work-orders/WORK-ORDER-INDEX.md` |
| HANDOFF | `~/.agents/prompts/handoffs/HANDOFF.md` |
| HANDOFF-DETAILED | `~/.agents/prompts/handoffs/HANDOFF-DETAILED.md` |
| HANDOFF-MINIMAL | `~/.agents/prompts/handoffs/HANDOFF-MINIMAL.md` |
| CONVERT-HANDOFF-TO-WORKORDER | `~/.agents/prompts/handoffs/CONVERT-HANDOFF-TO-WORKORDER.md` |
| DISCUSSION-MODE | `~/.agents/prompts/modes/DISCUSSION-MODE.md` |
| ORGANIZE-DOCS+DIRS | `~/.agents/prompts/general/organize-docs+dirs.md` |
| DEEP-RESEARCH-PROMPT-GENERATOR | `~/.agents/prompts/research/deep-research-prompt-generator.md` |
| DEEP-RESEARCH-MASTER | `~/.agents/prompts/research/deep-research-master.md` |
| INTERFACE-AUDIT-ORCHESTRATOR | `~/.agents/prompts/general/interface-audit-orchestrator.md` |
| PARALLEL-REVIEW-ORCHESTRATOR | `~/.agents/prompts/general/parallel-review-orchestrator.md` |
| REVIEW-LOOSE-ENDS | `~/.agents/prompts/general/review-loose-ends.md` |
| CONDUCT-MODEL-AUDIT | `~/.agents/prompts/research/CONDUCT-MODEL-AUDIT.md` |
| TRI-AGENT-RESEARCH-PIPELINE | `~/.agents/prompts/research/tri-agent-research-pipeline.md` |

## Full Directory Structure

```
~/.agents/prompts/
├── README.md                           # Main prompts documentation
├── PROMPT-PATH-INDEX.md               # THIS FILE - fast lookup
├── general/                           # General purpose prompts
│   ├── autonomous-mode-now.md
│   ├── do-you-know-what-to-do-next.md
│   ├── interface-audit-orchestrator.md
│   ├── organize-docs+dirs.md          # Documentation organization guide
│   ├── parallel-review-orchestrator.md
│   ├── prepare-work-for-review.md
│   ├── review-loose-ends.md           # AI work audit & loose ends extraction
│   ├── review-my-plan.md
│   └── verify-previous-work.md
│
├── agents/                             # Specialized AI agents
│   ├── README.md                       # Agent directory index
│   ├── agent-orchestrator.md
│   ├── agent-dev-general-contractor.md
│   ├── agent-dev-overseer.md
│   ├── agent-dev-worker.md
│   ├── agent-software-product-builder.md
│   ├── agent-research-analysis.md
│   ├── agent-research-gap-analysis.md
│   ├── agent-strategic-intelligence.md
│   ├── agent-chief-of-staff.md
│   ├── agent-chief-reality-officer.md
│   ├── agent-financial-analysis-planning.md
│   ├── agent-marketing-expert.md
│   ├── agent-project-coordinator.md
│   ├── agent-ux-design.md
│   ├── agent-content-crafting-alignment.md
│   ├── agent-innovation-ideation.md
│   ├── agent-communication-stakeholder.md
│   ├── agent-data-analysis-visualization.md
│   ├── agent-testing-validation.md
│   ├── agent-security-compliance.md
│   ├── agent-tooling.md
│   ├── agent-network-diagnostics-specialist.md
│   ├── agent-process-analysis-retrospective.md
│   ├── agent-process-analysis-retrospective-quick.md
│   ├── agent-process-design-optimization.md
│   ├── agent-document-analysis-audit.md
│   ├── agent-synthesis-integration.md
│   └── agent-learning-knowledge-management.md
│
├── creation/                           # Document creation prompts
│   ├── CREATE-WORK-PROPOSAL.md        # Work proposal generation
│   ├── CREATE-AUDITABLE-RECORD.md     # Auditable record creation
│   └── CREATE-FEATURE-REQUEST.md      # Feature request creation
│
├── work-orders/                        # Work order management
│   ├── CREATE-WORK-ORDER.md           # Work order creation
│   ├── EXECUTE-WORK-ORDER.md          # Work order execution
│   └── WORK-ORDER-INDEX.md            # Work order index
│
├── handoffs/                           # Handoff protocols
│   ├── HANDOFF.md                     # Standard handoff
│   ├── HANDOFF-DETAILED.md            # Detailed handoff
│   ├── HANDOFF-MINIMAL.md             # Minimal handoff
│   └── CONVERT-HANDOFF-TO-WORKORDER.md # Handoff to Work Order conversion
│
├── modes/                              # Special operation modes
│   └── DISCUSSION-MODE.md             # Discussion mode protocol
│
└── research/                           # Research prompts
    └── deep-research-prompt-generator.md
```

## Usage Instructions for AI Agents

### STEP 1: Check This Index FIRST
Before searching, read this file to find the exact path.

### STEP 2: Direct Read
Use the exact path from the table above.

### STEP 3: Only Search If Not Listed
If the file isn't in this index, THEN use search tools.

## Common Patterns

- **Creation tasks**: Check `creation/` directory
- **Work orders**: Check `work-orders/` directory
- **Handoffs**: Check `handoffs/` directory
- **Specialized agents**: Check `agents/` directory
- **Modes**: Check `modes/` directory
- **General prompts**: Check `general/` directory

## Path Resolution

All paths use `~/.agents/prompts/` as the base directory.

Example resolution:
- Index shows: `~/.agents/prompts/creation/CREATE-WORK-PROPOSAL.md`
- Full path: `~/.agents/prompts/creation/CREATE-WORK-PROPOSAL.md`

---

**Last Updated**: 2025-12-08
**Maintained by**: Automated sync from directory structure
