"""Tests that every unit the queue mints from the roster carries a serves line: regulars.json gives each entry a serves key
(default upkeep) and plan and sync copy it into the units they mint. This must hold before enqueue refuses a unit without one.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from test_serves import QUEUE, PoolCase, load_queue_module

ROSTER = QUEUE.parent / "regulars.json"


def roster():
    return json.loads(ROSTER.read_text())["regulars"]


class RosterEntries(unittest.TestCase):
    def test_every_roster_entry_has_a_serves_key_and_the_default_is_upkeep(self):
        for item in roster():
            self.assertIn("serves", item, item["id"])
            self.assertTrue(str(item["serves"]).strip(), item["id"])
        self.assertEqual({item["serves"] for item in roster()}, {"upkeep"})
        self.assertEqual(load_queue_module().DEFAULT_SERVES, "upkeep")

    def test_the_roster_file_keeps_its_compact_layout(self):
        raw = ROSTER.read_text()
        self.assertEqual(json.dumps(json.loads(raw), separators=(",", ":"), ensure_ascii=False), raw)


class Minting(PoolCase):
    def mint(self, item):
        queue = load_queue_module()
        planned = datetime.now(queue.LOCAL_TZ).replace(second=0, microsecond=0)
        return queue._produce_for_window(str(self.pool), item, planned)

    def serves_of(self, unit):
        return self.frontmatter_line("inbox", unit, "serves")

    def test_a_unit_minted_for_a_roster_regular_carries_its_roster_serves(self):
        item = next(i for i in roster() if i["id"] == "mail")
        unit = self.mint(item)
        self.assertEqual(self.serves_of(unit), "serves: upkeep")

    def test_a_custom_serves_in_the_entry_is_copied_and_a_missing_one_defaults_to_upkeep(self):
        item = dict(next(i for i in roster() if i["id"] == "help"), serves="snapshot of the help bubble")
        self.assertEqual(self.serves_of(self.mint(item)), "serves: snapshot of the help bubble")
        bare = {k: v for k, v in next(i for i in roster() if i["id"] == "gifts").items() if k != "serves"}
        self.assertEqual(self.serves_of(self.mint(bare)), "serves: upkeep")

    def test_the_serves_survives_claim_and_complete_for_a_minted_unit(self):
        unit = self.mint(next(i for i in roster() if i["id"] == "mail"))
        self.assertEqual(self.queue("claim", "--unit", unit, "--executor", "tester").returncode, 0)
        self.assertEqual(self.frontmatter_line("claimed", unit, "serves"), "serves: upkeep")
        self.assertEqual(self.queue("complete", "--unit", unit, "--status", "done", "--summary", "x").returncode, 0)
        self.assertEqual(self.frontmatter_line("done", unit, "serves"), "serves: upkeep")

    def test_a_full_sync_mints_only_units_that_carry_serves(self):
        r = self.queue("sync")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        units = sorted((self.pool / "inbox").glob("*.md"))
        self.assertGreater(len(units), 5)
        for path in units:
            front = path.read_text().split("\n---\n", 1)[0]
            self.assertRegex(front, r"(?m)^serves: \S", path.name)


if __name__ == "__main__":
    unittest.main()
