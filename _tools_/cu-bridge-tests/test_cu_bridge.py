"""Tests for the cu_bridge daemon lifecycle (IMP-20261123-07). A fake MCP server (a small Python script that speaks the
JSON-RPC lines of the real one) runs under a temporary copy of the bridge in /tmp, so no real computer-use server, device
or run is touched.

Nothing here sleeps on a guess: every wait is on a condition (a marker file, a process gone, a reachable daemon) with a
generous ceiling, so a loaded machine slows a test but cannot fail it. Every test is SKIPPED while `_queue_/claimed/` of
this checkout or of the main checkout holds a file (a live run holds the one desktop and its device token), and the fake
server runs under a seat name of its own, so a test can never hold or contend for what the operator's run needs.

Run: python3 -m unittest discover -s _tools_/cu-bridge-tests
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
BRIDGE_SOURCE = HERE.parent / "cu_bridge.py"

FAKE_SERVER = r'''
import json, os, sys, time
runs = {}
def say(msg_id, result):
    print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": result}), flush=True)
def text(msg_id, payload):
    say(msg_id, {"content": [{"type": "text", "text": json.dumps(payload)}]})
for line in sys.stdin:
    msg = json.loads(line)
    mid, method, params = msg.get("id"), msg.get("method"), msg.get("params") or {}
    if method == "initialize":
        say(mid, {"protocolVersion": "2025-06-18", "capabilities": {}})
    elif method == "tools/list":
        say(mid, {"tools": [{"name": n} for n in ("computer_use_start", "computer_use_status", "computer_use_control")]})
    elif method == "tools/call":
        name, args = params["name"], params.get("arguments") or {}
        if name == "computer_use_start":
            rid = "run-%d-%d" % (os.getpid(), len(runs) + 1)
            runs[rid] = "awaiting_consent"
            text(mid, {"run_id": rid, "state": runs[rid]})
        elif name == "computer_use_status":
            rid = args.get("run_id")
            if rid not in runs:
                text(mid, {"error": "no run in this server"})
            else:
                if int(args.get("wait_seconds", 0)) > 0 and os.environ.get("FAKE_INFLIGHT"):
                    open(os.environ["FAKE_INFLIGHT"], "w").close()       # tell the test the poll has reached the server
                    end = time.time() + 120
                    while time.time() < end and not os.path.exists(os.environ.get("FAKE_RELEASE", "")):
                        time.sleep(0.05)                                  # held until the test releases it
                elif int(args.get("wait_seconds", 0)) > 0:
                    time.sleep(min(int(args.get("wait_seconds", 0)), 10))
                text(mid, {"state": runs[rid]})
        elif name == "computer_use_control":
            rid = args.get("run_id")
            if rid not in runs:
                text(mid, {"error": "no run in this server"})
            else:
                if args.get("command") == "stop":
                    runs[rid] = "stopped"
                text(mid, {"state": runs[rid], "command": args.get("command")})
'''


def live_run_holds_the_desktop() -> str | None:
    """The claimed folder that holds a file (a live run, or its device token), in this checkout or the main one."""
    if os.environ.get("CU_TESTS_IGNORE_LIVE_RUN") == "1":
        return None
    repo = HERE.parent.parent
    folders = {repo / "_queue_" / "claimed"}
    common = subprocess.run(["git", "-C", str(repo), "rev-parse", "--git-common-dir"], capture_output=True, text=True).stdout.strip()
    if common:
        main = (repo / common).resolve().parent
        folders.add(main / "_queue_" / "claimed")
    for folder in sorted(folders):
        if folder.is_dir() and any(p.suffix == ".md" for p in folder.iterdir()):
            return str(folder)
    return None


def wait_for(condition, timeout=90, step=0.1):
    """True as soon as the condition holds, False after the ceiling; never a fixed sleep."""
    end = time.time() + timeout
    while time.time() < end:
        if condition():
            return True
        time.sleep(step)
    return bool(condition())


class BridgeCase(unittest.TestCase):
    def setUp(self):
        held = live_run_holds_the_desktop()
        if held:
            self.skipTest(f"a live run holds a file in {held}; set CU_TESTS_IGNORE_LIVE_RUN=1 to run anyway")
        self.root = Path(tempfile.mkdtemp(prefix="cu-test-", dir="/tmp"))     # short path: unix sockets are length limited
        tools = self.root / "_tools_"
        tools.mkdir()
        shutil.copy(BRIDGE_SOURCE, tools / "cu_bridge.py")
        self.bridge = str((tools / "cu_bridge.py").resolve())     # the daemon names itself by its resolved path
        server = self.root / "fake" / "_tools_" / "computer-use-mcp"
        server.mkdir(parents=True)
        (server / "server.mjs").write_text(FAKE_SERVER)
        (self.root / "key").write_text("fake-key\n")
        self.inflight, self.release = self.root / "inflight", self.root / "release"
        self.env = dict(os.environ, CU_PROJECT=str(self.root / "fake"), CU_KEY_FILE=str(self.root / "key"),
                        CU_NODE_BIN=sys.executable, CU_SEAT=f"cu-test-{self.root.name[-8:]}",
                        FAKE_INFLIGHT=str(self.inflight), FAKE_RELEASE=str(self.release))
        self.addCleanup(self.cleanup)

    def cleanup(self):
        subprocess.run([sys.executable, "-B", self.bridge, "stop-daemon"], capture_output=True, env=self.env, timeout=60)
        for pid in self.serve_pids():
            try:
                os.kill(pid, 9)
            except ProcessLookupError:
                pass
        shutil.rmtree(self.root, True)

    def run_bridge(self, *args, timeout=90):
        return subprocess.run([sys.executable, "-B", self.bridge, *args], capture_output=True, text=True, env=self.env,
                              timeout=timeout)

    def serve_pids(self):
        out = subprocess.run(["ps", "-axo", "pid=,command="], capture_output=True, text=True).stdout
        pids = []
        for line in out.splitlines():
            parts = line.split()
            if self.bridge in parts and parts[parts.index(self.bridge) + 1:][:1] == ["serve"]:
                pids.append(int(parts[0]))
        return pids

    def alive(self, pid):
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return False
        return True

    def gone(self, *pids, wait=60):
        return wait_for(lambda: not any(self.alive(p) for p in pids), wait, 0.1)

    def info(self, pid):
        return json.loads((self.root / "_tools_/state" / f"cu_bridge-{pid}.json").read_text())

    def listing(self, *args):
        r = self.run_bridge("runs")
        self.assertEqual(r.returncode, 0, r.stderr)
        return json.loads(r.stdout)["bridge"]

    def start_run(self):
        r = self.run_bridge("start", "--task", "demo")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return json.loads(r.stdout.split("\n\n")[0])["run_id"]

    def daemon(self):
        r = self.run_bridge("ensure")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        return json.loads(r.stdout)


class Restart(BridgeCase):
    def test_a_restart_during_a_run_ends_the_old_daemon_and_its_child_and_leaves_one_daemon(self):
        old = self.daemon()["pid"]
        run = self.start_run()
        child = self.info(old)["mcp_pid"]
        self.assertTrue(self.alive(child))
        r = self.run_bridge("restart")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        result = json.loads(r.stdout)
        self.assertEqual([e["pid"] for e in result["ended"]], [old])
        self.assertTrue(self.gone(old, child), "the old daemon or its MCP child survived the restart")
        new = result["started"]
        self.assertNotEqual(new, old)
        self.assertEqual(self.serve_pids(), [new])                             # no orphan serve process
        self.assertTrue(wait_for(lambda: self.listing()["daemons"][0]["reachable"]), "the new daemon never answered")
        listing = self.listing()
        self.assertEqual([d["pid"] for d in listing["daemons"]], [new])
        entry = next(x for x in listing["runs"] if x["run_id"] == run)
        self.assertEqual((entry["state"], entry["daemon"]), ("lost", "daemon gone"))
        status = self.run_bridge("status", "--run-id", run)
        self.assertEqual(status.returncode, 1)
        self.assertIn("is gone, so the run is lost", status.stderr)
        self.assertIn('"daemons"', status.stdout)                              # status still lists every daemon

    def test_control_stop_on_a_run_whose_daemon_was_restarted_answers_cleanly(self):
        self.daemon()
        run = self.start_run()
        self.run_bridge("restart")
        r = self.run_bridge("control", "--run-id", run, "--command", "stop")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("nothing of it is running", r.stdout)


class OneDaemon(BridgeCase):
    def test_a_second_serve_refuses_and_never_removes_the_live_daemons_files(self):
        first = self.daemon()["pid"]
        sock = self.root / "_tools_/state" / f"cu_bridge-{first}.sock"
        second = self.run_bridge("serve", timeout=30)
        self.assertEqual(second.returncode, 1, second.stdout + second.stderr)
        self.assertIn("another daemon is alive", second.stderr)
        self.assertTrue(sock.exists())
        self.assertEqual(self.serve_pids(), [first])
        self.assertTrue(self.daemon()["pid"] == first and not self.daemon()["started"])

    def test_serve_replace_ends_the_other_daemon_and_its_child_first(self):
        first = self.daemon()["pid"]
        child = self.info(first)["mcp_pid"]
        proc = subprocess.Popen([sys.executable, "-B", self.bridge, "serve", "--replace"], env=self.env,
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True)
        try:
            self.assertTrue(self.gone(first, child))
            self.assertTrue(wait_for(lambda: self.serve_pids() == [proc.pid], 90))
            self.assertEqual(self.serve_pids(), [proc.pid])
        finally:
            proc.terminate()
            proc.wait(timeout=10)

    def test_ensure_does_not_start_a_second_daemon_while_the_first_is_busy_with_a_long_poll(self):
        pid = self.daemon()["pid"]
        run = self.start_run()
        poll = subprocess.Popen([sys.executable, "-B", self.bridge, "status", "--run-id", run, "--wait", "4"], env=self.env,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.addCleanup(self.release.touch)                                     # never leave the fake server holding
        self.assertTrue(wait_for(self.inflight.exists), "the poll never reached the server")
        r = self.run_bridge("ensure")                                          # answered while the poll is still held
        self.assertIsNone(poll.poll(), "the poll finished before ensure was answered, so nothing was proven")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(json.loads(r.stdout)["pid"], pid)
        self.assertFalse(json.loads(r.stdout)["started"])
        self.release.touch()
        poll.communicate(timeout=120)
        self.assertEqual(poll.returncode, 0)
        self.assertEqual(self.serve_pids(), [pid])


class Reach(BridgeCase):
    def test_status_lists_every_daemon_and_every_run(self):
        pid = self.daemon()["pid"]
        first, second = self.start_run(), self.start_run()
        r = self.run_bridge("status", "--run-id", first)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        bridge = json.loads(r.stdout[r.stdout.index('{\n  "bridge"'):])["bridge"]
        self.assertEqual([d["pid"] for d in bridge["daemons"]], [pid])
        self.assertEqual({x["run_id"] for x in bridge["runs"]}, {first, second})
        self.assertTrue(all(x["daemon"] == "reachable" and x["daemon_pid"] == pid for x in bridge["runs"]))

    def test_control_reaches_the_owning_daemon(self):
        self.daemon()
        run = self.start_run()
        r = self.run_bridge("control", "--run-id", run, "--command", "stop")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(json.loads(r.stdout)["state"], "stopped")

    def test_an_orphan_daemon_is_listed_and_control_stop_ends_it_with_its_child(self):
        pid = self.daemon()["pid"]
        run = self.start_run()
        child = self.info(pid)["mcp_pid"]
        for name in (f"cu_bridge-{pid}.sock", "cu_bridge.sock"):                # what an older bridge did: unlink its files
            try:
                (self.root / "_tools_/state" / name).unlink()
            except FileNotFoundError:
                pass
        listing = self.listing()
        orphan = next(d for d in listing["daemons"] if d["pid"] == pid)
        self.assertEqual((orphan["alive"], orphan["reachable"], orphan["orphan"]), (True, False, True))
        self.assertEqual(next(x for x in listing["runs"] if x["run_id"] == run)["daemon"], "orphan")
        status = self.run_bridge("status", "--run-id", run)
        self.assertEqual(status.returncode, 1)
        self.assertIn("an orphan", status.stderr)
        self.assertIn(f"`control --run-id {run} --command stop` ends it", status.stderr)
        self.assertEqual(self.serve_pids(), [pid])                             # status did not start a second daemon
        r = self.run_bridge("control", "--run-id", run, "--command", "stop")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("an orphan", r.stdout)
        self.assertTrue(self.gone(pid, child), "stop did not end the orphan daemon and its child")
        self.assertEqual(self.serve_pids(), [])

    def test_stop_daemon_ends_the_daemon_and_its_child(self):
        pid = self.daemon()["pid"]
        child = self.info(pid)["mcp_pid"]
        r = self.run_bridge("stop-daemon")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue(json.loads(r.stdout)["stopped"])
        self.assertTrue(self.gone(pid, child))

    def test_a_term_signal_runs_the_daemons_cleanup_so_its_child_ends_too(self):
        pid = self.daemon()["pid"]
        child = self.info(pid)["mcp_pid"]
        os.kill(pid, 15)
        self.assertTrue(self.gone(pid, child), "SIGTERM left the MCP child behind")
        self.assertFalse((self.root / "_tools_/state" / f"cu_bridge-{pid}.json").exists())


if __name__ == "__main__":
    unittest.main()
