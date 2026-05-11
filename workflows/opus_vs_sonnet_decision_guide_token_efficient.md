# Model Selection Decision Guide — REDIRECTED

> **This file is no longer the canonical source of truth.**
>
> The single source of truth for model selection is now:
> **`~/.agents/docs/MODEL-SELECTION-POLICY.md`**
>
> That document is maintained by the usage management benchmark system and
> updates automatically as benchmark results complete and models improve.
>
> All model selection decisions — which model, which effort level, which tier —
> are governed by that policy. Do not duplicate rubrics here.

## Quick reference

```bash
# Classify a work order's complexity tier
~/.agents/tools/usage-management/benchmarks/scripts/classify-tier.sh <WO.md>

# Get the cheapest passing model + effort level for that tier
~/.agents/tools/usage-management/scripts/select-model.sh <tier>
```

## Rules that remain universal

- **Escalate on rework** — if any model fails iteration #1, escalate tier
- **Never hardcode model choices** — always use the script or policy defaults
- Model eligibility is determined by benchmark results, not hardcoded bans
