"""Tests for spawn_seat.py with a fake relay: the policy is fixed from TEAM.yaml, the model is read back, selectModel runs once
when the seat is idle and differs, and anything still wrong fails loudly. Nothing real is spawned; no secret may come back out.

Run: python3 -m unittest discover -s _tools_/spawn-seat
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
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "spawn_seat.py"
FAKE = HERE / "fake_relay.py"
REAL_RELAY = Path("~/dtadpole/reflection/_tools_/session-relay/session-relay.py").expanduser()
COOKIE, TOKEN = "/tmp/jar-secret-path-xyz", "ghp_" + "b2c3d4e5f6a7" * 3
TEAM = """version: 9.9.9
coordination:
  execution:
    approved_model: claude-test-model
    approved_effort: high-test
    approved_provider: test-provider
seats: []
"""


class Case(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="spawn-seat-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.team = self.tmp / "TEAM.yaml"
        self.team.write_text(TEAM)
        self.state = self.tmp / "state.json"
        self.prompt = self.tmp / "prompt.md"
        self.prompt.write_text("kickoff\n")

    def run_tool(self, *args, mode="ok", team=None, extra_env=None):
        env = dict(os.environ, SESSION_RELAY_MODULE=str(FAKE), FAKE_RELAY_STATE=str(self.state), FAKE_RELAY_MODE=mode,
                   SESSION_RELAY_JAR=COOKIE, GH_TOKEN=TOKEN)
        env.update(extra_env or {})
        return subprocess.run([sys.executable, "-B", str(TOOL), "--team", str(team or self.team), "--settle-seconds", "0", *args],
                              capture_output=True, text=True, env=env)

    def calls(self):
        return json.loads(self.state.read_text())["calls"] if self.state.exists() else []

    def select_calls(self):
        return [c for c in self.calls() if c.get("call") == "session/selectModel"]

    def silent(self, r):
        out = r.stdout + r.stderr
        for secret in (COOKIE, TOKEN, "abc123secret", "localhost", "ghp_"):
            self.assertNotIn(secret, out)


class Spawning(Case):
    def test_a_good_spawn_prints_the_id_and_the_read_back_model_only(self):
        r = self.run_tool("--title", "[Last War] Test seat", "--prompt-file", str(self.prompt))
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(r.stdout.strip().splitlines(),
                         ["session session-00000000-aaaa-bbbb-cccc-111111111111",
                          "model claude-test-model high-test test-provider (read back)"])
        self.assertEqual(r.stderr, "")
        self.silent(r)
        self.assertEqual(self.select_calls(), [])                          # it already came up right: no correction

    def test_the_model_effort_and_provider_come_from_team_yaml_and_the_title_and_files_pass_through(self):
        goal = self.tmp / "goal.md"
        goal.write_text("goal\n")
        self.run_tool("--title", "T 1", "--prompt-file", str(self.prompt), "--goal-file", str(goal), "--workspace", str(self.tmp))
        spawn = next(c["spawn"] for c in self.calls() if "spawn" in c)
        self.assertEqual((spawn["model"], spawn["effort"], spawn["provider"]), ("claude-test-model", "high-test", "test-provider"))
        self.assertEqual((spawn["title"], spawn["prompt_file"], spawn["goal_file"], spawn["workspace"]),
                         ("T 1", str(self.prompt), str(goal), str(self.tmp)))
        self.assertFalse(spawn["no_full_access"])

    def test_the_workspace_defaults_to_the_folder_holding_team_yaml(self):
        self.run_tool("--title", "T")
        self.assertEqual(next(c["spawn"] for c in self.calls() if "spawn" in c)["workspace"], str(self.tmp.resolve()))

    def test_model_effort_and_provider_cannot_be_overridden(self):
        for flag, value in (("--model", "claude-opus-5-5"), ("--effort", "low"), ("--provider", "other")):
            r = self.run_tool("--title", "T", flag, value)
            self.assertEqual(r.returncode, 2, flag)
            self.assertEqual(self.calls(), [], flag)                       # nothing was spawned

    def test_a_change_of_the_effort_in_team_yaml_changes_the_spawn_and_nothing_is_a_constant(self):
        """The owner's request of 2026-11-25 (xhigh to high): the tool follows the file, so a policy change needs no code change."""
        for effort in ("high", "xhigh", "medium"):
            team = self.tmp / f"team-{effort}.yaml"
            team.write_text(TEAM.replace("high-test", effort))
            out = self.run_tool("--title", "T", "--dry-run", team=team).stdout
            self.assertIn(f"on claude-test-model {effort} test-provider", out)

    def test_dry_run_states_the_policy_and_spawns_nothing(self):
        r = self.run_tool("--title", "T", "--dry-run")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("claude-test-model high-test test-provider", r.stdout)
        self.assertEqual(self.calls(), [])


class ReadBack(Case):
    def test_a_seat_that_comes_up_on_the_default_is_corrected_once_while_idle(self):
        r = self.run_tool("--title", "T", mode="drift")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(len(self.select_calls()), 1)
        req = self.select_calls()[0]["args"]["request"]
        self.assertEqual((req["model"], req["reasoningEffort"], req["provider"]), ("claude-test-model", "high-test", "test-provider"))
        self.assertIn("model claude-test-model high-test test-provider (read back)", r.stdout)
        self.silent(r)

    def test_a_running_seat_is_not_touched_and_the_failure_says_what_corrects_it(self):
        r = self.run_tool("--title", "T", mode="drift-running")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertEqual(self.select_calls(), [])
        self.assertIn("FAILED: the seat is running", r.stderr)
        self.assertIn("model_guard", r.stderr)
        self.assertIn("FAILED: model differs", r.stderr)
        self.assertIn("session session-00000000", r.stdout)                # the id is still printed for the follow-up
        self.silent(r)

    def test_a_correction_that_does_not_take_fails_loudly_after_one_try(self):
        r = self.run_tool("--title", "T", mode="drift-unfixable")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertEqual(len(self.select_calls()), 1)                       # once, not a loop
        self.assertIn("FAILED: model differs: model claude-opus-5-5 (policy claude-test-model)", r.stderr)

    def test_a_refused_correction_is_reported(self):
        r = self.run_tool("--title", "T", mode="selectmodel-refused")
        self.assertEqual(r.returncode, 1)
        self.assertIn("selectModel refused", r.stderr)
        self.assertEqual(len(self.select_calls()), 1)

    def test_a_model_that_cannot_be_read_is_a_failure_not_a_pass(self):
        for mode in ("inspect-fails", "no-model"):
            self.setUp()
            r = self.run_tool("--title", "T", mode=mode)
            self.assertEqual(r.returncode, 1, mode)
            self.assertIn("could not be read back", r.stderr, mode)
            self.assertNotIn("(read back)", r.stdout, mode)


class Failures(Case):
    def test_a_failed_spawn_is_exit_one_and_its_error_text_is_scrubbed(self):
        r = self.run_tool("--title", "T", mode="spawn-fails")
        self.assertEqual(r.returncode, 1)
        self.assertIn("FAILED: the spawn did not complete", r.stderr)
        self.assertNotIn("session session-", r.stdout)
        self.silent(r)

    def test_a_failed_spawn_step_fails_even_when_the_model_is_right(self):
        r = self.run_tool("--title", "T", mode="step-fails")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("spawn step failed: session/rename", r.stderr)
        self.assertIn("(read back)", r.stdout)
        self.silent(r)

    def test_unusable_policy_or_arguments_are_exit_two_and_spawn_nothing(self):
        (self.tmp / "no-keys.yaml").write_text("coordination:\n  execution:\n    approved_model: claude-test-model\n")
        (self.tmp / "broken.yaml").write_text("a: [unclosed\n")
        cases = [("--team-file", self.tmp / "no-keys.yaml"), ("--team-file", self.tmp / "broken.yaml"),
                 ("--team-file", self.tmp / "missing.yaml")]
        for _label, path in cases:
            r = self.run_tool("--title", "T", team=path)
            self.assertEqual(r.returncode, 2, str(path))
            self.assertEqual(self.calls(), [], str(path))
        r = self.run_tool("--title", "T", "--prompt-file", str(self.tmp / "nope.md"))
        self.assertEqual(r.returncode, 2)
        self.assertIn("approved_effort", self.run_tool("--title", "T", team=self.tmp / "no-keys.yaml").stderr)
        self.assertEqual(subprocess.run([sys.executable, "-B", str(TOOL), "--team", str(self.team)], capture_output=True, text=True).returncode, 2)

    def test_a_missing_relay_module_is_exit_two(self):
        r = self.run_tool("--title", "T", extra_env={"SESSION_RELAY_MODULE": str(self.tmp / "gone.py")})
        self.assertEqual(r.returncode, 2)
        self.assertIn("no relay module", r.stderr)


@unittest.skipUnless(REAL_RELAY.is_file(), "the real session-relay is not on this machine")
class AgainstTheRealRelay(unittest.TestCase):
    """The fake is only as good as its match to the relay: the tool needs these names and these spawn arguments."""

    def test_the_relay_still_offers_what_the_tool_uses(self):
        text = REAL_RELAY.read_text()
        for name in ("def cmd_spawn(a)", "def inspect(session_id", "def call(method"):
            self.assertIn(name, text)
        spawn = text[text.index("def cmd_spawn(a)"):text.index("def cmd_command")]
        for field in ("a.workspace", "a.title", "a.prompt_file", "a.goal_file", "a.provider", "a.model", "a.effort", "a.no_full_access"):
            self.assertIn(field, spawn, field)
        self.assertIn('"reasoningEffort"', text)
        self.assertIn('"session/selectModel"', text)


if __name__ == "__main__":
    unittest.main()
