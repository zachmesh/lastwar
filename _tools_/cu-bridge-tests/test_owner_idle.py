"""Tests that the bridge never defaults CU_OWNER_IDLE_SECONDS: the owner-idle wait (300 s without local input before synthetic input, rule D-066)
stays at the computer-use default unless the daemon's own environment carries a value. A fake MCP server records the variable it was started with.
Like the other bridge tests these are SKIPPED while `_queue_/claimed/` holds a file.

Run: python3 -m unittest discover -s _tools_/cu-bridge-tests
"""
from __future__ import annotations

from test_cu_bridge import BridgeCase, FAKE_SERVER

RECORDING_SERVER = FAKE_SERVER.replace(
    "runs = {}\n", "runs = {}\nopen(os.environ['FAKE_IDLE_FILE'], 'w').write(os.environ.get('CU_OWNER_IDLE_SECONDS', '<unset>'))\n", 1)


class OwnerIdle(BridgeCase):
    def setUp(self):
        super().setUp()
        (self.root / "fake" / "_tools_" / "computer-use-mcp" / "server.mjs").write_text(RECORDING_SERVER)
        self.idle_file = self.root / "idle-seen"
        self.env["FAKE_IDLE_FILE"] = str(self.idle_file)
        self.env.pop("CU_OWNER_IDLE_SECONDS", None)

    def seen(self):
        self.assertEqual(self.run_bridge("ensure").returncode, 0)
        r = self.run_bridge("self-test")                                         # the server has started and answered
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return self.idle_file.read_text()

    def test_unset_in_the_daemon_environment_means_unset_in_the_server(self):
        self.assertEqual(self.seen(), "<unset>")

    def test_a_value_the_daemon_carries_is_passed_through_unchanged(self):
        for value in ("300", "0", "120"):
            self.run_bridge("stop-daemon")
            self.env["CU_OWNER_IDLE_SECONDS"] = value
            self.assertEqual(self.seen(), value)

    def test_the_source_sets_no_default(self):
        import re
        from test_cu_bridge import BRIDGE_SOURCE
        code = "\n".join(l for l in BRIDGE_SOURCE.read_text().splitlines() if not l.strip().startswith("#"))
        self.assertNotRegex(code, r"CU_OWNER_IDLE_SECONDS[\"'],\s*[\"']")          # no setdefault or assignment of a value
        self.assertFalse(re.search(r"environ\[[\"']CU_OWNER_IDLE_SECONDS", code))
