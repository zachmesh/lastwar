"""Tests for the definition block (`## Brief`) every unit minted from the roster carries: the regular and its roster line, its activity folder with the
digest to read first, the regular-to-activity map and the route card (when those files exist in the repository), and the stop rule. One test per path
that mints: plan, sweep (and its fix-ups), sync, enqueue.

Run: python3 -m unittest discover -s _tools_/queue-tests
"""
from __future__ import annotations

import datetime
import json
import re
import subprocess

from test_serves import PoolCase, QUEUE

TOOLS = QUEUE.parent
REAL = json.loads((TOOLS / "regulars.json").read_text(encoding="utf-8"))
BRIEF = REAL["brief"]
STOP = "If the digest does not cover a step, stop with 'blocked by prerequisite' and say which step; never improvise."


class Briefed(PoolCase):
    def make_pointer_files(self, *keys):
        for key in keys or BRIEF:
            path = self.repo / BRIEF[key]
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("x\n")

    def roster(self, ids=None, **change):
        """The real roster (all of it when ids is None - the sweep's fix-up regulars must be in it) with changes to single entries."""
        items = [dict(r, **change.get(r["id"], {})) for r in REAL["regulars"] if ids is None or r["id"] in ids]
        path = self.repo / f"roster-{'-'.join(sorted(ids or ['all']))}.json"
        path.write_text(json.dumps({**REAL, "regulars": items}))
        return path

    def bodies(self):
        return {p.stem: p.read_text() for p in (self.pool / "inbox").glob("*.md")}

    def block(self, text):
        self.assertIn("## Brief (definition pointer, from the roster)", text)
        return text.split("## Brief (definition pointer, from the roster)", 1)[1]

    def check_full(self, text, regular):
        item = next(r for r in REAL["regulars"] if r["id"] == regular)
        block = self.block(text)
        self.assertIn(f"This unit is the regular `{regular}`: {item['name'].rstrip('.')}.", block)
        self.assertIn(f"the activity folder `_activities_/{item['activity']}/` (the folder is named for the activity, not the regular id): "
                      "read its `rule-digest.md` first, then its `INDEX.md`.", block)
        self.assertIn(f"The map of every regular to its activity folder is `{BRIEF['map']}`.", block)
        self.assertIn(STOP, block)
        self.assertIn(f"Routes and stop reasons: `{BRIEF['route_card']}` (routes in `{BRIEF['routes']}`).", block)
        self.assertIn(f"Red lines and snap: `{BRIEF['red_lines']}`.", block)


class Paths(Briefed):
    def setUp(self):
        super().setUp()
        self.make_pointer_files()

    def test_plan_writes_the_block_from_the_roster(self):
        r = self.queue("plan", "--regulars-json", str(self.roster({"mail"})), "--hours", "2")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        bodies = self.bodies()
        self.assertTrue(bodies)
        for text in bodies.values():
            self.check_full(text, "mail")

    def test_sweep_writes_the_block_on_the_sweep_units_and_their_fixups_and_keeps_the_task_text(self):
        tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).isoformat()
        r = self.queue("sweep", "--regulars-json", str(self.roster()), "--date", tomorrow)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        bodies = self.bodies()
        sweeps = {k: v for k, v in bodies.items() if k.startswith("zero-sweep")}
        self.assertTrue(sweeps)
        for text in sweeps.values():
            self.check_full(text, "zero-sweep")
            self.assertIn("## Task - pre-reset zero sweep", text)                         # the sweep task text is still there, after the block
            self.assertLess(text.index("## Brief"), text.index("## Task - pre-reset zero sweep"))
        fixups = {k: v for k, v in bodies.items() if k.startswith("harvest")}
        self.assertTrue(fixups)                                                           # the fix-up units go through the same funnel
        for text in fixups.values():
            self.check_full(text, "harvest")

    def test_sync_writes_the_block(self):
        mail = next(dict(r, due=True) for r in REAL["regulars"] if r["id"] == "mail")
        due = self.repo / "due.json"
        due.write_text(json.dumps({"items": [mail]}))
        r = self.queue("sync", "--due-json", str(due))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        (text,) = self.bodies().values()
        self.check_full(text, "mail")

    def test_enqueue_of_a_roster_regular_writes_it_and_any_other_regular_does_not(self):
        r = self.queue("enqueue", "--regular", "radar", "--est-minutes", "5")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.check_full(self.bodies()[re.search(r"queued (\S+)", r.stdout).group(1)], "radar")
        r = self.queue("enqueue", "--regular", "not-in-the-roster", "--activity", "x-activity", "--est-minutes", "5", "--serves", "upkeep")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertNotIn("## Brief", self.bodies()[re.search(r"queued (\S+)", r.stdout).group(1)])

    def test_every_regular_in_the_real_roster_gets_its_own_folder_and_roster_line(self):
        for item in (r for r in REAL["regulars"] if r["id"] != "zero-sweep"):      # the sweep pair is staged by `sweep`, tested above
            self.setUp()
            self.make_pointer_files()
            r = self.queue("enqueue", "--regular", item["id"], "--est-minutes", "5", "--segment", str(item.get("segment", "")))
            self.assertEqual(r.returncode, 0, f"{item['id']}: {r.stdout}{r.stderr}")
            block = self.block(next(iter(self.bodies().values())))
            self.assertIn(f"`_activities_/{item['activity']}/`", block, item["id"])
            self.assertIn(item["name"].rstrip("."), block, item["id"])


class Pointers(Briefed):
    def test_a_pointer_to_a_file_the_repository_lacks_is_left_out_but_the_folder_and_the_stop_rule_stay(self):
        r = self.queue("enqueue", "--regular", "mail", "--est-minutes", "5")
        block = self.block(next(iter(self.bodies().values())))
        self.assertNotIn(BRIEF["map"], block)
        self.assertNotIn("Routes and stop reasons", block)
        self.assertNotIn("Red lines", block)
        self.assertIn("`_activities_/mail-rewards/`", block)
        self.assertIn(STOP, block)

    def test_each_pointer_appears_only_when_its_own_file_exists(self):
        self.make_pointer_files("map", "route_card")
        self.queue("enqueue", "--regular", "mail", "--est-minutes", "5")
        block = self.block(next(iter(self.bodies().values())))
        self.assertIn(f"`{BRIEF['map']}`", block)
        self.assertIn(f"Routes and stop reasons: `{BRIEF['route_card']}`.", block)           # no routes file: no 'routes in'
        self.assertNotIn("routes in", block)
        self.assertNotIn("Red lines", block)

    def test_activity_ref_overrides_the_activity_folder(self):
        roster = self.roster({"mail"}, mail={"activity_ref": "mail-rewards-v2"})
        self.make_pointer_files("map")
        r = self.queue("plan", "--regulars-json", str(roster), "--hours", "2")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        block = self.block(next(iter(self.bodies().values())))
        self.assertIn("`_activities_/mail-rewards-v2/`", block)
        self.assertNotIn("`_activities_/mail-rewards/`", block)

    def test_the_block_stays_short(self):
        self.make_pointer_files()
        self.queue("enqueue", "--regular", "mail", "--est-minutes", "5")
        self.assertLess(len(self.block(next(iter(self.bodies().values()))).split()), 140)


class RealRepository(Briefed):
    def test_every_regulars_digest_and_index_exist_in_the_tracked_tree(self):
        top = subprocess.run(["git", "-C", str(TOOLS), "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
        tracked = set(subprocess.run(["git", "-C", top, "ls-files", "_activities_"], capture_output=True, text=True).stdout.split("\n"))
        for item in REAL["regulars"]:
            ref = item.get("activity_ref") or item["activity"]
            self.assertIn(f"_activities_/{ref}/rule-digest.md", tracked, item["id"])
            self.assertIn(f"_activities_/{ref}/INDEX.md", tracked, item["id"])

    def test_the_roster_brief_names_four_repository_paths(self):
        self.assertEqual(set(BRIEF), {"map", "route_card", "routes", "red_lines"})
        for value in BRIEF.values():
            self.assertTrue(value.startswith("_records_/") and not value.startswith("/") and ".." not in value, value)
