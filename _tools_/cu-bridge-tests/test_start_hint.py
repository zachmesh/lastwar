"""Tests for the hint `cu_bridge.py start` prints after the run starts: it appears only when a requested app has no `always` approval record in
$CU_HOME/app-approvals.json (the old line, printed after every start, was read as a first-use signal), names only the requested apps that lack
one, and is labelled a hint, not a request. The control-link line stays. Like the other bridge tests these are SKIPPED while `_queue_/claimed/`
holds a file.

Run: python3 -m unittest discover -s _tools_/cu-bridge-tests
"""
from __future__ import annotations

import json

from test_cu_bridge import BridgeCase

APP = "com.lastwar.ios"
OTHER = "com.example.other"
SECRET_ID = "com.example.private-tool"


class StartHint(BridgeCase):
    def setUp(self):
        super().setUp()
        self.home = self.root / "cuhome"
        self.home.mkdir()
        self.env["CU_HOME"] = str(self.home)

    def store(self, *apps, schema="cu-app-approvals/v1"):
        (self.home / "app-approvals.json").write_text(json.dumps({"schema": schema, "apps": [{"bundleId": a, "by": "owner", "grantedAt": "2026-11-22T19:53:00Z"} for a in apps]}))

    def start(self, *extra):
        r = self.run_bridge("start", "--task", "demo", *extra)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("run_id", r.stdout.split("\n\n")[0])                      # the JSON block stays first
        self.assertIn("control-link run-", r.stdout)                            # and the control-link line stays
        self.assertNotIn("first use only", r.stdout + r.stderr)                 # the old sentence never comes back
        return r.stdout

    def test_an_approved_app_prints_no_hint_and_keeps_the_control_line(self):
        self.store(APP, SECRET_ID)
        out = self.start("--app", APP)
        self.assertNotIn("hint:", out)
        self.assertIn("Control the run from a real terminal:", out)
        self.assertNotIn("Approve the app", out)

    def test_an_app_without_a_record_gets_a_hint_that_says_what_it_is(self):
        self.store(OTHER, SECRET_ID)
        out = self.start("--app", APP)
        self.assertIn(f"hint: {APP} has no 'always' approval record, so the run asks a human to approve it through the control-link (a hint, not a request)", out)
        self.assertNotIn(SECRET_ID, out)                                        # the other approved apps are never named
        self.assertNotIn(OTHER, out)

    def test_a_missing_store_means_no_records(self):
        out = self.start("--app", APP)
        self.assertIn(f"hint: {APP} has no 'always' approval record", out)

    def test_only_the_requested_apps_that_lack_a_record_are_named(self):
        self.store(APP)
        out = self.start("--app", f"{APP},{OTHER}")
        self.assertIn(f"hint: {OTHER} has no 'always' approval record", out)
        self.assertNotIn(f"{APP},", out.split("hint:")[1].split("\n")[0])

    def test_an_unreadable_or_foreign_store_says_so_instead_of_guessing(self):
        (self.home / "app-approvals.json").write_text("{not json")
        self.assertIn("hint: the app approval record could not be read", self.start("--app", APP))
        self.store(APP, schema="something-else/v9")
        self.assertIn("hint: the app approval record could not be read", self.start("--app", APP))

    def test_the_store_is_only_read_never_written(self):
        self.store(OTHER)
        before = (self.home / "app-approvals.json").read_bytes()
        self.start("--app", APP)
        self.assertEqual((self.home / "app-approvals.json").read_bytes(), before)
