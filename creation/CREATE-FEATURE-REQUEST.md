# Create Feature Request

Document a complex need or requirement that isn't ready for implementation. Use for ideas needing analysis before becoming proposals or work orders.

## Feature Request Structure

```markdown
# Feature Request: [Descriptive Title]

**Feature ID**: FR-[YYYY-MM-DD]-[sequence]
**Created**: [YYYY-MM-DD-HH-MM-SS]
**Status**: Analysis Phase | Under Discussion | Ready for Proposal | Deferred
**Complexity**: Small (Days) | Medium (Week) | Large (Weeks) | Strategic (Months)
**Priority**: Critical | High | Medium | Low | Undefined

## Executive Summary
[1-2 paragraphs describing the need/problem]

## Problem Statement
### Current Pain Points
- [Specific problems this would solve]

### User Story
"As a [role], I need [capability] so that [benefit]"

## Requirements
### Functional Requirements
- [What it must do]

### Non-Functional Requirements
- [Performance, security, usability needs]

## Challenges & Considerations
- [Technical challenges]
- [Design decisions needed]
- [Open questions]

## Success Criteria
- [How we know it's working]

## Related Systems
- [What this connects to or affects]

## Next Steps
- [ ] Gather requirements
- [ ] Technical analysis
- [ ] Create proposal
- [ ] Generate work orders
```

## When to Create Feature Requests

Use feature requests for:

- **Complex problems** without clear solutions
- **Ideas from inbox** that need analysis
- **Cross-system changes** requiring coordination
- **User requests** needing investigation
- **Strategic initiatives** requiring planning

## Feature Request vs Other Documents

| Document Type | Use When |
|--------------|----------|
| Feature Request | Problem exists but solution unclear |
| Proposal | Solution approach defined with tasks |
| Work Order | Specific executable tasks ready |
| Discussion | Need theoretical exploration |

## File Management
1. Save to: `.dev/ai/features/[YYYY-MM-DD-HH-MM-SS]-[feature-name].md`
2. Track in project system
3. Link from proposals when created

## Processing Flow
```
Inbox Item → Too Complex? → Feature Request → Analysis → Proposal → Work Orders
                                           ↓
                                    Discussion Mode
```
