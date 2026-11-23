"""Tests for the bridge's use of the computer-use desktop-run lock: a read-only report, a refusal before the server is asked while the
desktop is held (a live run or hold, ours or another seat's, a waiter) or the lock is an orphan, never a wait, a retry or a break,
a seat guard, and the server's own refusal reported once. A fake run-lock.mjs (a Python script the tests run as `node`) and a lock
directory of their own stand in for the real ones: nothing here touches /tmp/cu-desktop-run, the real server or a real run.

Like the other bridge tests these are SKIPPED while `_queue_/claimed/` holds a file (a live run holds the one desktop).

Run: python3 -m unittest discover -s _tools_/cu-bridge-tests
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
import unittest
from pathlib import Path

from test_cu_bridge import BridgeCase, FAKE_SERVER

FAKE_LOCK_CLI = r'''
import json, os, sys
open(os.environ["FAKE_LOCK_CALLS"], "a").write(" ".join(sys.argv[1:]) + "\n")
print(os.environ.get("FAKE_LOCK_STATUS", "{}"))
'''
REFUSING_SERVER = FAKE_SERVER.replace(
    '            text(mid, {"run_id": rid, "state": runs[rid]})',
    '            open(os.environ["FAKE_START_CALLS"], "a").write("start\\n")\n'
    '            if os.environ.get("FAKE_REFUSE"):\n'
    '                say(mid, {"content": [{"type": "text", "text": os.environ["FAKE_REFUSE"]}], "isError": True})\n'
    '            else:\n'
    '                text(mid, {"run_id": rid, "state": runs[rid]})')
HOLDER = {"seat": "cu-developer-two", "runId": "20261123T093311Z-a59935", "startedAt": "2026-11-23T09:33:11.552Z"}


def dead_pid() -> int:
    proc = subprocess.Popen([sys.executable, "-c", "pass"])
    proc.wait()
    return proc.pid


class LockCase(BridgeCase):
    def setUp(self):
        super().setUp()
        cli = self.root / "fake" / "_environments_" / "macos-desktop"
        cli.mkdir(parents=True)
        (cli / "run-lock.mjs").write_text(FAKE_LOCK_CLI)
        (self.root / "fake" / "_tools_" / "computer-use-mcp" / "server.mjs").write_text(REFUSING_SERVER)
        self.lockdir = self.root / "lockdir"
        self.lockdir.mkdir()
        self.calls, self.starts = self.root / "lock-calls", self.root / "start-calls"
        self.env.update(CU_RUN_LOCK_DIR=str(self.lockdir), FAKE_LOCK_CALLS=str(self.calls), FAKE_START_CALLS=str(self.starts))
        self.set_status()

    def set_status(self, run=None, hold=None, waiter=None, sentinel=False):
        self.env["FAKE_LOCK_STATUS"] = json.dumps({"hold": hold, "run": run, "sentinel": sentinel, "waiter": waiter,
                                                   "ownerIdle": {"seconds": 12}})

    def entry(self, pid, seat="cu-developer-two", sentinel=False):
        data = {**HOLDER, "seat": seat, "pid": pid}
        if sentinel:
            data["sentinel"] = True
        (self.lockdir / "run.json").write_text(json.dumps(data))
        return data

    def lock_digest(self):
        return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(self.lockdir.iterdir())}

    def n(self, path):
        return len(path.read_text().splitlines()) if path.exists() else 0

    def no_daemon_started(self):
        self.assertEqual(self.serve_pids(), [])
        self.assertEqual(self.n(self.starts), 0)


class Report(LockCase):
    def test_free_is_reported_and_exits_zero(self):
        r = self.run_bridge("lock")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("the desktop lock is free", r.stdout)
        self.assertEqual(json.loads(r.stdout.splitlines()[-1])["state"], "free")

    def test_a_foreign_live_run_is_held_and_names_the_holder_without_a_pid(self):
        pid = os.getpid()
        self.entry(pid)
        self.set_status(run=HOLDER)
        r = self.run_bridge("lock")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("held by cu-developer-two: run 20261123T093311Z-a59935 since 2026-11-23T09:33:11.552Z", r.stdout)
        self.assertNotIn(str(pid), r.stdout + r.stderr)

    def test_a_hold_a_waiter_and_a_sentinel_are_busy(self):
        self.set_status(hold={"seat": "cu-developer-three", "until": "2026-11-23T10:00:00Z", "reason": "a check"})
        r = self.run_bridge("lock")
        self.assertEqual(r.returncode, 1)
        self.assertIn("on hold for cu-developer-three until 2026-11-23T10:00:00Z (a check)", r.stdout)
        self.set_status(waiter="cu-coordinator")
        self.assertIn("a waiter (cu-coordinator) is queued", self.run_bridge("lock").stdout)
        self.set_status(sentinel=True)
        self.assertEqual(self.run_bridge("lock").returncode, 1)

    def test_an_entry_whose_process_is_dead_is_an_orphan_and_is_never_touched(self):
        self.entry(dead_pid())
        self.set_status(run=HOLDER)
        before = self.lock_digest()
        r = self.run_bridge("lock")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("ORPHAN desktop lock", r.stdout)
        self.assertIn("reported, not broken", r.stdout)
        self.assertEqual(self.lock_digest(), before)

    def test_an_unreadable_status_is_exit_two_and_says_why(self):
        os.remove(self.root / "fake" / "_environments_" / "macos-desktop" / "run-lock.mjs")
        r = self.run_bridge("lock")
        self.assertEqual(r.returncode, 2)
        self.assertIn("could not be read", r.stdout)


class StartRefuses(LockCase):
    def test_a_foreign_run_refuses_before_the_server_is_asked_and_never_loops(self):
        self.entry(os.getpid())
        self.set_status(run=HOLDER)
        before = self.lock_digest()
        began = time.time()
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("start refused: the desktop is held by cu-developer-two", r.stderr)
        self.assertIn("Retry later; this bridge never waits, retries or breaks a lock.", r.stderr)
        self.assertLess(time.time() - began, 20)
        self.assertEqual(self.n(self.calls), 1)                                          # the status was read once
        self.no_daemon_started()
        self.assertEqual(self.lock_digest(), before)
        self.assertNotIn(str(os.getpid()), r.stdout + r.stderr)

    def test_a_hold_a_waiter_and_this_seats_own_run_refuse_too(self):
        self.set_status(hold={"seat": "cu-developer-three", "until": "2026-11-23T10:00:00Z", "reason": ""})
        self.assertIn("on hold for cu-developer-three", self.run_bridge("start", "--task", "demo").stderr)
        self.set_status(waiter="cu-coordinator")
        self.assertIn("a waiter (cu-coordinator)", self.run_bridge("start", "--task", "demo").stderr)
        mine = self.env["CU_SEAT"]
        self.entry(os.getpid(), seat=mine)
        self.set_status(run={**HOLDER, "seat": mine})
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 1)
        self.assertIn(f"held by {mine} (this bridge's own seat)", r.stderr)
        self.no_daemon_started()

    def test_an_orphan_refuses_unless_the_coordinator_accepts_it_and_the_bridge_never_breaks_it(self):
        self.entry(dead_pid())
        self.set_status(run=HOLDER)
        before = self.lock_digest()
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("ORPHAN desktop lock", r.stderr)
        self.assertIn("Tell the coordinator", r.stderr)
        self.no_daemon_started()
        self.assertEqual(self.lock_digest(), before)
        ok = self.run_bridge("start", "--task", "demo", "--accept-orphan")
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        self.assertEqual(self.lock_digest(), before)                                     # still only the server may reclaim it

    def test_a_free_desktop_starts_and_an_unreadable_status_starts_with_a_note(self):
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("run-", r.stdout)
        os.remove(self.root / "fake" / "_environments_" / "macos-desktop" / "run-lock.mjs")
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("could not be read", r.stderr)

    def test_skip_lock_check_leaves_it_to_the_server_and_a_browser_run_has_no_desktop_check(self):
        self.entry(os.getpid())
        self.set_status(run=HOLDER)
        r = self.run_bridge("start", "--task", "demo", "--skip-lock-check")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(self.n(self.calls), 0)
        b = self.run_bridge("start", "--task", "demo", "--browser", "--start-url", "https://example.org")
        self.assertEqual(b.returncode, 0, b.stdout + b.stderr)
        self.assertEqual(self.n(self.calls), 0)


class ServerRefusal(LockCase):
    def test_the_servers_own_refusal_is_reported_once_and_not_retried(self):
        self.env["FAKE_REFUSE"] = "error: another desktop run is active (holder cu-developer-two)"
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("start refused: error: another desktop run is active (holder cu-developer-two)", r.stderr)
        self.assertIn("Retry later; this bridge never waits, retries or breaks a lock.", r.stderr)
        self.assertEqual(self.n(self.starts), 1)                                         # one call to the server, no loop
        self.assertNotIn("unexpected start result", r.stderr)
        self.assertEqual(json.loads(self.run_bridge("runs").stdout)["bridge"].get("runs", []), [])   # no phantom run was remembered

    def test_another_refusal_is_reported_without_the_retry_hint(self):
        self.env["FAKE_REFUSE"] = "error: max_steps must be an integer"
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 1)
        self.assertIn("start refused: error: max_steps must be an integer", r.stderr)
        self.assertNotIn("Retry later", r.stderr)


class Seat(LockCase):
    def test_a_seat_the_lock_would_refuse_stops_start_with_exit_two(self):
        self.env["CU_SEAT"] = "lastwar"
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("is not a [cu] seat key", r.stderr)
        self.assertIn("cu-lastwar", r.stderr)
        self.no_daemon_started()
        self.assertEqual(self.n(self.calls), 0)

    def test_cu_style_names_pass_including_the_default(self):
        for seat in ("cu-lastwar", "cu-owner", "cu-test-12345678"):
            self.env["CU_SEAT"] = seat
            r = self.run_bridge("start", "--task", "demo")
            self.assertEqual(r.returncode, 0, f"{seat}: {r.stdout}{r.stderr}")
            self.run_bridge("stop-daemon")


if __name__ == "__main__":
    unittest.main()
