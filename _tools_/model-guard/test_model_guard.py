"""Tests for model_guard.py with a fake relay: quiet at zero drift, a dry run that reports, idle seats fixed with --apply, a running
seat retried, a refusal and an unreadable session reported, children left alone, the steward included, no secret in any output.

Run: python3 -m unittest discover -s _tools_/model-guard
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "model_guard.py"
FAKE = HERE / "fake_relay.py"
COOKIE, TOKEN = "/tmp/jar-secret-path-xyz", "ghp_" + "c3d4e5f6a7b8" * 3
GOOD = {"provider": "test-provider", "model": "claude-test-model", "reasoningEffort": "high-test"}
OPUS = {"provider": "test-provider", "model": "claude-opus-5-5", "reasoningEffort": "high-test"}
LOW = {"provider": "test-provider", "model": "claude-test-model", "reasoningEffort": "low"}
SID = {k: f"session-{n:08x}-aaaa-bbbb-cccc-{n:012x}" for n, k in enumerate(("coordinator", "operator", "scout", "steward", "gone", "kid"), 1)}
TEAM = f"""version: 9.9.9
steward:
  session_id: {SID['steward']}
  title: 'Steer A'
coordination:
  execution:
    approved_model: claude-test-model
    approved_effort: high-test
    approved_provider: test-provider
seats:
  - key: coordinator
    principal: someone
    session_id: {SID['coordinator']}
    session_started: '2026-11-23T04:04:00Z'
    title: 'Coordinator'
    assignment: assigned
    roles:
      - coordinator
    responsibilities:
      - one
      - two
      - three
      - four
      - five
      - six
    seat_ref: x
  - key: operator
    session_id: {SID['operator']}
  - key: scout
    session_id: {SID['scout']}
  - key: retired
    session_id: session-ffffffff-0000-0000-0000-000000000000
    assignment: concluded
  - key: unstarted
    session_id: null
"""


class Case(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="model-guard-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.team = self.tmp / "TEAM.yaml"
        self.team.write_text(TEAM)
        self.state = self.tmp / "state.json"
        self.seats(coordinator=GOOD, operator=GOOD, scout=GOOD, steward=GOOD)

    def seats(self, **models):
        seats = {SID[k]: {"model": dict(v)} for k, v in models.items()}
        self.state.write_text(json.dumps({"seats": seats, "calls": []}))

    def tweak(self, key, **fields):
        data = json.loads(self.state.read_text())
        data["seats"][SID[key]].update(fields)
        self.state.write_text(json.dumps(data))

    def run_tool(self, *args, team=None):
        env = dict(os.environ, SESSION_RELAY_MODULE=str(FAKE), FAKE_GUARD_STATE=str(self.state), SESSION_RELAY_JAR=COOKIE, GH_TOKEN=TOKEN)
        return subprocess.run([sys.executable, "-B", str(TOOL), "--team", str(team or self.team), *args], capture_output=True, text=True, env=env)

    def calls(self, kind="call"):
        return [c for c in json.loads(self.state.read_text())["calls"] if kind in c]

    def silent(self, r):
        out = r.stdout + r.stderr
        for secret in (COOKIE, TOKEN, "abc123secret", "localhost", "ghp_"):
            self.assertNotIn(secret, out)


class Quiet(Case):
    def test_no_drift_prints_nothing_and_exits_zero_with_or_without_apply(self):
        for args in ((), ("--apply",)):
            r = self.run_tool(*args)
            self.assertEqual((r.returncode, r.stdout, r.stderr), (0, "", ""), args)
        self.assertEqual(self.calls(), [])                                              # nothing was corrected

    def test_verbose_prints_the_table_anyway(self):
        r = self.run_tool("--verbose")
        self.assertEqual(r.returncode, 0)
        self.assertIn("seats 4 | drift 0 | fixed 0 | unfixed 0", r.stdout)


class Drift(Case):
    def test_the_effort_is_the_policys_so_lowering_it_in_team_yaml_makes_the_old_one_drift_and_is_what_is_sent(self):
        """The owner's request of 2026-11-25 (xhigh to high) needed one line in TEAM.yaml and no code: every seat at the old effort drifts."""
        lowered = self.tmp / "TEAM-lower.yaml"
        lowered.write_text(TEAM.replace("approved_effort: high-test", "approved_effort: lower-test"))
        quiet = self.run_tool(team=self.team)
        self.assertEqual((quiet.returncode, quiet.stdout), (0, ""))                                # at the old policy nothing drifts
        r = self.run_tool("--apply", "--verbose", team=lowered)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("seats 4 | drift 4 | fixed 4 | unfixed 0 | policy claude-test-model lower-test", r.stdout)
        sent = self.calls()
        self.assertEqual(len(sent), 4)
        self.assertEqual({c["args"]["request"]["reasoningEffort"] for c in sent}, {"lower-test"})    # only the policy's effort is ever sent
        self.assertEqual(self.run_tool("--apply", team=lowered).stdout, "")                          # and the next tick is quiet again

    def test_a_dry_run_reports_and_exits_one_without_touching_anything(self):
        self.seats(coordinator=GOOD, operator=OPUS, scout=GOOD, steward=GOOD)
        r = self.run_tool()
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("operator", r.stdout)
        self.assertIn("claude-opus-5-5", r.stdout)
        self.assertIn("DRIFT (dry run: pass --apply)", r.stdout)
        self.assertEqual(self.calls(), [])
        self.silent(r)

    def test_an_idle_seat_is_fixed_with_apply_and_the_policy_is_what_is_sent(self):
        self.seats(coordinator=GOOD, operator=OPUS, scout=GOOD, steward=GOOD)
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("FIXED", r.stdout)
        self.assertIn("seats 4 | drift 1 | fixed 1 | unfixed 0", r.stdout)
        sent = self.calls()
        self.assertEqual(len(sent), 1)
        self.assertEqual(sent[0]["args"]["request"], {"sessionId": SID["operator"], "provider": "test-provider",
                                                       "model": "claude-test-model", "reasoningEffort": "high-test"})
        self.assertEqual(self.run_tool("--apply").stdout, "")                            # fixed: the next tick is quiet again

    def test_an_effort_or_provider_drift_alone_counts(self):
        self.seats(coordinator=LOW, operator=GOOD, scout={**GOOD, "provider": "other"}, steward=GOOD)
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(len(self.calls()), 2)

    def test_a_running_seat_is_left_and_retried_next_tick(self):
        self.seats(coordinator=GOOD, operator=OPUS, scout=GOOD, steward=GOOD)
        self.tweak("operator", running=True)
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("DRIFT (running: retry next tick)", r.stdout)
        self.assertEqual(self.calls(), [])
        self.tweak("operator", running=False)
        self.assertEqual(self.run_tool("--apply").returncode, 0)                          # idle now: fixed on the retry

    def test_a_refusal_is_reported_and_is_an_unfixed_drift(self):
        self.seats(coordinator=GOOD, operator=OPUS, scout=GOOD, steward=GOOD)
        self.tweak("operator", refuse=True)
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("FIX REFUSED", r.stdout)
        self.silent(r)

    def test_a_correction_that_does_not_take_is_reported_failed(self):
        self.seats(coordinator=GOOD, operator=OPUS, scout=GOOD, steward=GOOD)
        self.tweak("operator", noop=True)
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 1)
        self.assertIn("FIX FAILED: still model", r.stdout)

    def test_an_unreadable_session_is_reported_and_the_rest_are_still_checked(self):
        self.seats(coordinator=GOOD, operator=GOOD, scout=OPUS, steward=GOOD)
        self.tweak("operator", unreadable=True)
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("UNREADABLE", r.stdout)
        self.assertIn("FIXED", r.stdout)                                                  # scout was still corrected
        self.silent(r)

    def test_the_steward_block_is_checked_and_fixed_too(self):
        self.seats(coordinator=GOOD, operator=GOOD, scout=GOOD, steward=OPUS)
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("steward", r.stdout)
        self.assertEqual(self.calls()[0]["args"]["request"]["sessionId"], SID["steward"])


class Children(Case):
    def test_a_child_session_is_listed_as_informational_and_never_touched(self):
        self.seats(coordinator=OPUS, operator=GOOD, scout=GOOD, steward=GOOD, kid=OPUS)
        self.tweak("kid", origin="subagent")
        (self.tmp / "TEAM.yaml").write_text(TEAM.replace("seats:\n", f"seats:\n  - key: helper\n    session_id: {SID['kid']}\n", 1))
        r = self.run_tool("--apply")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)                            # the coordinator drift was fixed; the child is not a failure
        self.assertIn("child session: informational", r.stdout)
        touched = [c["args"]["request"]["sessionId"] for c in self.calls()]
        self.assertEqual(touched, [SID["coordinator"]])
        self.assertNotIn({"inspect": SID["kid"]}, self.calls("inspect"))

    def test_a_child_alone_adds_no_output_when_nothing_drifted(self):
        self.seats(coordinator=GOOD, operator=GOOD, scout=GOOD, steward=GOOD, kid=OPUS)
        self.tweak("kid", origin="subagent")
        (self.tmp / "TEAM.yaml").write_text(TEAM.replace("seats:\n", f"seats:\n  - key: helper\n    session_id: {SID['kid']}\n", 1))
        r = self.run_tool("--apply")
        self.assertEqual((r.returncode, r.stdout), (0, ""))


class Roster(Case):
    def test_the_roster_is_read_as_yaml_not_by_pattern(self):
        # a long seat block, a null session, a concluded seat and a duplicate id: only the live, distinct ones are checked
        (self.tmp / "TEAM.yaml").write_text(TEAM + f"  - key: twin\n    session_id: {SID['scout']}\n")
        r = self.run_tool("--verbose")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("seats 4 |", r.stdout)                                              # coordinator, operator, scout, steward
        self.assertEqual(len(self.calls("inspect")), 4)

    def test_missing_policy_keys_or_an_unreadable_roster_are_exit_two(self):
        (self.tmp / "bad.yaml").write_text("seats: []\ncoordination:\n  execution:\n    approved_model: claude-test-model\n")
        (self.tmp / "broken.yaml").write_text("a: [unclosed\n")
        for path in (self.tmp / "bad.yaml", self.tmp / "broken.yaml", self.tmp / "missing.yaml"):
            r = self.run_tool(team=path)
            self.assertEqual(r.returncode, 2, str(path))
            self.assertEqual(r.stdout, "")
        self.assertEqual(self.calls(), [])

    def test_a_missing_relay_module_is_exit_two(self):
        env = dict(os.environ, SESSION_RELAY_MODULE=str(self.tmp / "gone.py"), FAKE_GUARD_STATE=str(self.state))
        r = subprocess.run([sys.executable, "-B", str(TOOL), "--team", str(self.team)], capture_output=True, text=True, env=env)
        self.assertEqual(r.returncode, 2)
        self.assertIn("no relay module", r.stderr)

    def test_the_live_roster_parses_when_present(self):
        live = HERE.parent.parent / "TEAM.yaml"
        if "approved_model:" not in live.read_text():
            self.skipTest("this checkout's TEAM.yaml carries no policy keys yet")
        sys.path.insert(0, str(HERE))
        import model_guard
        policy, seats = model_guard.load_team(live)
        self.assertEqual(policy["model"], "claude-sonnet-5-5")
        self.assertGreaterEqual(len(seats), 10)


if __name__ == "__main__":
    unittest.main()
