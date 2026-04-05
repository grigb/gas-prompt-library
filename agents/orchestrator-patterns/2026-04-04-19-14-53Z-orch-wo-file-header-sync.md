---
id: P-015
category: CLEANUP
trigger: "When a WO is marked COMPLETED in WO-INDEX but the WO file header may still say NOT_STARTED/IN_PROGRESS"
source_session: 2026-04-04
---

# P-015: WO File Header Status Sync

**Action:** When updating WO-INDEX status, ALSO update the `**Status**` header line in the individual WO file. The index and file must always match. After any WO status change, verify both locations.

**Why:** Discovered in 2026-04-04 Week 1 reconciliation (T60): 5 WOs (WO-292..296) had COMPLETED status in the index with full closure notes, but the individual WO file headers still said NOT_STARTED or IN_PROGRESS. This is systemic drift — dev-worker closing checklists often forget the file header update step.

**How to apply:**
1. When delegating a WO execution task, include in the prompt: "After completing work, update BOTH the WO-INDEX row AND the `**Status**` header in the WO file itself."
2. When running WO-INDEX reconciliation sweeps (P-005), always also check individual WO file headers for drift — not just the index.
3. When a sub-agent reports WO completion, verify both the index entry AND the file header match before marking done.

**Examples:**
- Sub-agent reports "WO-299 complete" → orchestrator verifies: (1) WO-INDEX row shows COMPLETED, (2) `WO-PMDL-2026-04-03-299.md` header shows `**Status**: COMPLETED`. If only one matches, fix the other before accepting.
- Reconciliation sweep finds index has "WO-293 COMPLETED" but file says `**Status**: NOT_STARTED` → update the file header.
