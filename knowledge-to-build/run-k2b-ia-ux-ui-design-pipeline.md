Read `AGENTS.md` and `PROJECT-RULES.md` first, then execute.

Goal:
Run a K2B design-synthesis pipeline that transforms reconciled knowledge into:
- Information Architecture (IA) outputs,
- UX specifications,
- UI specifications,
- agent-ready structured design data,
- and build/action extraction inputs for work-order execution.

This method must work as:
1. a full end-to-end pipeline, and
2. a modular stage runner when only one part is needed.

Do not stop at report-only output unless hard-blocked.

Authority references (follow these if any conflict exists):
- `/Users/grig/.agents/docs/methodologies/knowledge-to-build-method.md`
- `/Users/grig/.agents/docs/methodologies/ia-synthesis-methodology.md`
- `/Users/grig/.agents/docs/methodologies/ia-pattern-optimization-and-journey-analysis-reference.md`
- `/Users/grig/.agents/modes/KNOWLEDGE-TO-BUILD-MODE.md`
- `/Users/grig/.agents/docs/vision/VISION-ADDENDUM-knowledge-index-to-build-mandate.md`
- `/Users/grig/.agents/scripts/validate-k2b-gates.sh`

Execution mode resolution:
- Resolve `DESIGN_RUN_MODE` in this order:
  1. Explicit mode in user request
  2. Existing run metadata from current design run (if resuming)
  3. Default: `full_pipeline`
- Supported values:
  - `full_pipeline`
  - `ia_only`
  - `ux_only`
  - `ui_only`
  - `structured_data_only`
  - `build_extraction_only`
  - `validate_only`

Context resolution (do not ask user for placeholders):
- `PROJECT_SOURCE_ROOT`: current working directory (`pwd`)
- `PROJECT_NAME`: from `PROJECT-ID.md` (`project:`, `id:`, or `Project Name`), else repo basename
- `K2B_ARTIFACT_ROOT` precedence:
  1. explicit `K2B_ARTIFACT_ROOT:` in project rules/docs
  2. existing `PROJECT_SOURCE_ROOT/.dev/ai`
  3. fallback `PROJECT_SOURCE_ROOT/.dev/ai`
- `DESIGN_ARTIFACT_ROOT` precedence:
  1. explicit `DESIGN_ARTIFACT_ROOT:` in project rules/docs
  2. existing `K2B_ARTIFACT_ROOT/design`
  3. fallback `K2B_ARTIFACT_ROOT/design`
- `DESIGN_WORKSPACE` precedence:
  1. explicit `DESIGN_WORKSPACE:` in project rules/docs
  2. existing `DESIGN_ARTIFACT_ROOT/workspace`
  3. fallback `DESIGN_ARTIFACT_ROOT/workspace`
- `DESIGN_KIT_ROOT` precedence:
  1. explicit `DESIGN_KIT_ROOT:` in project rules/docs
  2. existing `PROJECT_SOURCE_ROOT/.dev/kits/design-kit`
  3. `PROJECT_SOURCE_ROOT` only if `PROJECT_SOURCE_ROOT/scripts/run-design.sh` exists
  4. unset (design-kit compatibility mode disabled)

Optional design-kit compatibility mode:
- If `DESIGN_KIT_ROOT` resolves, reuse design-kit templates, scripts, and constraints.
- Prefer these templates when available:
  - `templates/02a-site-map-information-architecture.md`
  - `templates/04-interaction-design.md`
  - `templates/03-visual-design-requirements.md`
  - `templates/05-implementation-guidelines.md`
  - `templates/gate-definitions.md`
- Prefer these scripts when available:
  - `DESIGN_KIT_ROOT/scripts/run-design.sh`
  - `DESIGN_KIT_ROOT/scripts/bash/design-generate.sh`
  - `DESIGN_KIT_ROOT/scripts/bash/validate-design-kit-run.sh`
- If the design kit is absent, continue with this prompt's default contract.

Active Injection contract (mandatory when `DESIGN_KIT_ROOT` is set and mode includes IA/UX/UI generation):
1. Create/refresh the design workspace using design-kit generation:
   - `"$DESIGN_KIT_ROOT/scripts/run-design.sh" generate --input "<requirements-or-brief-path>" --workspace "$DESIGN_WORKSPACE"`
   - if `run-design.sh` is unavailable, fallback to:
     - `"$DESIGN_KIT_ROOT/scripts/bash/design-generate.sh" --interface "<interface-name>" --workspace "$DESIGN_WORKSPACE" --input "<requirements-or-brief-path>"`
2. Verify Active Rules payload exists and is non-empty:
   - `"$DESIGN_WORKSPACE/00-active-design-rules.md"`
3. Read and apply that payload before writing/updating IA/UX/UI outputs.
4. Ensure design-phase compliance sections exist in each design workspace phase file:
   - `01-design-philosophy.md`
   - `02-component-specifications.md`
   - `03-visual-design-requirements.md`
   - `04-interaction-design.md`
   - `05-implementation-guidelines.md`
5. If Active Rules payload is missing, stop with a blocker and exact remediation command.

Hard constraints:
- Use absolute paths only.
- Preserve source traceability for every design claim.
- No markdown tables in generated reports.
- Do not leave placeholder tokens like `[REPLACE:*]` in deliverables.
- Every "next actions" section must contain executable shell commands, not bare paths.
- If design-kit compatibility mode is active, do not skip Active Injection checks.

Mandatory cold-start note (required for every run):
- `K2B_ARTIFACT_ROOT/reports/K2B-DESIGN-COLD-START-CONTEXT-<YYYY-MM-DD-HH-MM-SS>.md`
- Must include:
  - why this run exists now,
  - active/open work orders this run advances,
  - current bottleneck stage/gate,
  - selected `DESIGN_RUN_MODE`,
  - root policy decisions for `K2B_ARTIFACT_ROOT` and `DESIGN_ARTIFACT_ROOT`.

Core stage map:
- IA synthesis aligns to K2B Applied Synthesis (Stage 5 specialization).
- UX synthesis aligns to K2B Applied Synthesis (Stage 5 specialization).
- UI synthesis aligns to K2B Applied Synthesis (Stage 5 specialization).
- Structured design data bridges synthesis outputs into build-ready records.
- Build extraction aligns to K2B Stage 7.

Stage execution contract:

1) IA synthesis stage (`ia_only` or part of `full_pipeline`)
- Inputs required:
  - Stage -1/0 readiness artifacts
  - Stage 1-4 outputs (ingestion, reconciliation, extraction, research)
  - active stakeholder decisions
- Process requirements:
  - classify surfaces by interaction model (active/semi-active/passive)
  - define surface-agnostic content object model (objects, attributes, relationships, CTAs)
  - map roles, visibility, and progressive disclosure
  - design per-surface navigation hierarchies and passive-surface programming rules
  - define cross-surface state handoffs and phase-gated IA scope
  - run IA pattern optimization and journey analysis per:
    - `/Users/grig/.agents/docs/methodologies/ia-pattern-optimization-and-journey-analysis-reference.md`
  - prioritize top journeys, generate at least 2 IA variants per journey, and score variants using the elegance model
  - enforce cognitive-load constraints:
    - top-level nav items per surface: <= 7
    - disclosure depth before content: <= 2
- Required outputs:
  - `DESIGN_ARTIFACT_ROOT/ia/00-ia-overview.md`
  - `DESIGN_ARTIFACT_ROOT/ia/01-content-model.md`
  - `DESIGN_ARTIFACT_ROOT/ia/02-surface-classification.md`
  - `DESIGN_ARTIFACT_ROOT/ia/03-navigation-hierarchies.md`
  - `DESIGN_ARTIFACT_ROOT/ia/04-user-role-map.md`
  - `DESIGN_ARTIFACT_ROOT/ia/05-cross-surface-flows.md`
  - `DESIGN_ARTIFACT_ROOT/ia/06-signage-tier-architecture.md` (when passive surfaces exist)
  - `DESIGN_ARTIFACT_ROOT/ia/07-phase-scope.md`
  - `DESIGN_ARTIFACT_ROOT/ia/08-pattern-library-application.md`
  - `DESIGN_ARTIFACT_ROOT/ia/09-journey-scorecards.md`
  - `DESIGN_ARTIFACT_ROOT/ia/10-ia-variant-comparison.md`
  - `DESIGN_ARTIFACT_ROOT/ia/11-ia-elegance-decision.md`
  - `DESIGN_ARTIFACT_ROOT/ia/optimization/pattern-candidates.json`
  - `DESIGN_ARTIFACT_ROOT/ia/optimization/journey-scorecards.json`
  - `DESIGN_ARTIFACT_ROOT/ia/optimization/ia-variant-scores.json`
  - `DESIGN_ARTIFACT_ROOT/ia/optimization/ia-elegance-decision.json`
- Gate:
  - every in-scope feature maps to an IA object or navigation entry
  - at least 2 IA variants scored per prioritized journey
  - selected IA variant (or hybrid) has an explicit elegance decision record with evidence paths
  - no unresolved IA contradictions

2) UX synthesis stage (`ux_only` or part of `full_pipeline`)
- Prerequisites:
  - IA outputs complete (or explicitly accepted with risks)
- Process requirements:
  - derive top journeys per role-surface pair
  - define task flows with entry, success, fallback, and recovery paths
  - specify progressive disclosure behavior and state transitions
  - define error, empty, loading, offline, and permission-denied behavior
  - define accessibility behavior contracts (keyboard, focus order, screen reader semantics)
  - map each UX requirement to IA evidence and source research
- Required outputs:
  - `DESIGN_ARTIFACT_ROOT/ux/00-ux-overview.md`
  - `DESIGN_ARTIFACT_ROOT/ux/01-journey-map.md`
  - `DESIGN_ARTIFACT_ROOT/ux/02-task-flows.md`
  - `DESIGN_ARTIFACT_ROOT/ux/03-screen-behavior-contracts.md`
  - `DESIGN_ARTIFACT_ROOT/ux/04-state-matrix.md`
  - `DESIGN_ARTIFACT_ROOT/ux/05-accessibility-behavior.md`
  - `DESIGN_ARTIFACT_ROOT/ux/06-ux-validation.md`
- Gate:
  - every primary journey is complete and testable
  - no UX flow depends on undefined IA objects/routes

3) UI synthesis stage (`ui_only` or part of `full_pipeline`)
- Prerequisites:
  - IA + UX outputs complete
- Process requirements:
  - create design foundations (tokens, typography, color roles, spacing, elevation, motion)
  - define component contracts (states, variants, density modes, responsiveness)
  - define per-surface layout structures and interaction affordances
  - specify copy/label standards and microcopy behaviors
  - enforce accessibility and contrast requirements at component level
  - keep all values tokenized (avoid arbitrary visual constants)
- Required outputs:
  - `DESIGN_ARTIFACT_ROOT/ui/00-ui-overview.md`
  - `DESIGN_ARTIFACT_ROOT/ui/01-design-foundations.md`
  - `DESIGN_ARTIFACT_ROOT/ui/02-component-contracts.md`
  - `DESIGN_ARTIFACT_ROOT/ui/03-layout-and-responsive-rules.md`
  - `DESIGN_ARTIFACT_ROOT/ui/04-motion-and-feedback.md`
  - `DESIGN_ARTIFACT_ROOT/ui/05-content-and-language-rules.md`
  - `DESIGN_ARTIFACT_ROOT/ui/06-ui-validation.md`
- Gate:
  - every UI component maps to a UX behavior and IA object
  - accessibility and responsive coverage documented for all core components
  - if `DESIGN_KIT_ROOT` is active, `DESIGN_WORKSPACE/00-active-design-rules.md` evidence path is present in the UI stage report

4) Structured design data stage (`structured_data_only` or part of `full_pipeline`)
- Prerequisites:
  - IA + UX + UI outputs complete
- Required transformation:
  - project design docs into machine-consumable records
  - preserve end-to-end traceability to source evidence
- Required fields per structured record:
  - `id`
  - `entity_type` (`ia_object`, `route`, `journey`, `screen`, `component`, `token`, `build_item`)
  - `surface_family`
  - `role_scope`
  - `phase_scope` (`MVP`, `V2`, `Later`, `Never`)
  - `priority` (`P0`, `P1`, `P2`)
  - `depends_on` (array)
  - `source_evidence` (absolute paths)
  - `acceptance_criteria` (array)
  - `build_targets` (array)
  - `status`
- Required outputs:
  - `DESIGN_ARTIFACT_ROOT/structured-data/design-token-map.json`
  - `DESIGN_ARTIFACT_ROOT/structured-data/ia-surface-map.json`
  - `DESIGN_ARTIFACT_ROOT/structured-data/journey-flow-map.json`
  - `DESIGN_ARTIFACT_ROOT/structured-data/component-contracts.json`
  - `DESIGN_ARTIFACT_ROOT/structured-data/screen-blueprints.json`
  - `DESIGN_ARTIFACT_ROOT/structured-data/build-ready-design-index.json`
- Gate:
  - every structured entity has evidence and acceptance criteria
  - no orphaned entity without stage/source provenance

5) Build extraction stage (`build_extraction_only` or part of `full_pipeline`)
- Prerequisites:
  - structured design data complete
  - Stage 6 validation findings resolved/accepted with risk notes
- Process requirements:
  - derive prioritized build items from structured records
  - identify foundational/shared build items first
  - map each build item to milestone criteria and work-order acceptance checks
  - update/create work orders and advance at least one actionable acceptance criterion when not blocked
- Required outputs:
  - `DESIGN_ARTIFACT_ROOT/build/design-build-items.md`
  - `DESIGN_ARTIFACT_ROOT/build/design-to-workorder-traceability.md`
  - updates under `K2B_ARTIFACT_ROOT/workorders/`
- Gate:
  - every build item traces to validated IA/UX/UI evidence
  - work-order sequence is dependency-aware

6) Validation stage (`validate_only` or required at end of `full_pipeline`)
- Run K2B gate validator (baseline + strict):
  - `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT"`
  - `/Users/grig/.agents/scripts/validate-k2b-gates.sh "$PROJECT_SOURCE_ROOT" --artifact-root "$K2B_ARTIFACT_ROOT" --strict`
- If shell/runtime compatibility fails, rerun using explicit Bash 4+ and record runtime path.
- Persist strict log to:
  - `K2B_ARTIFACT_ROOT/reports/K2B-DESIGN-PIPELINE-STRICT-<YYYY-MM-DD-HH-MM-SS>.log`
- If `DESIGN_KIT_ROOT` is active, also run design-kit validation:
  - `"$DESIGN_KIT_ROOT/scripts/bash/validate-design-kit-run.sh" "$DESIGN_WORKSPACE"`
  - `"$DESIGN_KIT_ROOT/scripts/bash/validate-design-kit-run.sh" "$DESIGN_WORKSPACE" --full`
- Persist design-kit validation logs to:
  - `K2B_ARTIFACT_ROOT/reports/K2B-DESIGN-KIT-VALIDATION-<YYYY-MM-DD-HH-MM-SS>.log`
- Active Injection validation expectations when design-kit mode is active:
  - `00-active-design-rules.md` exists and is non-empty
  - no placeholder tokens remain in design workspace outputs
  - compliance sections exist across all five design phase docs
  - failures in these checks keep run in remediation mode

Mode dependency rules:
- `ia_only`: requires Stage -1/0 and Stage 1-4 readiness.
- `ux_only`: requires complete IA outputs.
- `ui_only`: requires complete IA + UX outputs.
- `structured_data_only`: requires complete IA + UX + UI outputs.
- `build_extraction_only`: requires structured design data + validation readiness.
- `validate_only`: may run anytime; must report missing prerequisites explicitly.
- If prerequisites are missing, stop and emit blocker details with exact remediation commands.

Mandatory run report:
- `K2B_ARTIFACT_ROOT/reports/K2B-IA-UX-UI-DESIGN-RUN-<YYYY-MM-DD-HH-MM-SS>.md`

Report must include:
- resolved roots and mode selection
- stages requested vs stages executed
- stage-by-stage gate outcomes
- validator commands, exit codes, and strict-log path
- when `DESIGN_KIT_ROOT` is active:
  - Active Injection command used
  - Active Rules payload path
  - design-kit validator command(s), exit code(s), and log path(s)
- files created/updated/reused
- traceability quality status (research -> IA -> UX -> UI -> structured data -> build item -> work order)
- work order resumed/created and acceptance criteria moved
- blockers and exact unblock requests
- exact next 3 executable shell commands

Command validity rule:
- Next 3 commands must be copy/paste runnable shell commands.
- Command 1 must start with `cd "$PROJECT_SOURCE_ROOT"` (or equivalent absolute `cd`).
- Bare filenames/paths are invalid and make the run incomplete.

Final chat response format:
- Resolved project source root
- Resolved K2B artifact root
- Resolved design artifact root
- Resolved design workspace
- Resolved design-kit root (or `not detected`)
- Selected design run mode
- Stages executed
- Validator baseline command and exit code
- Validator strict command and exit code
- Strict validator log path
- Design-kit validator command(s) and exit code(s) when applicable
- Files changed
- WO resumed/created and acceptance criteria moved
- Blockers
- Exact next 3 commands
