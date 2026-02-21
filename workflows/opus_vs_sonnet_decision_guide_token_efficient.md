# Model Selection Decision Guide

## Purpose

Canonical, single source of truth for model selection across the GAS system. All other files reference this guide — they do not duplicate its rubric.

**Tuning this file tunes the entire system.**

---

## Model Registry

| Model ID | Alias | Role | Status |
|----------|-------|------|--------|
| `claude-opus-4-6` | `opus` | Default. Planning, orchestration, reviews, decisions, ambiguous work | Active |
| `claude-sonnet-4-5-20250929` | `sonnet` | Leaf-node execution of well-defined work orders | Active |
| `claude-haiku-4-5-20251001` | `haiku` | **FORBIDDEN** — unreliable for agent work | Banned |

**Future models** (not yet integrated — add rows here when activated):
- Gemini (Google) — TBD role, TBD status
- KIMI K2.5 — cost-optimized standard development (currently in GAS Team Runtime)
- Codex (OpenAI) — TBD role, TBD status

---

## Default Policy

- **Opus is the default.** All work starts with Opus unless the delegating agent explicitly downgrades.
- Only an Opus-level agent (orchestrator, planner, WO creator) may decide to delegate leaf work to Sonnet.
- **Sonnet never steers, never decides, never orchestrates, never plans.**

---

## Role-Based Defaults

| Role | Model | Rationale |
|------|-------|-----------|
| Orchestrators (L4 GAS Manager, agent-orchestrator) | Opus | Must handle unexpected situations, coordinate workers, make judgment calls |
| Planners (L2 Blueprint Keeper, L3 Request Router) | Opus | Strategic reasoning, alignment checks, tradeoff evaluation |
| Reviewers / QA (agent-qa, security-compliance) | Opus | Must catch subtle issues, not just obvious ones |
| Work order creators | Opus | Need context to assess complexity, write clear specs, choose model for execution |
| Documentation authors | Opus | Quality writing, architectural coherence, accurate representation |
| Leaf workers executing well-defined WOs | Sonnet (when criteria below are ALL met) | Instructions compensate for less autonomous reasoning |
| Leaf workers executing ambiguous WOs | Opus | Ambiguity requires the reasoning Sonnet lacks |

---

## When Opus May Delegate to Sonnet

Sonnet is acceptable for leaf-node execution **only when ALL five criteria are true**:

1. **Tight spec**: The work order has explicit inputs, outputs, constraints, and step-by-step instructions. The worker does not need to figure out *what* to do.
2. **Easy verification**: Correctness can be checked mechanically (tests, typecheck, lint, deterministic parsing, diffs).
3. **Low downside**: A subtle mistake costs minutes to fix, not data loss, security holes, or regressions.
4. **Short horizon**: < ~10 dependent steps; limited cross-file/cross-system reasoning.
5. **No steering**: The output does not feed into planning, architecture, decision-making, or documentation that others depend on.

**Examples of Sonnet-safe work:**

- Implement a function with a complete interface spec and test fixtures
- Refactor with unit tests already present and passing
- Apply a well-defined code transformation across files (rename, reformat, migrate syntax)
- Data transforms with golden tests
- Single-file changes with clear acceptance criteria

**Examples that MUST stay on Opus:**

- Any work order marked "figure out the approach"
- Anything touching auth, permissions, security, data integrity
- Cross-system reasoning (multiple modules, distributed flows)
- Creating documentation, proposals, or specs others will act on
- Debugging intermittent or concurrency issues
- Any WO where the author couldn't write explicit step-by-step instructions

---

## Escalation Rule

Escalate **Sonnet to Opus** immediately if ANY occur during execution:

- Output includes **nontrivial uncertainties** that block correctness
- Evidence of **hand-wavy reasoning** or hidden assumptions
- Fix touches **security or data-loss risk**
- You are on **iteration #2** (Sonnet's first attempt didn't converge)

**The 1.67x rule:** Opus is ~1.67x Sonnet per token. Opus becomes cheaper overall if Sonnet would take >=2 serious iterations or >=1.7x total tokens to converge. When in doubt, use Opus — the rework cost exceeds the token savings.

---

## Sonnet Safety Rails (required when using Sonnet)

When delegating to Sonnet, the work order or prompt MUST require these sections in output:

1. **Assumptions** (explicit — no hidden ones)
2. **Plan** (numbered steps before implementation)
3. **Implementation**
4. **Checks**: tests + linters + invariants run
5. **Edge cases** addressed
6. **Blockers**: if blockers exist, **stop** and report — do not guess

---

## Opus as Reviewer (cost-efficient hybrid)

Use Sonnet to draft, then Opus to **audit**:
- "Review for correctness, edge cases, and security. Return minimal diff/patch + test additions."

This beats using Opus for full generation when the task is well-scoped but the output matters.

---

## Pricing Reference (API)

- **Sonnet**: $3/MTok input, $15/MTok output (<=200K prompt); $6/$22.50 (>200K)
- **Opus**: $5/MTok input, $25/MTok output (<=200K prompt); $10/$37.50 (>200K)
- **Opus premium**: ~1.67x Sonnet per token

---

## Prompt Templates (for Sonnet-delegated work)

### 1) Gated output
> Produce: (1) assumptions, (2) solution, (3) tests/checks, (4) edge cases, (5) confidence blockers. If blockers exist, stop before solution and ask only for missing facts.

### 2) Minimal-diff mode
> Return only: unified diff + new/updated tests + one-paragraph rationale. No rewrites.

---

## Decision Checklist (one-line)

**Opus** = default for all work. Planning, orchestration, reviews, decisions, ambiguous tasks, documentation.

**Sonnet** = leaf-node execution ONLY when: tight spec + mechanical verification + low stakes + short horizon + no steering. Escalate to Opus on iteration #2.

**Haiku** = FORBIDDEN.
