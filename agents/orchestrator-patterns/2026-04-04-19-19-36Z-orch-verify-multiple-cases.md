---
id: P-016
category: VERIFICATION
trigger: "When verifying a fix, never test only the 'happy path' case"
source_session: 2026-04-04
---

# P-016: Multi-Case Verification (Probe the Attack Surface)

**Action:** When verifying a security or routing fix, test MULTIPLE cases — especially cases that share the same underlying mechanism. Never accept "one test passed" as proof.

**Why:** Discovered in 2026-04-04 Week 1 retest (T59). The orchestrator previously verified HIGH-001 catchall fix by testing ONLY `traefik.peermesh.org` returning 403, and reported "HIGH-001 truly fixed". But `traefik` had a specific router that happened to return 403 via auth. Unrouted subdomains like `s3.*`, `minio.*`, and `random-*` were still hitting an orphan whoami container that leaked internal IPs, container hostnames, and Traefik IDs. The single-case verification missed a wide-open information leak.

**How to apply:**

For catchall/routing fixes, test AT LEAST:
1. A specifically-routed subdomain (should hit its intended backend)
2. A subdomain that was leaking before (regression case)
3. A random/non-existent subdomain (true catchall exercise)
4. A known-working service (no-regression case)

For security header fixes, test AT LEAST:
1. The specific target endpoint
2. An adjacent endpoint on the same service
3. A different service behind the same proxy
4. An error response (404, 403, 500) — headers should still apply

For auth fixes, test AT LEAST:
1. Unauthenticated request (should 401)
2. Wrong credentials (should 401)
3. Correct credentials (should 200)
4. Header presence on both success and failure responses

**The rule:** If one curl passes, celebrate nothing. Run the other three first.

**Examples:**

WRONG (what I did):
```
curl https://traefik.peermesh.org/ → 403 ✓
"HIGH-001 fixed!"
```

RIGHT:
```
curl https://traefik.peermesh.org/ → 403 ✓ (specific router)
curl https://s3.peermesh.org/ → 403 ✓ (previously leaking)
curl https://random-$(date +%s).peermesh.org/ → 403 ✓ (true catchall)
curl https://core.peermesh.org/ → 200 ✓ (no regression)
"HIGH-001 fixed."
```
