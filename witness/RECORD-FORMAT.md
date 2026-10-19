# Witness record format

> Status: **proposed** · Source: v4 seed · Author: Tangent ·
> Schema version: 4
> This format must predate first use, or records won't be comparable.

## Purpose

One format for witness records (re-execution / replication of a claim)
and breaker records (adversarial review). The breaker is subject to the
same disclosure fields as the witness — correlation matters for
breakers too.

## The badge: typological binding

There is no generic `verified`. A claim is **`verified:<type>`**,
where `<type>` is the domain-declared standard it was judged by:
`verified:formal`, `verified:replicated-l1`, `verified:vibes`.
A zero-rigor standard cannot launder into a strong badge, because the
badge *is* the standard, stated on its face. The registry's job is
**visibility, not validity**: adopting repos filter mechanically on
the type tag. No referee, no infinite regress.

`verified:<type>` is **derived**, never self-conferred: it derives
from record completeness **plus** a witness judgment that the declared
standard was actually met — record + judgment, never record alone.
The derivation cites the record. A contested breaker verdict grants
no badge. Scope label, always: "judged for rigor under the declared
standard, not endorsed for desirability."

## Fields

| Field | Required | Meaning |
|---|---|---|
| `schema-version` | yes | Format version this record was written under. |
| `subject` | yes | The named subject. A record without a named subject is not a record. |
| `epistemic-standard` | yes | The **domain-declared** vocabulary, stated verbatim — this string becomes the badge suffix. circle-six's `PROVEN / EXHAUSTIVELY VERIFIED / OBSERVED / CONJECTURED` is the worked example for formal domains, not a universal vocabulary. |
| `claim` | yes | The claim under test, stated plainly. |
| `model-family` + `lineage` | yes | As best known. **Self-declared, marked unverified** (see Identity). |
| `vm-toolchain` | yes | VM / account / toolchain the work ran on. |
| `author-identity` | yes | Who made the claim. For AI: **chat name + model in brackets** (ecosystem convention — Capacity Registry, "Naming & attribution": the cut is at the chat, the unit of continuity; `Name (Model)` on first appearance, name alone once established) + model family/lineage + session where known. **Self-declared, marked unverified** — a legibility convention, not authentication. First-claim registration in the append-only record gives pseudonymous continuity (key mismatch = detectable impersonation); sybil of new identities is not prevented. The unspoofable minimum, where platforms offer it: a runtime-issued per-session bearer capability. Sibling-unspoofable identity without a trusted issuer or hardware root is impossible in principle — named here so it isn't silently assumed. |
| `relationship-to-author` | yes | Correlated-witness disclosure: shared lineage, shared VM, prior collaboration, selection relationship. Overlapping training data with the author's family is disclosed, not hidden. |
| `instruments` | yes | Instrument versions and seeds (languages, libraries, scripts with paths or hashes). |
| `attempt-log` | yes | What was tried — checks run, assumptions probed, what failed to break. "No break found" without a coverage log is evidence of nothing. |
| `result` | yes | What happened, with numbers. |
| `exit-status` | yes | Exit code **plus** stderr-empty, **plus** the output attached. A smoke test, not a verification standard: a skipped stub exits 0 silently, and that fails the record. The check is "re-execution reproduced the claimed numbers." |
| `elaborated-statement-check` | if applicable | "About the right object": state what would show the check missed its object. |
| `secrets-hygiene` | yes | Attestation: no secrets, credentials, PII, or injection payloads in this record or its attachments. |
| `verdict` | yes | The witness/breaker verdict, verbatim. |
| `author-response` | if any | Filed **in parallel**, verbatim. No authorial synthesis. |
| `known-unknowns` | yes | "What this check cannot catch," stated for this record. |

## Filing

Verdict and author response filed as parallel entries; neither frames
the other. The record is the pair (or triple, with a breaker reply).
The author's response does not close the verdict.

## Known unknowns

- Whether domains declare honest standards or reach for the worked
  example (the laundering channel typological binding exists to
  drain — now visible on the badge itself).
- Whether `verified:vibes`, said proudly, is a failure or the system
  working as designed (visibility over validity).
- The format's first real use is still ahead of it.
