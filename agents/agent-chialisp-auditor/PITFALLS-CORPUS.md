# ChiaLisp Auditor — Living Pitfalls / Lessons Corpus

**Companion to `agent-chialisp-auditor` (SKILL.md).** The reviewer READS this file at the
start of every run and APPENDS to it at the end. It accumulates known pitfalls, bug classes,
canonical-diff findings, novel attacks, and settled false-positives so each run sharpens the
next. **Keep it GENERIC ChiaLisp** — never record a specific project's secrets, strategy, or
private puzzle internals here (record those in the project). Only portable ChiaLisp lessons.

**Corpus version:** 1.2.0 (seed + WO-192 web-research enrichment + WO-193/194 fix-derived
checks: §4b real incidents, §4c sentinels/authority-boundary, **§4d the 35 SHA-cited fix-derived
review checks (D-01…D-33)**, §2 internal-custody/MIPS bounded-authority analogues, §5/§9
extensions; 2026-07-04). Bump when you add a substantive section.

---

## How to append (format)

At the end of a review, add a dated entry under **§10 Run log** using this shape:

```
### YYYY-MM-DD — <one-line title> [target class: singleton|did|nft|cat|offer|custom]
- LESSON / PITFALL / FALSE-POSITIVE / CANONICAL-DIFF-GAP / NOVEL-ATTACK: <what, in 1–3 lines>
- BASIS: canonical-diff | on-chain-consensus | independent-parser | model-reasoning
- REUSABLE CHECK: <the exact check that decides it next time, generic form>
```

Promote anything that recurs across ≥2 reviews into the relevant numbered section (§1–§8).

---

## §1 Condition codes — the numeric ground truth

Canonical: `chia/wallet/puzzles/condition_codes.clib` (decimal). Puzzles often write **hex**.
Cross-check every emitted opcode.

| Condition | dec | hex | Commits / note |
|---|---|---|---|
| REMARK | 1 | 0x01 | always true, ignores args |
| AGG_SIG_PARENT..PARENT_PUZZLE | 43–48 | 0x2b–0x30 | post-2.0 sig variants (bind parent/puzzle/amount subsets) |
| AGG_SIG_UNSAFE | 49 | 0x31 | signs message ONLY — replayable across coins/networks |
| AGG_SIG_ME | 50 | 0x32 | binds coin_id + genesis_challenge (per-coin, per-network) |
| CREATE_COIN | 51 | 0x33 | (ph amount [hint]); odd amount ⇒ singleton-relevant |
| RESERVE_FEE | 52 | 0x34 | reserves fee mojos |
| CREATE_COIN_ANNOUNCEMENT | 60 | 0x3c | announcer = coin id |
| ASSERT_COIN_ANNOUNCEMENT | 61 | 0x3d | asserts sha256(coin_id‖msg); same-bundle |
| CREATE_PUZZLE_ANNOUNCEMENT | 62 | 0x3e | announcer = puzzle hash |
| ASSERT_PUZZLE_ANNOUNCEMENT | 63 | 0x3f | asserts sha256(puzzle_hash‖msg); same-bundle |
| ASSERT_CONCURRENT_SPEND | 64 | 0x40 | requires another coin id spent same bundle |
| ASSERT_CONCURRENT_PUZZLE | 65 | 0x41 | requires a puzzle hash spent same bundle |
| SEND_MESSAGE / RECEIVE_MESSAGE | 66 / 67 | 0x42 / 0x43 | CHIP-0025 typed messages (mode mask) |
| ASSERT_MY_COIN_ID | 70 | 0x46 | pins spending coin id |
| ASSERT_MY_PARENT_ID | 71 | 0x47 | pins parent coin id |
| ASSERT_MY_PUZZLEHASH | 72 | 0x48 | pins coin puzzle hash (identity pin) |
| ASSERT_MY_AMOUNT | 73 | 0x49 | pins amount (singleton: 1) |
| ASSERT_MY_BIRTH_SECONDS / HEIGHT | 74 / 75 | 0x4a / 0x4b | pins creation time/height |
| ASSERT_EPHEMERAL | 76 | 0x4c | created+spent same block |
| ASSERT_SECONDS_RELATIVE / ABSOLUTE | 80 / 81 | 0x50 / 0x51 | "far enough" (wall clock) |
| ASSERT_HEIGHT_RELATIVE / ABSOLUTE | 82 / 83 | 0x52 / 0x53 | "far enough" (block height) |
| ASSERT_BEFORE_SECONDS_RELATIVE / ABSOLUTE | 84 / 85 | 0x54 / 0x55 | "not too far" (wall) — CHIP-0014 |
| ASSERT_BEFORE_HEIGHT_RELATIVE / ABSOLUTE | 86 / 87 | 0x56 / 0x57 | "not too far" (height); **vs PREVIOUS TX BLOCK (±1 wall-block)** |
| SOFTFORK | 90 | 0x5a | cost placeholder for soft-forked conditions |

- `AGG_SIG_ME` message = `raw_message ‖ coin_id ‖ genesis_challenge` (additional data). Its
  binding to one coin/network is what stops signature replay. `AGG_SIG_UNSAFE` has none of
  that — flag it and any reused signed message.

## §2 Canonical reference puzzles (obtain the ground truth)

Repo of record: **`Chia-Network/chia_puzzles`** → Python `chia_puzzles_py`. Get bytecode +
mod hash: `import chia_puzzles_py.programs as p; p.<NAME>, p.<NAME>_HASH`. Uncurry:
`Program.from_bytes(p.<NAME>).uncurry()`. Raw source:
`github.com/Chia-Network/chia_puzzles/blob/main/programs/<name>.clsp` (+ `.clsp.hex`).
Independent parser oracle: `chia-blockchain` drivers (`UncurriedNFT.uncurry`, `nft_get_info`,
`*_outer_puzzle.py`, `did_wallet_puzzles.py`).

Seed mod hashes (verified from `chia_puzzles_py` 0.20.3 — re-verify on the project's
toolchain, versions can differ):

| Puzzle | Mod hash | Reference for |
|---|---|---|
| SINGLETON_TOP_LAYER | `24e044101e57b3d8c908b8a38ad57848afd29d3eecc439dba45f4412df4954fd` | original singleton wrapper |
| SINGLETON_TOP_LAYER_V1_1 | `7faa3253bfddd1e0decb0906b2dc6247bbc4cf608f58345d173adb63e8b47c9f` | current singleton wrapper (NFT/DID) |
| SINGLETON_LAUNCHER | `eff07522495060c066f66f32acc2a77e3a3e737aca8baea4d1a64ea4cdc13da9` | singleton birth / launcher |
| DID_INNERPUZ | `33143d2bef64f14036742673afd158126b94284b4530a28c354fac202b0c910e` | DID inner puzzle |
| NFT_STATE_LAYER | `a04d9f57764f54a43e4030befb4d80026e870519aaa66334aef8304f5d0393c2` | NFT metadata + updater layer |
| NFT_OWNERSHIP_LAYER | `c5abea79afaa001b5427dfa0c8cf42ca6f38f5841b78f9b3c252733eb2de2726` | NFT owner + transfer-program layer |
| NFT_..._ONE_WAY_CLAIM_WITH_ROYALTIES | `025dee0fb1e9fa110302a7e9bfb6e381ca09618e2778b0184fa5c6b275cfce1f` | NFT transfer program w/ royalties |
| NFT_METADATA_UPDATER_DEFAULT | `fe8a4b4e27a2e29a4d3fc7ce9d527adbcaccbab6ada3903ccf3ba9a769d2d78b` | default metadata updater |
| CAT_PUZZLE | `37bef360ee858133b69d595a906dc45d01af50379dad515eb9518abb7c1d2a7a` | CAT2 outer puzzle |
| SETTLEMENT_PAYMENT | `cfbfdeed5c4ca2de3d0bf520b9cb4bb7743a359bd2e6a188d19ce7dffc21d3e7` | offers / settlement |
| P2_DELEGATED_PUZZLE_OR_HIDDEN_PUZZLE | `e9aaa49f45bad5c889b86ee3341550c155cfdd10c3a6757de618d20612fffd52` | standard wallet inner |
| P2_DELEGATED_CONDITIONS | `0ff94726f1a8dea5c3f70d3121945190778d3b2b3fcda3735a1f290977e98341` | delegated-conditions inner |
| P2_CONDITIONS | `1c77d7d5efde60a7a1d2d27db6d746bc8e568aea1ef8586ca967a0d60b83cc36` | conditions-only inner |

(`chia_puzzles_py.programs` ships ~93 constants incl. DAO, VC/credential, pool, and the new
member/restriction puzzles — enumerate with `grep -E '^[A-Z0-9_]+ = bytes.fromhex' programs.py`.)

**Authority-lifecycle analogues (bounded/revocable/rotatable — closest to a custom delegated
authority).** These are the references for the Phase-1 Step-5 authority-lifecycle diff:
- **`Chia-Network/internal-custody`** — CNI custody tool: M-of-N thresholds + timelocked rekeying
  + ACH clawback. Files under `cic/clsp/`: `singleton/prefarm_inner.clsp`,
  `drop_coins/{ach_clawback,ach_completion,rekey_clawback,rekey_completion,p2_new_lock_level}.clsp`,
  `filters/{only_rekey,rekey_and_payment}.clsp`. Mapping: **clawback ≈ revoke, rekey ≈ rotate,
  timelock ≈ expiry.** Its ~59-commit history contains real shipped-then-fixed bugs (see §4d
  D-03/D-13/D-15) — the history is itself ground truth.
- **MIPS / CHIP-0043** (`chia_puzzles/puzzles/mips_puzzles/`) — the canonical "bound a delegated
  puzzle" toolkit: `architecture_puzzles/{m_of_n,n_of_n,1_of_n,restrictions,delegated_puzzle_feeder}.clsp`,
  `member_puzzles/{bls_member,singleton_member,secp256*_member,passkey_member,fixed_puzzle_member}.clsp`,
  `restriction_puzzles/wrappers/{timelock,prevent_condition_opcode,prevent_multiple_create_coins,
  force_assert_coin_announcement,force_coin_message}.clsp`,
  `restriction_puzzles/{enforce_dpuz_wrappers,add_dpuz_wrapper}.clsp`. Restriction validators may
  NOT return conditions — they only inspect and `(x)`. ⚠️ CHIP-0043 states the MIPS ChiaLisp is
  **"not audited yet"** (see §4d D-32).
- **`P2_SINGLETON_OR_DELAYED_PUZHASH`** (in `chia_puzzles`) — the canonical **revocable +
  time-bounded** delegated-payout template: the claim branch pays only on proof the controlling
  singleton is live (`ASSERT_PUZZLE_ANNOUNCEMENT` of the singleton full puzzle hash +
  `ASSERT_MY_COIN_ID`); the delayed branch recovers to a fallback after `ASSERT_SECONDS_RELATIVE`.
  The closest production model for a revoke/expiry escape hatch.

### §2.13 Derived mod hashes (enrichment applied 2026-07-05 — the deferred hashes)

The authority-lifecycle analogue hashes the seed shipped WITHOUT (WO-193 declined to hardcode
unverified values). Derived here from real source and split by trust level.

**A. MIPS / CHIP-0043 restriction & member puzzles — CONSENSUS-CANONICAL** (they ship IN
`chia_puzzles_py`; obtain via `p.<NAME>_HASH`, each cross-checked `== Program.from_bytes(p.<NAME>).get_tree_hash()`).
Verified on `chia_puzzles_py` shipped with `chia-blockchain` 2.7.0:

| MIPS puzzle | Mod hash | Bounded-authority role |
|---|---|---|
| M_OF_N | `de27deb2ebc7f1e1b77e1d38cc2f9d90fbd54d4b13dd4e6fa1f659177e36ed4f` | threshold (distinct-leaf + root, D-21) |
| N_OF_N | `d4394f50cb1d6ef130788db2e69ab0087ef79b0737179f201c1d1d2a52df1e59` | all-of authority |
| ONE_OF_N | `bcb9aa74893bebcfa2da87271b0330bf2773b6391144ae72262b6824d9c55939` | any-of (merkle) authority |
| P2_1_OF_N | `46b29fd87fbeb6737600c4543931222a6c1ed3db6fa5601a3ca284a9f4efe780` | p2 wrapper for 1-of-N |
| P2_M_OF_N_DELEGATE_DIRECT | `0f199d5263ac1a62b077c159404a71abd3f9691cc57520bf1d4c5cb501504457` | m-of-n delegate |
| RESTRICTIONS | `a28d59d39f964a93159c986b1914694f6f2f1c9901178f91e8b0ba4045980eef` | restriction wrapper root |
| ENFORCE_DPUZ_WRAPPERS | `1f94aa2381c1c02fec90687c0b045ef3cad4b458f8eac5bd90695b4d89624f09` | D-16 (bounds can't be curried away) |
| ADD_DPUZ_WRAPPER | `6427724905f2dcf8187300ef9a0436a3c96198e4fcd17101d1ded9bc61c3f3bf` | D-16 wrapper add |
| TIMELOCK | `a6f96d8ecf9bd29e8c41822d231408823707b587bc0d372e5db4ac9733cbea3c` | expiry ≈ timelock (D-15) |
| PREVENT_CONDITION_OPCODE | `046dfa794bb1df14d5dc891b23764a0e31f119546d2c56cdc8df0d31daaa555f` | opcode deny-list (D-18) |
| PREVENT_MULTIPLE_CREATE_COINS | `93b8c8abeab8f6bdba4acb49ed49362ecba94b703a48b15c8784f966547b7846` | exact CREATE_COIN count (D-14) |
| FORCE_ASSERT_COIN_ANNOUNCEMENT | `ca0daca027e5ebd4a61fad7e32cfe1e984ad5b561c2fc08dea30accf3a191fab` | anti-replay pairing (D-11) |
| FORCE_COIN_MESSAGE | `9618c96b30b96362f6c01716a11f76c630a786697d5bac92345f5ff90b882268` | anti-replay message (D-11) |
| FORCE_1_OF_2_W_RESTRICTED_VARIABLE | `4f7bc8f30deb6dad75a1e29ceacb67fd0fe0eda79173e45295ff2cfbb8de53c6` | restricted-variable force |
| BLS_MEMBER | `21a3ae8b3ce64d41ca98d6d8df8f465c9e1bfb19ab40284a5da8479ba7fade78` | terminal auth (AGG_SIG_ME PK dpuz, D-19) |
| BLS_MEMBER_PUZZLE_ASSERT | `0db2c7260209fc59f28c2d188f62d8d85818f61744ade7794d675b4123acef19` | reusable (AGG_SIG_PUZZLE) variant, D-19 |
| BLS_WITH_TAPROOT_MEMBER | `35d2ad31aaf0df91c965909e5112294c57a18354ee4a5aae80572080ec3b6842` | taproot member |
| SINGLETON_MEMBER | `6f1cebc5a6d3661ad87d3558146259ca580729b244b7662757f8d1c34a6a9ad9` | singleton-gated member |
| SINGLETON_MEMBER_WITH_MODE | `a7611d7cf6246399ff07469211d6efed96e47a44fc3be6ac9375aee995b0e010` | singleton member + mode |
| FIXED_PUZZLE_MEMBER | `34ede3eadc52ed750e405f2b9dea9891506547f651290bb606356d997c64f219` | fixed-puzzle member |
| SECP256K1_MEMBER | `2b05daf134c9163acc8f2ac05b61f7d8328fca3dcc963154a28e89bcfc4dbfca` | secp256k1 member |
| SECP256R1_MEMBER | `05aaa1f2fb6c48b5bce952b09f3da99afa4241989878a9919aafb7d74b70ac54` | secp256r1 member |
| PASSKEY_MEMBER | `1d66225b71ec6caf33e3771ebaa7fcd50826fd31844dc8258116b37b3ff3c7ae` | passkey member |
| P2_SINGLETON_OR_DELAYED_PUZHASH | `adb656e0211e2ab4f42069a4c5efc80dc907e7062be08bf1628c8e5b6d94d25b` | revocable + time-bounded payout |

**B. `Chia-Network/internal-custody` — TOOLCHAIN-COMPILED, NOT consensus-canonical.** These do
NOT ship in `chia_puzzles_py`; compiled locally from source at commit
`4cb2b6bcd452596b4fd31f003e4c50d6128c9944` with its own `cic/clsp/include` (`clvm_tools_rs`).
**Treat as implementation-dependent (commit + include set + compiler version can shift them);
use them for structural/behavioral reference, NOT as pinned identity values.**

| internal-custody puzzle | Mod hash (@4cb2b6bc) | Reference for |
|---|---|---|
| prefarm_inner | `66f0fe81cbaf300b32f4b3ca19085ecd5b6378f0449e4c589f8590da0a6b9773` | self-recreate + `check_singleton_and_even` (D-13/D-14), decrement-and-recreate |
| rekey_clawback | `7e81af82627c0907a322df54bcf56732275b58177eb4b29a3eb18ea1fe0b4ff8` | revoke ≈ clawback + rekey-announcement ban (D-13/D-17) |
| rekey_completion | `ef888df7b2edf0fcc20b57fc9dea3a53b761518170b7e3cc97718acbe1e17118` | rotate ≈ rekey; `calculate_coin_id` for parent id (D-01) |
| ach_clawback | `38b68260d64d38397da1cfa1116c5a968432410a9a4568bf7e5f900a0b925bea` | payment clawback |
| ach_completion | `101df03a30c1098e2e9dbc3fff3cd4b75b064457a19ac05fc747d3af69f12564` | payment completion |
| p2_new_lock_level | `6f2fb262b1710a17550a6567ca072e5e982ae5bb029f899cfb336bd320a9de01` | lock-level change |
| p2_merkle_tree | `fa279361042957f4dd2c5dcb9ac082bf4c11f2b02d57fcb547347a4934344bf7` | merkle dispatch |
| filters/only_rekey | `a78393abb073577a1e60e4058e93b603a0bd06c398c87452bff070274d4ae159` | rekey-only condition filter |
| filters/rekey_and_payment | `89cb62c3c6b2fe873f78567143520a0fd6e1fca0f0f24cdc16374f734be6d56a` | rekey+payment filter |

**C. Re-confirmation of the §2 seed canonical NFT/DID/singleton hashes** — all still verified
`hashconst_match=True` on `chia_puzzles_py` shipped with `chia-blockchain` 2.7.0 (SINGLETON_TOP_LAYER_V1_1,
SINGLETON_LAUNCHER, DID_INNERPUZ, NFT_STATE_LAYER, NFT_OWNERSHIP_LAYER, NFT_..._ROYALTIES,
NFT_METADATA_UPDATER_DEFAULT). The seed values in §2 hold on this toolchain.

## §3 CLVM encoding pitfalls (the classics)

- **Sign bit**: big-endian two's-complement; top byte ≥ 0x80 ⇒ negative. `0xFF`=−1,
  `0x00FF`=255. Any `>`/arithmetic on a solution/curry value must be swept across
  0x7f/0x80 and 0xff/0x0100. A "positive" counter/expiry can be negative.
- **Non-minimal encoding (precise, correctly caveated)**: the same int has many byte forms
  (`0x01` and `0x0001` both = 1). The **base CLVM deserializer enforces only upper bounds**
  (errors on impossibly-large sizes / a size prefix > 6 bytes) and does NOT, in the general
  path, reject a merely non-minimal encoding. Canonical encoding **is** enforced as a
  *consensus* requirement in the **block-generator / transactions-generator context** (tied to
  the 0xFE back-reference format at the 2.0 hard fork; canonical-integer enforcement staged
  mempool-first in 2.6.1 → hard fork in 3.0). Don't over-claim "consensus rejects all
  non-minimal atoms"; the load-bearing rule is the next bullet.
- **nil vs 0**: equal as values in most ops; nil serializes `0x80` ≠ zero atom. "Not safe to
  compare CLVM programs in serialized form." Watch solution-field hashing.
- **`sha256tree`**: atom → `(sha256 1 atom)`; pair → `(sha256 2 left right)`. Curry-hash base
  is `(sha256 1 1)`. Off-by-one in reversed param order or base breaks self-hash.

## §4 Bug-class catalog (known-bad patterns)

1. **Unpaired/unasserted announcements** — a `CREATE_*_ANNOUNCEMENT` nothing asserts, or an
   `ASSERT_*` nothing creates ⇒ mint/melt/settlement bugs.
2. **Announcement attribution confusion** — needing a *coin* announcement but asserting a
   *puzzle* announcement (or vice-versa) lets a decoy coin satisfy a binding.
3. **Cross-bundle announcement replay** — assuming an announcement can be borrowed across
   bundles/blocks (it can't; try to exploit code that relies on it).
4. **Blind-sign / graftroot over-authorization** — signing `sha256tree(delegated_puzzle)`
   while the delegated puzzle's conditions depend on the *unsigned* solution ⇒ one signature
   authorizes many outcomes. Fix: `(q . conditions)` quote, no solution dependence.
5. **AGG_SIG_UNSAFE / reused signed message** — replayable across coins/networks.
6. **Self-hash / curry-order error** — recomputed puzzle hash diverges, breaking identity
   pins or announcement bindings (usually fails closed, sometimes opens a hole).
7. **Sign-bit / non-canonical misread** in `>`/arithmetic.
8. **Singleton uniqueness violation** — a second odd `CREATE_COIN`, an even recreation, or a
   reachable melt (`-113`).
9. **Trust-boundary regression** — an authority-gating value taken from the solution instead
   of curried/derived.
10. **Layer redirection** — royalty / recipient / metadata-updater / finalizer / inner not
    pinned to the intended (curried) shape.
11. **Cost/DoS** — unbounded recursion over solution lists; no fail-fast on oversized input.
12. **Amount/fee accounting** — outputs not summing; RESERVE_FEE / dust / change mishandled.

## §4b Real ChiaLisp incidents (the known-bad catalog, with sources)

Primary disclosure lives in **`Chia-Network/post-mortem`**, not CVEs/GHSAs. Study these —
they are the ground-truth precedents an expert pattern-matches against.

- **AGG_SIG_UNSAFE mimics AGG_SIG_ME (2023-05-08; fixed soft-fork @ block 3,630,000).** The
  single most on-point precedent for a delegated/blind-signed mint: because `AGG_SIG_UNSAFE`
  appends nothing, an attacker crafted an UNSAFE message *ending in* `coin_id ‖
  additional_data` to forge a signature byte-identical to an `AGG_SIG_ME`, then swapped in a
  malicious spend (worst in multi-coin bundles where one signer suffices). Lesson: bind
  signatures with domain separation; front any blind signer with a CLVM validation proxy.
  Source: `github.com/Chia-Network/post-mortem/.../2023-05-08-AGG_SIG_UNSAFE-can-mimic-AGG_SIG_ME-condition.md`
- **CAT1 token inflation (CVE-2022-36447 / GHSA-pvjg-jwp3-mrj5; migrated to CAT2 @ height
  2,311,760).** Coin id hashed `parent‖puzzle_hash‖amount` **without validating field
  boundaries**; variable-length `amount` next to fixed-32 `puzzle_hash` let bytes shift across
  the boundary to the same sha256 ⇒ infinite counterfeiting. **The dominant recurring bug =
  missing coin-identity binding.** Fix uses 32-byte component validation + the `coinid`
  operator (CHIP-0011). Note: the 2021 coloured-coins audit did NOT catch this — even audited
  puzzles ship critical flaws. Source: `chia.net/2022/07/29/cat1-vulnerability-explained…`
- **TibetSwap V1 (2023-04-26).** AMM pair-singleton coin id absent from mint/burn
  announcements ⇒ liquidity burned twice; ~50% withdrawn within the hour. Same family as
  CAT1. Source: `blog.kuhi.to/tibetswap-v1-post-mortem`
- **settlement_payments negative-value (2023-05-08).** Offer puzzle allowed negative amounts;
  `-113` could trigger TAIL execution in CATs. Every coin id must be in the offer **nonce** to
  stop one payment satisfying two offers.
- **NFT royalty bypass (CHIP-0046 draft).** Lying in / omitting `trade_prices_list` under-
  declares sale value; the NFT puzzle **cannot verify true price** ⇒ royalty bypass / wash
  trades. On-chain royalties are **not unconditionally enforced** (mitigation is ecosystem-
  level). Source: `github.com/Chia-Network/chips/pull/151`
- **Unbound CLVM cost on mempool (2023-07)** — a `chia_rs` u64 overflow wrapped past the ~5.5B
  bound. **CLVM infinite recursion (2023-01)** — deep recursion exhausted validator memory
  under budget. **FastForward (2025-02)** — invalid/melted singletons accepted into mempool.
- **2026 "AI Siege" (2.6.0/2.6.1/2.7.0; soft-fork @ block 8,655,000).** Chia turned LLM tooling
  inward and found edge cases "never surfaced by traditional auditing": **CLVM integer decoding
  misaligned between Rust and Python (consensus-split risk)**, non-canonical integers billed
  inconsistently, inconsistent amount parsing across helpers, `op_modpow`/`op_div`/`op_mod`/BLS
  mispricing DoS; full consensus fixes at the 3.0 hard fork. Also the **2026 v2.6.1 wallet
  "take offer" exploit** auto-signed *every* spend in a merged tx. Validates a deterministic,
  byte-level, machine-assisted audit over "an auditor glanced at it."
  Source: `chia.net/2026/03/26/chia-2-7-0-combatting-the-ai-siege/`

**Monoculture evidence (why the diff/consensus method matters):** `Chia-Network/Audit-Reports`
shows the **complete** external-audit inventory — NCC Group (consensus 2021), Least Authority
(CAT 2021, ETH bridge 2023, Offers 2023, Permuto 2025), Trail of Bits (CAT 2022). **No public
third-party audit of the singleton, NFT, or DID puzzles.** The entire GitHub Advisory DB has
**one** Chia GHSA (CAT1). Treat any singleton/NFT/DID-derived puzzle as un-audited ground.

## §4c Sentinels, genesis challenges, and the real authority boundary

- **Magic amounts / sentinels are NOT consensus opcodes** — consensus ignores unknown/negative
  codes; higher-level puzzles interpret them: `-10` = ownership-layer owner-assignment (prefix
  `0xad4c` = first 2 bytes of `sha256("Ownership Layer")`), `-24` = state-layer metadata update
  (gated by the curried `METADATA_UPDATER_PUZZLE_HASH`), `-113` = singleton melt (odd, so it
  counts as "the odd output" while suppressed). Don't audit them as if consensus enforces them.
- **AGG_SIG_ME additional_data = the network genesis challenge.** mainnet
  `ccd5bb71…e0e5fbb`; testnet11 `37a90eb5…236615`. This is what makes `_ME` non-replayable
  across coins and across networks (testnet↔mainnet).
- **`coinid` operator (CHIP-0011)** validates a coin id inside CLVM — the direct hardening for
  the CAT1 field-boundary class. Prefer it over hand-rolled `sha256(parent‖ph‖amount)`.
- **The real authority boundary in an NFT/DID mint is the p2 inner puzzle.** NFT owner-
  assignment is gated by `ASSERT_PUZZLE_ANNOUNCEMENT(sha256(DID_full_ph, nft_id))` with **zero
  AGG_SIG**; the DID blesses via `did_innerpuz` **mode-1 = bare `(a INNER_PUZZLE …)`
  pass-through**, so the only signature (if any) comes from the curried p2 inner. Audit that
  p2 inner as the seam where a keyless/bounded custom puzzle lives — it is where authority
  actually is (or isn't).

## §4d Fix-derived review checks (change-history ground truth — D-01…D-33)

The 35 checks below are distilled from how the CANONICAL Chia puzzles were actually FIXED over
time (WO-194 change-history mining). **A real fix in a real canonical puzzle is independent
ground truth**: it proves a bug class existed and shows exactly how Chia's core devs closed it.
Each check carries its upstream evidence so a matching finding can cite proven precedent — wire
this into the Phase-4 **Upstream precedent** field. The incident *narratives* already live in
§4b/§4c; this section is the actionable check-form, so it does not restate the stories.

**Provenance tags:** **[GT-FIX]** strongest — a real code fix in a canonical puzzle (commit SHA,
diff-visible). **[GT-AUDIT]** — a finding in a published external audit (Trail of Bits / Least
Authority / NCC). **[GT-INCIDENT]** — a public post-mortem / CVE. **[INFER]** weaker — inference
from a diff, flagged as such. **Detection:** DIFF = diff-detectable against a canonical puzzle;
ONCHAIN = needs on-chain / consensus / differential verification.

**Highest-value (lead with these on any bounded-authority / delegated-mint target):** D-01
(coin-id via `calculate_coin_id` — CATbleed), D-03 (signed-int range-assert before cap/counter
math), D-06/07/08 (length-commit + tree/merkle domain separation), the D.3 announcement-gated
checks (the announcement-blessing keystone), D-13 (a condition-scan wrapper must not truncate —
shipped-in-review in the closest analogue), D-19b (a claimable quantity must be authority-gated
on EVERY branch — the purest bounded-authority analogue), D-16 (restriction wrappers can't be
curried away), and D-33 (verify BOTH the deployed puzzle hash AND the driver wiring).

### D.1 Coin-ID, amount & value integrity
- **D-01. Coin/parent IDs must use `calculate_coin_id` (32-byte size + `amount > -1` guard), never a bare `sha256` of the three fields.** Guards the coin-id concatenation byte-slide (inflate/melt). Evidence: CVE-2022-36447 / CATbleed [GT-INCIDENT]; `curry-and-treehash.clib:89-94` [GT-FIX]; internal-custody `rekey_completion.clsp` raw-sha256→`calculate_coin_id` [GT-FIX]. CRITICAL / DIFF.
- **D-02. Assert amounts strictly positive before `CREATE_COIN`, except documented sentinels (-113 CAT melt; odd 1-mojo singleton).** Guards negative-amount bypass / the -113 CAT-TAIL offer trick. Evidence: settlement_payments post-mortems 2023-01/05 [GT-INCIDENT]; `settlement_payments.clsp create_coins_for_payment` `(> amount 0)`, commit `0be5eccff` (PR#13773) [GT-FIX]. CRITICAL / DIFF.
- **D-03. Range-assert every amount/counter operand (`>= 0`, `<= remaining`) BEFORE arithmetic — CLVM ints are signed; a negative solution value silently flips a `<=` bound.** Evidence: internal-custody `5f5c9d3` (PR#41) "Assert in_amount to be non-negative" [GT-FIX]; negative-coin-values post-mortem 2021-05 [GT-INCIDENT]. CRITICAL / DIFF (missing assert) + ONCHAIN (negative-input rejection). Gates any cumulative-cap/counter math.
- **D-04. Enforce amount conservation (a recreated amount must not silently decrease); don't let excess become an unbudgeted farmer fee.** Evidence: TOB-Chia-002 [GT-AUDIT]. HIGH / DIFF.
- **D-05. Force the singleton child's amount to `my_amount`, not the inner puzzle's declared amount.** Guards amount-substitution (inner mints a child with an arbitrary amount). Evidence: nft_state_layer `36a70ae8d` [GT-FIX]; DID `deab05048` `my_amount` pin [GT-FIX]. HIGH / DIFF.

### D.2 Hashing & domain separation
- **D-06. Never hash multiple variable-length values by bare concatenation; commit each component's length/size (or use fixed-size fields).** Guards `(sha256 "cl" "vm") == (sha256 "clvm")` field-split bypass. Evidence: TOB-Chia-004 [GT-AUDIT] (abstract root of CATbleed). HIGH / DIFF.
- **D-07. `sha256tree` must use the `1` (leaf) / `2` (internal) domain constants; reject any hand-rolled tree-hash that omits them.** Guards leaf-vs-internal collision that bypasses a tree-hash check. Evidence: TOB-Chia-006 [GT-AUDIT]. HIGH / DIFF.
- **D-08. Merkle proofs must domain-separate leaves (prefix `0x01`) from internal nodes (`0x02`), disjoint from `sha256tree`'s `1`/`2` tags.** Guards second-preimage / type-confusion in membership → forged authority. Evidence: internal-custody `574ae07` (PR#31) + `c2d72de` (PR#44) [GT-FIX]. HIGH / DIFF.

### D.3 Announcement-gated authority (the core delegated-mint mechanic)
- **D-09. A layer that emits a "blessing" announcement (owner-assignment) must FORBID the inner/delegated puzzle from forging it (prefix + exact-length check).** Evidence: nft_ownership_layer `71c7d3a8d` (prefix `0xad4c…`, ban forgery) [GT-FIX]; nft TP `540a130ce` [GT-FIX]; CAT2 `0xcb` morph firewall [GT-FIX]. CRITICAL / DIFF (ban present) + ONCHAIN (forged-announcement rejection). Closest analogue to a mint-authorization announcement.
- **D-10. Order security predicates so short/malformed inputs short-circuit safely (check length BEFORE `substr`/prefix compare).** Evidence: nft_ownership_layer `230d92b6f` (`; lazy eval`) [GT-FIX]. MEDIUM / DIFF + ONCHAIN.
- **D-11. Bind every authorization to a specific partner coin/target (anti-replay): force an `ASSERT_COIN_ANNOUNCEMENT`/`SEND_MESSAGE` pairing, and include the singleton launcher id in any signed/announced message.** Evidence: MIPS `force_assert_coin_announcement.clsp` / `force_coin_message.clsp` [GT-FIX]; nft TP `62a4747c2` (launcher-id in AGG_SIG_UNSAFE msg) [GT-FIX]; DID `edd9b2044` (launcher-id in ownership announcement) [GT-FIX]. HIGH / DIFF + ONCHAIN.
- **D-12. It must NOT be possible to validate a false announcement in an announcement ring.** Evidence: Least Authority Coloured-Coins invariant #9 [GT-AUDIT]; CAT2 ring firewall [GT-FIX]. HIGH / ONCHAIN.

### D.4 Bounding a delegated/inner puzzle (the bounded-authority core)
- **D-13. A wrapper/filter that scans a delegated puzzle's conditions must traverse the ENTIRE list and RETURN the full (possibly morphed) list — never stop early or truncate.** Guards condition-suppression / unchecked-tail leak (append a malicious condition after the accepted one; or the wrapper drops safety conditions). Evidence: internal-custody `5f5c9d3` (PR#41) "conditions accidentally discarded" [GT-FIX]; nft TP `f752863fa` "Make sure all conditions are returned" [GT-FIX]. CRITICAL / ONCHAIN (malicious condition LAST) + DIFF (does every branch tail-recurse?). **Shipped in review in the closest analogue — mandatory.**
- **D-14. Enforce an exact `CREATE_COIN` count/shape from the delegated body — reject BOTH extra coins (over-mint) AND missing outputs (grief).** Evidence: MIPS `prevent_multiple_create_coins.clsp` `(= count 1)` [GT-FIX]; internal-custody `prefarm_inner.clsp check_singleton_and_even` [GT-FIX]; nft_state_layer `649ac8426` odd-child uniqueness [GT-FIX]. CRITICAL / DIFF + ONCHAIN. (A `<= N remaining` counter generalizes the hard `1`.)
- **D-15. Bounds (cap/expiry/counter) must be CURRIED into the puzzle hash (not solution-read) and RE-COMMITTED on every recreation.** Evidence: internal-custody `e297269` (PR#16, timelock moved into hashed STATE, curried into the drop-coin ph) [GT-FIX]. CRITICAL / DIFF (currying boundary) + ONCHAIN (recreated coin re-commits). A solution-supplied bound is the finding.
- **D-16. Prove restriction wrappers cannot be curried away — reconstruct the full puzzle hash WITH the bounds and compare byte-for-byte.** Evidence: MIPS `enforce_dpuz_wrappers.clsp` / `add_dpuz_wrapper.clsp` [GT-FIX]. CRITICAL / byte-equality (not eyeball-diffable).
- **D-17. A spend path must not simultaneously exercise two mutually-exclusive authorities; each mode must affirmatively FORBID emitting the others' announcements/coins.** Guards confused-deputy / mode-confusion (mint also revoking; a clawback also completing the rekey it cancels). Evidence: internal-custody `5f5c9d3` (rekey_clawback bans the rekey announcement) [GT-FIX]; nft TP `d89c0cda6` (collapse -25/-10 to remove the desync surface) [GT-FIX]. HIGH / DIFF + ONCHAIN.
- **D-18. Ban opcodes/conditions that don't belong on a given authority path (deny-list)** — e.g. a delegated mint emitting `AGG_SIG`, a rotation/revocation announcement, a self-melt, or exfiltrating the singleton. Evidence: MIPS `prevent_condition_opcode.clsp` [GT-FIX]. HIGH / DIFF + ONCHAIN.
- **D-19. The terminal authority check must authenticate over the EXACT thing authorized (the delegated puzzle hash); prefer `AGG_SIG_ME` coin-binding unless cross-coin reuse is intended.** Evidence: MIPS `bls_member.clsp = (AGG_SIG_ME PK Delegated_Puzzle)` vs `_puzzle_assert` (`AGG_SIG_PUZZLE`, reusable) [GT-FIX]. HIGH / DIFF.
- **D-19b. A quantity/discrepancy a spend may claim (delta, amount-above-cap, mint count) must be GATED by the authority on EVERY path — never assertable "for free" on the ordinary/default/lineage branch.** Evidence: CAT `6dd8feade` "did not check delta in standard case" — added `(not extra_delta)` so only the TAIL authorizes a nonzero delta [GT-FIX]. CRITICAL / DIFF + ONCHAIN. **The archetypal bounded-authority bug — 1:1 with a per-spend mint cap.**
- **D-19c. When rebuilding/morphing a `CREATE_COIN`, PRESERVE its memo/hint tail (`(c … (r (r condition)))`), never truncate to `(list opcode ph amount)`.** Guards a silent hint/memo drop → recipient wallet can't discover the coin. Evidence: singleton v1→v1_1 `morph_condition` fix `b8f5d98be` [GT-FIX]. HIGH / DIFF.

### D.5 Signature-condition safety
- **D-20. If using `AGG_SIG_UNSAFE`, the signed message MUST be domain-separated so it can neither be replayed across coins NOR mimic an `AGG_SIG_ME` message (must not end with the chain's `additional_data`).** Evidence: AGG_SIG post-mortem / soft-fork @3630000 [GT-INCIDENT]; CHIP erratum #83 [GT-AUDIT]; nft TP `62a4747c2` (launcher-id separator) [GT-FIX]. HIGH / DIFF + ONCHAIN.
- **D-21. Recovery/rotation thresholds must reject the zero-threshold case (`NUM_VERIFICATIONS_REQUIRED > 0`) and count DISTINCT approvals against the committed root.** Evidence: DID `42f2e0719` (`> NUM_VERIFICATIONS_REQUIRED 0`) [GT-FIX]; MIPS `m_of_n.clsp` (distinct-leaf + root check) [GT-FIX]. HIGH / DIFF + ONCHAIN. Touches the revoke/rotate pillar.

### D.6 Input/solution validation & canonical encoding
- **D-22. Validate the structure AND size of every solution input; don't admit unbounded/extra elements (they yield an infinite valid-solution set and can confuse downstream puzzles/TAILs).** Evidence: TOB-Chia-005 [GT-AUDIT]. MEDIUM / DIFF + ONCHAIN.
- **D-23. Treat all externally-supplied encoded inputs (Bech32 offers, memos, metadata) as untrusted; validate fully in ONE place before processing ("parsing before processing").** Evidence: Least Authority Offers Issue B [GT-AUDIT]. MEDIUM / ONCHAIN / code-review.
- **D-24. Reject non-canonical integer encodings (leading zeros) and ensure a one-to-one object↔bytes serialization; the Rust and Python paths must agree on edge cases.** Evidence: NCC-CHIA001-004 [GT-AUDIT]; 2026 canonical-integer / serialization soft forks (2.6.1/2.7.0) [GT-INCIDENT]; chia_rs amount-parsing standardization [GT-INCIDENT]. HIGH (consensus) / ONCHAIN differential.

### D.7 Blind-signing, metadata & operational hygiene
- **D-25. Never blind-sign attacker-supplied spend bundles; a signer must validate (via a CLVM proxy or a bounded on-chain authority) that it only signs intended spends referencing its own coins.** Evidence: 2.6.1 wallet auto-signing-on-take-offer fix [GT-INCIDENT]. CRITICAL / architecture + ONCHAIN. Central to any non-custodial threat model.
- **D-26. Do not render untrusted off-chain NFT metadata as trusted/actionable UI (clickable links).** Evidence: GUI-clickable-links post-mortem (2024-06, PR #2331) [GT-INCIDENT]. MEDIUM / UI review.
- **D-27. Restrict which metadata fields are mutable (append-only URI allowlist); protect immutable fields (hashes, edition info).** Evidence: nft_metadata_updater `662c60da3` (`mu`/`lu`/`u` allowlist) [GT-FIX]. MEDIUM / DIFF. (Relevant only for updateable-metadata NFTs.)
- **D-28. Don't remove a "redundant" defense-in-depth check assuming a lower layer covers it; combine it with overflow-safe cost/limit math.** Evidence: unbound-CLVM-cost-on-mempool post-mortem (2023-07) [GT-INCIDENT]. MEDIUM / code review.
- **D-29. Keep security-relevant commit messages / PR titles out of any public repo interaction; a closed PR still exposes commit SHAs.** Evidence: 2026-05 private-dev-history-leak post-mortem [GT-INCIDENT]. MEDIUM / process.

### D.8 Meta / process (from audit method, not a single fix)
- **D-30. A clean external audit is NOT proof of absence — pair audits with adversarial + differential-vs-standard-artifact testing.** Evidence: Least Authority cleared CAT1 (2021-04); Trail of Bits found the fatal CATbleed bug 14 months later [GT-AUDIT]+[GT-INCIDENT]. Process.
- **D-31. Adopt a fixed invariant checklist and property-test it** (mirror Least Authority Coloured-Coins Suggestion 2): only one genesis; cannot be spent twice; lineage traceable to genesis; inner/delegated puzzle cannot influence the outer authority's behavior; output only of the intended shape/value; no false ring announcements; liveness under a correct puzzle+solution. Evidence: LA invariant list [GT-AUDIT]. Process / property tests.
- **D-32. Do NOT inherit CHIP-0043's "inner puzzles are individually upgradeable so patch-ability substitutes for audit" stance** for anything whose compromise is not individually reversible (a delegated mint's compromise is not). Evidence: CHIP-0043 §Security [GT-AUDIT]. Design posture.
- **D-33. A fix must be WIRED INTO the shipping artifact** — verify the corrected puzzle hash is the one actually curried/referenced (not left behind by a typo) AND that the driver feeds it the right inputs. Evidence: settlement_payments v1.6.1 typo that voided the fix, driver-side (2023-05) [GT-INCIDENT]. HIGH / byte-equality of the deployed hash + driver-wiring review.

## §5 Seed adversarial attack list (extend it)

Try, for any authority/mint/transfer puzzle: raise/preserve a counter; bypass a cap;
extend a time bound via encoding (negative/high-bit/over-ceiling); forge an announcement with
a decoy coin (same message, different announcer); cross-bundle announcement replay; redirect
royalty/recipient/updater/finalizer in the produced coin; reach a privileged branch as the
wrong actor; replay a whole signed spend on a successor coin; cross-install / cross-DID
authority confusion (spend built for A submitted against B); emit a second odd coin; melt when
forbidden; even-amount recreation; non-minimal atom at every solution/curry position;
malformed record lists (improper tail, atom-as-record, extra/missing fields) — verify each
fails closed or is provably neutral (e.g. a decrement never less than items actually created).

**Fix-derived additions (from §4d — each has real upstream precedent):** append a malicious
condition LAST to test a truncating filter (D-13); claim mint quantity on a default/lineage
branch that skips the authority (D-19b); feed a negative solution amount to flip a `<=`/`>` bound
(D-03); hand in a bare delegated puzzle with the bounds curried away (D-16); exercise two
mutually-exclusive modes (mint + revoke/rotate) in one spend (D-17); truncate the memo/hint tail
on a morphed `CREATE_COIN` (D-19c); drive a recovery/rotation with a zero threshold (D-21);
present an internal merkle node as a leaf (D-08); skim output value so the excess becomes a
farmer fee (D-04).

## §6 Assurance ladder (how to weight a finding's evidence)

Two axes decide how much a test substitutes for a human:
- **Oracle**: GT (ground truth — consensus / canonical-diff / independent parser) vs MR
  (model reasoning). Only GT is independent of the monoculture.
- **Input**: EX (exhaustive/random/differential — a real standard artifact or a fuzzer) vs
  HA (hand-authored attacks — bounded to what the model imagined).

Ranking: **GT+EX** (differential-vs-standard, consensus-oracle fuzzing) is strongest — a
genuine second-reviewer substitute. **GT+HA** (consensus-checked hand attacks) is strong but
bounded (verdict trustworthy, coverage limited to imagined attacks). **MR+*** is weakest.
**Novel logic with no canonical analogue is unreachable by the diff — GT+EX cannot touch it;
it stays model-reviewed until a human audit or an independent reimplementation.**

## §7 Common false-positives (don't re-flag)

- **Fail-closed rejection** presented as a vulnerability. If a redirect/forge just makes an
  announcement/assertion unsatisfiable ⇒ intended (Info), not a hole.
- **Per-coin/lineage differences** (launcher/coin ids, chain placement) flagged as
  "non-standard" in a differential — these are on the legitimate-difference ledger.
- **"Self-contained install curries the operator key in the client slot"** in a *test
  fixture* — irrelevant to a mint proof if the mint uses the operator branch (verify which
  branch, don't assume custody).
- **Comment-vs-code drift** with no behavioral effect ⇒ Low/Info, not High.
- **A curried default (e.g. a long expiry) in a sim/test harness** ⇒ deployment-config note,
  not a ChiaLisp flaw, as long as the puzzle enforces whatever is armed.

## §8 Toolchain notes

Semantics are build-specific — always name the pinned build. Relevant: `chia_rs` (the Rust
consensus/CLVM+BLS bindings — defines canonical-encoding + `ASSERT_BEFORE_*` + cost semantics;
the full node depends on it for consensus, Python `clvm` is now reference/tooling),
`chia-blockchain`, `clvm`/`clvm_tools`/`clvm_tools_rs` (compile with `run -d`; do NOT
round-trip compiled CLVM through text + `assemble()` — the printer can render atom `50` as
`g1_multiply` and `assemble()` silently corrupts it). Block-cost ceiling
(`MAX_BLOCK_COST_CLVM = 11,000,000,000`; mempool ~0.5×) and cost are measurable via
`Program.run_with_cost` / `brun --cost`.

- **Rust-vs-Python consensus split is a real risk class.** The two implementations must produce
  byte-identical accept/reject (incl. of non-canonical serializations) or the chain splits —
  which is why canonical/minimal encoding is a *consensus* property. The 2026 "AI Siege"
  post-mortems found CLVM integer decoding **misaligned between Rust and Python**. No public
  Python-vs-Rust *differential fuzzer* is documented (the parity infra that exists is
  Rust-internal + a shared binding test suite); `clvm_rs` does ship a dedicated
  `fuzz/fuzz_targets/canonical_serialization.rs`. If a project claims Python-vs-Rust
  differential testing, treat it as **unverified** until shown.
- **Cost anchors** (worst-case, not happy-path): `CREATE_COIN`=1,800,000, `AGG_SIG_*`=1,200,000,
  BLS pairing verify=3,000,000 base, MALLOC 10/byte of return, 12,000/byte of serialized
  puzzle+solution. Unbounded recursion/fan-out over solution-controlled lists can push a
  legitimate spend past the mempool limit and **grief-lock the coin** — bound the adversarial
  worst case.
- **Ladder bombs**: CLVM back-references (`0xFE`) form DAGs that expand exponentially as trees
  (~200 bytes / ~30 levels → gigabytes). Use the **non-back-reference deserializer** for
  untrusted CLVM.

## §9 Sources (seed — primary; extend as reviews add)

Canonical puzzles/config (raw): `raw.githubusercontent.com/Chia-Network/chia_puzzles/main/puzzles/…`
(`condition_codes.clib`, `singleton_top_layer_v1_1.clsp`, `singleton_launcher.clsp`,
`nft_puzzles/nft_state_layer.clsp`, `nft_puzzles/nft_ownership_layer.clsp`,
`nft_puzzles/nft_ownership_transfer_program_one_way_claim_with_royalties.clsp`,
`did_puzzles/did_innerpuz.clsp`, `curry-and-treehash.clib`, `singleton_truths.clib`);
`chia-blockchain/main/chia/types/condition_opcodes.py`, `.../consensus/default_constants.py`,
`.../util/initial-config.yaml`; `clvm_rs/main/src/serde/parse_atom.rs`,
`clvm_rs/main/fuzz/fuzz_targets/canonical_serialization.rs`.
CHIPs: `github.com/Chia-Network/chips/blob/main/CHIPs/` — chip-0011 (AGG_SIG 43–48, `coinid`),
chip-0014 (ASSERT_BEFORE_* 84–87, prev-tx-block, ephemeral), chip-0025 (SEND/RECEIVE_MESSAGE
66/67), chip-0035 (= DataLayer, NOT signatures), chip-0046 PR#151 (royalty bypass).
Docs: `chialisp.com/{conditions,clvm,costs,singletons,nfts,cats,offers,dids,standard-transactions,chialisp-currying,common_issues,attacks-and-countermeasures}/`;
`docs.chia.net/{coin-set-costs,coin-set-security,guides/crash-course/*}`.
Bounded-authority analogues: `github.com/Chia-Network/internal-custody` (`cic/clsp/…`),
`github.com/Chia-Network/chia_puzzles/tree/main/puzzles/mips_puzzles` (CHIP-0043 MIPS),
`github.com/Chia-Network/chips` (chip-0043), and `p2_singleton_or_delayed_puzhash.clsp`.
Incidents/audits: `github.com/Chia-Network/{post-mortem,Audit-Reports}`,
`osv.dev/vulnerability/GHSA-pvjg-jwp3-mrj5`, `chia.net/2022/07/29/cat1-vulnerability-explained…`,
`blog.kuhi.to/tibetswap-v1-post-mortem`, `chia.net/2026/03/26/chia-2-7-0-combatting-the-ai-siege/`.
(Full URL list + the WO-192 web-research synthesis are in the project brief
`.dev/ai/subtask-comms/2026-07-04-wo192-chialisp-reviewer-research-brief.md` of the originating
project. The §4d fix-derived checks D-01…D-33, with full commit-SHA provenance, come from the
WO-194 change-history mining,
`.dev/ai/research/2026-07-04-chia-network-chialisp-change-history-insights.md`.)

## §10 Run log (append below, newest last)

<!-- Append dated entries here per the format at the top. -->

### 2026-07-05 — First live run: quantity+time-bounded keyless DID-inner delegated mint [target class: did / custom]
- CANONICAL-DIFF-GAP / LESSON: a bounded-authority puzzle can be a **fixed condition emitter**
  (builds every condition itself from DATA records) instead of a **delegated-puzzle runner** (runs
  `(a puzzle_reveal solution)` and filters the result). When it is a fixed emitter, the D-13
  truncating-filter and D-18 opcode-injection bug classes are **structurally absent from that
  branch** — there is no attacker-supplied condition list to leak or filter. The review focus moves
  from "does the filter return the whole list" to "is the DATA-driven emission itself count/shape-
  bounded, and can the operator reach the delegated-runner branch at all" (here: only the Client
  branch runs `(a …)`, gated by `AGG_SIG_ME(CLIENT)`; the operator branch cannot reach it).
- BASIS: canonical-diff (vs internal-custody `prefarm_inner`/`rekey_clawback`, which ARE
  delegated-runners that must filter) + on-chain-consensus (live testnet over-cap/expiry rejections).
- REUSABLE CHECK: classify each authority branch as emitter-vs-runner FIRST. For an emitter branch,
  prove the emitted condition list is a pure function of curried params + bounded data (count k gated
  by the cap on every record); for a runner branch, apply D-13/D-14/D-18 to the returned list.

- PITFALL (non-exploitable, but a real canonical divergence): a cumulative counter decrement
  `(- REMAINING k)` whose non-negativity is enforced **indirectly** by a separate loop cap-check
  (`(> (+ count 1) REMAINING) -> (x)`) rather than an explicit range-assert (D-03). Safe **iff**
  loop-pass ⟺ `k <= REMAINING` ⟹ decrement ≥ 0 — the two must be logically coupled through the SAME
  k. Confirm the decrement result is never EMITTED (as a CREATE_COIN / recreation) on a path where
  the guard has not yet run. In this target the decremented next-hash is computed eagerly (a defun
  arg) but only emitted as the cons-tail *after* the guard's `(x)` would fire, so it is unreachable.
- BASIS: canonical-diff (vs internal-custody `handle_payment` `(assert (not (> 0 in_amount)))`, D-03)
  + on-chain-consensus (over-cap raises GENERATOR_RUNTIME_ERROR).
- REUSABLE CHECK: when a decrement lacks its own `>= 0` assert, prove guard-pass ⟹ decrement ≥ 0
  through a shared variable AND that no emitted condition depends on the decrement on an un-guarded
  path; else it is a real underflow finding.

- LESSON (self-hash decisive test): the strongest single check on an N-param on-chain self-curry
  (a puzzle that recomputes its own curried hash for `ASSERT_MY_PUZZLEHASH` / self-recreation) is a
  **sign-byte-boundary sweep** comparing the in-puzzle math to the real SDK `Program.curry(...)
  .get_tree_hash()` at the counter/atom values {…,127,128,255,256,65535,65536,…}. A reversed-param
  or `(sha256 1 1)`-base off-by-one, or a bad integer encoding, breaks exactly at 0x7f/0x80 etc.
  Here ref==SDK held at every boundary AND the reconstructed did_inner/full-singleton matched the
  REAL `DID_INNERPUZ_MOD` / `SINGLETON_TOP_LAYER_MOD` — that is CANONICAL-DIFF ground truth for the
  novel self-curry.
- BASIS: canonical-diff (SDK `Program.curry` oracle).
- REUSABLE CHECK: sweep the self-curry vs SDK curry across sign-byte boundaries; cross-check the
  composed layers against the real canonical mods via `<MOD>.curry(...).get_tree_hash()`.

- FALSE-POSITIVE (don't re-flag): (1) `branch_selector = <any truthy>` routing to the same branch as
  `= 1` (boolean dispatch; verify byte-identical output, then it's intended). (2) Eager `count-records`
  walking the full untrusted list before the cap-guard → cost O(list) not O(cap): over-cap always
  raises (never enters a block) and in-cap lists are small; self-inflicted, no value impact (measured
  5000 elems ≈ 0.02 s). (3) The graftroot client branch signing `sha256tree(delegated_puzzle)` only —
  standard `p2_delegated` pattern, safe iff the client's delegated puzzles fix their conditions.
- NOVEL-ATTACK residual the diff CANNOT reach: the **cumulative-cap INDUCTION** across recreations
  ("lifetime mints ≤ initial cap"). Each step is GT-verified (self-curry ref==SDK, single byte-forced
  CREATE_COIN, `ASSERT_MY_PUZZLEHASH` pins the true counter, on-chain chain proof) but the induction
  over the coin lifetime is model-reasoning — no canonical puzzle carries a cross-recreation mint
  counter (internal-custody decrements a coin's *mojo amount*, not an abstract counter). This is the
  narrow residual an independent human audit / second-team reimplementation must close.
