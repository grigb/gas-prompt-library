# Ceremony Clause (canonical prompt fragment)

**Purpose:** A reusable clause defining what "ceremony" means when a prompt asks an
agent to cut over-engineering or process waste from a plan. Fold into any prompt
that mentions ceremony, elegance, efficiency, or anti-over-engineering.

**Trigger phrase:** "avoid ceremony"

## Canonical wording (full, with examples)

> treating as ceremony, and cutting, any step that exists to satisfy process rather than to produce or verify the deliverable, such as extra approval gates or recaps that restate what artifacts already say

## Compact wording (rule only, no examples)

> treating as ceremony, and cutting, any step that exists to satisfy process rather than to produce or verify the deliverable

## Placement guidance

- Fold in where the prompt discusses elegance, efficiency, or optimization —
  not as a separate instruction block.
- Use the full wording the first time a prompt family gets the clause; the
  compact wording is fine for prompts where space matters or the agent has
  already seen the examples.
- Keep the core test unchanged: **exists to satisfy process rather than to
  produce or verify the deliverable.** Examples may be tuned per prompt, but
  the test is the calibration anchor.

## History

- 2026-08-28 — Created from a prompt-improvement session with the owner.
  Definition pattern chosen: decision rule + short example list, per owner
  preference for minimal, single-line, portable prompts.
