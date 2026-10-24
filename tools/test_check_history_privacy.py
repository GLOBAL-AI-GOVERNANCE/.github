"""Adversarial tests for reachable-history attribution policy."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("check_history_privacy.py")
SPEC = importlib.util.spec_from_file_location("check_history_privacy", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def strict(kind, value):
    return MODULE.approved_trailer(kind, value, exact=True, allow_dependabot_signoff=True)


class StrictTrailerPolicyTests(unittest.TestCase):
    """--exact-trailers --allow-dependabot-signoff"""

    def test_exact_dependabot_service_signoff_passes(self):
        self.assertTrue(
            strict(
                "Signed-off-by", "dependabot[bot] <support@github.com>"
            )
        )

    def test_support_email_with_other_name_fails(self):
        self.assertFalse(
            strict("Signed-off-by", "Another Bot <support@github.com>")
        )

    def test_dependabot_looking_name_with_wrong_email_fails(self):
        self.assertFalse(
            strict("Signed-off-by", "dependabot[bot] <wrong@example.com>")
        )

    def test_dependabot_service_identity_is_not_a_coauthor(self):
        self.assertFalse(
            strict("Co-authored-by", "dependabot[bot] <support@github.com>")
        )

    def test_unapproved_human_signoff_fails(self):
        self.assertFalse(
            strict("Signed-off-by", "Example Person <person@example.com>")
        )

    def test_unapproved_human_coauthor_fails(self):
        self.assertFalse(
            strict("Co-authored-by", "Example Person <person@example.com>")
        )

    def test_canonical_project_attribution_passes(self):
        self.assertTrue(
            strict(
                "Signed-off-by",
                "Global AI Governance <288799817+GLOBAL-AI-GOVERNANCE@users.noreply.github.com>",
            )
        )

    def test_existing_github_service_attribution_passes(self):
        self.assertTrue(
            strict("Reviewed-by", "GitHub <noreply@github.com>")
        )

    def test_identity_must_match_exactly(self):
        self.assertFalse(
            strict(
                "Signed-off-by",
                "Impostor dependabot[bot] <support@github.com>",
            )
        )


class DefaultTrailerPolicyTests(unittest.TestCase):
    """Default policy: trailer must name an approved identity."""

    def test_canonical_attribution_passes(self):
        self.assertTrue(MODULE.approved_trailer(
            "Signed-off-by", "Global AI Governance <288799817+GLOBAL-AI-GOVERNANCE@users.noreply.github.com>"))

    def test_unapproved_human_fails(self):
        self.assertFalse(MODULE.approved_trailer("Co-authored-by", "Example Person <person@example.com>"))

    def test_dependabot_service_signoff_not_accepted_without_flag(self):
        self.assertFalse(MODULE.approved_trailer("Signed-off-by", "dependabot[bot] <support@github.com>"))

    def test_dependabot_flag_only_adds_signoff(self):
        self.assertTrue(MODULE.approved_trailer(
            "Signed-off-by", "dependabot[bot] <support@github.com>", allow_dependabot_signoff=True))
        self.assertFalse(MODULE.approved_trailer(
            "Co-authored-by", "dependabot[bot] <support@github.com>", allow_dependabot_signoff=True))


if __name__ == "__main__":
    unittest.main()
