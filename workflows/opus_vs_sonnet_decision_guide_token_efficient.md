# Opus 5 Effort-Ladder Decision Guide — Token Efficient

> **Retitled 2026-07-24. The filename is stale on purpose.**
>
> This file used to be an "Opus vs Sonnet" rubric. That premise is dead: Sonnet
> is retired and banned, so there is no Opus-vs-Sonnet decision left to make.
> The live decision is **which rung of the Opus 5 effort ladder to run** —
> `low`, `high`, or `max` — and that is what this document now covers.
>
> The filename `opus_vs_sonnet_decision_guide_token_efficient.md` is kept
> because other documents link to this path. Do not rename it without updating
> every referrer.
>
> **This file is not the canonical source of truth.** Canonical sources:
> - Compiled policy: `~/.agents/tools/usage-management/model-routing-policy.json`
> - Prose policy: `~/.agents/docs/MODEL-SELECTION-POLICY.md`
>
> Those are maintained by the usage-management benchmark system and update as
> benchmark results land. Do not duplicate the routing matrix here.

## Quick reference

```bash
# Classify a work order's complexity tier
~/.agents/tools/usage-management/benchmarks/scripts/classify-tier.sh <WO.md>

# Get the routed model + effort level for that tier
# (selector default provider is Codex; pass --provider claude on a Claude parent)
~/.agents/tools/usage-management/scripts/select-model.sh <tier>
~/.agents/tools/usage-management/scripts/select-model.sh <tier> --provider claude
```

## The one rule that replaced "Opus vs Sonnet"

**Pick the rung, not the model. When you need to go cheaper or faster, move
DOWN the Opus 5 ladder (`max` → `high` → `low`) — never ACROSS to a weaker
model.**

Sonnet 5 is retired (owner directive 2026-07-24: expensive for what it
delivers, must not be recommended). Haiku remains banned. Fable is retired.
There is no "cheap tier" that is a different model; the cheap tier is a lower
Opus rung.

## Why — CursorBench 3.2, imported 2026-07-24

Opus 5:

- `low` — 62.8% / $2.55 / 18,529 tokens / 37 steps
- `medium` — 64.3% / $3.29 / 23,612 tokens / 44 steps
- `high` — 66.7% / $3.91 / 27,932 tokens / 48 steps
- `xhigh` — 69.3% / $7.35 / 54,239 tokens / 72 steps
- `max` — 70.0% / $8.23 / 61,838 tokens / 78 steps

Sonnet 5:

- `low` — 47.7% / $1.30 / 16,269 tokens / 33 steps
- `medium` — 52.4% / $2.16 / 26,200 tokens / 46 steps
- `high` — 56.9% / $3.19 / 39,483 tokens / 57 steps
- `xhigh` — 58.7% / $4.16 / 52,871 tokens / 67 steps
- `max` — 61.5% / $6.45 / 92,882 tokens / 86 steps

**Sonnet 5 is dominated by Opus 5 at every point on the curve.** Sonnet 5 at its
best rung (`max`: 61.5%, $6.45, 92.9k tokens, 86 steps) loses to Opus 5 at its
cheapest rung (`low`: 62.8%, $2.55, 18.5k tokens, 37 steps) — worse quality at
2.5x the cost, 5x the token burn, and more steps. Every Sonnet rung is worse
than every routed Opus rung.

Snapshot: `~/.agents/tools/usage-management/model-capability/sources/cursorbench/snapshots/2026-07-24-cursorbench-3.2.json`

## Which rung

Classify first with `classify-tier.sh`; the tier picks the rung. Default
substantive work to 4-Extra High — a task is not 1-Low merely because it is
read-only, short, tool-based, or delegated, and it is not 5-Max merely because
it is substantive.

- **5-Max → Opus 5 `max` (70.0%). Exceptional, not a default.** Novel
  architecture with no established pattern, whole-system redesign, gnarly
  concurrency or correctness problems, security-critical or data-integrity
  design, or work whose failure is expensive to unwind. Costs 61.8k tokens and
  78 steps per task — the most quota-hungry route GAS runs, so spend it where it
  decides something. The bar is a clear indication *before the work starts*, or
  evidence the work is failing to get done properly at level 4.
- **4-Extra High → Opus 5 `xhigh` (69.3%). THE DEFAULT.** Where most GAS work
  runs, all the time: implementation, multi-file change, debugging, code review,
  interpretive QA, refactors, test writing, research and synthesis, writing work
  orders and proposals, and design inside an established pattern. 54.2k tokens
  and 72 steps. **Do not justify level 4 — justify anything else.**
- **3-High → Opus 5 `high` (66.7%). Reasoning without unknowns.** 27.9k tokens
  and 48 steps: **less than half the burn of `max` for -3.3pp**, the best
  quota-efficiency point on the curve. A settled work order carried out:
  nothing left to decide AND doable straight through. If it needs discovery, a
  testing loop, or a check of what it affected, it is level 4.
- **2-Medium → Opus 5 `medium` (64.3%).** Bounded procedure with clear scope and
  low ambiguity: commits and commit messages, report and changelog generation,
  applying an exact specified diff, running an established checklist end to
  end. 23.6k tokens and 44 steps.
- **1-Low → Opus 5 `low` (62.8%).** Files and documents: finding files, checking
  documentation, moves, renames, formatting, mechanical edits, index and README
  updates, deterministic search and inventory. 18.5k tokens and 37 steps — about
  a third of `max`'s tokens and half its steps. Still above every Sonnet rung.

**All five rungs are routed 1:1 — GAS level N is rung N.** The retired
three-level quantization threw away information the vendors already give us and
forced every judgment into a coarser bucket than the hardware supports (owner
directive 2026-07-26).

## When time is the binding constraint (burn windows, fast scouting/audits)

Tier classification optimizes for token/complexity fit — it assumes tokens are
the scarce resource. That inverts during a **time-boxed credit burn** (e.g. a
week's credit that must be spent in ~20 hours) or any deadline-bound
scouting/audit/research pass, where wall-clock TIME is what's actually scarce.

**In that specific case: step down the Opus ladder.** `low` is the fast lane
(18.5k tokens / 37 steps); `high` is the balanced default when `max` is too
slow (27.9k / 48). Reserve `max` for the hardest final synthesis, design, or
verification step.

The old advice here — "prefer Sonnet 5 @ xhigh over Opus @ max when the clock
binds" — was wrong on every axis, including the latency axis it was chosen for.
Sonnet 5 `xhigh` (58.7%, $4.16, 52.9k tokens, 67 steps) versus Opus 5 `low`
(62.8%, $2.55, 18.5k tokens, 37 steps): 4.1 points worse, 1.6x the cost, 2.9x
the tokens, 1.8x the steps. More tokens and more steps is more wall clock, so
it was not even fast.

This is a routing shift for time-pressured scouts and leaves, not a tier
reclassification, and not a licence to downshift for cost or quota pressure
alone. Keep scouts leaf-shaped (no re-delegation) and calibrate audit depth to
shelf-life — see
`~/.agents/docs/SUB-AGENT-ORCHESTRATION-GUIDE.md#time-constrained-delegation-burn-windows`
for fan-out and perishability guidance.

## Rules that remain universal

- **Escalate on rework** — if a route fails iteration #1, reclassify upward with
  evidence. Escalation goes UP the ladder, never sideways.
- **Never hardcode model choices** — always use `select-model.sh` or the
  compiled policy defaults.
- **Effort labels are not comparable across vendors.** Both providers now map
  1:1 — GAS level N is rung N on either harness — but the same-named Codex rung
  is weaker than the Claude one at every level, and each route carries a
  recorded band shortfall. Codex's ceiling (67.2) sits
  below Opus 5 `max` (70.0) — level-5 work where that gap matters belongs on
  Claude.
- Model eligibility is determined by benchmark results and owner directive, not
  by habit.

**Origin of the reversal:** owner directive 2026-07-24 (stop recommending
Sonnet; Claude uses Opus 5 across the board), corroborated by CursorBench 3.2.
The earlier time-pressure directive — memory
`feedback_prefer_fast_models_when_time_constrained`, from a 2026-07 credit-burn
window where Opus-max scouts with nested fan-out were too slow to return — was
right that `max` is the wrong rung for a deadline-bound scout, and wrong that
the fix was a different model.
