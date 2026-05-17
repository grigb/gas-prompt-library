Your task is to report ONLY blockers the current agent cannot resolve itself.

A blocker is any work that cannot move forward with the current agent's
available tools, permissions, context, and executable queue. This includes
items waiting on a user/owner, a specific time/date window, another project or
team, an external service, credentials/access, hardware availability, legal or
policy review, or a runtime/tool capability gap.

Do NOT limit the report to user-action blockers. Also do NOT report work that
is merely unstarted, low priority, deferred by planning choice, or waiting for
the current agent to dispatch/complete work it is capable of doing.

Do not summarize completed work.
Do not list all work orders.
Do not include internal implementation detail unless it is necessary to route
or unblock the item.
Do not compress blockers into cryptic one-line references.
Do not require the user to ask follow-up questions to understand the block.

Your output must be optimized for fast human routing and action.

## Delta Detection (Token Conservation)

Before running the full triage process, check whether this project's blocker
state has materially changed since the last scan. This avoids burning tokens
on a full re-scan when nothing moved.

**Step 1 — Read the existing INDEX.md:**
Check `{project_path}/.dev/ai/blockers/INDEX.md` for `last_scanned_at` and
the `totals` block (idle, claimed, in_progress, resolved, unresolvable counts).

**Step 2 — Quick-check for changes since last scan:**
Run a lightweight check for material changes:
```bash
# Files modified in blockers dir since last scan
find {project_path}/.dev/ai/blockers -name "*.md" -newer {project_path}/.dev/ai/blockers/INDEX.md 2>/dev/null | head -1
# WO status changes since last scan
find {project_path}/.dev/ai/workorders -name "*.md" -newer {project_path}/.dev/ai/blockers/INDEX.md 2>/dev/null | head -1
# Subtask-comms results since last scan
find {project_path}/.dev/ai/subtask-comms -name "*.md" -newer {project_path}/.dev/ai/blockers/INDEX.md 2>/dev/null | head -1
```

**Step 3 — Decide scan depth:**
- If NO files are newer than INDEX.md AND the agent has not completed any
  work since the last scan: run in **refresh-only mode**. Update only
  `last_scanned_at` in INDEX.md and PROJECT-STATUS.md. Print the existing
  blocker summary from INDEX.md without re-scanning. Emit the status seal.
  This costs ~200 tokens instead of ~5000+.
- If ANY files are newer, OR the agent completed work that may have resolved
  blockers, OR no INDEX.md exists: run the **full triage process** below.

Refresh-only mode MUST still:
- Update `last_scanned_at` in INDEX.md
- Update PROJECT-STATUS.md timestamp
- Print the human-readable summary (from existing INDEX data)
- Emit the status seal

Refresh-only mode MUST NOT:
- Skip the full process when INDEX.md does not exist (first scan)
- Skip the full process when the agent explicitly requests a full rescan
- Alter any blocker file status or content

## Output Mode

This prompt operates in TWO MODES:

- **catalog mode** (default when invoked under `agent-blocker-supervisor-cataloger.md`):
  Emit durable blocker files at `{project_path}/.dev/ai/blockers/{prefix}-{slug}.md`,
  update `{project_path}/.dev/ai/blockers/INDEX.md`, then print the human-readable summary.
- **print mode** (legacy, when user invokes directly without orchestrator):
  Skip file emission; print only the human-readable summary.

Detect mode via:

1. Environment variable `BLOCKER_TRIAGE_MODE=catalog` (set by cataloger), OR
2. User explicitly says "print only" / "no files" -> print mode.
3. Otherwise default to catalog mode.

Notes for catalog mode:

- Emit ALL discovered blockers as files (no 10-cap on file emission); the
  10-blocker cap below applies ONLY to the human-readable summary printed
  at the end of the run.
- Use absolute paths in every emitted file (front-matter `project_path`,
  any embedded references, and the closing "Files written/updated" block).
- Use `printf` rather than `echo` for any human-readable output an executing
  agent prints to terminal.

## Catalog Emission Rules (catalog mode only)

For each blocker you would have reported, perform the following deterministic
steps. The schema source-of-truth is
`~/.agents/docs/specs/blocker-file-schema.md`; the file template is
`~/.agents/templates/BLOCKER-TEMPLATE.md`; the per-project index
spec is
`~/.agents/docs/specs/blocker-project-index-format.md` (template:
`~/.agents/templates/BLOCKER-PROJECT-INDEX-TEMPLATE.md`).

1. **Compute signature.**
   `signature = sha1(project_path + ":" + category + ":" + normalized(user_action_required))`
   where `normalized(s)` lowercases `s`, collapses any run of whitespace to a
   single space, and strips trailing punctuation (`.`, `,`, `;`, `:`, `!`, `?`).

2. **Look up existing files by signature.**
   Scan `{project_path}/.dev/ai/blockers/` for any existing blocker file whose
   front-matter resolves to the same signature (recompute on the fly from the
   existing file's `project_path`, `category`, and `user_action_required`).

3. **If a non-terminal match is found** (`status` in `{idle, claimed, in_progress}`):
   UPDATE the existing file in place. Refresh `last_seen_at` and `updated_at`
   (and any body fields that have legitimately changed). DO NOT change `id`,
   `status`, `claimed_by`, `claimed_at`, `attempts`, or `attempts_count`.

4. **If no match is found** (or only terminal matches `resolved` /
   `unresolvable` / `stale` exist — recurrence creates a NEW file with a NEW id):
   CREATE a new file using the template at
   `~/.agents/templates/BLOCKER-TEMPLATE.md`. Filename:
   `{prefix}-{slug}.md` where `{prefix}` is the value emitted by
   `~/.agents/scripts/get-filename-prefix.sh` at file-creation time and
   `{slug}` is the kebab-case slug derived from the blocker's short name,
   truncated to 60 characters (cut at the last hyphen at or before char 60
   if possible). The front-matter `id` is `BLK-{prefix}-{slug}` and reuses
   the same `{prefix}` and `{slug}` as the filename.

5. **Touch every blocker observed this scan.**
   For every file you saw or wrote during this scan, set `last_seen_at` to
   the scan timestamp. Files NOT seen this scan: do NOT delete; do NOT alter
   their `status`. The cataloger handles staleness in a later pass per
   WO-BLK-005.

6. **Regenerate the per-project index.**
   After all blockers are processed, regenerate
   `{project_path}/.dev/ai/blockers/INDEX.md` per the
   `BLOCKER-PROJECT-INDEX-TEMPLATE` (front matter `type:
   blocker-project-index`, totals computed from the scan, sections rendered
   only when non-empty, no markdown tables). Always write this file even
   when no blockers exist (empty totals + refreshed `last_scanned_at`) so
   "never scanned" is distinguishable from "scanned, no blockers".

### V1 default values (must be present, even when empty)

Every emitted file MUST include the V2-placeholder fields with their V1
defaults so future populators (linker WO-BLK-012, recurrence detector
WO-BLK-013) can round-trip without a schema migration:

- `dependency_hints: []`
- `depends_on_blockers: []`
- `depended_on_by: []`
- `depended_on_by_count: 0`
- `possible_recurrence_of: null`
- `recurrence_confidence: null`

### Provenance and handoff-target fields (must be present on new blockers)

Every NEW blocker file MUST also include the WO-BLK-035 provenance and
handoff-target fields from `~/.agents/docs/specs/blocker-file-schema.md`.
These fields solve the routing problem where the blocker file physically lives
under one project but the unblock message belongs to a different waiting agent
or work order.

Populate them as follows:

- `agent_task_id`: if the triage request came from a handoff/session/subtask
  that has `agent_task_id`, reuse it. If no incoming chain exists, generate a
  new ID once with `~/.agents/scripts/get-agent-task-id.sh blocker` and reuse it
  for every blocker emitted from this triage invocation.
- `source_artifact_type`, `source_artifact_id`, `source_artifact_path`: record
  the durable source artifact when known. Supported types are `handoff`,
  `subtask-comms`, `workorder`, `session`, `chat`, `unknown`, or `null`.
- `origin_project_path`: the absolute project/workspace root where the creating
  agent believed it was working when it discovered the blocker. If the
  cataloged project is also the origin, set this to `project_path` rather than
  leaving it ambiguous.
- `origin_cwd`: the absolute current working directory of the creating agent
  when known.
- `handoff_target_project`: the project/workstream name the user or supervisor
  should notify when this blocker resolves. If the receiver is the same as the
  cataloged project, write that explicitly.
- `handoff_target_project_path`: the absolute `/Users/...` path of the
  project/agent context that should receive the unblock message. This is the
  critical field for preventing Social/STC/LAN-style routing confusion.
- `handoff_target_work_order_id`: the exact work order expected to resume when
  this blocker resolves, if known. Prefer the most specific WO from
  `related_work`.
- `handoff_target_agent_role`: the target lane or agent role when known
  (for example, `LAN project agent`, `Save The Creators site agent`, or
  `Social Module orchestrator`).
- `handoff_target_notes`: a short disambiguation note when labels or paths are
  likely to confuse a human.
- `handoff_targets`: optional list of target objects for multi-agent
  notification. Use this when one blocker unlocks multiple waiting agents. Each
  object may include `project`, `project_path`, `work_order_id`, `agent_role`,
  and `notes`. When present, make the flat `handoff_target_*` fields summarize
  the first/primary target.

If environment variables are supplied by the cataloger/orchestrator, prefer
them over inference:

- `BLOCKER_AGENT_TASK_ID`
- `BLOCKER_SOURCE_ARTIFACT_TYPE`
- `BLOCKER_SOURCE_ARTIFACT_ID`
- `BLOCKER_SOURCE_ARTIFACT_PATH`
- `BLOCKER_ORIGIN_PROJECT_PATH`
- `BLOCKER_ORIGIN_CWD`
- `BLOCKER_HANDOFF_TARGET_PROJECT`
- `BLOCKER_HANDOFF_TARGET_PROJECT_PATH`
- `BLOCKER_HANDOFF_TARGET_WORK_ORDER_ID`
- `BLOCKER_HANDOFF_TARGET_AGENT_ROLE`
- `BLOCKER_HANDOFF_TARGET_NOTES`

Do NOT infer a handoff target from brand shorthand alone. If a label like
`STC`, `LAN`, `payments`, `auth`, or `Social Module` could refer to more than
one project/thread, either write the exact target path or set
`handoff_target_notes` to say the target is ambiguous. A blocker with an
ambiguous receiver is not ready for a human-facing unblock handoff until the
receiver is disambiguated.

### Owner / routing action summary (required on new blockers when useful context exists)

Every NEW blocker file MUST include the optional front-matter field
`owner_action_summary` with one or two human-readable sentences for the owner.
This is the field the dashboard shows before raw `user_action_required` or
`unresolvable_reason`, so write it for fast human routing and action.

The summary MUST answer:

1. What is blocked.
2. What non-agent condition must change: owner decision/input, external-team
   delivery, scheduled time, service/dashboard action, credential/access,
   hardware availability, policy/legal review, or runtime/tool capability.
3. Where the responsible person/system should act, only when a path, URL, or
   artifact is essential.

The summary MUST NOT be only an absolute path, raw `requires_*` code, a copied
`unresolvable_reason`, or a cryptic blocker ID. Good summaries are specific
without forcing the owner to open another file just to understand the ask.

When updating an existing non-terminal blocker, preserve any existing
non-empty `owner_action_summary` unless the currently observed source artifact
clearly supersedes it. If the existing blocker lacks the field and the current
scan has enough context to write a useful summary, add it. Existing blockers
without this field remain valid.

### `dependency_hints` population guidance

When the unblock-condition description hints at an upstream blocker that itself
needs to be resolved first (for example: "waiting on auth-service SSO",
"depends on Cloudflare DNS provisioning", "blocked by upstream payment-gateway
migration"), append a short natural-language string capturing the hint to
`dependency_hints` in the emitted front matter. Keep each hint concise and
human-readable. The hint is NOT a concrete blocker ID — that is the linker's
job in WO-BLK-012. If no upstream hint is present, leave the list empty
(`dependency_hints: []`). Do NOT invent dependencies you cannot ground in
the unblock-condition text.

This rule applies WITH PARTICULAR FORCE to **cross-project dependencies**:
when the blocker is gated on work happening in a different project (e.g.,
the current project waits on `auth-service` to ship SSO support, or on
`ingestion-pipeline` to expose a new parquet output, or on a `billing-api`
team to publish a webhook secrets endpoint), the prompt MUST populate
`dependency_hints` with one short natural-language string per distinct
upstream dependency. Each hint MUST include:

1. The **target project name** (or the best guess at it — the linker is
   tolerant of fuzzy keyword matches) so the V1 linker heuristic can score
   project-name overlaps heavily (`+3` per token match per WO-BLK-012
   §11.3).
2. The **capability being awaited** (e.g., "SSO support", "parquet output",
   "webhook secrets endpoint") so the linker can score on tag/category/
   unblock-condition keyword overlap as a secondary signal.

Do NOT attempt to resolve a cross-project hint to a concrete blocker ID
yourself; the prompt has no read access to other projects' blocker
catalogs and any guess would be unsafe. Leaving the resolution to the
linker is the correct division of labor: the triage prompt produces
high-recall natural-language hints; the linker produces high-precision
edges by scoring across the global catalog.

One hint per distinct upstream dependency. If a single unblock-condition text
implies two cross-project dependencies (e.g., "blocked by auth-service
SSO AND by billing-api webhook secrets"), emit TWO hint strings. If the
text only implies one upstream concern with multiple sub-aspects, emit
ONE hint that captures the concern in plain language. The cataloger's
linker phase will dedup downstream.

### Idempotency rule (explicit)

Re-running this prompt against the same project with the same blockers MUST
produce zero new files. Only `last_seen_at` and `updated_at` should change
on existing files (and only if the scan timestamp differs). The signature
is the dedup key. Recurrence of a previously-resolved (terminal) blocker
is the one exception: it intentionally creates a NEW file with a NEW id,
because `resolved` / `unresolvable` are terminal per the schema lifecycle.

### Incremental signature matching (token conservation)

When running a full scan (not refresh-only), skip signature recomputation
for existing blocker files whose modification time is OLDER than the last
scan timestamp in INDEX.md. These files have not changed and their
signatures are stable. Only compute signatures for:
- Newly discovered blockers (no existing file)
- Existing blocker files modified since the last scan
- Blockers whose source artifacts (WOs, subtask-comms) are newer than
  the blocker file itself

This avoids reading and hashing every blocker file on every scan when most
are unchanged.

## Workstream-aware emission (catalog mode only)

This section is ADDITIVE to the Catalog Emission Rules above. It was added
by WO-BLK-017 to retrofit the prompt for the workstream extension shipped
in WO-BLK-014. The schema source-of-truth is
`~/.agents/docs/specs/blocker-file-schema.md` §10.3. All rules
above remain in force; the rules below refine HOW the emitter populates
two specific fields and HOW the dedup signature is computed when a project
has multiple workstreams declared.

A "workstream" is a named subset of a project's scope, declared in
`~/.agents/agents/blocker-engineer/projects.yaml` under the
project's optional `workstreams` list. Each workstream has a `name` and
an ordered `roots` list of absolute paths. When `workstreams` is absent
from a project entry, the project has exactly one implicit workstream
named `default` whose `roots` is `[project_path]` — the prompt MUST emit
`workstream: null` in that case (the schema treats `null` and `"default"`
as equivalent).

### How to read the workstream registry (do NOT parse YAML directly)

When determining the active workstream context for a project, the prompt
MUST shell out to `~/.agents/scripts/blocker-projects.sh` and
use its `workstream-list` subcommand rather than parsing
`projects.yaml` inline. This avoids duplicating yaml-parsing logic and
keeps the workstream registry's interpretation in a single place. Example
invocation (illustrative; an executing agent would run this via shell):

```
~/.agents/scripts/blocker-projects.sh workstream-list ~/.agents
```

If the command lists no workstreams (exit 0, empty output), treat the
project as implicit-default: `workstream: null`, `external_dirs: []`,
`roots: [project_path]`. If the command lists one or more workstreams,
match the work-in-progress files against each workstream's `roots` to
pick the active workstream (see "Matching" below).

When emitting human-readable output that references workstream lookups,
use `printf` rather than `echo` per the catalog-mode output rules above.

### Rule W1 — Populate `workstream`

For every blocker file the prompt creates or updates in catalog mode:

- If the project has NO `workstreams` declared in `projects.yaml`
  (the `workstream-list` subcommand returns no entries), emit
  `workstream: null` in the front matter. Do NOT invent a workstream
  name; the implicit-default convention is `null`, not `"default"`.
- If the project has one or more declared `workstreams`, emit the
  matching workstream's `name` as a string, chosen by inspecting where
  the work-in-progress files (the files the blocker is grounded in,
  including `where_to_act` paths and any source files referenced in
  the unblock-condition description) live relative to each workstream's
  `roots` list. Use longest-common-prefix matching against `roots[0]`
  to break ties when multiple workstreams' `roots` overlap, identical
  to the cataloger's tie-breaking rule in §10.4.
- The `workstream` field is set ONCE at first emission and is treated
  as immutable on subsequent passes (the cataloger preserves it). If
  the prompt is updating a previously-emitted blocker file whose
  `workstream` is already non-null, leave it untouched.

### Rule W2 — Populate `external_dirs`

For every blocker file the prompt creates or updates in catalog mode:

- Collect the absolute paths the blocker references that fall OUTSIDE
  `project_path` but INSIDE one of the matched workstream's `roots`.
- Emit those paths (deduplicated, sorted lexicographically) as the
  `external_dirs` list in the front matter.
- NEVER include `project_path` itself in `external_dirs`. The schema
  forbids it (§7 rule 10) and consumers will reject the file.
- If no such paths exist, emit `external_dirs: []`.
- On updates, treat `external_dirs` as additive: do NOT remove a
  previously-recorded external dir unless the workstream itself was
  removed from `projects.yaml` (in which case the cataloger handles
  cleanup; the prompt's job is to NOT shrink the list).

### Rule W3 — Workstream-aware dedup signature

The V1 signature defined in the Catalog Emission Rules section above
remains the baseline for any blocker file whose `workstream` is `null`
(implicit-default). When the prompt emits a non-null `workstream`, the
signature is REFINED to include workstream context so the same blocker
observed in two workstreams of the same project produces TWO separate
blocker files (different signatures by virtue of different workstream
context).

- **V1 form (preserved for implicit-default projects):**

  `signature = sha1(project_path + ":" + category + ":" + normalized(user_action_required))`

- **V2 form (supersedes V1 once `workstream` is populated):**

  `signature = sha1(project_path + ":" + (workstream or "default") + ":" + category + ":" + normalized(user_action_required))`

V2 supersedes V1 only for blockers whose project declares `workstreams`
in `projects.yaml`. For implicit-default projects, the V2 form reduces
to `sha1(project_path + ":" + "default" + ":" + category + ":" + normalized(user_action_required))`,
which is intentionally distinct from the V1 hash. Implementations MAY
compute both forms when scanning legacy files for dedup matches, and
MUST prefer the V2 form on write. The `normalized(s)` function is
unchanged from the V1 definition.

When generating `where_to_act` hints in catalog mode, the prompt MUST
treat the workstream's full `roots` set as in-scope. A blocker whose
resolution requires touching `~/.agents-projects/foo/...`
under workstream `gas-runtime` (whose `roots` include
`~/.agents-projects`) is in-scope; do NOT downgrade the
`where_to_act` to a project-root-only path or refuse to emit it.

### Cross-workstream dependency hints (refinement of `dependency_hints`)

The `dependency_hints` population guidance above remains in force. As
an additive refinement: when the unblock-condition description hints at a
blocker that lives in ANOTHER workstream of the SAME project (for
example: "waiting on the gas-runtime workstream's PSE deploy") the
prompt MUST still record the hint as free-text — workstream-aware
dependency resolution is the linker's job (WO-BLK-012), not the
triage prompt's. Do NOT attempt to resolve the cross-workstream
reference into a concrete blocker ID; do NOT short-circuit to
`depends_on_blockers`. Append the natural-language hint to
`dependency_hints` exactly as the unblock-condition text describes it.

### Worked example

Project: `~/.agents` with one declared workstream `gas-runtime`
whose `roots` are
`[~/.agents, ~/.agents-projects]` (per the
`projects.yaml` shape in §9.1 of the schema spec). A blocker observed
during triage references files under
`~/.agents-projects/foo/...`.

The prompt MUST emit:

- `workstream: gas-runtime`
- `external_dirs:` containing the relevant absolute paths under
  `~/.agents-projects/foo/...` (e.g.,
  `[~/.agents-projects/foo/cmd/server]`), deduplicated and
  sorted lexicographically.
- A V2-form signature that incorporates the workstream:
  `sha1("~/.agents:gas-runtime:" + category + ":" + normalized(user_action_required))`.

The same logical blocker observed under a different workstream of the
same project (e.g., `blocker-engineer` whose `roots` is just
`[~/.agents]`) produces a SEPARATE blocker file because the
signature differs.

For an implicit-default project (no `workstreams` declared), the prompt
emits `workstream: null`, `external_dirs: []`, and uses the V1 signature
form unchanged.

## Objective

Produce a short, decision-ready blocker report that tells the user:

1. What is blocked.
2. Why it is blocked.
3. Who or what must change the condition.
4. Where the responsible person/system must act, if applicable.
5. What decision, delivery, access, time window, or external event is needed.
6. Which option you recommend.
7. What becomes unblocked after the condition clears.

## Output Rules

- Include ONLY currently blocked items.
- Exclude anything you can resolve yourself.
- Exclude anything that is merely low-confidence but not blocked.
- Exclude anything that is merely waiting for your own dispatched background
  agents or for work you can dispatch yourself.
- Merge duplicate blockers that require the same unblock condition.
- Group related blockers under one item when one unblock condition unblocks
  multiple tasks.
- Use plain language.
- Avoid work-order IDs unless they are necessary for traceability.
- If including IDs, place them at the end under `Related work`.
- Prioritize blockers by user leverage: highest unblock value first.
- Maximum output: 10 blockers.
- If there are more than 10 blockers, show the top 10 and include a final line: `Additional blocked items: N`.
- Note (catalog mode, added by WO-BLK-004): the 10-blocker cap above applies ONLY to the human-readable summary printed at the end. In catalog mode, ALL discovered blockers are still emitted as durable files under `{project_path}/.dev/ai/blockers/` and counted in the per-project `INDEX.md` totals. The cap is a display rule for the summary, not a discovery cap.

## Blocker Categories

Classify each blocker as exactly one of:

- `Approval needed`
- `User decision needed`
- `Account/login needed`
- `External service action needed`
- `Credential/API key needed`
- `Payment/billing needed`
- `File/input needed`
- `Policy/legal decision needed`
- `Architecture/product decision needed`
- `Manual verification needed`
- `External project/team dependency`
- `Time/date window needed`
- `Runtime/tool capability needed`
- `Unknown blocker`

## Required Format

Use this exact format for every blocked item:

### [Priority #] [Short blocker name]

**Category:**  
[One category from the list]

**Blocked because:**  
[One or two plain-language sentences explaining the actual blocker.]

**Unblock condition:**  
[The concrete condition that must change. If a user/owner must act, state the
action. If not, state the responsible external project/team/service, time
window, hardware/access condition, or runtime/tool capability gap.]

**Where to act:**  
[Link, file path, dashboard, website, repo, document, or “Not applicable.”]

**Decision / delivery needed:**  
[The exact decision, approval, credential, login, file, confirmation, external
delivery, time/date arrival, hardware availability, or runtime capability
needed.]

**Recommended choice:**  
[Your best recommendation, with a brief reason. If no recommendation is possible, say “No recommendation; user-specific judgment required.”]

**Unblocks:**  
[What work can continue once this condition clears.]

**Related work:**  
[Only include work-order IDs, issue numbers, PRs, branches, files, or tickets if useful. Otherwise write “Not needed.”]

---

## If There Are No Blockers

Respond only with:

`No unresolved blockers remain.`

## Quality Bar

Before responding, verify that each blocker is understandable by a user who has not read the work-order history.

Each blocker must answer:

- What is the actual obstacle?
- What exact condition must change, and who/what controls it?
- Where does the responsible person/system act, if applicable?
- What happens after the condition clears?

If any blocker fails that test, rewrite it before responding.

## Owner-Facing Clarity Requirements

Every blocker surfaced to the owner in the human-readable summary MUST include all four:

1. **Plain-language situation** (2-3 sentences). No blocker IDs, schema jargon, or unexpanded acronyms as the primary explanation. A non-technical reader must understand on first read.
2. **Action type** (exactly one of): `verbal approval`, `choose between options`, `provide information`, `do something external`, `delegate to someone`, `external dependency`, `wait for scheduled time`, `runtime/tool capability gap`, `no owner action available`.
3. **Exact ask or condition**. Copy-pasteable when user/owner action exists:
   an approval sentence the owner can reply with, lettered choices with
   one-line consequences, the specific question to answer, the URL and steps to
   follow, who to contact and what to tell them, or the external/time/runtime
   condition that must clear when no owner action exists.
4. **What this unblocks** (one sentence). State impact in terms the owner cares about — project progress, user-facing capability, deadline — not blocker IDs or internal queue state.

Map these to the Required Format fields: situation goes in `Blocked because`,
action type goes in `Category` context or `Decision / delivery needed`, exact
ask or condition goes in `Unblock condition` and `Decision / delivery needed`,
unblock impact goes in `Unblocks`.

## Deferred WO Awareness

During triage, scan the project's WO index (typically `{project_path}/.dev/ai/workorders/WO-INDEX.md` or `INDEX.yaml`) for entries with status `BLOCKED` or `DEFERRED`. For each, check whether the stated blocker condition has been resolved (e.g., a credential was provided, an upstream dependency shipped, an approval was given). If a previously-blocked WO is now unblockable, surface it in the human-readable summary as an informational item:

```
### Newly unblocked: [WO-ID] [short name]
Previously blocked by: [original reason]
Now actionable because: [what changed]
```

This is informational, not a blocker. Place it AFTER the blocker list, BEFORE "Files written/updated". If the project has no WO index or no BLOCKED/DEFERRED entries, skip silently.

## Files written/updated (catalog mode only)

After the human-readable summary above, append a closing block listing the
absolute paths of every file written or updated during this scan. Use this
exact heading and bullet-list shape (no markdown tables):

```
## Files written/updated

- ~/.../<project>/.dev/ai/blockers/INDEX.md
- ~/.../<project>/.dev/ai/blockers/{prefix}-{slug-1}.md
- ~/.../<project>/.dev/ai/blockers/{prefix}-{slug-2}.md
```

Rules for this block:

- Every path MUST be absolute (start with `/Users/`).
- Include the project's `INDEX.md` even if its totals did not change (the
  cataloger contract requires `last_scanned_at` to be refreshed every scan).
- Include every blocker file CREATED or UPDATED during the scan.
- Do NOT include files that were merely read but not written.
- Omit this entire block when running in print mode.
- If no files were written (catalog mode, no blockers, only INDEX.md
  refreshed), still list `INDEX.md` so callers can confirm the scan ran.

### Unblock file emission (catalog mode only)

When blockers are resolved during a triage run (status changed to `resolved`), write ONE bundled unblock file per affected project to `{project_path}/.dev/ai/unblocks/{prefix}-{slug}.md` where `{prefix}` comes from `~/.agents/scripts/get-filename-prefix.sh`. The file must be brief (3-8 sentences, no headers, no YAML front matter) and state: what was blocked, what resolved it, and what work can now resume. Bundle multiple resolved blockers for the same project into a single file.

This is the primary delivery mechanism. When the owner says "unblocked" to a
project orchestrator, the orchestrator reads the newest file in
`{project_path}/.dev/ai/unblocks/` to know what changed and what to do next.
The owner does NOT need to paste any text — just the word "unblocked" is enough.
Include unblock files in the "Files written/updated" list.

### Optional post-emission view refresh (catalog mode only)

After the closing "Files written/updated" block has been printed, an
OPTIONAL final step refreshes this project's `INDEX.md` and the master
`MASTER-INDEX.md` from the canonical files just emitted, so direct
triage runs (invoked outside the cataloger) keep the cross-project
master fresh:

```
if [ -x ~/.agents/scripts/blocker-views-refresh.py ] || [ -f ~/.agents/scripts/blocker-views-refresh.py ]; then
    python3 ~/.agents/scripts/blocker-views-refresh.py --project "<project_path>"
fi
```

Substitute `<project_path>` with the absolute project root passed in via
`PROJECT_PATH` (the same value used elsewhere in this prompt). Rules
for this hook:

- The hook is OPTIONAL with explicit graceful fallback. If
  `~/.agents/scripts/blocker-views-refresh.py` does NOT exist on disk
  (e.g. during early WO-BLK-027 rollout where this prompt landed before
  the script), skip the invocation silently. The cataloger or the user
  will refresh views later; this prompt MUST NOT abort or fail when the
  script is absent.
- If the script exists and returns exit code 0, proceed silently.
- If the script exists and returns a non-zero exit code, print a single
  one-line warning of the form
  `view refresh failed (exit {code}); INDEX and master may be stale until next cataloger run`
  via `printf` (never `echo`) and proceed.
- This hook is catalog-mode only. Print mode MUST NOT invoke it. The
  hook fires AFTER the "Files written/updated" block has been emitted
  in full so callers always see the canonical file list before the
  refresh runs.
- The hook is additive — it does not replace any existing emission step
  in this prompt. Bundle creation, signature dedup, and `INDEX.md`
  authoring all run unchanged before the hook fires.

## PROJECT-STATUS.md Maintenance (MANDATORY)

Every triage run MUST update the project's status file at
`{project_path}/.dev/ai/PROJECT-STATUS.md`. This file gives the supervisor a
single-line answer to "is this project blocked?" without parsing blocker indexes.

### At triage START, write:

```
status: working
updated: <ISO timestamp>
agent: blocker-triage

## Active Work
- Blocker triage scan in progress
```

### At triage END, write one of:

**If blockers exist AND open/dispatchable WOs exist:**
```
status: blocked
updated: <ISO timestamp>
agent: blocker-triage

## Blocked Items (priority order)
1. <short blocker name> — <plain-language reason>
2. <short blocker name> — <plain-language reason>

## Dispatchable Now
- <WO-ID> <short name> — can proceed despite other blockers
- <WO-ID> <short name> — partial lane, unblocked

## Completed This Session
- Blocker triage scan completed, <N> blockers cataloged
```

**If blockers exist but some work can still proceed (partial lanes):**
Use `status: blocked` but ALWAYS include the `## Dispatchable Now` section
listing WOs that are NOT gated by any active blocker. The supervisor reads this
section to know which lanes to wake. A project with 5 blockers and 3
dispatchable WOs is partially unblocked — those 3 WOs represent real work
that an agent can do right now.

**If no blockers AND open/dispatchable WOs exist:**
```
status: working
updated: <ISO timestamp>
agent: blocker-triage

## Dispatchable Now
- <WO-ID> <short name>
- <WO-ID> <short name>

## Completed This Session
- No blockers found — project is clear, <N> WOs ready
```

**If no blockers AND no open/dispatchable WOs (queue is empty):**
```
status: parked
updated: <ISO timestamp>
agent: blocker-triage

## Queue Empty
- No active blockers and no open work orders
- Deferred items: <N> (future-posture/hardening only)
- Next activation: when new WOs are created or deferred items are promoted

## Completed This Session
- Blocker triage scan completed, queue empty
```

The `parked` status tells the supervisor: do NOT recommend waking this agent.
There is nothing for it to do. The supervisor must not waste the owner's time
sending relay text to a parked project.

Write atomically: write to a temp file in the same directory, then `mv` to the
final path. Never delete this file — only overwrite with new state. Line 1 is
always `status: working` or `status: blocked` so `head -1` gives the answer.

## End-of-Run Protocol

After all blocker discovery, emission, and view refresh steps are complete, perform these closing steps in order:

1. **Update blocker INDEX files.** Ensure `{project_path}/.dev/ai/blockers/INDEX.md` reflects the current scan (already handled by catalog emission rules above).
2. **Write unblock files.** For any blockers resolved during this run, emit unblock files per the "Unblock file emission" section above.
3. **Surface newly-unblocked WOs.** Per the "Deferred WO Awareness" section above, report any BLOCKED/DEFERRED WOs whose conditions are now met.
4. **Emit the status seal.** End your final output with the status seal per the section below.

## Turn-Ending Status Seal (MANDATORY)

Every triage run MUST end with exactly one of these two lines as the final output. No text, bullets, or whitespace may appear after it.

```
I am unblocked.
```

```
I am blocked.
```

**Semantics:**

- **`I am unblocked.`** = open WOs exist and are dispatchable. Background agents
  are running, more work to launch, or work is in progress. The user does NOT
  need to act. This includes partial lanes: if some WOs are blocked but others
  can proceed, the agent is unblocked for those lanes.
- **`I am blocked.`** = unresolved blockers remain that the current agent cannot
  clear itself AND no dispatchable WOs exist. Every open WO is gated.
- **`I am parked.`** = no active blockers AND no open/dispatchable WOs. The queue
  is empty. Nothing to do until new work is created or deferred items are
  promoted. The supervisor must NOT recommend waking this agent.

**Key distinctions:**

- Waiting on your OWN dispatched background agents = `I am unblocked.`
- Waiting on a DIFFERENT project's agent/team/service to deliver work = `I am blocked.`
- All blockers resolved, no remaining work gated on a non-agent condition = `I am unblocked.`
- Active blockers remain that the current agent cannot resolve = `I am blocked.`
- No blockers AND no open WOs = `I am parked.`
- Blockers exist but some WOs are NOT gated = `I am unblocked.` (partial lanes)
