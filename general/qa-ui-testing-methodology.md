# QA UI Testing Methodology — Exhaustive Interactive Element Coverage

**Purpose:** Reusable methodology for any QA agent to systematically test every interactive element in a web application. Works with `agent-browser` CLI.

**Reference tool:** `~/.agents/skills/agent-browser/SKILL.md`
**Full browser guide:** `~/.agents/docs/AGENT-BROWSER-GUIDE.md`

---

## Philosophy

Every interactive element must be tested. "The page loads" is not verification.

A screen is a directed graph. Each node is a screen state. Each edge is an interactive element that transitions state. QA maps and traverses this entire graph. The goal is 100% interactive element coverage for every reachable screen.

An untested button is an unknown. An unknown is a risk. QA eliminates unknowns.

---

## Pre-Requisites

Before starting, the QA agent must have:

1. **A running application** — local or deployed URL
2. **agent-browser available** — `agent-browser open <url>` works
3. **A QA session directory** — `.dev/ai/qa/YYYY-MM-DD-HH-MM-SS-[scope]/`
4. **Auth credentials** if the app requires login (use `agent-browser state` for persistence)

### Session Setup

```bash
# Create session directory
SESSION_DIR=".dev/ai/qa/$(date +%Y-%m-%d-%H-%M-%S)-[scope]"
mkdir -p "$SESSION_DIR/screenshots"
mkdir -p "$SESSION_DIR/issues"

# Open application
agent-browser open <app-url>
agent-browser errors                          # Check for pre-existing errors
agent-browser screenshot "$SESSION_DIR/screenshots/baseline.png"
```

---

## Phase 1: Screen Discovery (Element Inventory)

For each page/route in the application:

### Step 1: Navigate and Snapshot

```bash
agent-browser open <page-url>
agent-browser snapshot -i                     # Get ALL interactive elements with refs
agent-browser screenshot "$SESSION_DIR/screenshots/[page-name]-initial.png"
```

### Step 2: Inventory Every Interactive Element

From the snapshot output, identify and document every element:

| Property | What to Record |
|----------|---------------|
| **Ref** | The element reference (e.g., `@e1`, `@e2`) |
| **Type** | button, link, input, textarea, dropdown/select, toggle/switch, checkbox, radio, tab, accordion, menu item, icon button, card (clickable), slider, file upload |
| **Label/Text** | The visible text or aria-label |
| **Current State** | enabled/disabled, checked/unchecked, expanded/collapsed, selected/unselected |
| **Expected Behavior** | What SHOULD happen when activated (based on code analysis, label semantics, or common UI patterns) |
| **Auth Required** | Whether the element requires authentication to function |
| **Visible** | Whether the element is visible or hidden behind a menu/accordion |

### Step 3: Discover Hidden Elements

Many interactive elements are not visible on initial load. The QA agent MUST check:

1. **Hover states** — elements that appear on hover (dropdown menus, tooltips with actions)
2. **Scroll regions** — elements below the fold or in scrollable containers
3. **Conditional elements** — elements that appear only after a specific action (e.g., "Edit" button appears after selecting an item)
4. **Keyboard-accessible elements** — elements reachable only via Tab key
5. **Right-click/context menus** — elements in context menus

```bash
# Check for elements below the fold
agent-browser eval "document.body.scrollHeight > window.innerHeight"

# Scroll to bottom and re-snapshot
agent-browser eval "window.scrollTo(0, document.body.scrollHeight)"
agent-browser snapshot -i
```

### Step 4: Record the Screen Map

For each screen, produce a structured record:

```
### Screen: [URL or route]
**Screenshot:** [path-to-screenshot]
**Total Interactive Elements:** [N]
**Hidden Elements Discovered:** [N]

| # | Ref | Type | Label | State | Expected Behavior | Auth? |
|---|-----|------|-------|-------|-------------------|-------|
| 1 | @e1 | button | "Create Post" | enabled | Opens compose modal | yes |
| 2 | @e2 | link | "Settings" | enabled | Navigates to /settings | yes |
| 3 | @e3 | input | "Search" | enabled | Accepts text, triggers search | no |
| 4 | @e4 | toggle | "Dark Mode" | checked | Switches theme | no |
```

---

## Phase 2: Interaction Testing (Click-Through)

For EVERY interactive element discovered in Phase 1, activate it and record the result.

### Step 1: Test Each Element

```bash
# For buttons and links
agent-browser click @e1
agent-browser errors                          # Check for JS errors
agent-browser screenshot "$SESSION_DIR/screenshots/[page]-after-e1.png"

# For inputs
agent-browser fill @e3 "test query"
agent-browser screenshot "$SESSION_DIR/screenshots/[page]-after-fill-e3.png"

# For dropdowns
agent-browser click @e5                       # Open dropdown
agent-browser snapshot -i                     # See dropdown options
agent-browser click @e5-option1               # Select first option
```

### Step 2: Classify the Outcome

For each interaction, classify what happened:

| Outcome | Classification | Action |
|---------|---------------|--------|
| Page navigated to new URL | **Screen transition** | Add new screen to Phase 1 queue |
| Modal/dialog appeared | **Modal spawn** | Map the modal as a sub-screen (apply Phase 1 to modal contents) |
| Dropdown/menu opened | **Expansion** | Map all options, test each one |
| Data changed on screen | **State mutation** | Verify the change is correct, check persistence (Phase 5) |
| Toast/notification appeared | **Feedback** | Record the message, verify it is appropriate |
| Nothing visible happened | **Possible dead element** | Check console for errors, check network tab, mark as SUSPECT |
| Error displayed to user | **Error state** | Document the error, determine if expected or bug |
| Console error appeared | **Silent failure** | Document the error, file as defect |
| Page crashed or went blank | **Critical failure** | File as Critical severity defect immediately |

### Step 3: Record Interaction Results

Update the screen map with actual results:

```
| # | Ref | Type | Label | Expected | Actual | Status |
|---|-----|------|-------|----------|--------|--------|
| 1 | @e1 | button | "Create Post" | Opens compose modal | Opens compose modal | PASS |
| 2 | @e2 | link | "Settings" | Navigates to /settings | 404 page | FAIL |
| 3 | @e3 | input | "Search" | Triggers search | Nothing happens | FAIL |
| 4 | @e4 | toggle | "Dark Mode" | Switches theme | Theme switches | PASS |
```

### Step 4: Recursive Discovery

When an interaction produces a new screen, modal, or expanded section:

1. Apply Phase 1 (Screen Discovery) to the new screen/modal
2. Apply Phase 2 (Interaction Testing) to all its elements
3. Continue recursively until no new screens are discovered
4. Track visited screens to avoid infinite loops (especially for navigation that returns to a previous screen)

```
VISITED SCREENS:
- / (landing) — 12 elements tested
- /studio — 18 elements tested
- /studio [compose modal] — 6 elements tested
- /settings — 14 elements tested
- /settings/profile — 8 elements tested
```

---

## Phase 3: Form Testing

For every form discovered during Phase 1/2, perform exhaustive input testing.

### 3.1: Valid Submission

```bash
# Fill all fields with valid data
agent-browser fill @name "Jane Smith"
agent-browser fill @email "jane@example.com"
agent-browser fill @bio "A short bio."
agent-browser click @submit
agent-browser screenshot "$SESSION_DIR/screenshots/form-[name]-valid-submit.png"
```

Verify:
- [ ] Form accepts the input
- [ ] Success message or redirect occurs
- [ ] Data is actually saved (check by navigating away and back)

### 3.2: Empty Required Fields

Submit the form with each required field left empty, one at a time:

```bash
# Leave name empty, fill everything else
agent-browser fill @email "jane@example.com"
agent-browser click @submit
# Expected: validation message on name field
agent-browser screenshot "$SESSION_DIR/screenshots/form-[name]-empty-name.png"
```

Verify:
- [ ] Validation message appears
- [ ] Validation message is specific (not generic "error")
- [ ] Form does NOT submit
- [ ] Focus moves to the invalid field

### 3.3: Invalid Data

Test each field with invalid input:

| Field Type | Invalid Input Examples |
|-----------|----------------------|
| Email | `notanemail`, `@missing.com`, `user@`, empty |
| URL | `notaurl`, `ftp://wrong`, `javascript:alert(1)` |
| Phone | `abc`, `12345678901234567890` |
| Number | `abc`, `-1`, `99999999999`, `0.0001` |
| Text (with max length) | String exceeding max length |
| Date | `2099-13-45`, `not-a-date` |
| Password | Too short, no special chars (if rules exist) |

### 3.4: Boundary Values

- Max length strings (paste 10,000 characters into a text field)
- Special characters: `< > " ' & \ / { } | ; : ! @ # $ % ^ * ( )`
- Unicode: emojis, RTL text, CJK characters
- SQL injection patterns: `'; DROP TABLE users; --`
- XSS patterns: `<script>alert('xss')</script>`
- Null bytes: `%00`

### 3.5: Form State

- [ ] Can the form be submitted multiple times rapidly? (double-submit protection)
- [ ] Does the form preserve entered data on validation failure? (no data loss on error)
- [ ] Can the form be cancelled/dismissed without side effects?

---

## Phase 4: Navigation Flow Testing

### 4.1: Map All Navigation Paths

Identify every navigation mechanism:

- **Top navigation bar** — every link and dropdown
- **Sidebar navigation** — every link and section
- **Breadcrumbs** — every breadcrumb link
- **In-page links** — links within content areas
- **Footer links** — every footer link
- **Logo/home link** — click the logo
- **Back button** — browser back behavior after each navigation

### 4.2: Test Every Navigation Link

```bash
# For each navigation link
agent-browser click @nav-link
agent-browser eval "window.location.href"      # Verify URL changed
agent-browser errors                           # Check for errors
agent-browser screenshot "$SESSION_DIR/screenshots/nav-[target].png"
```

Verify for each link:
- [ ] Navigates to a real page (no 404, no blank page)
- [ ] Page content is appropriate for the link label
- [ ] URL matches expected pattern
- [ ] No console errors on the destination page

### 4.3: Auth Gate Testing

For pages that require authentication:

```bash
# Test in unauthenticated state
agent-browser open <protected-url>
# Expected: redirect to login/join page
agent-browser eval "window.location.href"
agent-browser screenshot "$SESSION_DIR/screenshots/auth-gate-[page].png"
```

Verify:
- [ ] Protected pages redirect to login when unauthenticated
- [ ] Redirect preserves the intended destination (return after login)
- [ ] Public pages remain accessible without auth

### 4.4: Back Button Behavior

After each navigation action, test:

```bash
agent-browser eval "history.back()"
agent-browser eval "window.location.href"
```

- [ ] Back button returns to the previous page
- [ ] Previous page state is preserved (scroll position, form data, selections)
- [ ] No infinite redirect loops

---

## Phase 5: State Persistence Testing

### 5.1: Create-Navigate-Verify Pattern

For every data mutation (create, edit, delete):

```bash
# Step 1: Make a change
agent-browser fill @bio "Updated bio text"
agent-browser click @save
agent-browser screenshot "$SESSION_DIR/screenshots/state-save.png"

# Step 2: Navigate away
agent-browser open <different-page>

# Step 3: Navigate back
agent-browser open <original-page>
agent-browser screenshot "$SESSION_DIR/screenshots/state-verify.png"

# Step 4: Verify the change persisted
agent-browser eval "document.querySelector('[data-testid=bio]')?.textContent"
```

### 5.2: Refresh Persistence

```bash
# After making a change and saving
agent-browser eval "location.reload()"
# Verify data still shows the change
```

### 5.3: Cross-Tab Consistency

If the app supports multiple views of the same data:
- Make a change in one view
- Navigate to another view of the same data
- Verify consistency

---

## Phase 6: Error Handling Verification

### 6.1: Console Error Audit

After every page load and every interaction:

```bash
agent-browser errors
agent-browser console
```

Any console error that appears during normal usage is a defect (severity depends on impact).

### 6.2: Network Error Simulation (if possible)

- Disconnect from network and attempt actions — verify graceful degradation
- Submit forms when API is slow — verify loading states

### 6.3: User-Facing Error Quality

When errors DO occur (expected or not), verify:

- [ ] Error message is human-readable (no raw JSON, no stack traces, no technical codes)
- [ ] Error message tells the user what to do (actionable guidance)
- [ ] Error does not expose internal implementation details (security)
- [ ] Error is dismissable or recoverable (user is not stuck)

---

## Output Format

### Per-Screen Report

For each screen tested, produce:

```markdown
### Screen: [URL]
**Screenshot:** [path]
**Interactive Elements Found:** [N]
**Elements Tested:** [N]
**Pass:** [N] | **Fail:** [N] | **Suspect:** [N]

| # | Ref | Type | Label | Expected | Actual | Status |
|---|-----|------|-------|----------|--------|--------|
| 1 | @e1 | button | "Create Post" | Opens compose | Opens compose | PASS |
| 2 | @e2 | link | "Settings" | Nav to /settings | 404 | FAIL |
| 3 | @e3 | input | "Search" | Accepts text | Works | PASS |
| 4 | @e4 | button | "Delete" | Confirms then deletes | Deletes without confirm | FAIL |
```

### Coverage Tracking

Maintain a running coverage map across all screens:

```markdown
## Coverage Map

| Screen URL | Elements Found | Elements Tested | Pass | Fail | Suspect | Coverage |
|-----------|---------------|-----------------|------|------|---------|----------|
| / | 12 | 12 | 11 | 1 | 0 | 100% |
| /studio | 18 | 18 | 15 | 2 | 1 | 100% |
| /settings | 14 | 14 | 14 | 0 | 0 | 100% |
| /join | 8 | 8 | 7 | 1 | 0 | 100% |
| **TOTAL** | **52** | **52** | **47** | **4** | **1** | **100%** |
```

The target is **100% interactive element coverage** for every discovered screen.

### Defect Filing

For each FAIL, create a defect document following the format in the QA agent prompt (`~/.agents/prompts/agents/agent-qa-full-review.md`, Phase 3). Minimum fields:

- **Severity:** Critical / High / Medium / Low
- **Screen:** URL where the defect was found
- **Element:** The interactive element that failed
- **Expected:** What should have happened
- **Actual:** What did happen
- **Steps to Reproduce:** Exact sequence
- **Screenshot:** Path to evidence
- **Code Reference:** If known from code analysis

---

## Traversal Strategy

### Depth-First vs Breadth-First

Use **breadth-first** for initial discovery (map all screens at their top level first), then **depth-first** for thorough testing of each screen's elements.

### Handling Cycles

Track all visited screen states. A "state" is defined by URL + visible element set. If you return to a state you have already fully tested, skip it. If the same URL has different elements (e.g., different auth state), test it as a new screen.

### Priority Order

When time is limited, test in this priority order:

1. **Happy paths** — primary user flows (sign up, create content, navigate)
2. **Auth gates** — protected pages redirect correctly
3. **Forms** — all forms accept valid data and reject invalid data
4. **Navigation** — all links go somewhere real
5. **Edge cases** — boundary values, special characters, error states
6. **Cosmetic** — visual alignment, responsive behavior

---

## Integration with Verification Manifest

When a project has a Verification Manifest (`.dev/ai/verification/VERIFICATION-MANIFEST.md`), this methodology provides the HOW for UI-related VM assertions:

- **VM assertions define WHAT to verify** (e.g., "VM-055: Studio profile page renders with user data")
- **This methodology defines HOW to verify it** (navigate, snapshot, identify elements, click each one, document results)

When executing VM assertions that involve UI:

1. Follow this methodology for the relevant screen
2. Update the VM assertion status based on test results
3. Cross-reference the per-screen report with the VM assertion ID

---

## Checklist Before Concluding

Before declaring a UI QA session complete:

- [ ] Every reachable screen has been visited
- [ ] Every interactive element on every screen has been activated
- [ ] Every form has been tested with valid, invalid, and boundary inputs
- [ ] Every navigation link has been followed
- [ ] Auth gates have been verified for protected routes
- [ ] State persistence has been verified for all data mutations
- [ ] Console errors have been checked after every interaction
- [ ] Screenshots exist for every screen (initial state + after interactions)
- [ ] Coverage map shows 100% element coverage (or documents why not)
- [ ] All FAIL items have defect documents filed
- [ ] All SUSPECT items have been investigated and reclassified
