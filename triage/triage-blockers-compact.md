Report only current blockers that require user action.

For each blocker, use this exact format:

### [Priority #] [Short blocker name]

**Category:** Approval needed / User decision needed / Account/login needed / External service action needed / Credential/API key needed / Payment/billing needed / File/input needed / Policy/legal decision needed / Architecture/product decision needed / Manual verification needed / Unknown blocker

**Blocked because:** [Plain-language explanation.]

**User action required:** [Concrete action.]

**Where to act:** [Link, dashboard, file, repo, website, or Not applicable.]

**Decision needed:** [Exact approval, choice, login, key, file, or confirmation.]

**Recommended choice:** [Best option and brief reason.]

**Unblocks:** [What can continue.]

**Related work:** [IDs only if useful; otherwise “Not needed.”]

Rules:
- Include only user-blocked items.
- Merge duplicate blockers.
- Group related blockers when one user action unblocks multiple tasks.
- Prioritize highest-leverage blockers first.
- Avoid cryptic work-order references.
- Include enough context that the user does not need to ask what the blocker means.
- Maximum 10 blockers.
- If none: `No user-blocked items remain.`