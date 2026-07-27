---
created: 2026-07-07T01:22:35Z
agent: orchestrator
scope: global-candidate
source: owner correction during Browser Deep Research A1 no-submit recertification
---

# Browser Research Must Verify Chrome Profile, Not Just App Binary

When the owner corrects a browser route by saying to use their existing signed-in
Chrome, treat that as a profile/session correction, not only an app-binary
correction. `/Applications/Google Chrome.app` can be the right app while a
worker still opens the wrong `--user-data-dir`.

For signed-in provider work, require workers to record both app identity and
profile/session identity before interpreting provider gates. If a previous
worker used the wrong profile, mark its provider observations as superseded
wrong-profile evidence and do not promote them into provider-state truth.

Preferred owner-profile exception route remains GAS `agent-browser` with real
Google Chrome and the selected owner Chrome profile/session. If that route
cannot open or attach, stop with
`BLOCKED_ROUTE_OWNER_CHROME_PROFILE_NOT_ATTACHED` instead of falling back to the
GAS-managed `browser-research` profile. Do not switch to the Codex Chrome
Extension unless the owner explicitly selects that route.
