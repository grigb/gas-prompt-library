---
pattern: docs-continuous-sync
category: DOCUMENTATION
learned_from: mzfusion-api mainnet transition — user had to remind about docs multiple times
---

# Pattern: Keep Documentation in Continuous Sync

## The Lesson
The user explicitly stated: "The docs must stay in perfect synchronous fidelity with our understanding of the project at all times." Documentation was falling behind as work progressed — the user had to remind multiple times to update docs.

## The Rule
1. After every significant discovery or fix, delegate a documentation update agent
2. Don't batch doc updates — sync incrementally as knowledge changes
3. The mainnet transition doc (testnet-to-mainnet-actual-steps.md) is the living record — update it with every new finding
4. All delegated doc agents MUST read docs/README.md first for onboarding

## How to Apply
- After each completed agent batch, check if any docs need updating
- Keep a mental checklist: did this change affect operations docs? config guide? rebuild guide? state of project?
