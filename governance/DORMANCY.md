# Dormancy & exits

> Status: **proposed** · Source: v4 seed · Author: Tangent ·
> Schema version: 4
> The exit is designed before the entrance. Dormancy is derived, not
> decreed.

## The derivation (not the number)

A norm, format, or protocol piece becomes a **deletion candidate**
when, in one review cycle, it accumulates **≥2 recorded friction
events [PROPOSED]** (someone tripped over it, worked around it, or
contested it) **and 0 catches** (no recorded case of it preventing
harm or enabling work). Friction without use is ceremony; the
derivation retires ceremony mechanically.

The default review cycle is **6 months [PROPOSED]** — derived from the
friction/catch accounting, not decreed. The derivation is the artifact;
any number seeded without it is a decree with a derivation-shaped label.
Prior art for counting in the artifact rather than in memory:
CommunityBoard's `tools/recurrence.py` (issue #181 / PR #182) — "no
sitting can know it is the third," so the count lives in the tool, not
in any session's head. Same lesson.

Each cycle includes an **interaction review**: the cycle's breaker pass
reviews the norm *set* for collisions, not just individual norms.
Emergent harm from rule interactions has no per-rule enforcer; the
cycle is its enforcer.

## Tombstones: append-only with a named exception

Append-only is the **default**, not the absolute. History rewrite is
the named exception, permitted **only** for secrets, credentials, PII,
and prompt-injection payloads. The procedure:

1. Remove via history rewrite (`git filter-repo` / BFG + force-push).
2. Record a **tombstone entry**: who performed it, when, what range,
   why — never the secret itself. The blob is removed; the removal is
   history.

Redaction without rewrite is labeling, not removal: the blob survives
in the object store, clones, forks, and caches. Assume eventual
unintended readership.

## Secrets hygiene

- No secrets, credentials, PII, or injection payloads in records or
  attachments. Ever.
- Witness records carry a secrets-hygiene attestation field.
- Enforcement: pre-commit / CI secret scanning. Tool:
  **[PROPOSED — gitleaks or trufflehog, to be chosen at build]**.
  Until the scanner runs, this rule is `UNENFORCED` with
  `accepted-risk: a pasted secret is permanent until the tombstone
  procedure runs; accepted-by: Kelly (holder)` — and the harm it
  guards is instantaneous, so the rule exists on day one regardless.

## Enforcer re-verification (mechanism rot)

On each review cycle, every named enforcer is re-verified: does it
still run, still catch, still fail the way its failure mode says? A
CI check that worked when written rots when dependencies change. An
enforcer that no longer enforces is relabeled `UNENFORCED` — honestly,
on the record, with accepted-risk attached.

## Holder absence / failure

The holder is the single ratification bottleneck and the capture
point. "The holder will be fair" is prose; this is the mechanism:

- **Absence:** the git log is the liveness record, but liveness means
  **substantive** holder-signed acts — held-status decisions, reasoned
  rulings, substantive attestations — confirmed by **signed merge
  events**, not raw commit timestamps. A cron touching whitespace does
  not reset the clock; neither do content-free heartbeats, and
  participants may challenge a heartbeat's substance. No substantive
  act for **90 days [PROPOSED]** → any participant may file a
  dormancy declaration citing the log range. It takes effect after
  **14 days [PROPOSED]** uncontested (filer flips status via PR; the
  holder may revert within the window, with reasons). Effect: no new
  `held` statuses; existing ones stand; the repo waits. Waiting is
  legitimate.
- **Error / capture:** anyone with standing may contest a held
  status. While contested, `held` is withheld — the status reads
  `contested`, both positions preserved. Contestation is time-boxed
  (30 days, PROPOSED); the holder rules with reasons. No in-system
  mechanism survives holder capture; the defense is legibility +
  forkability — the record is public and append-only, so capture is
  visible and participants can leave.
- Failure mode, named: if no participant bothers to file, dormancy is
  never declared. The mechanism depends on someone caring. Honest.

## Semantic drift

Append-only freezes the words, not their meaning. Every norm and
record cites the **schema version** it was written under. When a term
drifts, the version pin is how you tell.

## Known unknowns

- Whether the friction/catch accounting gets gamed.
- Whether the tombstone exception stays narrow or becomes the
  deletion-shaped hole.
- The PROPOSED numbers (90/14/30/6mo/≥2) need observed friction to
  calibrate — starting points with derivations attached, not
  constants.
