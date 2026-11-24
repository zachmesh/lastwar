"""Tests for the computer-use tree the bridge runs (CU-721 option (a)): the default is the worktree cu-integrator keeps under
~/dtadpole/computer-use-wt/ (not the pinned checkout behind ~/computer-use), CU_PROJECT overrides it, and the daemon prints, records and shows the path in force
(`project=PATH (source: env | default)`). A fake tree under a temporary HOME stands in for the worktree. Like the other bridge tests these are SKIPPED while
`_queue_/claimed/` holds a file.

Run: python3 -m unittest discover -s _tools_/cu-bridge-tests
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from test_cu_bridge import BridgeCase, FAKE_SERVER, BRIDGE_SOURCE

DEFAULT = "~/dtadpole/computer-use-wt/lastwar-bridge"


class ProjectPath(BridgeCase):
    def default_tree(self):
        """A HOME of its own whose default worktree holds the fake server: the bridge started without CU_PROJECT finds it there."""
        home = self.root / "home"
        server = home / "dtadpole/computer-use-wt/lastwar-bridge/_tools_/computer-use-mcp"
        server.mkdir(parents=True)
        (server / "server.mjs").write_text(FAKE_SERVER)
        self.env.pop("CU_PROJECT")
        self.env["HOME"] = str(home)
        return home / "dtadpole/computer-use-wt/lastwar-bridge"

    def test_the_checked_in_default_is_the_worktree_and_not_the_pinned_checkout(self):
        source = BRIDGE_SOURCE.read_text()
        self.assertIn(f'DEFAULT_PROJECT = "{DEFAULT}"', source)
        self.assertNotIn('str(Path.home() / "computer-use")', source)
        comment = " ".join(source[:source.index("DEFAULT_PROJECT =")].splitlines()[-8:])
        for word in ("CU-721", "CU-720", "CU_PROJECT still overrides", "a313b4f2c"):
            self.assertIn(word, comment)

    def test_a_daemon_without_cu_project_runs_the_default_worktree_and_says_so(self):
        tree = self.default_tree()
        r = self.run_bridge("ensure")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        out = json.loads(r.stdout)
        self.assertEqual(out["project"], f"project={tree} (source: default)")
        self.assertIn(f"cu_bridge: project={tree} (source: default)", r.stderr)
        listing = json.loads(self.run_bridge("runs").stdout)["bridge"]["daemons"][0]
        self.assertEqual((listing["project"], listing["project_source"]), (str(tree), "default"))
        self.assertIn(f"project={tree} (source: default)", (self.root / "_tools_" / "state" / "cu_bridge.log").read_text())

    def test_cu_project_overrides_the_default_and_is_reported_as_env(self):
        out = json.loads(self.run_bridge("ensure").stdout)
        self.assertEqual(out["project"], f"project={self.root / 'fake'} (source: env)")

    def test_a_missing_default_worktree_refuses_to_start_and_names_the_path(self):
        self.env.pop("CU_PROJECT")
        self.env["HOME"] = str(self.root / "emptyhome")
        r = self.run_bridge("ensure")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("dtadpole/computer-use-wt/lastwar-bridge/_tools_/computer-use-mcp/server.mjs", r.stdout + r.stderr + (self.root / "_tools_/state/cu_bridge.log").read_text())

    def test_status_and_restart_show_the_path_of_the_daemon_that_owns_the_run(self):
        self.run_bridge("ensure")
        run = self.run_bridge("start", "--task", "demo")
        run_id = json.loads(run.stdout.split("\n\n")[0])["run_id"]
        status = self.run_bridge("status", "--run-id", run_id)
        body, _end = json.JSONDecoder().raw_decode(status.stdout)
        self.assertEqual(body["bridge_project"], f"project={self.root / 'fake'} (source: env)")
        self.assertIn(f"cu_bridge: project={self.root / 'fake'} (source: env)", status.stderr)
        restarted = self.run_bridge("restart")
        self.assertEqual(json.loads(restarted.stdout)["project"], f"project={self.root / 'fake'} (source: env)")

    def test_the_path_is_the_daemons_own_not_the_callers_shell(self):
        self.run_bridge("ensure")
        self.env["CU_PROJECT"] = "/somewhere/else"
        out = json.loads(self.run_bridge("ensure").stdout)
        self.assertEqual(out["project"], f"project={self.root / 'fake'} (source: env)")

    def test_a_daemon_that_started_before_the_bridge_recorded_the_path_says_unknown(self):
        self.run_bridge("ensure")
        info = next((self.root / "_tools_" / "state").glob("cu_bridge-*.json"))
        data = json.loads(info.read_text())
        for key in ("project", "project_source"):
            data.pop(key)
        info.write_text(json.dumps(data) + "\n")
        out = json.loads(self.run_bridge("ensure").stdout)
        self.assertIn("project=unknown (source: unknown)", out["project"])
