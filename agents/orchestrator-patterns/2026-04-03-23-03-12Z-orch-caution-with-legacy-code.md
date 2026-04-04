---
pattern: caution-with-legacy-code
category: SAFETY
learned_from: mzfusion-api mainnet transition session (2026-03-27 to 2026-04-03)
---

# Pattern: Exercise Extra Caution with Legacy/Critical Codebases

## The Lesson
The MZFusion project has 2+ years of critical code. Multiple agent fixes during this session introduced regressions:
- 3D exploded view rewrite broke the UI completely (had to revert)
- auto-config.py overwrote config.toml silently after generate_config.py fixed it
- Agents claimed fixes worked without actually verifying visually
- Render offset fix needed multiple iterations
- Pedigree ancestor fix took 4 attempts (v1, v2, v3, then manual orchestrator fix)

## The Rule
1. **Prefer minimal, surgical changes** over rewrites. Tweak one formula, don't replace an entire rendering system.
2. **Agents MUST verify their own work** before reporting success — by checking actual output, not just "it compiles."
3. **Never trust an agent's claim that something is fixed** without independent verification (browser test, API call, log check).
4. **Two-year-old code that works should be treated as fragile** — understand WHY it works before changing HOW it works.
5. **When delegating to sub-agents, explicitly state: "make minimal changes only, do not rewrite existing working systems."**

## How to Apply
- Add "MINIMAL CHANGES ONLY — do not rewrite existing working code" to all sub-agent prompts for this project
- Require agents to include verification output (not just "it works") in their reports
- When an agent reports a fix, run an independent verification before telling the user it's done
