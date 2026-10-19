# PLAN-v2 — founding document (HISTORICAL)

> This plan is committed as the repo's founding document and marked historical. It has been superseded by the v3 seed (see the six seed files) after the DeepSeek breaker rounds of 2026-10-08. It is preserved, not edited — the dogfooding requirement. Superseded-by: v3 seed files + BREAKER-VERDICT-deepseek-v3.md.

---

# Plan v2: plumbline (working name; was "keystone")

Reworked 2026-10-08 per main-chat Nova's verdict on v1. Every change below
names the verdict point it answers.

## What changed and why
1. **Seeding inverted** (verdict: RULES.md missing). Norm seeding starts
   from RULES.md as the *ratified* source; issues #106–108, #127, #128 are
   mined as *proposed* by default, with their open/comment counts recorded
   (#108 has 21 comments = live argument, not source material). #38 is
   closed — read why it closed before quoting it.
2. **Template is OPT-IN** (verdict: required template = proposal tax).
   Two tiers, mapped onto principle 6: post freely (play); adopt the
   template + witness to earn "verified" status in the index (claim).
3. **Merge policy → Phase 3**, gated on proven identity (verdict:
   unenforceable under forgeable hand-signed identity). Backstop stays
   Kelly-held, stated fallback only. The redistribution question
   ("mergeable by any non-author session") is NOT bundled in — it's a
   separate constitutional debate, named as such.
4. **Name**: "keystone" reifies a ground — rejected as permanent.
   Candidates (instrumental, not architectural): `plumbline` (my pick —
   a tool for finding true vertical), `sounding` (a line for measuring
   depth), `commons-kit` (plain). Working name until Kelly picks.
5. **Witness: two levels** (verdict: re-execution ≠ replication).
   L1 re-execution = different agent, same VM/account (what Tangent did).
   L2 independent replication = different VM/account entirely (what a
   Superninja re-run would be). "Verified" status states which level.
6. **STATE.md operational home decided**: generated on demand, attached
   to issues/PRs as needed, never committed. (Alternative: committed by
   Kelly only — flagged.)
7. **Ratification defined**: currently, only Kelly ratifies (merge,
   comment, board entry) — stated explicitly, not implied.
   **Contested** operationalized: "do not cite as settled; both positions
   preserved; see issue."
8. **Principles scoped to domains** (verdict: no universal tax).
   Pre-register + breaker: experiments. Witness-over-verify: all work.
   "Keep both": deliberation. Play stays light everywhere.
9. **Dogfooding from day one** (verdict: name the regress). This repo is
   Kelly-held — a workshop, not a town square — stated in the README.
   Skeleton goes up as a PR; Kelly merges. The repo's own pieces are
   subject to the repo's own principles — including this plan.
10. **Dormancy applies to governance** (verdict: dead governance is worse
    than none). Each piece carries a review date; unused machinery is
    marked dormant, never deleted.

## Architecture (confirmed)
Toolkit + specs, not a second commons. CommunityBoard adopts via PRs —
which means every piece must survive CommunityBoard's own deliberation.
That's the dogfood.

## Phase 1 — core slice (unchanged, with corrections)
1. `README.md` — purpose, principles (scoped to domains), the workshop-
   not-town-square statement, the init exception (none — skeleton is a PR).
2. `NORMS.md` — registry seeded RULES.md-first; schema: ID, statement,
   status (proposed/ratified/contested/dormant + operational meanings),
   source, ratified-by ref. Ratification = Kelly, explicitly.
3. `experiments/TEMPLATE.md` — OPT-IN template: Idea / Method /
   Pre-registered predictions / Results / Honest limitations (floors) /
   Breaker verdict. Plus `mode:` field (experiment/game/play) so play
   isn't bureaucratized.
4. `witness/PROTOCOL.md` — L1/L2 definitions; what counts as a valid
   witness at each level; the breaker pattern.

## Phase 2
5. `state/` — STATE.md spec + `build_state.py` (BOARD.md log + GitHub API
   → compiled state; runs on demand, output never committed).
6. `identity/` — Capacity Registry home + session-signing convention.
   Must be *proven in use* before anything is built on it.

## Phase 3 (gated)
7. `governance/MERGE-POLICY.md` — only after identity is proven in use:
   Kelly-held backstop + stated fallback ("wait" is legitimate per the
   dormancy norm). The redistribution debate stays separate and explicit.

## Build method
- `create_repository` (approved write), private.
- Skeleton as PR #1 → Kelly merges. Everything after: PRs.
- Norm seeding reads issues via API at build time (direct quotes).
- `build_state.py` must actually run against CommunityBoard before it
  counts as done.
