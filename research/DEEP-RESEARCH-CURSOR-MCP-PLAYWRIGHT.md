---
title: Deep Research – Cursor MCP Playwright Reliability
owner: Infra/AI Tooling
platforms: [macOS, Cursor, MCP]
updated: 2025-10-14
purpose: Diagnose breakages and lock-in robust, repeatable fixes
---

# Goal

Produce a clear, repeatable playbook to: (1) diagnose why the Playwright MCP server breaks in Cursor on macOS, (2) fix it immediately, and (3) harden configuration so it does not regress. Keep other MCP servers intact.

# Environment Facts

- Host: macOS (Apple Silicon likely)
- Client: Cursor app (VSCode-based)
- Config: `~/.cursor/mcp.json`
- Logs: `~/Library/Application Support/Cursor/logs/**`
- Node via NVM commonly unavailable to GUI apps’ PATH
- Playwright browsers default OS cache: `~/Library/Caches/ms-playwright`

# Inputs To Collect (Scripts OK, No Destructive Steps)

- `~/.cursor/mcp.json` content (focus: `playwright` entry)
- Node/npm/npx availability and absolute paths
- Cursor logs containing `mcp`, `playwright`, or the server package name
- Playwright cache presence: `~/Library/Caches/ms-playwright/chromium-*`
- Package metadata: `npm view @executeautomation/playwright-mcp-server version bin dependencies --json`

# Repro & Triage Steps

1) Open Cursor and trigger a tool call that uses the Playwright MCP
2) Inspect logs:
   - Grep `~/Library/Application Support/Cursor/logs/**` for `mcp|playwright`
   - Open the latest `MCP user-playwright.log`
3) Confirm whether `npx` resolves in Cursor’s PATH (logs often show `_npx/...` temp dirs)
4) Note error messages verbatim (missing executable, ENOENT, EACCES/quarantine, signature issues)

# Known Failure Modes And What To Check

- Missing browsers: `Executable doesn't exist` with suggestion to `npx playwright install`
  - Check `~/Library/Caches/ms-playwright/chromium-<rev>` exists
  - Confirm Playwright version match (server depends on `playwright@1.53.x` → chromium rev 1179)

- GUI PATH missing npx/node (NVM shells not loaded for apps)
  - `command` is `npx` in `mcp.json` → brittle; GUI PATH often lacks NVM shims
  - Solution: use absolute `node` and a local installed server path

- Gatekeeper quarantine on downloaded Chromium
  - Errors mention `quarantine` / `operation not permitted`
  - Fix: `xattr -dr com.apple.quarantine "~/Library/Caches/ms-playwright/chromium-<rev>"`

- Corporate proxy/SSL intercept blocks browser downloads
  - Downloads hang or 403/SSL errors
  - Fix: set proxy env for install step or provide offline bundle

# Immediate Fix (Minimal Risk)

Install exact browsers to the location the server uses on macOS:

```bash
PLAYWRIGHT_BROWSERS_PATH="$HOME/Library/Caches/ms-playwright" \
  npx -y playwright@1.53.1 install chromium
```

Why: The server depends on `playwright@1.53.x` and expects Chromium rev 1179 in the OS cache. Installing there makes the server launch succeed regardless of ephemeral `npx` behavior.

# Robust Hardening (Prevents Future Breaks)

- Avoid `npx` at runtime: preinstall the server and point to absolute paths
- Keep browsers in OS cache; do not rely on ephemeral `.local-browsers`
- Pin versions to reduce surprises

Recipe:

```bash
mkdir -p "$HOME/.cursor/servers/playwright" && cd "$HOME/.cursor/servers/playwright"
npm init -y >/dev/null
npm i @executeautomation/playwright-mcp-server@1.0.6 --prefer-offline

# Optional: preinstall browsers to OS cache
PLAYWRIGHT_BROWSERS_PATH="$HOME/Library/Caches/ms-playwright" \
  npx -y playwright@1.53.1 install chromium
```

Update `~/.cursor/mcp.json` (example):

```json
{
  "mcpServers": {
    "playwright": {
      "command": "/Users/USER/.nvm/versions/node/v20.19.5/bin/node",
      "args": [
        "/Users/USER/.cursor/servers/playwright/node_modules/@executeautomation/playwright-mcp-server/dist/index.js"
      ],
      "env": {
        "PLAYWRIGHT_BROWSERS_PATH": "/Users/USER/Library/Caches/ms-playwright",
        "PW_HEADLESS": "1"
      }
    }
  }
}
```

Note: Use your actual Node absolute path (not `npx`). Keep other servers unchanged.

# Validation Checklist

- Playwright MCP server starts without ENOENT/EACCES
- Cursor MCP tool calls return promptly (no long cold start downloads)
- Browser path exists at `~/Library/Caches/ms-playwright/chromium-<rev>`
- No new errors in latest `MCP user-playwright.log`

# Output (Deliverables)

- A one-line fix (exact command) that installs the needed browser build
- A hardened `mcp.json` example that avoids `npx`
- A short decision tree mapping error → fix
- Notes on preserving other MCP servers (no changes to their entries)

# Bonus: Quick Diagnostics Script

Use `~/.agents/scripts/mcp-diagnose.sh` to:

- Summarize `mcp.json` servers and commands
- Verify Node/npx are resolvable
- Check Playwright caches
- Surface relevant Cursor log errors

# References

- Playwright browser installation and cache behaviors
- Cursor MCP extension log structure and locations
- `@executeautomation/playwright-mcp-server` npm metadata (bins, deps)

