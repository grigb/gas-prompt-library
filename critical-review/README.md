# GAS Critical Review Prompts

These prompts support the Critical Review skill:

`/Users/grig/.agents/skills/critical-review/SKILL.md`

Use them when a project steward or project agent needs a compact paste-in prompt for a Critical Review workflow without copying the full protocol.

## Prompt Index

- Existing Fable review assimilation:
  `/Users/grig/.agents/prompts/critical-review/assimilate-existing-fable-review.md`
- Second-pass Fable direct-edit preparation:
  `/Users/grig/.agents/prompts/critical-review/prepare-fable-direct-edit-followup.md`
- Post-review gap capture follow-up:
  `/Users/grig/.agents/prompts/critical-review/post-review-gap-capture-followup.md`
- Pre-Critical Review Package Stability Check:
  `/Users/grig/.agents/prompts/critical-review/pre-critical-review-package-stability-check.md`
- True owner gate brief:
  `/Users/grig/.agents/prompts/critical-review/true-owner-gate-brief.md`
- Artifact scoring prep:
  `/Users/grig/.agents/prompts/critical-review/artifact-scoring-prep.md`

## Owner-Facing Short Forms

Use these when giving work to a project steward:

```text
Consume the Fable review for this Critical Review packet using the current GAS Critical Review skill. Classify findings, create/update WOs, dispatch safe work, isolate true owner gates, update project state, and prepare the next direct-edit Fable prompt if needed.
```

```text
Run the Pre-Critical Review Package Stability Check for [project/workstream/issue].

Use: /Users/grig/.agents/prompts/critical-review/pre-critical-review-package-stability-check.md
Report readiness status and next safe action. Do not launch Fable/top-model from this check.
```

```text
Prepare a second-pass Fable direct-edit prompt for this Critical Review packet. Include current state, project principles/goals, completed follow-up WOs, remaining findings, mutation boundary, verification requirements, and report path.
```

```text
Before this Critical Review session closes, run the post-review gap capture follow-up:
/Users/grig/.agents/prompts/critical-review/post-review-gap-capture-followup.md

Write a standalone gap addendum next to the main report and reply with the addendum path.
```

## Final Dispatch Prompt Skeleton

Use this shape for each final Fable/top-model/high-effort prompt. Critical Review is the durable process; Fable is only the current model flavor.

```text
Provide your session transcript absolute path.

Directory: /absolute/project/root
Mode: review-and-remediate
Stability status: READY_FOR_REVIEW
Thread title: exact-existing-thread-title
/absolute/path/to/critical-review-or-prompt.md
Continue in this same thread. Do not create or rename a thread.

Use the packet/prompt path above. Inspect curated evidence, challenge the architecture and assumptions, apply safe scoped local file/report changes directly when mutation_allowed permits them, run verification, and write the report to the packet's report_path.

Before mutation starts, write/update the execution ledger named in the packet with packet path, thread title, transcript path if known, run/session id, requested model, actual model if detectable, started timestamp, status, report path, and duplicate-run/report detection.

Use normal local engineering wording for visible status/report text. Preserve safety boundaries: no production, mainnet/custody, credential/secret, money, deployment, external-account, destructive, legal/financial/business authority, or irreversible action unless the packet explicitly authorizes that exact action.

Return with: recommendation, changed files, verification, remaining findings, next front, owner action yes/no, report path, execution-ledger path, and transcript path.
Relay back using return marker: <RETURN_MARKER>. If direct Codex thread relay is available and receipt-producing, use it; otherwise write the durable report/result artifact and state relay was unavailable.
```

For a new thread, replace `Thread title:` with `New thread title:`. For an existing thread, the title must be the exact harness-visible title and the prompt must include `Continue in this same thread. Do not create or rename a thread.`

## Multi-Prompt Pack Rules

Write every multi-prompt pack to a durable Markdown file. The Markdown file must include one section per target, each with `Directory:`, `Thread title:` or `New thread title:`, packet/prompt path, mode, stability status, transcript-first request, relay-back instructions, constraints, collision domain, and report/result path.

Required sections:

- `READY TO PASTE NOW`
- `CONDITIONAL`
- `HOLD / DO NOT PASTE`

Do not include already-started or prerequisite-waiting prompts in `READY TO PASTE NOW`. Prefer direct Codex thread relay when the exact target thread and receipt-producing send tool are available; owner paste is fallback only.

Use plain language. Define internal labels inline; `per-target minimal presentation` means selective minimum disclosure per viewer/system/use case. If a provider safeguard flags a prompt, rewrite only that prompt in normal local engineering language and record the flagged prompt plus rewrite.
