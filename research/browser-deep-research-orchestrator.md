# Browser Deep Research Orchestrator

**Purpose**: Run deep research through logged-in browser UIs while keeping the human in control of authentication, provider selection, long-running waits, and final artifact storage.

Use this when the user wants the agent to open browser-based deep research tools such as ChatGPT/OpenAI, Gemini, Claude, Perplexity, Grok, or Kimi, wait for the user to confirm sign-in, submit a research brief, wait for completion, capture each provider's output, and save both raw and synthesized results.

---

## Activation

When the user asks for browser-controlled deep research:

1. Read the current project's `AGENTS.md` first when available.
2. Confirm the research topic, decision context, and target provider list.
3. Confirm the output directory. If the user does not provide one, use:
   `{PROJECT_ROOT}/.dev/ai/research/{YYYY-MM-DD}-{topic-slug}/`
4. Prefer a browser automation path that can use the user's real signed-in browser profile. Never ask for, store, paste, or infer credentials.
5. Open each requested provider in a browser tab and pause for the user to verify sign-in before submitting any prompt.

Do not run providers the user has not requested. Treat Grok and Kimi as later-stage providers unless the user explicitly asks to include them. If the user asks for Codex/OpenAI browser deep research, use ChatGPT Deep Research at `https://chatgpt.com/` by default and record the requested alias in `browser-provider-status.md`; do not use Codex web/cloud as the default deep-research target unless the user explicitly asks for a Codex work-agent workflow.

This prompt follows GAS Deep Research Mode's mandatory directory contract:

```text
[research-topic]/
|-- .meta.md
|-- prompt.md
|-- browser-provider-status.md
|-- sources.md
|-- RESEARCH-SYNTHESIS.md
|-- handoff.md
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
- Provider list to run now.
- Output directory, if not using the default.
- Desired depth: quick scan, standard deep research, or exhaustive.
- Any required source types, forbidden sources, date ranges, geography, or output format.

### Checkpoint 2: Sign-In

For each provider:

1. Open the provider in the browser.
2. Ask the user to complete sign-in or confirm the session is already signed in.
3. Do not proceed until the user confirms: "signed in", "ready", or equivalent.
4. If there is CAPTCHA, 2FA, account selection, age gate, payment wall, extension prompt, or bot challenge, pause and ask the user to handle it manually.

### Checkpoint 3: Prompt Review

Before submitting the first provider prompt, show the exact research prompt that will be pasted. Ask the user to approve or revise it if the research is high-stakes, expensive, or likely to run for a long time.

### Checkpoint 4: Long-Running Waits

If a provider is still working after 20 minutes, tell the user the current visible status and ask whether to keep waiting, skip that provider, or continue later. Do not abandon a run silently.

---

## Provider Execution Loop

For each requested provider, perform this loop:

1. **Open** the provider URL in the browser.
2. **Verify sign-in** with the user.
3. **Select research mode** if the UI offers one.
4. **Submit the research prompt** exactly once unless submission visibly fails.
5. **Wait for completion** using the provider-specific completion signals below.
6. **Capture raw output** using the best available method:
   - Provider copy/export button when available.
   - Browser text extraction when reliable.
   - Manual selection/copy when the user must intervene.
   - Screenshots only as fallback evidence, not as the primary result.
7. **Save raw output** immediately before moving to the next provider.
8. **Log run metadata** including provider, URL, account context if visible without exposing private data, start time, end time, completion status, capture method, and visible limitations.

Never enter private credentials. Never bypass access controls. Never attempt to defeat CAPTCHA, bot checks, paywalls, rate limits, or provider safety systems.

---

## Provider-Specific Instructions

### ChatGPT

1. Navigate to `https://chatgpt.com/`.
2. Confirm the user is signed in.
3. Start a clean new chat.
4. Select **Deep research** using the most stable available route:
   - Preferred: slow-type `/Deepresearch` into the composer and select the command if it appears.
   - Fallback: open the tools/composer menu such as **Add files and more** and choose **Deep research**.
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

Preferred capture: final assistant-message **Copy** action, then clipboard read. If links/citations are stripped, use scoped DOM extraction for the final assistant message and record the capture limitation.

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
3. Ask the user whether to retry, skip, or continue with other providers.
4. Do not substitute a different provider without user approval.

If output capture fails:

1. Try provider copy/export controls.
2. Try browser text extraction.
3. Ask the user to manually copy the response into the chat or a file.
4. Record the capture limitation in `browser-provider-status.md`.

If the browser session expires:

1. Pause.
2. Ask the user to sign in again.
3. Resume only after user confirmation.

---

## Completion Criteria

The research run is complete only when:

- Each requested provider is marked `completed`, `skipped_by_user`, or `blocked`.
- Raw output is saved for every completed provider.
- `browser-provider-status.md` is updated.
- `sources.md` exists, even if it only states that no sources were captured.
- `RESEARCH-SYNTHESIS.md` exists if at least one provider completed.
- `handoff.md` gives the user absolute paths and the next logical step.
