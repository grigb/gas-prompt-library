Read the current `AGENTS.md` and `PROJECT-RULES.md` when not already loaded.
Execute the requested design-synthesis scope using the existing project records.

Goal: preserve a connected chain from needs and domain understanding through
journey/interface study, information architecture, screen outlines and a separate
reusable-component outline. When separately authorized, these can inform mockup
review, agreed functionality and build/action extraction. This prompt adds no
permission or automatic continuation across those boundaries.

Authority and method:

- `~/.agents/skills/design-workflow/SKILL.md` — workflow and shared typed contract.
- `~/.agents/docs/methodologies/knowledge-to-build-method.md` — relevant K2B stages.
- `~/.agents/docs/methodologies/ia-synthesis-methodology.md` — IA compatibility.
- `~/.agents/docs/methodologies/ia-pattern-optimization-and-journey-analysis-reference.md`
  — conditional patterns and historical artifact bindings.
- `~/.agents/agents/project-manager/knowledge/PROJECT-MANAGER-PLANNING-APPROACH-STANDARD.md`
  — existing PRD/model/mockup/agreement/implementation progression.

## Resolve scope and existing state

Resolve `PROJECT_SOURCE_ROOT` from the actual project. Resolve name/identity from
`PROJECT-ID.md` or existing project records. Preserve explicit artifact roots in
project rules; otherwise reuse the relevant existing `.dev/ai` design artifact.
Do not create parallel cold-start notes, state stores or report sets when the
existing project run already records authority, evidence and continuation.

`DESIGN_RUN_MODE` uses the current request first, then valid existing run metadata.
Default to the authorized bounded stages, not `full_pipeline`. Retain these names
for callers, with the following meaning:

| Mode | Required evidence and consuming boundary |
|---|---|
| `ia_only` | Existing supported needs/model, journeys, priorities and interface evidence; IA output ends at its requested handoff |
| `ux_only` | Supported IA/model plus journeys; screen behavior/state and unresolved presentation questions |
| `ui_only` | Supported screen behavior/model; component outlines or specifically authorized visual work |
| `structured_data_only` | Existing typed artifacts and identified downstream consumer; no invented design decisions |
| `build_extraction_only` | Validated design and functionality agreement for the scoped build; extract work under existing authority |
| `validate_only` | Named record/revision/check question; report actual missing inputs and scope |
| `full_pipeline` | Explicit authorization for the named stages; each still stops at the current scope/pause boundary |

Load `design-workflow/references/workflow.md` and `references/contract.md`; bind
its project-run fields to existing PRD/understanding/decisions. Each stage records
applicability and reason, source producer, output consumer, checks, unresolved
issues and current next action. For a new product mark current-interface study
not applicable. For a partial return preserve accepted work and revisit only
affected decisions. A current pause overrides old run metadata and leaves no
executable next action or dispatch.

## Stage 5 design specialization

1. Use `journey-interface-study` for bounded evidence intake, whole-app/domain
   understanding, retained-foundation fit, complete goal journeys and separate
   current-interface mechanics. Preserve observed interface priority, agent
   recommendation and owner choice/history. Screenshots establish visible states,
   not hidden paths, click counts, permission enforcement or full-app coverage.
2. Use `information-architecture-synthesis` to consume that typed boundary. Keep
   content/capabilities, access, state, history and platform constraints. Test
   identity, authority, cardinality and lifecycle before menus. Trace structural
   hypotheses to requirements, material alternatives, disconfirmation, relevant
   checks and decisions. Compare the same journeys/roles/states/data. No universal
   navigation count, disclosure-depth limit, automatic score winner or fixed
   alternative quota applies.
3. Use `screen-component-outline` to produce concise screens first, then a
   distinct reusable-component outline. Preserve purpose, scope, entry/exit,
   permissions, consequences, feedback, interruption/recovery and accessibility.
   Reuse actual patterns and retain unique screen behavior. One-to-three-word
   labels are a target only where meaning survives.
4. Account for every requirement at each boundary, including API, export, history,
   migration and administration without invented screens. Name open semantic
   decisions and affected outputs. A layout choice cannot settle missing rules.
5. Deliver shared typed data plus concise Markdown views in existing project
   artifacts, with the same stable IDs and revision. The old fixed document sets
   and four scoring files are optional historical compatibility views, not required
   outputs for this path. Do not silently coerce old score fields into new semantics.

Use existing K2B ingestion/reconciliation/research outputs when relevant. A bounded
design request does not require all K2B stages to rerun. Missing facts return to
their producer and stop only dependent commitments. Record access/tool failures
as failed invocations, not invented observations or platform limitations.

## Existing design-kit integration

If the project has an explicitly configured `DESIGN_KIT_ROOT`, retain its supported
templates, current active design rules and design workspace. Read applicable
`00-active-design-rules.md` before changing covered outputs. If a required rule
payload is absent, identify the affected design-kit operation and its documented
generation command; independent authorized study can continue. Do not execute
generation, overwrite project files or require all five kit phases merely because
a directory exists. Resolve actual rule conflicts against current owner/project
authority and record their effects.

When an authorized operation uses the kit, run its supported local validator on
the changed outputs. Do not invent outputs or report missing unused phases as a
failure of a bounded study. Keep design-kit scripts/contracts unchanged by this
prompt; use an explicit project adapter if a caller needs their legacy shape.

## Handoff beyond outlines

A later authorized visual/mockup stage may define tokens, typography, color,
spacing, responsiveness, motion, interaction and copy while preserving supported
model/functionality. Reuse existing foundations. Mockups test presentation and
interaction; they need not be decided entirely in prose. Functionality agreement
remains before feature implementation, with the planning standard's proportional
exceptions and existing authorization intact.

For structured-data consumers, retain existing `id`, entity type, surface/role/
phase scope, dependencies, source evidence, acceptance criteria, build targets and
status where actually required. Bind them explicitly to shared IDs; do not convert
three priority sources silently into one P0/P1/P2 value. Preserve the source,
mapping rationale and current owner target. Name the exact downstream consumer.

Build extraction is K2B Stage 7, conditional on actual requested scope and required
functionality agreement. Reuse existing work orders, map accepted requirements to
build items and acceptance checks, and preserve non-screen work. Completing an
IA or outline is not authority to create/execute implementation tasks.

## Verification and durable result

Before consuming a stage, run the shared local checker on its record with
`--through interface`, `--through synthesis` or `--through components` as applicable.
For corrections add `--previous` and verify the affected dependency set. Then
review actual evidence-to-decision reasoning, requirement preservation and the
Markdown view; shape validation alone does not prove meaning, usability or access.

For work actually using the wider K2B pipeline, run its existing
`~/.agents/scripts/validate-k2b-gates.sh` on the declared artifact root and scope;
record unsupported scope assumptions if its full-pipeline checks do not describe
this bounded run. Use its strict mode when that full contract applies. Do not
manufacture unrelated artifacts just to make a full-pipeline validator green.

The existing result records requested/executed stages, source revisions, actual
commands/outcomes, changed/reused paths, check limits, unresolved decisions and
the next authorized action or explicit stop. Report real usability/runtime only
when exercised. Do not add a compulsory three-command continuation or repeated
clean pass. A fresh session must recover evidence, priorities, decisions and the
current stopping point from that record without owner re-explanation.
