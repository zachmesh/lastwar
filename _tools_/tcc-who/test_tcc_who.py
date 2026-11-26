"""Tests for tcc_who.py: the Python list (what counts as a Python, the shortened command, masked secrets, the parent chain to the DSH host, the hint for a
home-glob tool) and the tccd window read (grouping by requester, Apple's own left out, the protected-folder pointer, time forms, limits, no path or
reason ever printed). `ps` and `log` output come from recorded files (TCC_WHO_PS_FILE, TCC_WHO_LOG_FILE).

Run: python3 -m unittest discover -s _tools_/tcc-who
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "tcc_who.py"
sys.path.insert(0, str(HERE))
import tcc_who as tw  # noqa: E402

PY = "/opt/homebrew/Cellar/python@3.12/3.12.12_2/Frameworks/Python.framework/Versions/3.12/Resources/Python.app/Contents/MacOS/Python"
PS = f"""    1     0 11-15:00:00 /sbin/launchd
97086     1    01:50:00 /Users/someone/.volta/bin/dsh web
97087 97086    01:50:00 node /Users/someone/.volta/tools/image/packages/@deepseek-ai/dsh/bin/dsh web
65586 97087    01:44:38 bash -c cd /work && python3 release-watch.py 8
65589 65586    01:44:38 {PY} release-watch.py 8
10975 97087    03:02 {PY} /Users/someone/reflection/_tools_/session-inbox/session-inbox.py send --roster x --to y --text GH_TOKEN=ghp_abcdefghijklmnop1234
20001 97087    00:05 /usr/bin/python3 -c print(1)
30001 97087    02:00 vim notes.md
40001     1 2-03:04:05 /Users/someone/.hermes/hermes-agent/venv/bin/python -m hermes_cli.main gateway run
50001 97087    10:00 node server.mjs python
"""
LOG = """Timestamp               Ty Process[PID:TID]
2026-11-26 08:58:18.974 Df tccd[420:6aa5ca3] [com.apple.TCC:access] AUTHREQ_CTX: msgID=84090.3, function=TCCAccessRequest, service=kTCCServiceSystemPolicyAllFiles, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>
2026-11-26 08:58:18.974 Df tccd[420:6aa5ca3] [com.apple.TCC:access] AUTHREQ_ATTRIBUTION: msgID=84090.3, attribution={responsible={TCCDProcess: identifier=volta_shim-abc, pid=97086, auid=501, euid=501, responsible_path=/Users/someone/.volta/bin/volta-shim, binary_path=/Users/someone/.volta/bin/volta-shim}, accessing={TCCDProcess: identifier=org.python.python, pid=10975, auid=501, euid=501, binary_path=/opt/homebrew/x/Python}, requesting={TCCDProcess: identifier=com.apple.sandboxd, pid=500, auid=0, euid=0, binary_path=/usr/libexec/sandboxd}, },
2026-11-26 08:58:18.981 Df tccd[651:6aa3ab6] [com.apple.TCC:access] AUTHREQ_CTX: msgID=84090.4, function=TCCAccessRequest, service=kTCCServiceMediaLibrary, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>
2026-11-26 08:58:18.981 Df tccd[651:6aa3ab6] [com.apple.TCC:access] AUTHREQ_ATTRIBUTION: msgID=84090.4, attribution={responsible={TCCDProcess: identifier=volta_shim-abc, pid=97086, auid=501, euid=501, binary_path=/Users/someone/.volta/bin/volta-shim}, accessing={TCCDProcess: identifier=org.python.python, pid=10975, auid=501, euid=501, binary_path=/opt/homebrew/x/Python}, },
2026-11-26 08:58:19.038 Df tccd[651:6aa6e2a] [com.apple.TCC:access] AUTHREQ_CTX: msgID=84090.5, function=TCCAccessRequest, service=kTCCServiceSystemPolicyDesktopFolder, preflight=no, query=1, client_dict=(null), daemon_dict=<private>
2026-11-26 08:58:19.038 Df tccd[651:6aa6e2a] [com.apple.TCC:access] AUTHREQ_ATTRIBUTION: msgID=84090.5, attribution={responsible={TCCDProcess: identifier=volta_shim-abc, pid=97086, auid=501, euid=501, binary_path=/Users/someone/.volta/bin/volta-shim}, accessing={TCCDProcess: identifier=org.python.python, pid=10975, auid=501, euid=501, binary_path=/opt/homebrew/x/Python}, },
2026-11-26 08:58:19.093 Df tccd[420:6aa6e28] [com.apple.TCC:access] AUTHREQ_CTX: msgID=419.175434, function=TCCAccessRequest, service=kTCCServiceListenEvent, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>
2026-11-26 08:58:19.105 Df tccd[420:6aa6e28] [com.apple.TCC:access] AUTHREQ_ATTRIBUTION: msgID=419.175434, attribution={accessing={TCCDProcess: identifier=com.apple.UserNotificationCenter, pid=11040, auid=501, euid=501, binary_path=/System/x/UserNotificationCenter}, requesting={TCCDProcess: identifier=com.apple.WindowServer, pid=419, auid=88, euid=88, binary_path=/System/x/WindowServer}, },
2026-11-26 08:58:24.900 Df tccd[651:6aa3ab6] [com.apple.TCC:access] AUTHREQ_CTX: msgID=11533.1, function=TCCAccessRequest, service=kTCCServiceAddressBook, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>
2026-11-26 08:58:24.914 Df tccd[651:6aa3ab6] [com.apple.TCC:access] AUTHREQ_ATTRIBUTION: msgID=11533.1, attribution={requesting={TCCDProcess: identifier=com.apple.routined, pid=11533, auid=501, euid=501, binary_path=/usr/libexec/routined}, },
2026-11-26 09:01:16.279 Df tccd[420:6aa6e28] [com.apple.TCC:access] AUTHREQ_CTX: msgID=21427.1, function=TCCAccessRequest, service=kTCCServiceScreenCapture, preflight=yes, query=1, client_dict=(null), daemon_dict=<private>
2026-11-26 09:01:16.280 Df tccd[420:6aa6e28] [com.apple.TCC:access] AUTHREQ_ATTRIBUTION: msgID=21427.1, attribution={requesting={TCCDProcess: identifier=com.reflection.cu-helper, pid=21427, auid=501, euid=501, binary_path=/Users/someone/.computer-use/helper/CUHelper.app/Contents/MacOS/CUHelper}, },
"""


class PythonList(unittest.TestCase):
    def rows(self, **kw):
        return tw.pythons(tw.parse_ps(PS), **kw)

    def test_etime_forms(self):
        self.assertEqual([tw.etime_seconds(t) for t in ("05:03", "01:02:03", "2-03:04:05", "00:05")], [303, 3723, 183845, 5])

    def test_what_counts_as_a_python(self):
        ids = {r["pid"] for r in self.rows()}
        self.assertEqual(ids, {65589, 10975, 20001, 40001})                      # the app binary, a system python3, a venv python; not node, vim, bash or a word in args

    def test_longest_running_first_and_min_age(self):
        self.assertEqual([r["pid"] for r in self.rows()], [40001, 65589, 10975, 20001])
        self.assertEqual([r["pid"] for r in self.rows(min_age=120)], [40001, 65589, 10975])

    def test_only_the_script_file_name_is_kept_never_a_path_or_an_argument(self):
        scripts = {r["pid"]: r["script"] for r in self.rows()}
        self.assertEqual(scripts, {65589: "release-watch.py", 10975: "session-inbox.py", 20001: "-c (inline code)", 40001: "-m hermes_cli.main"})
        text = tw.show_pythons(self.rows())
        for private in ("/Users/", "someone", "ghp_", "--roster", "GH_TOKEN", "/opt/homebrew"):
            self.assertNotIn(private, text)

    def test_a_module_or_an_option_before_the_script(self):
        self.assertEqual(tw.script_name("/x/python -u -B /a/b/run.py arg"), "run.py")
        self.assertEqual(tw.script_name("/x/python -m http.server 8765"), "-m http.server")
        self.assertEqual(tw.script_name("/x/python"), "(interactive)")
        self.assertEqual(tw.script_name("/x/python '/a b/my script.py' x"), "my script.py")

    def test_secrets_are_masked_in_what_little_is_shown(self):
        self.assertEqual(tw.mask("x --api-key=abc123 y Bearer tok123 z ghp_abcdefghijk1234"), "x --api-key=*** y *** z ***")
        self.assertNotIn("ghp_", tw.script_name("/x/python ghp_abcdefghijklmnop1234.py"))

    def test_the_parent_chain_ends_at_the_dsh_host_by_name(self):
        chains = {r["pid"]: r["chain"] for r in self.rows()}
        self.assertEqual(chains[65589], ["bash(65586)", "node(97087) [DSH host]"])
        self.assertEqual(chains[40001], [])

    def test_the_kill_rule_needs_all_three_conditions(self):
        procs = tw.parse_ps(f"""97087 1 01:00:00 node /x/dsh web
100 97087 03:02 {PY} /a/session-inbox.py send --to y
101 97087 00:30 {PY} /a/session-inbox.py send --to y
102 97087 05:00 {PY} /a/other-tool.py
103 97087 05:00 {PY} /a/release-watch.py 8
1335 1 99:00:00 {PY} /a/cu_bridge.py serve
""")
        verdicts = {r["pid"]: r["verdict"] for r in tw.pythons(procs)}
        self.assertEqual(verdicts[100], "eligible")
        self.assertIn("alive 30 s, not over 60", verdicts[101])
        self.assertIn("not session-inbox.py", verdicts[102])
        self.assertIn("it is release-watch", verdicts[103])
        self.assertEqual(verdicts[1335].count("bridge daemon"), 1)
        text = tw.show_pythons(tw.pythons(procs))
        self.assertIn("1 could be stopped under the 17:11Z rule", text)
        self.assertIn("stop it once with `kill 100`, no -9, BEFORE the window is dismissed", text)
        self.assertNotIn("kill 101", text)

    def test_no_eligible_python_points_at_the_single_killall(self):
        procs = tw.parse_ps(f"1335 1 99:00:00 {PY} /a/cu_bridge.py serve\n65589 1 01:00:00 {PY} /a/release-watch.py 8\n")
        self.assertIn("none: if a window stands, only the one `killall -9 UserNotificationCenter`", tw.show_pythons(tw.pythons(procs)))
        self.assertIn("1 could be stopped under the 17:11Z rule", tw.show_pythons(self.rows()))                  # the fixture's 3-minute session-inbox call is eligible

    def test_the_home_glob_hint_follows_the_script_name_not_the_arguments(self):
        procs = tw.parse_ps(f"1 0 00:01 {PY} /a/session-relay.py send --text session-inbox.py\n2 0 00:01 {PY} /a/session-inbox.py read\n")
        hints = {r["pid"]: r["hint"] for r in tw.pythons(procs)}
        self.assertEqual(hints[1], "")
        self.assertIn("globs ~/*/*/TEAM.yaml", hints[2])

    def test_the_tool_does_not_list_itself(self):
        procs = tw.parse_ps(f"{os.getpid()} 1 00:01 {PY} tcc_who.py pythons\n")
        self.assertEqual(tw.pythons(procs), [])


class Window(unittest.TestCase):
    def rows(self):
        return tw.parse_tccd(LOG)

    def test_requests_are_joined_with_their_attribution(self):
        rows = self.rows()
        python = [r for r in rows if r["who"][0] == "org.python.python"]
        self.assertEqual([(r["service"], r["preflight"]) for r in python], [("SystemPolicyAllFiles", "yes"), ("MediaLibrary", "yes"), ("SystemPolicyDesktopFolder", "no")])
        self.assertEqual(python[0]["responsible"], ("volta_shim-abc", 97086))

    def test_apple_services_are_left_out_unless_all(self):
        rows = self.rows()
        names = [g["who"][0] for g in tw.group(rows, False)]
        self.assertEqual(names, ["org.python.python", "com.reflection.cu-helper"])
        self.assertIn("com.apple.routined", [g["who"][0] for g in tw.group(rows, True)])

    def test_the_output_names_the_python_its_host_and_the_services_and_points_at_the_pythons_list(self):
        text = tw.show_window(self.rows(), tw.group(self.rows(), False), "16:58:10Z", "16:58:25Z", False)
        self.assertIn("org.python.python pid 10975  responsible volta_shim-abc pid 97086  ->  MediaLibrary, SystemPolicyAllFiles, SystemPolicyDesktopFolder(access)", text)
        self.assertIn("UserNotificationCenter pid 11040 first asked at 08:58:19.093", text)
        self.assertIn("times below are this Mac's local time", text)
        self.assertIn("asked for protected folders: find it with `tcc_who.py pythons` BEFORE dismissing the window", text)
        self.assertNotIn("/Users/", text)                                                   # no path ever
        self.assertNotIn("binary_path", text)

    def test_the_cu_helper_alone_is_not_a_protected_folder_request(self):
        only = [r for r in self.rows() if r["who"][0] == "com.reflection.cu-helper"]
        text = tw.show_window(only, tw.group(only, False), "17:01:10Z", "17:01:20Z", False)
        self.assertIn("com.reflection.cu-helper pid 21427", text)
        self.assertNotIn("asked for protected folders", text)

    def test_an_empty_window_says_so(self):
        text = tw.show_window([], [], "01:00:00Z", "01:00:10Z", False)
        self.assertIn("no non-Apple requester in this window", text)

    def test_time_forms(self):
        today = datetime(2026, 11, 26, 18, 0, tzinfo=timezone.utc)
        self.assertEqual(tw.parse_when("16:58:10Z", today), datetime(2026, 11, 26, 16, 58, 10, tzinfo=timezone.utc))
        self.assertEqual(tw.parse_when("2026-11-25T03:00:00Z", today), datetime(2026, 11, 25, 3, 0, tzinfo=timezone.utc))
        self.assertEqual(tw.parse_when("16:58Z", today), datetime(2026, 11, 26, 16, 58, tzinfo=timezone.utc))
        with self.assertRaises(ValueError):
            tw.parse_when("yesterday", today)


class CommandLine(unittest.TestCase):
    def run_tool(self, *args, ps=PS, log=LOG):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ)
            (Path(tmp) / "ps.txt").write_text(ps)
            (Path(tmp) / "log.txt").write_text(log)
            env["TCC_WHO_PS_FILE"], env["TCC_WHO_LOG_FILE"] = str(Path(tmp) / "ps.txt"), str(Path(tmp) / "log.txt")
            return subprocess.run([sys.executable, "-B", str(TOOL), *args], capture_output=True, text=True, env=env)

    def test_pythons_prints_the_list(self):
        r = self.run_tool("pythons", "--min-age", "120")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("3 Python process(es)", r.stdout)
        self.assertIn("pid 65589  script release-watch.py  elapsed 1h44m38s  parent bash(65586)  chain bash(65586) < node(97087) [DSH host]", r.stdout)
        self.assertNotIn("ghp_", r.stdout)
        self.assertNotIn("/Users/", r.stdout)

    def test_window_prints_the_requesters(self):
        r = self.run_tool("window", "16:58:10Z", "16:58:25Z")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("org.python.python pid 10975", r.stdout)

    def test_window_limits_and_bad_times_exit_two(self):
        self.assertEqual(self.run_tool("window", "16:58:25Z", "16:58:10Z").returncode, 2)
        self.assertEqual(self.run_tool("window", "10:00:00Z", "12:00:00Z").returncode, 2)
        self.assertEqual(self.run_tool("window", "soon", "later").returncode, 2)

    def test_the_tool_writes_nothing(self):
        before = sorted(p.name for p in HERE.iterdir())
        self.run_tool("pythons")
        self.run_tool("window", "16:58:10Z", "16:58:25Z")
        self.assertEqual(sorted(p.name for p in HERE.iterdir()), before)


if __name__ == "__main__":
    unittest.main()
