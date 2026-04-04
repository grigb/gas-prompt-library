---
pattern: verify-before-reporting
category: QUALITY
learned_from: mzfusion-api pedigree fix (took 4 attempts), 3D view rewrite (reverted)
---

# Pattern: Always Verify Agent Work Before Reporting to User

## The Lesson
The user explicitly said: "no matter what the agent tells you, you've got to test it yourself before you decide it's done." Multiple agents reported fixes as complete when they weren't:
- Pedigree ancestor traversal: 4 versions before it actually worked
- The orchestrator reported "fixed" after each agent completed, then the user showed screenshots proving it wasn't
- The 3D view agent said it was fixed but the result was completely broken

## The Rule
1. After an agent reports a fix, the orchestrator MUST run independent verification before telling the user
2. For frontend changes: use agent-browser to take a screenshot and check visually
3. For backend changes: query the API directly and check the response
4. For config changes: read the actual file and verify the values
5. NEVER say "fixed" based solely on an agent's report

## How to Apply
- After every sub-agent completion, run a verification step (browser test, API call, file read)
- If verification can't be done programmatically, tell the user "agent reports fix, needs your visual verification" instead of "fixed"
