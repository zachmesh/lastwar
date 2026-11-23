"""Tests that `queue.py next` never names a unit whose window has closed. pick_key sorts by expiry first, so an expired unit
used to sort ahead of every live one: on 2026-11-23 it named an expired priority 1 growth fill while 75 live units waited.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import re
import subprocess
from datetime import datetime, timedelta, timezone

from test_serves import PoolCase


def iso(delta_minutes):
    return (datetime.now(timezone.utc) + timedelta(minutes=delta_minutes)).strftime("%Y-%m-%dT%H:%M:%SZ")


class NextSkipsExpired(PoolCase):
    def unit(self, regular, priority, expires_in, activity="x-activity"):
        """Enqueue a live unit, then move its expiry (minutes from now, negative = past) in the file."""
        r = self.queue("enqueue", "--regular", regular, "--activity", activity, "--est-minutes", "5", "--priority", str(priority),
                       "--serves", "made up", "--expires-at", iso(180))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        unit = re.search(r"queued (\S+)", r.stdout).group(1)
        path = self.path("inbox", unit)
        text = path.read_text()
        path.write_text(re.sub(r"(?m)^expires_at:.*$", f"expires_at: {iso(expires_in)}" if expires_in is not None else "expires_at:", text, count=1))
        return unit

    def next(self, *extra):
        return self.queue("next", *extra)

    def test_an_expired_priority_one_unit_does_not_beat_a_live_priority_two_unit(self):
        expired = self.unit("building-queues-growth-fill", 1, -25)
        live = self.unit("building-queues", 2, 120)
        r = self.next()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(r.stdout.strip(), live)
        self.assertNotEqual(r.stdout.strip(), expired)
        self.assertIn(f"skipping 1 expired unit(s)", r.stderr)
        self.assertIn(expired, r.stderr)                                              # the pass record shows the filter working

    def test_with_only_expired_units_next_names_nothing(self):
        self.unit("building-queues-growth-fill", 1, -1)
        self.unit("building-queues", 2, -600)
        r = self.next()
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(r.stdout.strip(), "")
        self.assertIn("skipping 2 expired unit(s)", r.stderr)

    def test_a_unit_that_expires_in_the_future_or_never_is_still_handed_out(self):
        soon = self.unit("building-queues", 3, 2)
        self.assertEqual(self.next().stdout.strip(), soon)
        self.path("inbox", soon).unlink()
        never = self.unit("research-queue", 3, None)
        self.assertEqual(self.next().stdout.strip(), never)

    def test_the_order_among_live_units_is_unchanged_earlier_expiry_first(self):
        later = self.unit("building-queues", 1, 120)
        sooner = self.unit("research-queue", 3, 30)
        self.assertEqual(self.next().stdout.strip(), sooner)
        self.assertNotEqual(sooner, later)

    def test_the_budget_form_skips_it_too(self):
        self.unit("building-queues-growth-fill", 1, -25)
        live = self.unit("building-queues", 2, 120)
        self.assertEqual(self.next("--budget-minutes", "15").stdout.strip(), live)

    def test_the_deadline_command_ranks_only_live_units(self):
        expired = self.unit("building-queues-growth-fill", 1, -25)
        live = self.unit("building-queues", 2, 120)
        r = self.queue("deadline", "--unit", live, "--expires-at", iso(100), "--reason", "test")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("rank 1", r.stdout)                                             # the expired unit is not ahead of it
        self.assertNotEqual(expired, live)
