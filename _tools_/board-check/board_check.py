#!/usr/bin/env python3
"""board_check: check a GitHub Project board against reflection's project-boards convention.

Reports, as JSON, any missing or extra field, option or view, a name off by case, a view whose layout, columns, swimlanes,
card fields or filter differ (five views in order), the Agent options (TEAM.yaml seats) and Priority options, the Epic
parent and Agent coverage of open issues, and epics without `## Acceptance criteria`. Read-only. The token comes ONLY
from GH_TOKEN or GITHUB_TOKEN in the caller's environment: it never reads the keychain or a credential helper, and
never prints the token. `--fixture PREFIX` reads recorded responses instead of the network (no token needed).
Exit 0 clean, 1 drift, 2 cannot read or no token.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

VERSION = "1.0.0"
CONVENTION = "_conventions_/issue-driven-work/project-boards.md (reflection)"
API = "https://api.github.com/graphql"
DEFAULT_OWNER, DEFAULT_PROJECT = "dtadpole", 11

# --- the convention, as data -----------------------------------------------------------------------------------
STATUS = ["Draft", "Ready", "In progress", "Waiting", "In review", "Needs owner", "Done", "Sunset"]
FEEDBACK_STATE = ["new", "triaged", "accumulating", "accepted", "applied", "rejected", "duplicate", "wontfix",
                  "superseded", "archived"]
FEEDBACK_KIND = ["defect", "gap", "ambiguity", "outdated", "friction", "proposal", "works-well"]   # FEEDBACK-ITEM schema
# name, type, options (None: text, or Agent which follows TEAM.yaml)
FIELDS = [
    ("Status", "SINGLE_SELECT", STATUS), ("Agent", "SINGLE_SELECT", None), ("Session", "TEXT", None),
    ("Kind", "SINGLE_SELECT", ["research", "tool", "ops", "knowledge"]),
    ("Priority", "SINGLE_SELECT", ["P0", "P1", "P2", "P3"]),
    ("Feedback state", "SINGLE_SELECT", FEEDBACK_STATE), ("Feedback kind", "SINGLE_SELECT", FEEDBACK_KIND),
    ("Feedback severity", "SINGLE_SELECT", ["high", "medium", "low"]), ("Feedback unit", "TEXT", None),
    ("Feedback item", "TEXT", None), ("Feedback by", "TEXT", None), ("Work", "TEXT", None),
]
CUSTOM_TYPES = {"TEXT", "NUMBER", "DATE", "SINGLE_SELECT", "ITERATION"}   # every other field is a built-in column
# Reference-board practice the convention text does not state. Each is a note, and drift under --strict.
ACCEPTED_EXTRA_OPTIONS = {"Feedback state": ["verified"]}   # on nexus #8 and lastwar #11; absent from dsh-web-ops #6
DEFAULT_CARDS = ["Title", "Assignees", "Status", "Linked pull requests", "Sub-issues progress"]
VIEW_NAMES = ["Kanban", "By Agent", "Recently Done", "Feedback loop", "Epics"]


def view_specs(epic_by: str = "label") -> list[dict]:
    epic, not_epic = ("label:epic", "-label:epic") if epic_by == "label" else ("type:Epic", "-type:Epic")
    return [
        {"name": "Kanban", "filter": f"no:feedback-state {not_epic}", "columns": ["Status"], "cards": ["Work"]},
        {"name": "By Agent", "filter": "-status:Done,Sunset", "columns": ["Agent"], "cards": ["Work"]},
        {"name": "Recently Done", "filter": "status:Done,Sunset updated:>@today-14d", "columns": ["Agent"], "cards": []},
        # all three reference boards group Feedback loop by Status; the convention table says Feedback state
        {"name": "Feedback loop", "filter": "has:feedback-state updated:>@today-14d",
         "columns": ["Feedback state", "Status"], "cards": ["Agent", "Feedback kind", "Feedback severity", "Work"]},
        {"name": "Epics", "filter": epic, "columns": ["Status"], "cards": ["Agent", "Work"]},
    ]


class ReadError(Exception):
    """The board cannot be read (exit 2)."""


# --- pure checks (also used by the self-test) --------------------------------------------------------------------
def finding(area: str, kind: str, subject: str, message: str) -> dict:
    return {"area": area, "kind": kind, "subject": subject, "message": message}


def expected_agent(team: str, seats: list[str]) -> list[str]:
    return ["owner (zhenc)"] + [f"{team} {s}" for s in seats]


def check_fields(nodes: list[dict], agent_options: list[str], strict: bool = False) -> tuple[list[dict], list[str]]:
    out, notes = [], []
    by_name = {n["name"]: n for n in nodes}
    folded = {n["name"].casefold(): n for n in nodes}
    expected_names = {f[0] for f in FIELDS}
    for name, kind, options in FIELDS:
        node = by_name.get(name)
        if node is None and name.casefold() in folded:
            node = folded[name.casefold()]
            out.append(finding("field", "name-case", name, f"field is named {node['name']!r}, expected {name!r}"))
        if node is None:
            out.append(finding("field", "missing", name, f"missing {kind.lower().replace('_', ' ')} field {name!r}"))
            continue
        if node.get("dataType") != kind:
            out.append(finding("field", "type", name, f"{name!r} is {node.get('dataType')}, expected {kind}"))
            continue
        if kind != "SINGLE_SELECT":
            continue
        want = agent_options if name == "Agent" else options
        have = [o["name"] for o in node.get("options", [])]
        accepted = [] if strict else ACCEPTED_EXTRA_OPTIONS.get(name, [])
        for extra in [o for o in have if o in accepted]:
            notes.append(f"field {name!r}: option {extra!r} is a reference-board extension, not in the convention text")
        have_core = [o for o in have if o not in accepted]
        missing = [o for o in want if o not in have_core]
        extra = [o for o in have_core if o not in want]
        for o in list(missing):
            twin = next((e for e in extra if e.casefold() == o.casefold()), None)
            if twin:
                out.append(finding("option", "case", f"{name}/{o}", f"option {twin!r} should be {o!r}"))
                missing.remove(o)
                extra.remove(twin)
        for o in missing:
            out.append(finding("option", "missing", f"{name}/{o}", f"{name!r} lacks option {o!r}"))
        for o in extra:
            out.append(finding("option", "extra", f"{name}/{o}", f"{name!r} has extra option {o!r}"))
        if sorted(have_core) == sorted(want) and have_core != want:
            out.append(finding("option", "order", name, f"{name!r} options are ordered {have_core}, expected {want}"))
    for n in nodes:
        if n.get("dataType") in CUSTOM_TYPES and n["name"] not in expected_names and n["name"].casefold() not in {
                e.casefold() for e in expected_names}:
            out.append(finding("field", "extra", n["name"], f"extra {n['dataType'].lower().replace('_', ' ')} field "
                                                          f"{n['name']!r}"))
    return out, notes


def names(conn: dict | None) -> list[str]:
    return [n["name"] for n in (conn or {}).get("nodes", []) if n and "name" in n]


def check_views(nodes: list[dict], epic_by: str = "label", strict: bool = False) -> tuple[list[dict], list[str]]:
    out, notes, specs = [], [], view_specs(epic_by)
    if len(nodes) != len(specs):
        out.append(finding("view", "count", "views", f"{len(nodes)} view(s), exactly {len(specs)} expected: "
                                                       f"{', '.join(repr(n['name']) for n in nodes)}"))
    by_name = {v["name"]: v for v in nodes}
    folded = {v["name"].casefold(): v for v in nodes}
    matched: list[dict] = []
    for spec in specs:
        name = spec["name"]
        view = by_name.get(name)
        if view is None and name.casefold() in folded:
            view = folded[name.casefold()]
            out.append(finding("view", "name-case", name, f"view is named {view['name']!r}, expected {name!r}"))
        if view is None:
            out.append(finding("view", "missing", name, f"missing view {name!r}"))
            continue
        matched.append(view)
        if view.get("layout") != "BOARD_LAYOUT":
            out.append(finding("view", "layout", name, f"{name!r} is {view.get('layout')}, expected BOARD_LAYOUT"))
        have_filter = " ".join((view.get("filter") or "").split())
        if have_filter != spec["filter"]:
            out.append(finding("view", "filter", name, f"{name!r} filter is {have_filter!r}, expected {spec['filter']!r}"))
        columns = names(view.get("verticalGroupByFields"))
        accepted = spec["columns"][:1] if strict else spec["columns"]
        if columns != [accepted[0]] and not (len(columns) == 1 and columns[0] in accepted):
            out.append(finding("view", "columns", name, f"{name!r} columns are {columns}, expected [{accepted[0]!r}]"))
        elif columns[0] != spec["columns"][0]:
            notes.append(f"view {name!r}: columns are {columns[0]!r}; the convention table says {spec['columns'][0]!r} "
                         f"(all reference boards use {columns[0]!r})")
        lanes = names(view.get("groupByFields"))
        if lanes:
            out.append(finding("view", "swimlanes", name, f"{name!r} has swimlanes {lanes}; the convention has none"))
        want = DEFAULT_CARDS + spec["cards"]
        have = names(view.get("fields"))
        for f in [c for c in want if c not in have]:
            out.append(finding("view", "cards-missing", name, f"{name!r} cards lack {f!r}"))
        for f in [c for c in have if c not in want]:
            out.append(finding("view", "cards-extra", name, f"{name!r} cards show extra {f!r}"))
    expected_order = [s["name"] for s in specs]
    if len(matched) == len(specs) and [v["name"] for v in matched] != [v["name"] for v in nodes if v in matched]:
        out.append(finding("view", "order", "views", f"views are listed {[v['name'] for v in nodes]}, expected "
                                                     f"{expected_order}"))
    for v in nodes:
        if v not in matched:
            out.append(finding("view", "extra", v["name"], f"extra view {v['name']!r}"))
    return out, notes


def first(numbers: list[int], n: int = 10) -> list[int]:
    return sorted(numbers)[:n]


def check_hierarchy(issues: list[dict], project_id: str, epic_bodies: dict[int, str]) -> tuple[list[dict], dict]:
    """issues: open issues with labels, parent (number, labels) and project items (project id, Agent)."""
    out, epics = [], []
    not_on_board, no_parent, no_agent = [], [], []
    for it in issues:
        labels = {n.casefold() for n in it["labels"]}
        items = [p for p in it["items"] if p["project"] == project_id]
        if not items:
            not_on_board.append(it["number"])
        if "epic" in labels:
            epics.append(it["number"])
            continue
        parent = it.get("parent")
        if not (parent and "epic" in {n.casefold() for n in parent["labels"]}):
            no_parent.append(it["number"])
        if not any(p.get("agent") for p in items):
            no_agent.append(it["number"])
    for num in sorted(epics):
        body = epic_bodies.get(num, "")
        m = re.search(r"(?mi)^##[ \t]+acceptance criteria[ \t]*$", body)
        if not m:
            out.append(finding("hierarchy", "epic-criteria", f"#{num}", f"epic #{num} has no '## Acceptance criteria' heading"))
        elif m.group(0).split(None, 1)[1].strip() != "Acceptance criteria":
            out.append(finding("hierarchy", "epic-criteria-case", f"#{num}",
                               f"epic #{num} heading is {m.group(0)!r}, expected '## Acceptance criteria'"))
    both = sorted(set(no_parent) & set(no_agent))
    non_epic = len(issues) - len(epics)
    pct = lambda n: round(100 * n / non_epic, 1) if non_epic else 100.0
    triage = {
        "open_issues": len(issues), "epics": len(epics), "non_epic_issues": non_epic,
        "with_parent_epic": {"count": non_epic - len(no_parent), "percent": pct(non_epic - len(no_parent))},
        "with_agent": {"count": non_epic - len(no_agent), "percent": pct(non_epic - len(no_agent))},
        "not_on_board": {"count": len(not_on_board), "first": first(not_on_board)},
        "no_parent_epic": {"count": len(no_parent), "first": first(no_parent)},
        "no_agent": {"count": len(no_agent), "first": first(no_agent)},
        "no_parent_epic_and_no_agent": {"count": len(both), "first": first(both)},
    }
    labels = {"not_on_board": "open issues not on the board",
              "no_parent_epic": "open non-epic issues with no parent Epic",
              "no_agent": "open non-epic issues with no Agent",
              "no_parent_epic_and_no_agent": "open non-epic issues with no parent Epic and no Agent"}
    for key, text in labels.items():
        if triage[key]["count"]:
            out.append(finding("triage", key, key, f"{triage[key]['count']} {text}; first {triage[key]['first']}"))
    return out, triage


# --- reading the board: the network (token from the environment only) or recorded fixtures -----------------------
def token_from_env(env=None) -> str:
    env = os.environ if env is None else env
    for name in ("GH_TOKEN", "GITHUB_TOKEN"):
        value = (env.get(name) or "").strip()
        if value:
            return value
    raise ReadError("no token: set GH_TOKEN or GITHUB_TOKEN in the environment (read access to projects and the "
                    "repository); this tool never reads the keychain or a credential helper")


FIELD_NAME = "... on ProjectV2Field{name} ... on ProjectV2SingleSelectField{name} ... on ProjectV2IterationField{name}"
BOARD_QUERY = """query($o:String!,$n:Int!){ repositoryOwner(login:$o){ ... on ProjectV2Owner{ projectV2(number:$n){
 id title public closed
 fields(first:60){ nodes{ ... on ProjectV2Field{name dataType} ... on ProjectV2IterationField{name dataType}
   ... on ProjectV2SingleSelectField{name dataType options{name}} } }
 views(first:20){ nodes{ name number layout filter fields(first:40){nodes{%(f)s}}
   groupByFields(first:5){nodes{%(f)s}} verticalGroupByFields(first:5){nodes{%(f)s}} } }
 items(first:100){ pageInfo{hasNextPage endCursor} nodes{ content{ ... on Issue{ repository{nameWithOwner} } } } } } } } }
""" % {"f": FIELD_NAME}
ITEMS_QUERY = """query($o:String!,$n:Int!,$c:String){ repositoryOwner(login:$o){ ... on ProjectV2Owner{ projectV2(number:$n){
 items(first:100,after:$c){ pageInfo{hasNextPage endCursor} nodes{ content{ ... on Issue{ repository{nameWithOwner} } } } } } } } }"""
ISSUES_QUERY = """query($o:String!,$r:String!,$c:String){ repository(owner:$o,name:$r){ issues(first:100,states:OPEN,after:$c){
 pageInfo{hasNextPage endCursor} nodes{ number labels(first:30){nodes{name}}
  parent{ number labels(first:30){nodes{name}} }
  projectItems(first:20){ nodes{ project{id} fieldValueByName(name:"Agent"){ ... on ProjectV2ItemFieldSingleSelectValue{name} } } } } } } }"""


def repos_of(items: dict) -> set[str]:
    return {n["content"]["repository"]["nameWithOwner"] for n in items["nodes"]
            if n.get("content") and n["content"].get("repository")}


def project_from_data(data: dict, repos: set[str]) -> dict:
    project = (data.get("repositoryOwner") or {}).get("projectV2")
    if not project:
        raise ReadError("project not found or not readable with this token")
    project["repos"] = sorted(repos)
    return project


def issues_from_nodes(repo: str, nodes: list[dict]) -> list[dict]:
    out = []
    for n in nodes:
        parent = n.get("parent")
        out.append({
            "repo": repo, "number": n["number"], "labels": names(n["labels"]),
            "parent": {"number": parent["number"], "labels": names(parent["labels"])} if parent else None,
            "items": [{"project": p["project"]["id"], "agent": (p.get("fieldValueByName") or {}).get("name")}
                      for p in n["projectItems"]["nodes"]],
        })
    return out


class LiveSource:
    name = "live"

    def __init__(self, api_url: str = API, env=None):
        self.token = token_from_env(env)
        self.api_url = api_url

    def gql(self, query: str, variables: dict) -> dict:
        req = urllib.request.Request(self.api_url, data=json.dumps({"query": query, "variables": variables}).encode(),
                                     headers={"Authorization": f"bearer {self.token}", "Content-Type": "application/json",
                                              "User-Agent": "lastwar-board-check", "GraphQL-Features": "sub_issues"})
        try:
            body = json.load(urllib.request.urlopen(req, timeout=60))
        except urllib.error.HTTPError as exc:
            raise ReadError(f"GitHub GraphQL HTTP {exc.code}")
        except (urllib.error.URLError, OSError, ValueError) as exc:
            raise ReadError(f"GitHub GraphQL unreachable: {type(exc).__name__}")   # never the exception text or headers
        if body.get("errors"):
            raise ReadError("GitHub GraphQL error: " + "; ".join(str(e.get("message", e))[:160] for e in body["errors"][:3]))
        return body["data"]

    def board(self, owner: str, number: int) -> dict:
        data = self.gql(BOARD_QUERY, {"o": owner, "n": number})
        project = (data.get("repositoryOwner") or {}).get("projectV2")
        if not project:
            raise ReadError(f"project {number} of {owner} not found or not readable with this token")
        items, repos = project["items"], set()
        for _ in range(10):
            repos |= repos_of(items)
            if not items["pageInfo"]["hasNextPage"]:
                break
            page = self.gql(ITEMS_QUERY, {"o": owner, "n": number, "c": items["pageInfo"]["endCursor"]})
            items = page["repositoryOwner"]["projectV2"]["items"]
        return project_from_data(data, repos)

    def issues(self, repo: str) -> list[dict]:
        owner, name = repo.split("/", 1)
        out, cursor = [], None
        while True:
            data = self.gql(ISSUES_QUERY, {"o": owner, "r": name, "c": cursor})
            conn = (data.get("repository") or {}).get("issues")
            if conn is None:
                raise ReadError(f"repository {repo} not found or not readable")
            out += issues_from_nodes(repo, conn["nodes"])
            if not conn["pageInfo"]["hasNextPage"]:
                return out
            cursor = conn["pageInfo"]["endCursor"]

    def epic_bodies(self, repo: str, numbers: list[int]) -> dict[int, str]:
        owner, name = repo.split("/", 1)
        bodies = {}
        for i in range(0, len(numbers), 20):
            chunk = numbers[i:i + 20]
            aliases = " ".join(f"i{n}:issue(number:{n}){{body}}" for n in chunk)
            data = self.gql('query($o:String!,$r:String!){ repository(owner:$o,name:$r){ %s } }' % aliases,
                            {"o": owner, "r": name})
            for n in chunk:
                bodies[n] = ((data["repository"] or {}).get(f"i{n}") or {}).get("body") or ""
        return bodies


class FixtureSource:
    """Recorded responses: <PREFIX>-board.json (the BOARD_QUERY data), <PREFIX>-issues.json (one ISSUES_QUERY page) and
    <PREFIX>-epic-bodies.json (number to body). No network and no token."""
    name = "fixture"

    def __init__(self, prefix: str):
        self.prefix = prefix

    def load(self, suffix: str, required: bool = True):
        path = Path(f"{self.prefix}-{suffix}.json")
        if not path.is_file():
            if required:
                raise ReadError(f"fixture file missing: {path.name}")
            return {}
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise ReadError(f"fixture {path.name} unreadable: {type(exc).__name__}")

    def board(self, owner: str, number: int) -> dict:
        data = self.load("board")
        project = (data.get("repositoryOwner") or {}).get("projectV2")
        return project_from_data(data, repos_of(project["items"]) if project else set())

    def issues(self, repo: str) -> list[dict]:
        data = self.load("issues")
        return issues_from_nodes(repo, data["repository"]["issues"]["nodes"])

    def epic_bodies(self, repo: str, numbers: list[int]) -> dict[int, str]:
        bodies = self.load("epic-bodies", required=False)
        return {n: bodies.get(str(n), "") for n in numbers}


def read_team(path: Path) -> dict:
    """Seat keys (assigned ones) and the repository from TEAM.yaml, by line patterns: no YAML library."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ReadError(f"cannot read {path}: {exc.strerror}")
    remote = re.search(r"^\s*remote:\s*(\S+)", text, re.M)
    repo = None
    if remote:
        m = re.search(r"github\.com[:/]([^/]+)/([^/\s]+?)(?:\.git)?$", remote.group(1))
        repo = f"{m.group(1)}/{m.group(2)}" if m else None
    seats, in_seats = [], False
    for line in text.splitlines():
        if re.match(r"^seats:\s*$", line):
            in_seats = True
        elif in_seats and re.match(r"^[A-Za-z]", line):
            break
        elif in_seats:
            m = re.match(r"^  - key:\s*(\S+)", line)
            if m:
                seats.append({"key": m.group(1), "assignment": None})
                continue
            m = re.match(r"^    assignment:\s*(\S+)", line)
            if m and seats:
                seats[-1]["assignment"] = m.group(1).strip("'\"")
    keys = [s["key"] for s in seats if s["assignment"] in (None, "assigned")]
    if not keys:
        raise ReadError(f"no assigned seats found in {path}")
    return {"seats": keys, "repo": repo}


# --- report ------------------------------------------------------------------------------------------------------
def run(args, source=None) -> dict:
    source = source or (FixtureSource(args.fixture) if args.fixture else LiveSource(args.api_url))
    board = source.board(args.owner, args.project)
    title = board["title"]
    team_file = Path(args.team_file)
    team = read_team(team_file) if team_file.is_file() else {"seats": [], "repo": None}
    if args.seats:
        seats, seat_source = [s.strip() for s in args.seats.split(",") if s.strip()], "--seats"
    elif team["seats"]:
        seats, seat_source = team["seats"], team_file.name
    else:
        raise ReadError(f"no seats: {team_file} is unreadable; pass --seats a,b,c")
    agents = expected_agent(args.team or title, seats)
    findings, notes = [], []
    if board.get("public"):
        findings.append(finding("board", "public", "visibility", "the board is public; the convention keeps it private"))
    f, n = check_fields(board["fields"]["nodes"], agents, args.strict)
    findings += f
    notes += n
    f, n = check_views(board["views"]["nodes"], args.epic_by, args.strict)
    findings += f
    notes += n
    structural = len(findings)
    coverage, repos, epics_missing = None, [], []
    if not args.structure_only:
        repos = list(args.repo) or sorted(set(board["repos"]) | ({team["repo"]} if team["repo"] and not args.project_given else set()))
        if not repos:
            raise ReadError("no repository to check the hierarchy of; pass --repo OWNER/NAME")
        issues = [i for repo in repos for i in source.issues(repo)]
        bodies = {}
        for repo in repos:
            nums = [i["number"] for i in issues if i["repo"] == repo and "epic" in {x.casefold() for x in i["labels"]}]
            if nums:
                bodies.update(source.epic_bodies(repo, nums))
        f, coverage = check_hierarchy(issues, board["id"], bodies)
        findings += f
        epics_missing = [int(x["subject"][1:]) for x in f if x["kind"].startswith("epic-criteria")]
    by_name = {x["name"]: x for x in board["fields"]["nodes"]}
    options = {name: {"expected": agents if name == "Agent" else dict((f[0], f[2]) for f in FIELDS)[name],
                      "found": [o["name"] for o in by_name.get(name, {}).get("options", [])]} for name in ("Agent", "Priority")}
    return {
        "tool": "board_check", "version": VERSION, "source": source.name, "owner": args.owner, "project": args.project,
        "title": title, "convention": CONVENTION, "strict": args.strict, "epic_by": args.epic_by,
        "ok": not findings, "structural_ok": not structural, "drift_findings": len(findings),
        "structural_findings": structural, "findings": findings, "notes": notes,
        "views": {"expected": VIEW_NAMES, "found": [v["name"] for v in board["views"]["nodes"]]},
        "options": options, "agent_source": seat_source, "repos": repos, "coverage": coverage,
        "epics_without_acceptance_criteria": epics_missing,
        "tab_order_note": "view order is the GraphQL listing order; tab position is checked by eye",
    }


def text_report(r: dict) -> str:
    lines = [f"board_check: project {r['project']} ({r['title']}) of {r['owner']} [{r['source']}] - "
             f"{'CLEAN' if r['ok'] else 'DRIFT, ' + str(r['drift_findings']) + ' finding(s)'}",
             f"structure (fields, options, views): {'ok' if r['structural_ok'] else str(r['structural_findings']) + ' finding(s)'}"]
    c = r["coverage"]
    if c:
        lines.append(f"open issues {c['open_issues']}: epic parent {c['with_parent_epic']['percent']}%, "
                     f"Agent {c['with_agent']['percent']}% of {c['non_epic_issues']} non-epic; {c['epics']} epics")
    lines += [f"  [{x['area']}/{x['kind']}] {x['message']}" for x in r["findings"]]
    lines += [f"  note: {n}" for n in r["notes"]] + [f"  note: {r['tab_order_note']}"]
    return "\n".join(lines)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="board_check.py", description=__doc__.split("\n\n")[0])
    p.add_argument("--owner", default=DEFAULT_OWNER)
    p.add_argument("--project", type=int, default=None, help=f"project number (default {DEFAULT_PROJECT}, this team's board)")
    p.add_argument("--repo", action="append", default=[], metavar="OWNER/NAME",
                   help="repository whose open issues are checked (default: the board's, plus TEAM.yaml's for the default project)")
    p.add_argument("--team", help="the team name in Agent options (default: the board title)")
    p.add_argument("--seats", help="comma list of seat keys instead of TEAM.yaml")
    p.add_argument("--team-file", default=str(Path(__file__).resolve().parent.parent.parent / "TEAM.yaml"))
    p.add_argument("--epic-by", choices=("label", "type"), default="label", help="Epics are label:epic here; type:Epic per the text")
    p.add_argument("--strict", action="store_true", help="reference-board variances count as drift")
    p.add_argument("--structure-only", action="store_true", help="fields, options and views only; no issue reads")
    p.add_argument("--fixture", metavar="PREFIX", help="read recorded <PREFIX>-board.json, -issues.json, -epic-bodies.json; no network")
    p.add_argument("--api-url", default=API, help=argparse.SUPPRESS)
    p.add_argument("--text", action="store_true", help="a short text report instead of JSON")
    args = p.parse_args(argv)
    args.project_given = args.project is not None
    args.project = args.project if args.project is not None else DEFAULT_PROJECT
    try:
        report = run(args)
    except ReadError as exc:
        print(f"board_check: cannot read: {exc}", file=sys.stderr)
        return 2
    except (KeyError, TypeError, IndexError, AttributeError) as exc:
        print(f"board_check: cannot read: unexpected response shape ({type(exc).__name__})", file=sys.stderr)
        return 2
    print(text_report(report) if args.text else json.dumps(report, indent=1))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
