"""Tests for the bridge's owner-idle setting (OD-20261123-27): the launcher line LAUNCHER_OWNER_IDLE_SECONDS in cu_bridge.py (0 until CU-720 is on our tree,
then None), an explicit CU_OWNER_IDLE_SECONDS in the daemon's environment that wins, and the default (nothing set: the lock's own 300). A fake MCP server
records the variable it was started with; the daemon prints `owner_idle_seconds=N (source: launcher | env | default)` at start, `ensure` and `restart`
repeat it, and `status` and `runs` show the daemon's own value, so a drift back to 300 is visible. Like the other bridge tests these are SKIPPED while
`_queue_/claimed/` holds a file.

Run: python3 -m unittest discover -s _tools_/cu-bridge-tests
"""
from __future__ import annotations

import json
import re

from test_cu_bridge import BridgeCase, FAKE_SERVER, BRIDGE_SOURCE

RECORDING_SERVER = FAKE_SERVER.replace(
    "runs = {}\n", "runs = {}\nopen(os.environ['FAKE_IDLE_FILE'], 'w').write(os.environ.get('CU_OWNER_IDLE_SECONDS', '<unset>'))\n", 1)


class OwnerIdle(BridgeCase):
    def setUp(self):
        super().setUp()
        (self.root / "fake" / "_tools_" / "computer-use-mcp" / "server.mjs").write_text(RECORDING_SERVER)
        self.idle_file = self.root / "idle-seen"
        self.env["FAKE_IDLE_FILE"] = str(self.idle_file)
        self.env.pop("CU_OWNER_IDLE_SECONDS", None)

    def launcher_line(self, value):
        """Set the launcher line of THIS test's copy of the bridge (the checked-in file is not touched)."""
        copy = self.root / "_tools_" / "cu_bridge.py"
        text = copy.read_text()
        text, n = re.subn(r"(?m)^LAUNCHER_OWNER_IDLE_SECONDS = .*$", f"LAUNCHER_OWNER_IDLE_SECONDS = {value}", text)
        self.assertEqual(n, 1)
        copy.write_text(text)

    def start_daemon(self):
        r = self.run_bridge("ensure")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.run_bridge("self-test")                                             # the server has started and answered
        return r, json.loads(r.stdout)

    def seen(self):
        return self.idle_file.read_text()

    def test_the_checked_in_launcher_line_is_zero_and_names_the_decision_and_the_target(self):
        source = BRIDGE_SOURCE.read_text()
        lines = [ln for ln in source.splitlines() if ln.startswith("LAUNCHER_OWNER_IDLE_SECONDS = ")]
        self.assertEqual(lines, ["LAUNCHER_OWNER_IDLE_SECONDS = 0"])             # one line: the setting, and where it is restored
        before = source[:source.index(lines[0])].splitlines()[-5:]
        comment = " ".join(before)
        self.assertIn("OD-20261123-27", comment)
        self.assertIn("300 s AGAIN", comment)
        self.assertIn("CU-720", comment)
        self.assertIn("None", comment)

    def test_a_daemon_started_without_the_variable_carries_the_launcher_value_and_says_so(self):
        r, out = self.start_daemon()
        self.assertEqual(self.seen(), "0")                                       # the launcher put it in the server's environment
        self.assertEqual(out["owner_idle"], "owner_idle_seconds=0 (source: launcher)")
        self.assertIn("cu_bridge: owner_idle_seconds=0 (source: launcher)", r.stderr)
        listing = json.loads(self.run_bridge("runs").stdout)["bridge"]["daemons"][0]
        self.assertEqual((listing["owner_idle_seconds"], listing["owner_idle_source"]), (0, "launcher"))
        log = (self.root / "_tools_" / "state" / "cu_bridge.log")
        self.assertIn("owner_idle_seconds=0 (source: launcher)", log.read_text())           # the start line is in the daemon's own log

    def test_an_explicit_variable_in_the_daemons_environment_wins_and_is_reported_as_env(self):
        self.env["CU_OWNER_IDLE_SECONDS"] = "120"
        _r, out = self.start_daemon()
        self.assertEqual(self.seen(), "120")
        self.assertEqual(out["owner_idle"], "owner_idle_seconds=120 (source: env)")

    def test_an_invalid_variable_is_reported_as_what_the_lock_will_use(self):
        self.env["CU_OWNER_IDLE_SECONDS"] = "999"
        _r, out = self.start_daemon()
        self.assertEqual(self.seen(), "999")                                     # passed through untouched; the lock ignores it
        self.assertIn("owner_idle_seconds=300 (source: env) - CU_OWNER_IDLE_SECONDS='999' is outside 0 to 300, so the lock uses 300", out["owner_idle"])

    def test_with_the_launcher_line_removed_a_daemon_without_the_variable_reports_source_default_and_300(self):
        self.launcher_line("None")                                               # the restore: one line, the same place
        r, out = self.start_daemon()
        self.assertEqual(self.seen(), "<unset>")                                 # nothing is put into the server's environment
        self.assertEqual(out["owner_idle"], "owner_idle_seconds=300 (source: default)")
        self.assertIn("cu_bridge: owner_idle_seconds=300 (source: default)", r.stderr)

    def test_status_shows_the_value_in_force_in_the_daemon_that_owns_the_run(self):
        self.start_daemon()
        run = self.run_bridge("start", "--task", "demo")
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        run_id = json.loads(run.stdout.split("\n\n")[0])["run_id"]
        status = self.run_bridge("status", "--run-id", run_id)
        self.assertEqual(status.returncode, 0, status.stdout + status.stderr)
        self.assertIn("cu_bridge: owner_idle_seconds=0 (source: launcher)", status.stderr)
        body, _end = json.JSONDecoder().raw_decode(status.stdout)
        self.assertEqual(body["bridge_owner_idle"], "owner_idle_seconds=0 (source: launcher)")

    def test_the_value_is_the_daemons_own_not_the_callers_shell(self):
        self.start_daemon()
        self.env["CU_OWNER_IDLE_SECONDS"] = "120"                                # a different shell asks later
        out = json.loads(self.run_bridge("ensure").stdout)
        self.assertEqual(out["owner_idle"], "owner_idle_seconds=0 (source: launcher)")

    def test_a_daemon_that_started_before_the_bridge_recorded_the_value_says_unknown(self):
        self.start_daemon()
        info = next((self.root / "_tools_" / "state").glob("cu_bridge-*.json"))
        data = json.loads(info.read_text())
        for key in ("owner_idle_seconds", "owner_idle_source"):
            data.pop(key)
        info.write_text(json.dumps(data) + "\n")
        out = json.loads(self.run_bridge("ensure").stdout)
        self.assertIn("owner_idle_seconds=unknown (source: unknown)", out["owner_idle"])
        self.assertIn("restart it between runs", out["owner_idle"])

    def test_restart_prints_the_new_daemons_line(self):
        self.start_daemon()
        r = self.run_bridge("restart")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(json.loads(r.stdout)["owner_idle"], "owner_idle_seconds=0 (source: launcher)")
        self.assertIn("cu_bridge: owner_idle_seconds=0 (source: launcher)", r.stderr)
