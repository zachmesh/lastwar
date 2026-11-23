"""Tests for board_check.py on recorded fixtures and a local fake GraphQL server; never the live board.

Run: python3 -m unittest discover -s _tools_/board-check
"""
from __future__ import annotations

import copy
import http.server
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIX = HERE / "fixtures"
SPEC = importlib.util.spec_from_file_location("board_check", HERE / "board_check.py")
bc = importlib.util.module_from_spec(SPEC)
sys.modules["board_check"] = bc
SPEC.loader.exec_module(bc)

NEXUS_SEATS = "coordinator,reviewer,integrator"
SECRET = "SENTINEL-token-9f3a"


def load(name: str) -> dict:
    return json.loads((FIX / name).read_text())


def kinds(findings) -> list[str]:
    return sorted({f["kind"] for f in findings})


def run_cli(*args, env=None, cwd=None):
    full = {k: v for k, v in os.environ.items() if k not in ("GH_TOKEN", "GITHUB_TOKEN")}
    full.update(env or {})
    return subprocess.run([sys.executable, "-B", str(HERE / "board_check.py"), *args], capture_output=True, text=True,
                          env=full, cwd=cwd)


class Checks(unittest.TestCase):
    """The pure rules, on the recorded boards and on mutations of them."""

    def setUp(self):
        self.lastwar = load("lastwar-11-board.json")["repositoryOwner"]["projectV2"]
        self.nexus = load("nexus-8-board.json")["repositoryOwner"]["projectV2"]
        self.agents = bc.expected_agent("lastwar", ["coordinator", "operator", "scout", "researcher", "planner", "coach",
                                                    "toolsmith", "scribe"])

    def test_recorded_boards_are_clean_with_notes_for_reference_variances(self):
        f, n = bc.check_fields(self.lastwar["fields"]["nodes"], self.agents)
        self.assertEqual(f, [])
        self.assertTrue(any("verified" in x for x in n))
        f, n = bc.check_views(self.lastwar["views"]["nodes"])
        self.assertEqual(f, [])
        self.assertEqual(len(n), 1)
        f, _ = bc.check_fields(self.nexus["fields"]["nodes"], bc.expected_agent("nexus", NEXUS_SEATS.split(",")))
        self.assertEqual(f, [])
        self.assertEqual(bc.check_views(self.nexus["views"]["nodes"])[0], [])

    def test_strict_turns_variances_into_drift(self):
        self.assertEqual(kinds(bc.check_fields(self.lastwar["fields"]["nodes"], self.agents, True)[0]), ["extra"])
        self.assertEqual(kinds(bc.check_views(self.lastwar["views"]["nodes"], strict=True)[0]), ["columns"])

    def test_field_and_option_drift(self):
        nodes = copy.deepcopy(self.lastwar["fields"]["nodes"])
        field = lambda name: next(x for x in nodes if x["name"] == name)
        field("Priority")["options"].pop()                                  # missing P3
        field("Agent")["options"].append({"name": "lastwar intern"})        # extra Agent option
        field("Kind")["options"][0]["name"] = "Research"                    # off by case
        field("Work")["name"] = "work"                                      # field name off by case
        nodes.append({"name": "Sprint", "dataType": "ITERATION"})           # extra custom field
        got = bc.check_fields(nodes, self.agents)[0]
        self.assertEqual(kinds(got), ["case", "extra", "missing", "name-case"])
        subjects = {f["subject"] for f in got}
        self.assertEqual(subjects, {"Priority/P3", "Agent/lastwar intern", "Kind/research", "Work", "Sprint"})

    def test_agent_options_follow_the_seats_and_their_order(self):
        nodes = copy.deepcopy(self.lastwar["fields"]["nodes"])
        agent = next(x for x in nodes if x["name"] == "Agent")
        self.assertEqual([o["name"] for o in agent["options"]], self.agents)
        self.assertEqual(bc.check_fields(nodes, self.agents[:-1])[0][0]["kind"], "extra")   # a seat left TEAM.yaml
        agent["options"][1], agent["options"][2] = agent["options"][2], agent["options"][1]
        self.assertEqual(kinds(bc.check_fields(nodes, self.agents)[0]), ["order"])

    def test_view_drift(self):
        views = copy.deepcopy(self.lastwar["views"]["nodes"])
        views[1]["name"] = "By agent"
        views[0]["layout"] = "TABLE_LAYOUT"
        views[2]["filter"] = "status:Done"
        views[3]["groupByFields"] = {"nodes": [{"name": "Agent"}]}
        views[4]["fields"]["nodes"].pop()
        views[4]["fields"]["nodes"].append({"name": "Priority"})
        self.assertEqual(kinds(bc.check_views(views)[0]),
                         ["cards-extra", "cards-missing", "filter", "layout", "name-case", "swimlanes"])

    def test_view_count_missing_extra_and_order(self):
        views = copy.deepcopy(self.lastwar["views"]["nodes"])
        self.assertEqual(kinds(bc.check_views(views[:4])[0]), ["count", "missing"])
        extra = views + [{"name": "View 1", "layout": "TABLE_LAYOUT", "filter": "", "fields": {"nodes": []}}]
        self.assertEqual(kinds(bc.check_views(extra)[0]), ["count", "extra"])
        views[0], views[1] = views[1], views[0]
        self.assertEqual(kinds(bc.check_views(views)[0]), ["order"])

    def test_epic_by_type_changes_the_two_filters(self):
        got = bc.check_views(self.lastwar["views"]["nodes"], "type")[0]
        self.assertEqual({f["subject"] for f in got}, {"Kanban", "Epics"})


class Hierarchy(unittest.TestCase):
    ISSUES = [
        {"repo": "o/r", "number": 1, "labels": ["epic"], "parent": None, "items": [{"project": "P", "agent": "demo coach"}]},
        {"repo": "o/r", "number": 2, "labels": ["Epic"], "parent": None, "items": []},
        {"repo": "o/r", "number": 3, "labels": [], "parent": {"number": 1, "labels": ["epic"]},
         "items": [{"project": "P", "agent": "demo coach"}]},
        {"repo": "o/r", "number": 4, "labels": [], "parent": None, "items": [{"project": "P", "agent": None}]},
        {"repo": "o/r", "number": 5, "labels": [], "parent": {"number": 9, "labels": ["bug"]}, "items": []},
    ]

    def test_coverage_counts_and_percentages(self):
        f, c = bc.check_hierarchy(self.ISSUES, "P", {1: "## Acceptance criteria\n- x\n", 2: "nothing"})
        self.assertEqual((c["open_issues"], c["epics"], c["non_epic_issues"]), (5, 2, 3))
        self.assertEqual(c["with_parent_epic"], {"count": 1, "percent": 33.3})
        self.assertEqual(c["with_agent"], {"count": 1, "percent": 33.3})
        self.assertEqual(c["not_on_board"], {"count": 2, "first": [2, 5]})
        self.assertEqual(c["no_parent_epic"], {"count": 2, "first": [4, 5]})
        self.assertEqual(c["no_agent"], {"count": 2, "first": [4, 5]})
        self.assertEqual(c["no_parent_epic_and_no_agent"], {"count": 2, "first": [4, 5]})
        self.assertEqual([x["subject"] for x in f if x["kind"] == "epic-criteria"], ["#2"])

    def test_first_ten_only(self):
        many = [{"repo": "o/r", "number": n, "labels": [], "parent": None, "items": []} for n in range(30, 0, -1)]
        _, c = bc.check_hierarchy(many, "P", {})
        self.assertEqual(c["not_on_board"], {"count": 30, "first": list(range(1, 11))})

    def test_heading_off_by_case_is_a_finding(self):
        f, _ = bc.check_hierarchy(self.ISSUES[:1], "P", {1: "## acceptance Criteria\n"})
        self.assertEqual(kinds(f), ["epic-criteria-case"])

    def test_a_clean_hierarchy_has_no_findings(self):
        f, _ = bc.check_hierarchy([self.ISSUES[0], self.ISSUES[2]], "P", {1: "# E\n\n## Acceptance criteria\n- x\n"})
        self.assertEqual([x for x in f if x["area"] == "hierarchy"], [])


class FixtureRuns(unittest.TestCase):
    P = str(FIX / "lastwar-11")

    def test_lastwar_fixture_reports_structure_ok_and_only_triage_drift(self):
        r = run_cli("--fixture", self.P)
        self.assertEqual(r.returncode, 1, r.stderr)
        d = json.loads(r.stdout)
        self.assertTrue(d["structural_ok"])
        self.assertEqual({f["area"] for f in d["findings"]}, {"triage"})
        self.assertEqual(d["source"], "fixture")
        self.assertEqual(d["views"]["found"], d["views"]["expected"])
        self.assertEqual(d["options"]["Priority"]["found"], ["P0", "P1", "P2", "P3"])
        self.assertEqual(d["options"]["Agent"]["found"], d["options"]["Agent"]["expected"])
        self.assertEqual(d["coverage"]["open_issues"], 25)
        self.assertEqual(len(d["coverage"]["not_on_board"]["first"]), 10)

    def test_nexus_fixture_is_clean(self):
        r = run_cli("--fixture", str(FIX / "nexus-8"), "--project", "8", "--seats", NEXUS_SEATS, "--structure-only")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        d = json.loads(r.stdout)
        self.assertTrue(d["ok"] and d["structural_ok"])
        self.assertEqual(d["drift_findings"], 0)

    def test_nexus_checked_against_another_teams_seats_drifts(self):
        r = run_cli("--fixture", str(FIX / "nexus-8"), "--project", "8", "--seats", "coordinator", "--structure-only")
        self.assertEqual(r.returncode, 1)
        self.assertEqual(kinds(json.loads(r.stdout)["findings"]), ["extra"])

    def test_mutated_recording_exits_one_with_the_structural_finding(self):
        tmp = Path(tempfile.mkdtemp(prefix="board-check-test-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        for suffix in ("board", "issues"):
            shutil.copy(FIX / f"lastwar-11-{suffix}.json", tmp / f"b-{suffix}.json")
        board = json.loads((tmp / "b-board.json").read_text())
        board["repositoryOwner"]["projectV2"]["views"]["nodes"].pop()
        (tmp / "b-board.json").write_text(json.dumps(board))
        d = json.loads(run_cli("--fixture", str(tmp / "b")).stdout)
        self.assertFalse(d["structural_ok"])
        self.assertEqual(kinds([f for f in d["findings"] if f["area"] == "view"]), ["count", "missing"])

    def test_text_report(self):
        r = run_cli("--fixture", self.P, "--text")
        self.assertIn("DRIFT, 4 finding(s)", r.stdout)
        self.assertIn("structure (fields, options, views): ok", r.stdout)

    def test_missing_fixture_file_exits_two(self):
        r = run_cli("--fixture", str(FIX / "nowhere"))
        self.assertEqual(r.returncode, 2)
        self.assertIn("fixture file missing", r.stderr)


class Defaults(unittest.TestCase):
    def test_the_default_board_is_the_current_team_board(self):
        self.assertEqual((bc.DEFAULT_OWNER, bc.DEFAULT_PROJECT), ("zachmesh", 1))
        r = run_cli("--fixture", str(FIX / "lastwar-11"))
        self.assertEqual((json.loads(r.stdout)["owner"], json.loads(r.stdout)["project"]), ("zachmesh", 1))
        r = run_cli("--help")
        self.assertIn("default 1 of owner zachmesh", " ".join(r.stdout.split()))


class Token(unittest.TestCase):
    def test_token_comes_only_from_the_environment(self):
        self.assertEqual(bc.token_from_env({"GH_TOKEN": "a", "GITHUB_TOKEN": "b"}), "a")
        self.assertEqual(bc.token_from_env({"GITHUB_TOKEN": " b "}), "b")
        for env in ({}, {"GH_TOKEN": "  "}):
            with self.assertRaises(bc.ReadError):
                bc.token_from_env(env)

    def test_no_token_exits_two_with_a_clear_message_and_reads_no_keychain(self):
        tmp = Path(tempfile.mkdtemp(prefix="board-check-test-"))
        self.addCleanup(shutil.rmtree, tmp, True)
        fake = tmp / "git"
        marker = tmp / "git-was-called"
        fake.write_text(f"#!/bin/sh\necho called >> {marker}\nexit 1\n")
        fake.chmod(0o755)
        r = run_cli(env={"PATH": f"{tmp}:{os.environ['PATH']}"})
        self.assertEqual(r.returncode, 2)
        self.assertIn("no token: set GH_TOKEN or GITHUB_TOKEN", r.stderr)
        self.assertEqual(r.stdout, "")
        self.assertFalse(marker.exists(), "board_check ran git (a credential helper)")

    def test_source_never_touches_a_credential_helper(self):
        source = (HERE / "board_check.py").read_text()
        self.assertNotIn("import subprocess", source)
        self.assertNotIn("credential fill", source)


class Handler(http.server.BaseHTTPRequestHandler):
    seen_auth: list = []
    mode = "recorded"

    def log_message(self, *a):
        pass

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        Handler.seen_auth.append(self.headers.get("Authorization"))
        query = body["query"]
        if Handler.mode == "401":
            self.send_response(401)
            self.end_headers()
            self.wfile.write(b'{"message":"Bad credentials"}')
            return
        if Handler.mode == "graphql-error":
            payload = {"errors": [{"message": "Resource not accessible"}]}
        elif "items(first:100,after:" in query:   # the recorded board has more than one page of items
            payload = {"data": {"repositoryOwner": {"projectV2": {"items": {"pageInfo": {"hasNextPage": False,
                                                                                          "endCursor": None}, "nodes": []}}}}}
        elif "projectV2(number" in query and "views(first" in query:
            payload = {"data": load("lastwar-11-board.json")}
        elif "issues(first:100,states:OPEN" in query:
            payload = {"data": load("lastwar-11-issues.json")}
        else:
            payload = {"data": {"repository": {}}}
        data = json.dumps(payload).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(data)


class LivePath(unittest.TestCase):
    """The network code path against a local fake server that replays the recorded responses."""

    def serve(self, mode):
        Handler.mode, Handler.seen_auth = mode, []
        server = http.server.HTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        return f"http://127.0.0.1:{server.server_port}/graphql"

    def test_live_path_matches_the_fixture_path_and_sends_the_token_only_as_a_header(self):
        url = self.serve("recorded")
        live = run_cli("--api-url", url, env={"GH_TOKEN": SECRET})
        recorded = run_cli("--fixture", str(FIX / "lastwar-11"))
        self.assertEqual(live.returncode, 1, live.stderr)
        self.assertNotIn(SECRET, live.stdout + live.stderr)
        self.assertEqual(set(Handler.seen_auth), {f"bearer {SECRET}"})
        a, b = json.loads(live.stdout), json.loads(recorded.stdout)
        a.pop("source"), b.pop("source")
        self.assertEqual(a, b)

    def test_http_and_graphql_errors_exit_two_without_leaking_the_token(self):
        for mode in ("401", "graphql-error"):
            r = run_cli("--api-url", self.serve(mode), env={"GH_TOKEN": SECRET})
            self.assertEqual(r.returncode, 2, mode)
            self.assertNotIn(SECRET, r.stdout + r.stderr, mode)

    def test_unreachable_server_exits_two_without_leaking_the_token(self):
        r = run_cli("--api-url", "http://127.0.0.1:9/graphql", env={"GH_TOKEN": SECRET})
        self.assertEqual(r.returncode, 2)
        self.assertNotIn(SECRET, r.stdout + r.stderr)
        self.assertIn("unreachable", r.stderr)


if __name__ == "__main__":
    unittest.main()
