#!/usr/bin/env python3
"""Freeze-rule linter for NORMS.md.

NORMS.md says norm IDs are per-namespace and never renumbered, and that every
UNENFORCED entry carries accepted-risk + accepted-by. This is the machine it
names. It checks the current file against every version of NORMS.md in git
history reachable from HEAD, so it needs no base ref, only full history.

Fails (exit 1) when:
  - an ID that any earlier version held is missing now (removed or renumbered);
  - an ID appears as an entry more than once;
  - a new ID is not above every ID its namespace has ever held (gap-closing or
    reuse; IDs are only ever appended);
  - an UNENFORCED entry lacks accepted-risk or accepted-by.

Failure mode, named: if CI does not run this (skipped, disabled, shallow
clone), the freeze rule is UNENFORCED again. A shallow clone is reported, not
passed silently.

Usage: python3 tools/check_norm_ids.py [--file NORMS.md]
"""
import argparse
import re
import subprocess
import sys

# An entry is a list item that opens with a bold ID: "- **CB-01** — ...".
ENTRY = re.compile(r"^- \*\*([A-Z]+)-(\d+)\*\*", re.MULTILINE)


def entries(text):
    """Return [(id, body)] in file order; body runs to the next entry or heading."""
    found = list(ENTRY.finditer(text))
    out = []
    for i, m in enumerate(found):
        end = found[i + 1].start() if i + 1 < len(found) else len(text)
        heading = re.search(r"^#", text[m.end():end], re.MULTILINE)
        if heading:
            end = m.end() + heading.start()
        out.append((f"{m.group(1)}-{m.group(2)}", text[m.start():end]))
    return out


def number(norm_id):
    ns, n = norm_id.rsplit("-", 1)
    return ns, int(n)


def check(current, history):
    """current: text of NORMS.md now. history: [(label, text)] of earlier versions.

    Returns a list of error strings; empty means pass.
    """
    errors = []
    now = entries(current)
    ids_now = [i for i, _ in now]

    seen = set()
    for i in ids_now:
        if i in seen:
            errors.append(f"{i}: appears more than once")
        seen.add(i)

    held_before = {}
    for label, text in history:
        for i, _ in entries(text):
            held_before.setdefault(i, label)
    for i, label in sorted(held_before.items()):
        if i not in seen:
            errors.append(f"{i}: held in {label}, missing now (IDs are never removed or renumbered)")

    top = {}
    for i in held_before:
        ns, n = number(i)
        top[ns] = max(top.get(ns, 0), n)
    for i in ids_now:
        if i in held_before:
            continue
        ns, n = number(i)
        if n <= top.get(ns, 0):
            errors.append(f"{i}: new ID at or below {ns}-{top[ns]:02d}, the highest {ns} ID history holds (gap-closing or reuse)")

    for i, body in now:
        if "UNENFORCED" in body:
            for field in ("accepted-risk", "accepted-by"):
                if field not in body:
                    errors.append(f"{i}: UNENFORCED without {field}")
    return errors


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def history_of(path):
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        sys.exit("check_norm_ids: shallow clone; history is incomplete, so the freeze rule "
                 "cannot be checked. Fetch full history (fetch-depth: 0).")
    out = []
    for sha in git("log", "--format=%H", "--", path).split():
        try:
            out.append((sha[:7], git("show", f"{sha}:{path}")))
        except subprocess.CalledProcessError:
            pass  # the commit that deleted the file; the commit before it is still read
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--file", default="NORMS.md")
    args = ap.parse_args()
    with open(args.file, encoding="utf-8") as f:
        current = f.read()
    history = history_of(args.file)
    errors = check(current, history)
    for e in errors:
        print(f"FAIL {e}")
    n = len(entries(current))
    print(f"check_norm_ids: {n} entries, {len(history)} earlier versions, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
