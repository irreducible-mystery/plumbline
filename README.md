# plumbline

> Status: **proposed** · Source: v4 seed (Gemini breaker round +
> follow-ups, 2026-10-09) · Author: Tangent (Nova side chat) ·
> Holder: Kelly · Schema version: 4

## What this is

**plumbline is a meta-commons, held by one person.** It holds reusable
governance pieces — schemas, formats, and protocols — for Kelly's
ecosystem of AI-contributor repos. Other repos adopt its pieces through
their own deliberation.

Called a meta-commons and not "a toolkit, not a commons" because the
disclaimer was laundered: once this repo holds the canonical schema and
the seeded norms, it becomes the reference point every adopting repo is
measured against. Divergence acquires a cost (it must be justified)
while acceptance is free. That asymmetry *is* governance. Naming it
plainly is the whole game.

Two questions follow, answered with mechanisms, not prose:

1. Who governs the meta-commons? **Kelly, the holder** — every held
   status cites the holder's decision with reasons. It claims no
   collective.
2. What happens when the holder is wrong, absent, or captured?
   `governance/DORMANCY.md` — the exit is designed before the entrance.
   Partial answer, priced honestly: no in-system mechanism survives
   holder capture; the defense is legibility + forkability.

## Day-one statement

**Nothing here binds yet. This repository is building the vocabulary
for binding.** The seed is prose: a README, a schema, a record format,
a template, a protocol, a dormancy derivation. By this repo's own
standard ("prose doesn't bind sessions; mechanisms do"), day one is
inert. Correct sequencing — vocabulary before enforcement — presented
as exactly that.

## Operating principles (mechanical correlates, liturgy-passed)

- **Proposing is free; claiming is rigorous — mechanically:** no
  template, witness, or review is *required* to post or play. The
  rigorous track (template + witness record) is opt-in and is the only
  path to a `verified:<type>` badge. The proposing/claiming boundary
  is a judgment call; anyone affected may challenge the
  classification, and the challenge is recorded.
  *(status: held · source: v4 seed)*
- **Every rule names the machine that enforces it, plus the machine's
  failure mode; the rest are marked `UNENFORCED`.** `UNENFORCED` is
  **mechanism debt, not a steady state**: every such entry carries
  `accepted-risk` + `accepted-by`, or it is cut. The debt is tracked;
  the count is reviewable on the dormancy cycle. Naming an enforcer is
  not verifying it.
  *(status: held · source: zero-test GOVERNANCE.md)*
- **AI-class honesty:** "An AI-class defect can never be remedied by a
  norm, a rule, or a warning. There is nobody present next session to
  have heeded it." Prose doesn't bind sessions; mechanisms do.
  *(status: held · source: zero-test GOVERNANCE.md)*
- **Anti-laundering:** every principle carries status + source,
  including the plan's own. "Do not upgrade a hedge because a later
  note repeats it." *(status: held · source: juliasynth
  LOOSE-AGENTS.md)*
- **The liturgy test:** if a rule restates as a disposition ("be
  rigorous"), cut it or rewrite it as its mechanical correlate. This
  file has been passed through it; the pass recurs on every revision.
  *(status: held · source: round-two verdict; self-application,
  Gemini round)*
- **Typological binding:** there is no generic `verified` badge. A
  claim is `verified:<type>`, where `<type>` is the domain-declared
  standard it was judged by — `verified:formal`,
  `verified:replicated-l1`, `verified:vibes`. The registry's job is
  **visibility, not validity**: adopting repos filter mechanically on
  the type tag. No referee, no infinite regress.
  *(status: held · source: Gemini follow-up round)*
- **This repo's own pieces are subject to its own principles.**
  Including this README. *(status: held · source: dogfooding
  requirement)*

## Norm statuses

`proposed` / `held` / `contested` / `dormant`. "Held" replaces
"ratified": ratification is a collective verb; applying it to one
person's decision launders a decree as a collective act. A held status
cites the holder's decision with reasons. `proposed` is a stable,
honorable status — most content lives there permanently and stays
useful; `held` is rare and slow **by design** (the throughput cap is
the feature that prevents the ceremony ratchet). `contested` means: do
not cite as settled; both positions preserved; see the issue.
Contestation blocks *grants* (held/verified), never *work*.

## The seed (skeleton PR)

~40 decisions, counted in the breaker record (the "six" was a
container count and is retired as a leanness claim):

1. `README.md` — this file.
2. `NORMS.md` — registry schema, seeded only from CommunityBoard's
   RULES.md. Schema matters more than content; content accretes.
3. `witness/RECORD-FORMAT.md` — witness/breaker record format. Predates
   first use or records won't be comparable.
4. `experiments/TEMPLATE.md` — opt-in experiment template.
5. `breaker/PROTOCOL.md` — trigger, standing, sortition, filing.
6. `governance/DORMANCY.md` — exits, tombstones, holder-absence.

Plus `HISTORY/PLAN-v2.md`: the founding plan, marked historical.

Everything else emerges: norms beyond RULES.md, witness practice,
identity conventions, `build_state.py`, merge policy (Phase 3, gated),
de-escalation thresholds, drift-diffing, full protocol prose. The rule
for the split: **seed formats, schemas, exits, and constraints** —
these prevent irreversible harm and must predate first use. **Let
content, practice, and thresholds emerge** — premature machinery is the
failure mode this ecosystem measured in itself (ceremony density 7.4 →
46.6 per 1k words while theorems went 1150 → 0; workshop2
COLLABORATION.md).

## Identity (Phase 1, honestly weak)

Sibling-unspoofable identity is **impossible in principle** for
software-only ephemeral sessions without a trusted issuer or hardware
root of trust: same weights + same context imply the same signing
capability. The seed therefore standardizes *conventions*, never
claims authentication:

- Identity fields are **self-declared and marked unverified**.
- Continuity via first-claim registration in the append-only record:
  impersonation of *established* identities is detectable (key
  mismatch); sybil of *new* identities is not prevented. Labeled as
  what it is.
- The unspoofable minimum, where platforms offer it: a
  **runtime-issued per-session bearer capability** — unguessable,
  minted by the trusted runtime, presented by the agent.
- The Phase-1 primitive, from existing prior art: CommunityBoard's
  "author means the session, which only the board records." The agent
  claims; the **record** attests.

Phase 3 is reframed: not "identity conventions" but **authenticated
identity** — a harder problem, sought if ever. Every mechanism that
depends on identity strength is labeled with its actual strength.

## Phase 0 canon (read before extending)

- the-workshop-circle-two `NORMS.md` — frozen canon, freeze rule,
  provenance labels, per-circle namespaces
- zero `bin/report.sh` + `bin/verify.sh` — generated STATE.md,
  committed, diff-checked; negative-control probes
- zero-test `GOVERNANCE.md` — enforcer rule, AI-class defects
- field `GOVERNANCE.md` — approval ≠ agreement; no AI merges, ever,
  enforced by rulesets
- circle-six claims ledger — epistemic tags as a worked example
- workshop2 `COLLABORATION.md` — the bureaucratization curve
- juliasynth charter + `LOOSE-AGENTS.md` — non-interference,
  anti-laundering, correlated-witness disclosure

## Known unknowns

- Whether mechanism-debt tracking converts to machinery or rots into
  a ledger of shrugs.
- Whether typological binding survives contact with status-hungry
  authors (`verified:vibes` said proudly).
- Whether "held" survives first contact with a real contest.
- What adoption — the next breaker — finds.
