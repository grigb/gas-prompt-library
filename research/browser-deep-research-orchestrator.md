# Browser Deep Research Orchestrator

**Purpose**: Run deep research through logged-in browser UIs while keeping the human in control of authentication, provider selection, prompt submission, source scope, long-running waits, and final artifact storage.

Use this when the user wants the agent to open browser-based deep research tools such as ChatGPT/OpenAI, Gemini, Claude, Perplexity, Grok, or Kimi, wait for the user to confirm sign-in, submit a research brief, wait for completion, capture each provider's output, and save both raw and synthesized results.

Also use this when an agent identifies a material knowledge gap mid-task and browser-provider research is justified. The agent may generate and normalize the research prompt autonomously, but it must not open provider sessions or submit prompts until the human gate has approved the prompt, providers, source scope, and cost/quota assumptions.

---

## Activation

When the user asks for browser-controlled deep research or an agent identifies a gap that warrants signed-in provider research:

1. Read the current project's `AGENTS.md` first when available.
2. Identify the entry path:
   - `human_supplied_path`: the user supplied a prompt file.
   - `human_supplied_inline`: the user supplied prompt text in conversation.
   - `agent_generated_gap`: the agent hit a knowledge gap that affects the current task.
   - `agent_generated_review`: the agent is preparing browser research after reviewing prior work, research, or specs.
3. Confirm or generate the research topic, decision context, and target provider list.
4. Confirm the output directory. If the user does not provide one, use:
   `{PROJECT_ROOT}/.dev/ai/research/{YYYY-MM-DD}-{topic-slug}/`
5. Normalize every prompt source into `prompt.md` in that topic folder and record provenance in `.meta.md` and `browser-provider-status.md`.
6. Verify the signed-in provider route before opening provider pages: GAS
   `agent-browser` + Interaction Recipes + real Google Chrome at
   `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome` + canonical
   profile `/Users/grig/browser-auth/profiles/browser-research` + encrypted
   auth state under `/Users/grig/browser-auth/<provider>.json.enc`.
   Never ask for, store, paste, or infer credentials.
7. If no approval exists for provider submission, set the topic status to `queued_awaiting_owner_approval`, record provider statuses as `not_started`, write the next approval needed in `handoff.md`, and stop before opening provider sessions.
8. Open each requested provider only through the verified route, only after
   approval, and pause for the user to verify sign-in before submitting any
   prompt.

Do not run providers the user has not requested. Treat Grok and Kimi as later-stage providers unless the user explicitly asks to include them. If the user asks for Codex/OpenAI browser deep research, use ChatGPT Deep Research at `https://chatgpt.com/` by default and record the requested alias in `browser-provider-status.md`; do not use Codex web/cloud as the default deep-research target unless the user explicitly asks for a Codex work-agent workflow.

Autonomous gap entry rules:

- Use ordinary Deep Research when normal web/source research is sufficient.
- Use browser-provider research when signed-in provider research modes materially improve the decision, the user asked for provider comparison, or the work order explicitly requires this route.
- If the original task is blocked and no browser-run approval exists, create the normalized topic folder, set `status: queued_awaiting_owner_approval`, and report the approval needed.
- If the original task can continue, queue the browser research artifact without claiming the browser run will continue autonomously.
- Do not assume the owner supplied the prompt. Agent-generated prompts are first-class inputs to the same method.

This prompt follows GAS Deep Research Mode's mandatory directory contract:

```text
[research-topic]/
|-- .meta.md
|-- prompt.md
|-- browser-provider-status.md
|-- sources.md
|-- RESEARCH-SYNTHESIS.md
|-- handoff.md
|-- browser-runs/
|   `-- {run_id}/
|       |-- final-report.md
|       |-- result.md
|       `-- result.sidecar.json
`-- responses/
    |-- claude.md
    |-- perplexity.md
    |-- chatgpt.md
    |-- gemini.md
    |-- grok.md
    |-- kimi.md
    |-- chatgpt-browser-cli.md
    |-- gemini-browser-cli.md
    |-- claude-browser-cli.md
    `-- perplexity-browser-cli.md
```

Provider placeholder files such as `responses/chatgpt.md` are for human-supplied research. Agent-captured browser results must be saved to `responses/[provider]-browser-cli.md`.

## Artifact Naming Boundary

Use context-complete artifact names when writing status, handoffs, and worker
results:

- `Claude Research browser-step catalog` or `Claude Research Interaction
  Recipes step-catalog` means
  `/Users/grig/.agents/tools/interaction-recipes/interfaces/claude-research/catalog.json`.
- `Claude Deep Research provider recipe` means
  `/Users/grig/.agents/.dev/ai/deep-research/recipes/claude-research.md`.
- `Claude Browser Deep Research run packet` means one run directory under
  `/Users/grig/.agents/.dev/ai/deep-research/browser-runs/{run_id}/`.
- `final-report.md` is the captured provider report inside a run packet;
  `canonical response` means the normalized topic response under
  `responses/[provider]-browser-cli.md`.

---

## Prompt Source Normalization

Every entry path produces the same topic folder and the same canonical prompt file:

- Save the final clipboard-ready prompt as `prompt.md`.
- Record `prompt_source_type` in `.meta.md` using one of:
  - `human_supplied_path`
  - `human_supplied_inline`
  - `agent_generated_gap`
  - `agent_generated_review`
- Record prompt provenance where available:
  - source path,
  - source hash,
  - prompt author,
  - whether the prompt was edited,
  - approved provider list,
  - approved source scope.
- Mirror the relevant provenance in `browser-provider-status.md` and each run packet sidecar.

Minimum `.meta.md` fields:

```yaml
---
research_type: browser_provider_deep_research
gap: ""
impact: ""
created: YYYY-MM-DD
updated: YYYY-MM-DDTHH:MM:SSZ
status: queued_awaiting_owner_approval
prompt_source_type: agent_generated_gap
prompt_source_path: null
prompt_source_hash: null
prompt_author: agent
provider_plan:
  - claude
  - chatgpt
  - gemini
  - perplexity
provider_stage: staged_single_provider
source_scope: public_web_only
owner_approval:
  prompt_approved: false
  providers_approved: []
  private_sources_approved: []
  cost_or_quota_approved: false
browser_run_packets: []
canonical_responses: []
---
```

Topic status values:

- `pending`
- `queued_awaiting_owner_approval`
- `approved_not_started`
- `in_progress`
- `partially_complete`
- `complete`
- `blocked`
- `failed`

---

## Browser Control Route And Human Gates

For signed-in provider Deep Research, the primary browser route is **GAS
`agent-browser` through Interaction Recipes**, using:

- real Google Chrome at
  `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`;
- canonical GAS-managed profile
  `/Users/grig/browser-auth/profiles/browser-research`;
- encrypted provider auth state under
  `/Users/grig/browser-auth/<provider>.json.enc`;
- accessibility-tree/DOM controls as the primary executor path.

Before any provider-page launch, run the Interaction Recipes auth dry run or an
equivalent route check. The resolved browser must be real Google Chrome with
bundle id `com.google.Chrome`; if it resolves to Chrome for Testing, Brave, the
system default browser, generic Chromium, browser SaaS, or the owner's everyday
Chrome profile, stop before opening the provider and record
`browser_wrong_app_brave_or_default_route`.

Default `agent-browser open` can remain the right tool for public, local,
unauthenticated, un-fingerprinted browser automation. It is prohibited for this
signed-in provider Deep Research route, login flows, and bot-fingerprinting
provider/consumer sites. Codex Chrome Extension/browser-client and ad hoc CDP
routes are historical or explicitly owner-approved exception paths only, not the
primary authority. Record any exception reason in `browser-provider-status.md`.

Human-gate safety rules:

- Never ask for, store, paste, or infer credentials.
- Do not submit a prompt until the human has approved the exact prompt, provider list, source scope, and cost/quota assumptions.
- Pause for login, passkeys, 2FA, CAPTCHA, account selection, age gates, payment walls, terms prompts, workspace selection, extension prompts, bot challenges, entitlement checks, quota warnings, billing warnings, or private-source prompts.
- Do not enable private sources such as Gmail, Drive, Docs, Chat, NotebookLM, uploaded files, connected apps, workspaces, repositories, or private threads unless the user explicitly approves those sources for that provider run.
- Do not bypass access controls, provider safety systems, rate limits, paywalls, or sharing restrictions.
- Do not publish, share, export to a cloud document, or create a public provider page unless the user explicitly approves that artifact.

---

## Round-Robin And No-Duplicate Policy

When more than one approved prompt/provider cell exists, execute the matrix as
round-robin cells. Each cell is uniquely identified by:

`prompt_path + provider + prompt_hash`

Before opening or submitting a provider cell, check `browser-provider-status.md`
and any run packet sidecars for that exact key. Do not submit a duplicate cell
when the same `prompt_path + provider + prompt_hash` is already submitted,
running, completed, partial, blocked, failed, or parked. Duplicate provider
submission is allowed only when the owner explicitly approves a retry for that
exact cell. An approved retry must create a new `run_id` and record the retry
approval, reason, prior run id, and cell key.

If a cell becomes `blocked` or `failed`, park that cell instead of looping on it:

- Leave the provider browser tab open where safe and non-sensitive.
- If keeping the tab open would expose private history, account state, or
  sensitive content, close it and record why.
- Record the parked browser state in `browser-provider-status.md`, the run
  packet result, and the worker result file.
- Advance to the next approved round-robin cell.

One provider block does not halt other approved providers or prompts. Continue
with the next eligible cell unless the owner-approved matrix is exhausted or a
global gate affects every remaining cell.

Worker result files must identify the current cell, its status, the next
round-robin cell to attempt, and the parked browser state for any blocked or
failed cells.

---

## Staged And Promoted Provider Flows

### Staged Single-Provider Flow

Use this flow when a provider route, prompt class, capture adapter, account state, quota state, or research-mode behavior is not yet proven.

1. Select one prompt and one provider with explicit owner approval.
2. Calculate the cell key from `prompt_path + provider + prompt_hash` and verify
   no duplicate submission exists unless the owner explicitly approved a retry.
3. Create one provider run packet under `browser-runs/{run_id}/`.
4. Use the verified Interaction Recipes + GAS `agent-browser` route with real
   Google Chrome and `/Users/grig/browser-auth/profiles/browser-research`.
5. Verify research mode, source scope, and all human gates before submission.
6. Submit exactly once unless submission visibly fails.
7. Move provider state through:
   - `not_started`
   - `submitted`
   - `plan_review` or `clarification_questions` when applicable
   - `running`
   - `capture_ready`
   - `completed`, `partial`, `blocked`, or `failed`
8. Treat the run as complete only after verified local Markdown capture.
9. Normalize the verified capture into `responses/[provider]-browser-cli.md`.
10. Promote the provider for this prompt class only after submission, wait/revisit, completion detection, capture, source preservation, and redaction checks pass.

### Promoted Four-Provider Flow

Use this flow only after the same prompt class has passed provider gates for Claude, ChatGPT/OpenAI, Gemini, and Perplexity.

1. Confirm owner approval for four-provider execution.
2. Check provider status for quota, concurrency, subscription, cost, and active human gates.
3. Create one run packet per provider after verifying each
   `prompt_path + provider + prompt_hash` cell is unique or owner-approved for
   retry.
4. Run providers in parallel only when provider gates have passed, quota/concurrency allows it, owner approval covers the provider list and source scope, and an actual continuation/scheduling mechanism exists.
5. Normalize completed captures into:
   - `responses/claude-browser-cli.md`
   - `responses/chatgpt-browser-cli.md`
   - `responses/gemini-browser-cli.md`
   - `responses/perplexity-browser-cli.md`
6. Create or update `sources.md`, `RESEARCH-SYNTHESIS.md`, and `handoff.md`.

---

## Run Packet Normalization

Each provider attempt has an evidence packet under `browser-runs/{run_id}/`. The run packet is evidence; the canonical GAS research response is the normalized file under `responses/`.

Mapping:

- `browser-runs/{run_id}/final-report.md` -> `responses/chatgpt-browser-cli.md`
- `browser-runs/{run_id}/final-report.md` -> `responses/gemini-browser-cli.md`
- `browser-runs/{run_id}/final-report.md` -> `responses/claude-browser-cli.md`
- `browser-runs/{run_id}/final-report.md` -> `responses/perplexity-browser-cli.md`
- `browser-runs/{run_id}/final-report.md` -> `responses/grok-browser-cli.md` only when Grok is explicitly requested.
- `browser-runs/{run_id}/final-report.md` -> `responses/kimi-browser-cli.md` only when Kimi is explicitly requested.

After capture verification:

1. Write or copy the verified Markdown from `browser-runs/{run_id}/final-report.md` into the provider's canonical response file.
2. Add a short provenance header to the canonical response with provider, run id, run packet path, capture method, prompt hash, source scope, completion status, and capture limitations.
3. Add `canonical_response_path` to `browser-runs/{run_id}/result.sidecar.json`.
4. Record the canonical response path in `browser-provider-status.md`.
5. Use only `responses/[provider]-browser-cli.md` files for synthesis. Do not synthesize from screenshots or incomplete run-packet notes.

---

## Supported Providers

### Active Providers

- **ChatGPT/OpenAI**: `https://chatgpt.com/`
- **Gemini**: `https://gemini.google.com/`
- **Claude**: `https://claude.ai/`
- **Perplexity**: `https://www.perplexity.ai/`

### Later Providers

- **Grok**: `https://grok.com/` or the user's preferred Grok entrypoint.
- **Kimi**: `https://kimi.moonshot.cn/` or the user's preferred Kimi entrypoint.

For later providers, ask the user to confirm the correct URL and workflow before the first run.

---

## Required User Checkpoints

### Checkpoint 1: Research Setup

Before opening providers, ask for any missing essentials:

- Research topic or question.
- Intended decision this research should support.
- Prompt source type and provenance, unless already recorded.
- Provider list to run now.
- Staged single-provider run or promoted four-provider run.
- Output directory, if not using the default.
- Desired depth: quick scan, standard deep research, or exhaustive.
- Source scope, including any required source types, forbidden sources, date ranges, geography, private-source approvals, or output format.
- Cost, quota, subscription, and long-running wait assumptions.
- Whether human approval already exists for prompt submission.

### Checkpoint 2: Sign-In

For each provider:

1. Open the provider in the browser.
2. Ask the user to complete sign-in or confirm the session is already signed in.
3. Do not proceed until the user confirms: "signed in", "ready", or equivalent.
4. If there is CAPTCHA, 2FA, account selection, age gate, payment wall, extension prompt, or bot challenge, pause and ask the user to handle it manually.

### Checkpoint 3: Prompt Review

Before submitting the first provider prompt, show the exact research prompt that will be pasted. Ask the user to approve or revise it before any browser-provider submission. If the prompt was agent-generated, approval is still required.

### Checkpoint 4: Long-Running Waits

If a provider is still working after 20 minutes, tell the user the current visible status and ask whether to keep waiting, skip that provider, or continue later. Do not abandon a run silently.

---

## Provider Execution Loop

For each requested provider, perform this loop:

1. **Calculate** the round-robin cell key from `prompt_path + provider +
   prompt_hash` and verify it has not already been submitted unless the owner
   explicitly approved a retry.
2. **Create or update** a `browser-runs/{run_id}/` packet for this provider attempt.
3. **Verify approval** for prompt, provider, source scope, cost/quota, and any private sources.
4. **Open** the provider URL in the browser.
5. **Verify sign-in** with the user.
6. **Select research mode** if the UI offers one and confirm the selected source scope.
7. **Submit the research prompt** exactly once unless submission visibly fails.
8. **Wait for completion** using the provider-specific completion signals below.
9. **Capture raw output** into `browser-runs/{run_id}/final-report.md` using the best available method:
   - Provider copy/export button when available.
   - Browser text extraction when reliable.
   - Manual selection/copy when the user must intervene.
   - Screenshots only as fallback evidence, not as the primary result.
10. **Normalize raw output** into `responses/[provider]-browser-cli.md` with a provenance header.
11. **Log run metadata** including provider, URL, account context if visible without exposing private data, start time, end time, completion status, browser route, run packet path, canonical response path, capture method, visible limitations, cell key, next round-robin cell, and parked browser state when applicable.

Never enter private credentials. Never bypass access controls. Never attempt to defeat CAPTCHA, bot checks, paywalls, rate limits, or provider safety systems.

---

## Provider-Specific Instructions

### ChatGPT

1. Navigate to `https://chatgpt.com/`.
2. Confirm the user is signed in.
3. Start a clean new chat.
4. Select **Deep research** using the most stable available route:
   - Preferred: use the current Interaction Recipes ChatGPT catalog tools-menu path: open **Add files and more**, choose **Deep research**, and verify the non-editable Deep Research mode chip in the composer before prompt insertion.
   - Fallback: slow-type `/Deepresearch` into the composer and select the command only when the current catalog/recipe scopes that path and it exposes the same mode-chip verification.
   - Fallback: use the sidebar **Deep research** entry when it opens the deep-research composer.
5. Keep the first smoke run on public web only unless the user explicitly authorizes uploaded files, connected apps, or specific private sources.
6. Paste the approved research prompt.
7. Submit once.
8. If ChatGPT shows a research plan, clarifying question, source-access prompt, or plan approval step, capture it in `browser-provider-status.md` and proceed only if it stays within the approved scope.

Completion signals:

- The message has stopped streaming.
- Any "researching", "searching", "analyzing", or progress state is gone.
- The report is stable across two observations or a provider-visible completion state is present.
- Final answer, citations, sources, activity history, table of contents, download/export controls, or explicit source limitations are visible.

Preferred capture: official Markdown download. Fallback to provider copy/export, then scoped DOM/text extraction. Screenshots are supporting evidence only.

Save as: `responses/chatgpt-browser-cli.md`

Codex/OpenAI note: When the user says "Codex" in this browser deep-research context, treat it as the OpenAI/ChatGPT Deep Research surface unless the user explicitly requests Codex web/cloud. Save the run as `responses/chatgpt-browser-cli.md` and note `requested_alias: codex_openai` in status metadata.

### Gemini

1. Navigate to `https://gemini.google.com/`.
2. Confirm the user is signed in.
3. Start a clean chat.
4. Select **Deep Research** through the current Tools/Add files control.
5. Confirm `Google Search` is enabled and private sources such as Gmail, Drive, Docs, Chat, NotebookLM, uploaded files, and other connected Google Workspace sources are disabled unless the user explicitly authorized them.
6. Paste the approved research prompt.
7. Submit once and wait for Gemini's research plan.
8. Capture the plan in `browser-provider-status.md`; click **Start research** only if the plan is on-topic, allowed-source-only, and within the approved scope.

Completion signals:

- The UI is no longer showing planning, researching, searching, or writing progress.
- The final report is visible, usually through an **Open** or **View report** action and then the Canvas/report surface.
- The input area is usable again.
- Copy, export, share, or source controls are available, or Gemini explicitly reports it cannot complete.

Preferred capture: **Share and export** -> **Copy contents**, then preserve clipboard text/HTML when the browser adapter exposes both. Use **Export to Docs** only when the user explicitly authorizes creating a Drive artifact.

Save as: `responses/gemini-browser-cli.md`

### Claude

1. Navigate to `https://claude.ai/`.
2. Confirm the user is signed in.
3. Start a clean chat.
4. Ensure web search is available and enabled because Claude Research depends on it.
5. Enable the **Research** button or the user's preferred research mode. If the control is color-only, verify with a screenshot plus any accessible pressed/selected state.
6. Paste the approved research prompt. If Research is enabled but may not trigger, prepend a short instruction such as `Claude, please use the Research tool to...`.
7. Submit once.

Completion signals:

- The response has stopped streaming.
- Search/research activity indicators are gone.
- The composer is usable again.
- Final answer, citations, source references, or explicit research limitations are visible.
- A final response action such as **Copy** is visible, or two consecutive observations show stable final text.

Preferred capture: open/scope to the Claude Research Report artifact and use scoped DOM-to-Markdown extraction into `final-report.md`. Use final assistant-message **Copy** only as a fallback when it does not trigger browser clipboard permission prompts and does not strip the required report body, links, or citations; record any capture limitation.

Save as: `responses/claude-browser-cli.md`

### Perplexity

1. Navigate to `https://www.perplexity.ai/`.
2. Confirm the user is signed in.
3. Start a clean thread unless the user explicitly asks to use a Space.
4. Select Research mode through the current mode selector:
   - Preferred: open the **Search** mode popover and choose **Deep research** or **Research**.
   - Fallback: type `/` in an empty input and select **Deep research** or **Research** from the search-mode typeahead.
   - Fallback: use keyboard navigation only after a fresh snapshot confirms menu order.
5. Do not manually choose a model for Research mode unless a live authenticated retune proves Perplexity has changed that behavior.
6. Paste the approved research prompt.
7. Submit once.
8. If Perplexity asks clarifying questions before research starts, stop for user input unless the run policy already authorizes the answer.

Completion signals:

- Research progress, key findings, report file/editor updates, or source-reading indicators are no longer active.
- Final report text is visible in the thread or report file.
- Export, Copy, Source, Share, or equivalent final-answer controls are visible.
- Source links/citations or source metadata are visible or recoverable.
- Mode proof is captured when possible, such as final-answer Source metadata showing Research or Deep research.

Preferred capture: final report **Export** to Markdown. Fallback to DOCX converted locally to Markdown, PDF with citation-risk note, provider Copy, or scoped DOM extraction. Do not publish/share a private thread or create a public Perplexity Page unless the user explicitly authorizes sharing.

Save as: `responses/perplexity-browser-cli.md`

### Grok Later

Only run when explicitly requested.

1. Confirm the correct Grok URL with the user.
2. Confirm sign-in.
3. Use the closest available deep research, search, or reasoning mode.
4. Capture output and limitations.

Save as: `responses/grok-browser-cli.md`

### Kimi Later

Only run when explicitly requested.

1. Confirm the correct Kimi URL with the user.
2. Confirm sign-in.
3. Use the closest available deep research, search, or long-context research mode.
4. Capture output and limitations.

Save as: `responses/kimi-browser-cli.md`

---

## Research Prompt Template

Use this as the base prompt unless the user provides their own:

```markdown
# Deep Research Request

Research question:
[Insert the user's research question.]

Decision context:
[Explain what decision this research must support, who will use it, and what would make the result actionable.]

Scope:
- Include: [topics, products, organizations, methods, markets, papers, standards, or source classes]
- Exclude: [anything out of scope]
- Timeframe: [default: emphasize the last 12-24 months, with historical context when useful]
- Geography: [default: global]

Method:
- Search broadly before synthesizing.
- Prioritize primary sources, official documentation, peer-reviewed papers, standards, reputable technical writing, credible news, and direct evidence.
- Separate facts, interpretations, and speculation.
- Identify disagreement among sources.
- Note confidence levels and evidence gaps.
- Include source links or citations wherever the interface supports them.

Output:
- Executive summary.
- Key findings with evidence.
- Comparison or taxonomy where useful.
- Risks, trade-offs, and unknowns.
- Recommendations or next investigative steps.
- Source list with links.
```

---

## Output Files

Create these files in the output directory:

- `.meta.md`: Research metadata, tags, priority, status, provider list, and browser-run notes.
- `prompt.md`: Final approved prompt, clean and clipboard-ready.
- `browser-provider-status.md`: Per-provider status, timestamps, browser URL, capture method, and issues.
- `browser-runs/{run_id}/final-report.md`: Verified local Markdown capture for one provider attempt.
- `browser-runs/{run_id}/result.md`: Human-readable run evidence and outcome.
- `browser-runs/{run_id}/result.sidecar.json`: Machine-readable run evidence, including `canonical_response_path`.
- `responses/chatgpt-browser-cli.md`: ChatGPT raw browser-captured output, if run.
- `responses/gemini-browser-cli.md`: Gemini raw browser-captured output, if run.
- `responses/claude-browser-cli.md`: Claude raw browser-captured output, if run.
- `responses/perplexity-browser-cli.md`: Perplexity raw browser-captured output, if run.
- `responses/grok-browser-cli.md`: Grok raw browser-captured output, if run.
- `responses/kimi-browser-cli.md`: Kimi raw browser-captured output, if run.
- `sources.md`: Consolidated source list, deduplicated when possible.
- `RESEARCH-SYNTHESIS.md`: Cross-provider synthesis.
- `handoff.md`: Short summary of what was run, what completed, where files are, and what remains.

Every file path reported to the user must be absolute.

---

## Synthesis Requirements

After all requested provider runs complete or are explicitly skipped:

1. Read the raw outputs that were saved.
2. Create `RESEARCH-SYNTHESIS.md` with:
   - Executive summary.
   - Consensus findings.
   - Provider-specific unique findings.
   - Conflicts and disagreements.
   - Source quality notes.
   - Confidence levels.
   - Practical recommendations.
   - Remaining research gaps.
3. Create `sources.md` with:
   - Deduplicated source links.
   - Provider that surfaced each source.
   - Notes on source type and reliability.
4. Create `handoff.md` with:
   - Research topic.
   - Providers run.
   - Providers skipped or failed.
   - Absolute output directory path.
   - Next logical step.

---

## Failure Handling

If a provider cannot be used:

1. Record the blocker in `browser-provider-status.md`.
2. Capture a screenshot only if it helps the user understand the blocker.
3. Park the cell with the browser tab left open where safe, or record why it
   was closed.
4. Ask the user whether to retry, skip, or continue with other providers.
5. Unless the owner explicitly approves retrying that exact cell, advance to
   the next eligible round-robin cell.
6. Do not substitute a different provider without user approval.

If output capture fails:

1. Try provider copy/export controls.
2. Try browser text extraction.
3. Ask the user to manually copy the response into the chat or a file.
4. Record the capture limitation in `browser-provider-status.md`.
5. Park the capture-failed cell and continue with other approved cells unless a
   global gate affects the whole matrix.

If the browser session expires:

1. Pause.
2. Ask the user to sign in again.
3. Resume only after user confirmation.

---

## Completion Criteria

The research run is complete only when:

- `.meta.md` records `prompt_source_type`, owner approval state, provider stage, source scope, and topic status.
- `prompt.md` contains the canonical prompt regardless of human-supplied or agent-generated source.
- Each requested provider is marked `completed`, `skipped_by_user`, or `blocked`.
- Raw output is saved as `browser-runs/{run_id}/final-report.md` for every completed provider.
- Every completed provider has a normalized `responses/[provider]-browser-cli.md` file with provenance.
- Every completed provider sidecar records `canonical_response_path`.
- Every completed provider run packet passes
  `/Users/grig/.agents/.dev/ai/deep-research/bin/validate-run-packet.py`
  before completion/assimilation is claimed.
- `browser-provider-status.md` is updated.
- `browser-provider-status.md` and worker result files identify each
  `prompt_path + provider + prompt_hash` cell, duplicate-retry approvals if
  any, the next round-robin cell, and parked browser state for blocked or failed
  cells.
- `sources.md` exists, even if it only states that no sources were captured.
- `RESEARCH-SYNTHESIS.md` exists if at least one provider completed and uses canonical response files as inputs.
- `handoff.md` gives the user absolute paths and the next logical step.
