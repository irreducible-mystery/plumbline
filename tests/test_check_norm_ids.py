"""Negative controls for tools/check_norm_ids.py: each break must be caught."""
import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from check_norm_ids import check, entries  # noqa: E402

OK = "accepted-risk: low; accepted-by: holder"
BASE = f"""## Held

- **CB-01** — one. *enforcer: UNENFORCED · {OK}*
- **CB-02** — two. *enforcer: UNENFORCED · {OK}*
- **CB-03** — three. *enforcer: CI*

## Proposed

- **PL-01** — plumbline one. *enforcer: CI*
"""


class FreezeRule(unittest.TestCase):
    def errors(self, current):
        return check(current, [("base", BASE)])

    def test_unchanged_passes(self):
        self.assertEqual(self.errors(BASE), [])

    def test_append_passes(self):
        self.assertEqual(self.errors(BASE + "- **CB-04** — four. *enforcer: CI*\n"), [])

    def test_removal_fails(self):
        current = BASE.replace(f"- **CB-02** — two. *enforcer: UNENFORCED · {OK}*\n", "")
        self.assertTrue(any("CB-02" in e and "missing" in e for e in self.errors(current)))

    def test_renumbering_fails(self):
        current = BASE.replace("**CB-03**", "**CB-04**")
        errs = self.errors(current)
        self.assertTrue(any("CB-03" in e and "missing" in e for e in errs))

    def test_gap_closing_fails(self):
        history = [("v1", BASE + "- **CB-05** — five. *enforcer: CI*\n")]
        current = BASE + "- **CB-05** — five. *enforcer: CI*\n- **CB-04** — late. *enforcer: CI*\n"
        self.assertTrue(any("CB-04" in e and "gap-closing" in e for e in check(current, history)))

    def test_duplicate_fails(self):
        current = BASE + "- **CB-03** — again. *enforcer: CI*\n"
        self.assertTrue(any("more than once" in e for e in self.errors(current)))

    def test_unenforced_without_accepted_risk_fails(self):
        current = BASE + "- **CB-04** — four. *enforcer: UNENFORCED*\n"
        errs = self.errors(current)
        self.assertIn("CB-04: UNENFORCED without accepted-risk", errs)
        self.assertIn("CB-04: UNENFORCED without accepted-by", errs)

    def test_body_stops_at_heading(self):
        # CB-03's body must not absorb the next section's text.
        body = dict(entries(BASE))["CB-03"]
        self.assertNotIn("Proposed", body)


if __name__ == "__main__":
    unittest.main()
