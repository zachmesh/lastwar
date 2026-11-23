"""Tests for the device token's longer lease and the exclusive (quiet window) token: `token-acquire --lease-minutes N` (1 to 60, default 15, a renewal
takes it again) and `--exclusive`, which makes `claim` refuse every other executor while the token is live. An ordinary token never blocks a claim.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import datetime
import re

from test_serves import PoolCase


def minutes_until(out: str) -> float:
    stamp = re.search(r"until (\S+Z)", out).group(1)
    until = datetime.datetime.strptime(stamp, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    return (until - datetime.datetime.now(datetime.timezone.utc)).total_seconds() / 60


class Lease(PoolCase):
    def token(self, *extra, executor="cu-integrator"):
        return self.queue("token-acquire", "--executor", executor, *extra)

    def test_the_default_lease_is_fifteen_minutes_and_a_longer_one_is_a_flag(self):
        self.assertAlmostEqual(minutes_until(self.token(executor="operator").stdout), 15, delta=0.5)
        self.queue("token-release", "--executor", "operator")
        r = self.token("--lease-minutes", "30")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertAlmostEqual(minutes_until(r.stdout), 30, delta=0.5)
        self.assertIn("lease_until:", (self.pool / "claimed" / "device-token.md").read_text())

    def test_the_lease_is_bounded(self):
        for bad in ("0", "-5", "61", "600"):
            r = self.token("--lease-minutes", bad)
            self.assertEqual(r.returncode, 2, bad)
            self.assertIn("outside 1 to 60", r.stdout)
        self.assertFalse((self.pool / "claimed" / "device-token.md").exists())
        self.assertEqual(self.token("--lease-minutes", "60").returncode, 0)

    def test_the_holders_renewal_takes_the_flag_again_and_a_plain_renewal_goes_back_to_fifteen(self):
        self.assertAlmostEqual(minutes_until(self.token("--lease-minutes", "25").stdout), 25, delta=0.5)
        renewed = self.token("--lease-minutes", "40")
        self.assertIn("token renewed by cu-integrator", renewed.stdout)
        self.assertAlmostEqual(minutes_until(renewed.stdout), 40, delta=0.5)
        self.assertAlmostEqual(minutes_until(self.token().stdout), 15, delta=0.5)

    def test_another_executor_is_still_refused_while_the_lease_is_live(self):
        self.token("--lease-minutes", "30")
        r = self.token(executor="operator")
        self.assertEqual(r.returncode, 1)
        self.assertIn("token held by cu-integrator until", r.stdout)
        self.assertEqual(self.queue("token-release", "--executor", "operator").returncode, 1)
        self.assertEqual(self.queue("token-release", "--executor", "cu-integrator").returncode, 0)
        self.assertEqual(self.token(executor="operator").returncode, 0)


class QuietWindow(PoolCase):
    def setUp(self):
        super().setUp()
        self.unit = self.enqueue("--serves", "upkeep")

    def claim(self, executor="operator", *extra):
        return self.queue("claim", "--unit", self.unit, "--executor", executor, *extra)

    def still_in_inbox(self):
        return self.path("inbox", self.unit).exists() and not self.path("claimed", self.unit).exists()

    def test_an_exclusive_token_makes_claim_refuse_every_other_executor(self):
        r = self.queue("token-acquire", "--executor", "cu-integrator", "--lease-minutes", "25", "--exclusive")
        self.assertIn("(exclusive)", r.stdout)
        refused = self.claim()
        self.assertEqual(refused.returncode, 1, refused.stdout + refused.stderr)
        self.assertIn(f"cannot claim {self.unit}: the device token is held exclusively by cu-integrator until", refused.stdout)
        self.assertIn("--ignore-token", refused.stdout)
        self.assertTrue(self.still_in_inbox())                                           # nothing moved, no attempt counted
        self.assertNotIn("attempts: 1", self.path("inbox", self.unit).read_text())

    def test_the_holder_itself_and_the_emergency_flag_can_claim(self):
        self.queue("token-acquire", "--executor", "cu-integrator", "--exclusive")
        self.assertEqual(self.claim("cu-integrator").returncode, 0)
        self.queue("release", "--unit", self.unit)
        self.assertEqual(self.claim("operator", "--ignore-token").returncode, 0)

    def test_release_and_expiry_end_the_quiet_window(self):
        self.queue("token-acquire", "--executor", "cu-integrator", "--exclusive")
        self.assertEqual(self.claim().returncode, 1)
        self.queue("token-release", "--executor", "cu-integrator")
        self.assertEqual(self.claim().returncode, 0)
        self.queue("release", "--unit", self.unit)
        token = self.pool / "claimed" / "device-token.md"
        token.write_text("---\nclaimed_by: cu-integrator\nclaimed_at: 2026-11-23T10:00:00Z\nlease_until: 2026-11-23T10:15:00Z\nexclusive: true\n---\n\n# Device token\n")
        self.assertEqual(self.claim().returncode, 0)                                     # an expired exclusive token blocks nothing

    def test_an_ordinary_token_never_blocks_a_claim_so_the_operators_own_token_does_not_deadlock_it(self):
        self.queue("token-acquire", "--executor", "operator-token-name")
        self.assertEqual(self.claim("some-other-name").returncode, 0)

    def test_a_renewal_keeps_the_token_exclusive(self):
        self.queue("token-acquire", "--executor", "cu-integrator", "--exclusive")
        self.assertIn("(exclusive)", self.queue("token-acquire", "--executor", "cu-integrator", "--lease-minutes", "30").stdout)
        self.assertEqual(self.claim().returncode, 1)

    def test_the_flags_are_in_the_help(self):
        out = self.queue("token-acquire", "--help").stdout
        self.assertIn("--lease-minutes", out)
        self.assertIn("--exclusive", out)
        self.assertIn("--ignore-token", self.queue("claim", "--help").stdout)
