# Opus vs Sonnet Decision Guide (Token‑Efficient)

## Goal
Minimize **total cost + iteration time** while avoiding quality cliffs.

---

## Pricing (API)
- **Sonnet**: $3/MTok input, $15/MTok output (≤200K prompt); $6/MTok input, $22.50/MTok output (>200K prompt)
- **Opus**: $5/MTok input, $25/MTok output (≤200K prompt); $10/MTok input, $37.50/MTok output (>200K prompt)
- **Opus premium**: ~**1.67×** Sonnet per token

**Rule of thumb:** Opus becomes cheaper overall if Sonnet would take **≥2 serious iterations** or **≥1.7× total tokens** to converge.

---

## Default Policy
- **Start with Sonnet** unless any “Opus triggers” apply.
- Require **verification artifacts** in the same response for Sonnet tasks.

---

## Use Sonnet when ALL are true
- **Tight spec**: inputs/outputs + constraints are explicit.
- **Easy verification**: correctness can be checked mechanically (tests, typecheck, lint, deterministic parsing, diffs).
- **Low downside**: a subtle mistake costs minutes (not data loss/security/regression).
- **Short horizon**: < ~10 dependent steps; limited cross-file/cross-system reasoning.
- **High volume**: batch transformations, repetitive tasks, agent loops.

Examples:
- Refactor with unit tests already present
- Codegen for well-defined interfaces
- Data transforms with golden tests
- Writing parsers/serializers with fixtures

---

## Use Opus when ANY are true (Opus triggers)
- **Ambiguity + tradeoffs**: underspecified requirements; needs judgment calls.
- **Long-horizon reasoning**: multi-module refactors, migrations, distributed flows, orchestration.
- **High stakes**: auth/permissions, security reviews, data integrity, financial/legal/safety impact.
- **Complex debugging**: intermittent bugs, concurrency, performance pathologies.
- **Instruction-following must be exact**: cannot tolerate “almost right.”
- **Iteration already happened**: Sonnet attempt #1 produced uncertainty or rework.

Examples:
- Designing an end-to-end architecture with competing constraints
- Security-sensitive changes (OAuth/OIDC/JWT/ACLs)
- Database migration with rollback + invariants
- Debugging a production-only race condition

---

## Escalation Rule (fast)
Escalate **Sonnet → Opus** immediately if any occur:
- Output includes **nontrivial uncertainties** that block correctness.
- Evidence of **hand-wavy reasoning** / hidden assumptions.
- Fix touches **security/data-loss risk**.
- You are on **iteration #2**.

---

## Sonnet Safety Rails (required)
For Sonnet tasks, require these sections:
1. **Assumptions** (explicit)
2. **Plan** (numbered)
3. **Implementation**
4. **Checks**: tests + linters + invariants
5. **Edge cases**
6. **Blockers**: if blockers exist → **stop** and request missing facts

---

## Opus as Reviewer (cost-efficient)
Use Sonnet to draft; use Opus to **audit**:
- “Review for correctness, edge cases, and security. Return minimal diff/patch + test additions.”

This often beats using Opus for full generation when the task is mostly scoped.

---

## Two Prompt Templates
### 1) Gated output
> Produce: (1) assumptions, (2) solution, (3) tests/checks, (4) edge cases, (5) confidence blockers. If blockers exist, stop before solution and ask only for missing facts.

### 2) Minimal-diff mode
> Return only: unified diff + new/updated tests + one-paragraph rationale. No rewrites.

---

## Decision Checklist (one-line)
**Sonnet** = scoped + verifiable + low-stakes + short-horizon.

**Opus** = ambiguous/tradeoff-heavy OR long-horizon OR high-stakes OR complex debugging OR iteration #2.

