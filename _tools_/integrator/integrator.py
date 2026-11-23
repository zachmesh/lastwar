#!/usr/bin/env python3
"""integrator: the one sanctioned route for landing a branch on main (the Integrator seat's wrapper).

  status    open PRs, local main ahead/behind origin/main, the claimed folder
  check     BRANCH --seat KEY [--test DIR]...   the five-step scan, counts only
  push      BRANCH       push that named non-main branch, never forced
  open      BRANCH --title T [--body B]         open the pull request into main
  merge     PR --head-sha SHA                   merge commit only, refused when the head moved
  readback  PR | --branch B --merge-sha S       parents, tree equal to the branch tree, head an ancestor of main

It REFUSES main, force, squash, rebase and branch deletion (the flags are not options and any of them on the command
line stops the run), pushes only a named branch, merges only a head that a passing `check` recorded, and logs one JSON
line per action under _records_/<date>/integration/ - counts and SHAs only. Nothing here reads, prints or stores a
credential: GitHub is reached through `gh` (already logged in) and git, and every line printed or logged is scrubbed of
token-shaped text. Exit 0 ok, 1 failed or a check did not pass, 3 refused, 2 cannot run.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

VERSION = "1.0.0"
HERE = Path(__file__).resolve().parent
REFUSED_FLAGS = {"--force", "-f", "--force-with-lease", "--squash", "--rebase", "--delete-branch", "--delete", "-d", "-D",
                 "--admin", "--no-verify"}
MAIN_NAMES = {"main", "master", "head", "origin/main", "refs/heads/main", "refs/remotes/origin/main", "origin/master"}
BRANCH = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$")
BINARY_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".ico", ".pdf", ".zip", ".gz", ".tar", ".bin", ".mp4",
                   ".mov", ".heic", ".psd", ".so", ".dylib", ".exe"}
SECRET = re.compile(r"(gh[pousr]_[A-Za-z0-9]{16,}|github_pat_[A-Za-z0-9_]{16,}|x-access-token:[^@\s]+@)")
CONTROL_PATTERN = r"qzx\s+wvb"                       # made up: the positive control never uses a real pattern


class Refused(Exception):
    pass


class Failed(Exception):
    pass


def scrub(text: str) -> str:
    for name in ("GH_TOKEN", "GITHUB_TOKEN", "GH_ENTERPRISE_TOKEN"):
        value = os.environ.get(name)
        if value and len(value) >= 4:
            text = text.replace(value, "[token]")
    return SECRET.sub("[token]", text)


def say(text: str = "") -> None:
    print(scrub(text))


def run(cmd, cwd=None, check=False, input_text=None, env=None):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, input=input_text, env=env)
    if check and proc.returncode:
        raise Failed(scrub(f"{cmd[0]} {cmd[1] if len(cmd) > 1 else ''} failed: {(proc.stderr or proc.stdout).strip()[:300]}"))
    return proc


def git(root, *args, check=True):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    return run(["git", "-C", str(root), *args], check=check, env=env)


def gh(root, *args):
    exe = os.environ.get("INTEGRATOR_GH") or shutil.which("gh") or "gh"
    return run([exe, *args], cwd=str(root))


def repo_top(arg: str) -> Path:
    out = run(["git", "-C", arg, "rev-parse", "--show-toplevel"])
    if out.returncode:
        raise Failed(f"{arg} is not inside a git repository")
    return Path(out.stdout.strip())


def repo_args(root) -> list[str]:
    """--repo OWNER/NAME for gh when origin is a GitHub URL; none otherwise (a fake remote in the tests)."""
    url = git(root, "remote", "get-url", "origin", check=False).stdout.strip()
    m = re.search(r"github\.com[:/]+([^/\s]+)/([^/\s]+?)(?:\.git)?$", url)
    return ["--repo", f"{m.group(1)}/{m.group(2)}"] if m else []


# --- guards --------------------------------------------------------------------------------------------------------

def refuse_flags(argv: list[str]) -> None:
    for token in argv:
        bare = token.split("=", 1)[0]
        if bare in REFUSED_FLAGS or token.startswith("+"):
            raise Refused(f"refused: {bare} - this route never forces, squashes, rebases, deletes a branch or skips a check")


def named_branch(name: str) -> str:
    if name.lower() in MAIN_NAMES or name.lower().endswith("/main") or name.lower().endswith("/master"):
        raise Refused("refused: main is never pushed, opened or merged from here; name a work branch")
    if not BRANCH.match(name) or ".." in name or name.endswith("/") or name.endswith(".lock"):
        raise Refused(f"refused: {name!r} is not a plain branch name")
    return name


def resolve(root, name: str) -> str:
    sha = git(root, "rev-parse", "--verify", "--quiet", f"refs/heads/{name}^{{commit}}", check=False).stdout.strip()
    if not sha:
        raise Failed(f"no local branch {name}")
    return sha


# --- the log -------------------------------------------------------------------------------------------------------

def log_dir(root) -> Path:
    return Path(root) / "_records_" / datetime.now().strftime("%Y-%m-%d") / "integration"


def log_action(root, action: str, **fields) -> None:
    """One JSON line per action: counts, SHAs, names and result codes, scrubbed; never a token or a matched value."""
    folder = log_dir(root)
    folder.mkdir(parents=True, exist_ok=True)
    stub = folder / "INDEX.md"
    if not stub.exists():
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        stub.write_text(f"---\ntitle: Integration log\ncreated: {now}\nmodified: {now}\nversion: 1.0.0\n"
                        "description: One JSON line per integrator action, counts and SHAs only\n---\n\n# Integration log\n\n"
                        "`actions.jsonl` holds one line per action of `_tools_/integrator/integrator.py`: counts, SHAs and "
                        "result codes, never a token or a matched value.\n")
    record = {"at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), "action": action}
    record.update({k: v for k, v in fields.items() if v is not None})
    line = scrub(json.dumps(record, sort_keys=True))
    with open(folder / "actions.jsonl", "a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def check_recorded(root, sha: str) -> bool:
    """True when a passing check of exactly this head is in the integration log."""
    for path in sorted((Path(root) / "_records_").glob("*/integration/actions.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            if rec.get("action") == "check" and rec.get("result") == "pass" and rec.get("head") == sha:
                return True
    return False


# --- denylist and scope --------------------------------------------------------------------------------------------

def denylist_patterns(root) -> list[str]:
    common = git(root, "rev-parse", "--git-common-dir").stdout.strip()
    path = (Path(root) / common if not os.path.isabs(common) else Path(common)) / "privacy-denylist.txt"
    if not path.is_file():
        return []
    return [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines()
            if line.strip() and not line.strip().startswith("#")]


def team_scopes(text: str) -> dict[str, tuple[list[str], list[str]]]:
    """Seat key to (write scopes, excluded scopes) from TEAM.yaml by line patterns: no YAML library."""
    seats, key, section = {}, None, None
    for line in text.splitlines():
        m = re.match(r"^  - key: (\S+)\s*$", line)
        if m:
            key, section = m.group(1), None
            seats[key] = ([], [])
            continue
        if key is None:
            continue
        m = re.match(r"^    (\w+):\s*(.*)$", line)
        if m:
            section = {"write_scopes": 0, "excluded_write_scopes": 1}.get(m.group(1))
            if section is not None and m.group(2).strip() == "[]":
                section = None
            continue
        m = re.match(r"^      - (\S.*?)\s*$", line)
        if m and section is not None:
            seats[key][section].append(m.group(1))
    return seats


def in_scope(path: str, include: list[str], exclude: list[str]) -> bool:
    def hit(scope):
        return path == scope or (scope.endswith("/") and path.startswith(scope))
    return any(hit(s) for s in include) and not any(hit(s) for s in exclude)


# --- subcommands ---------------------------------------------------------------------------------------------------

def open_prs(root, with_files=False) -> list[dict]:
    fields = "number,headRefName,headRefOid,mergeable,isDraft" + (",files" if with_files else "")
    out = gh(root, "pr", "list", *repo_args(root), "--state", "open", "--limit", "100", "--json", fields)
    if out.returncode:
        raise Failed(scrub(f"gh pr list failed: {out.stderr.strip()[:200]}"))
    return json.loads(out.stdout or "[]")


def fetch_main(root) -> bool:
    return git(root, "fetch", "--quiet", "--no-tags", "origin", "main", check=False).returncode == 0


def cmd_status(a, root):
    fetched = fetch_main(root)
    ahead, behind = (git(root, "rev-list", "--left-right", "--count", "main...origin/main", check=False).stdout.split() + ["?", "?"])[:2]
    shallow = git(root, "rev-parse", "--is-shallow-repository", check=False).stdout.strip() == "true"
    claimed = sorted(p.name for p in (root / "_queue_" / "claimed").glob("*.md")) if (root / "_queue_" / "claimed").is_dir() else []
    local_only = git(root, "log", "--format=%h", "--max-count=30", "origin/main..main", check=False).stdout.split()
    direct = git(root, "log", "--first-parent", "--no-merges", "--since=24.hours", "--format=%h", "origin/main", check=False).stdout.split()
    prs = open_prs(root)
    result = {"open_prs": [{"number": p["number"], "branch": p["headRefName"], "head": p["headRefOid"][:10],
                           "mergeable": p.get("mergeable")} for p in prs],
              "main_ahead_of_origin": ahead, "main_behind_origin": behind, "origin_fetched": fetched,
              "shallow": shallow, "claimed_units": len(claimed), "local_only_commits": local_only,
              "direct_pushes_to_main_24h": direct}
    if a.json:
        say(json.dumps(result, indent=1, sort_keys=True))
    else:
        say(f"open PRs: {len(prs)}")
        for p in result["open_prs"]:
            say(f"  #{p['number']} {p['branch']} head {p['head']} mergeable {p['mergeable']}")
        say(f"local main against origin/main: ahead {ahead}, behind {behind}" + ("" if fetched else " (origin unreachable, not refreshed)"))
        if local_only:
            say(f"commits on local main not on origin/main (first {len(local_only)}): " + " ".join(local_only))
        say(f"direct pushes to main in the last 24 h (first-parent commits that are not merges): {len(direct)}"
            + (" - " + " ".join(direct[:10]) if direct else ""))
        if shallow:
            say("warning: this clone is shallow, so ahead and behind can be wrong (git fetch --unshallow)")
        say(f"claimed folder: {len(claimed)} unit file(s)" + (" - a live run holds the desktop" if claimed else ""))
    log_action(root, "status", open_prs=len(prs), ahead=ahead, behind=behind, claimed=len(claimed), local_only=len(local_only),
               direct_pushes=len(direct), result="ok")
    return 0


def grep_engine(wt: Path, patterns_file: str, sha: str) -> tuple[int, int, str]:
    """(files, lines, engine) the patterns match in the tree's file contents, by git grep -P -i -f; counts only."""
    out = git(wt, "grep", "-I", "-P", "-i", "-c", "-f", patterns_file, check=False)
    if out.returncode not in (0, 1):
        raise Failed("git grep -P failed (engine error, not a zero): " + scrub(out.stderr.strip()[:120]))
    files = lines = 0
    for row in out.stdout.splitlines():
        count = row.rsplit(":", 1)[-1]
        if count.isdigit() and int(count):
            files += 1
            lines += int(count)
    return files, lines, "git grep -P"


def lint_gate_path(a) -> str:
    return a.lint_gate or str(HERE.parent / "lint-gate" / "lint_gate.py")


def watch_engine(a, wt: Path) -> tuple[int, str]:
    """Files the wrap-aware census finds in the clean worktree (--worktree: it records no census); counts only."""
    out = run([sys.executable, "-B", lint_gate_path(a), "watch", "--privacy", "--worktree", "--format", "json", "--root", str(wt)])
    try:
        return int(json.loads(out.stdout)["files_matching_any"]), "watch --privacy"
    except (ValueError, KeyError):
        raise Failed("lint_gate watch --privacy gave no census (engine error, not a zero): " + scrub(out.stderr.strip()[:120]))


def positive_control(a) -> bool:
    """Prove both engines see a match, including one wrapped over a line break, on made-up text and a made-up pattern."""
    tmp = Path(tempfile.mkdtemp(prefix="integrator-control-"))
    try:
        subprocess.run(["git", "init", "-q", str(tmp)], check=True)
        (tmp / "control.md").write_text("one Qzx Wvb here\nand Qzx\n   Wvb wrapped\n")
        (tmp / ".git" / "privacy-denylist.txt").write_text(f"# control\n# marker: control\n{CONTROL_PATTERN}\n")
        git(tmp, "add", "-A")
        git(tmp, "-c", "user.email=c@example.org", "-c", "user.name=c", "commit", "-q", "-m", "control")
        patterns = tmp / ".git" / "patterns.txt"
        patterns.write_text(CONTROL_PATTERN + "\n")
        files, _, _ = grep_engine(tmp, str(patterns), "HEAD")
        census, _ = watch_engine(a, tmp)
        return files >= 1 and census >= 1
    except Failed:
        return False
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def cmd_check(a, root):
    branch = named_branch(a.branch)
    sha = resolve(root, branch)
    base = a.base
    if not git(root, "rev-parse", "--verify", "--quiet", f"{base}^{{commit}}", check=False).stdout.strip():
        # an unreadable base would make the diff and the log ranges empty, and an empty scan reads as a pass
        say(f"check {branch} head {sha[:10]} against {base}: FAIL\n  reasons: base-unreadable")
        log_action(root, "check", branch=branch, head=sha, base=base, seat=a.seat, result="fail", reasons=["base-unreadable"])
        return 1
    patterns = denylist_patterns(root)
    reasons, counts = [], {}
    if not patterns:
        reasons.append("no-denylist")
    seats = team_scopes(git(root, "show", f"{sha}:TEAM.yaml", check=False).stdout)
    if a.seat not in seats:
        reasons.append("unknown-seat")
    changed = [p for p in git(root, "diff", "--name-only", "--no-renames", f"{base}...{sha}", check=False).stdout.splitlines() if p]
    counts["changed_files"] = len(changed)
    include, exclude = seats.get(a.seat, ([], []))
    outside = [p for p in changed if not in_scope(p, include, exclude)]
    counts["outside_scope"] = len(outside)
    if outside:
        reasons.append("outside-scope")
    numstat = git(root, "diff", "--numstat", "--no-renames", f"{base}...{sha}", check=False).stdout.splitlines()
    binaries = sum(1 for row in numstat if row.startswith("-\t-\t")) + sum(
        1 for p in changed if Path(p).suffix.lower() in BINARY_SUFFIXES)
    counts["binaries_added"] = binaries
    if binaries:
        reasons.append("binary-added")
    control = positive_control(a)
    counts["positive_control"] = "ok" if control else "failed"
    if not control:
        reasons.append("positive-control-failed")
    wt = Path(tempfile.mkdtemp(prefix="integrator-wt-"))
    patterns_file = None
    try:
        git(root, "worktree", "add", "--detach", "--quiet", str(wt), sha)
        if patterns and control:
            fd, patterns_file = tempfile.mkstemp(prefix="integrator-patterns-")
            with os.fdopen(fd, "w") as handle:
                handle.write("\n".join(patterns) + "\n")
            os.chmod(patterns_file, 0o600)
            files, lines, engine = grep_engine(wt, patterns_file, sha)
            compiled = [re.compile(p, re.IGNORECASE) for p in patterns]
            names = [n for n in git(wt, "ls-tree", "-r", "--name-only", sha).stdout.splitlines()
                     if any(c.search(n) for c in compiled)]
            log_text = git(root, "log", f"{base}..{sha}", "--format=%an%x00%ae%x00%cn%x00%ce%x00%B%x01").stdout
            commits = [c for c in log_text.split("\x01") if c.strip()]
            msg_hits = sum(1 for c in commits if any(x.search(c.split("\x00", 4)[-1]) for x in compiled))
            who_hits = sum(1 for c in commits if any(x.search(" ".join(c.split("\x00")[:4])) for x in compiled))
            census_files, _ = watch_engine(a, wt)
            counts.update({"tree_files_matching": files, "tree_lines_matching": lines, "file_names_matching": len(names),
                           "commit_messages_matching": msg_hits, "author_names_matching": who_hits,
                           "wrap_aware_files_matching": census_files})
            if files or lines or names or msg_hits or who_hits or census_files:
                reasons.append("privacy-matches")
        lint = run([sys.executable, "-B", lint_gate_path(a), "check", "--base", base, "--landing", "--root", str(wt)])
        counts["lint_gate_exit"] = lint.returncode
        counts["lint_gate_blocked"] = lint.stdout.count("BLOCKED")
        if lint.returncode == 2:                          # OD-20261123-06: a landing waits until the gate can run
            reasons.append("lint-gate-could-not-run")
        elif lint.returncode:
            reasons.append("lint-gate")
        for folder in a.test or []:
            out = run([sys.executable, "-B", "-m", "unittest", "discover", "-s", str(wt / folder)])
            ran = re.search(r"Ran (\d+) test", out.stderr + out.stdout)
            counts[f"tests[{folder}]"] = f"{ran.group(1) if ran else 0} ran, {'ok' if out.returncode == 0 else 'FAILED'}"
            if out.returncode:
                reasons.append("tests")
        others = [p for p in open_prs(root, with_files=True) if p["headRefName"] != branch]
        overlap = sorted(p["number"] for p in others if set(changed) & {f["path"] for f in p.get("files", [])})
        counts["overlapping_prs"] = len(overlap)
    finally:
        git(root, "worktree", "remove", "--force", str(wt), check=False)
        shutil.rmtree(wt, ignore_errors=True)
        if patterns_file:
            os.unlink(patterns_file)
    result = "pass" if not reasons else "fail"
    say(f"check {branch} head {sha[:10]} against {base}: {result.upper()}")
    for k, v in counts.items():
        say(f"  {k}: {v}")
    if reasons:
        say("  reasons: " + ", ".join(sorted(set(reasons))))
    log_action(root, "check", branch=branch, head=sha, base=base, seat=a.seat, result=result,
               reasons=sorted(set(reasons)) or None, **{k.replace("[", "_").replace("]", ""): v for k, v in counts.items()})
    return 0 if result == "pass" else 1


def cmd_push(a, root):
    branch = named_branch(a.branch)
    sha = resolve(root, branch)
    if not check_recorded(root, sha):
        log_action(root, "push", branch=branch, head=sha, result="refused", reason="no-passing-check")
        raise Refused(f"refused: no passing check is recorded for {branch} at {sha[:10]}; run check first")
    out = git(root, "push", "--quiet", "origin", f"refs/heads/{branch}:refs/heads/{branch}", check=False)
    if out.returncode:
        log_action(root, "push", branch=branch, head=sha, result="failed")
        raise Failed(scrub(f"push of {branch} failed (never forced): {out.stderr.strip()[:200]}"))
    log_action(root, "push", branch=branch, head=sha, result="ok")
    say(f"pushed {branch} at {sha[:10]} (not forced)")
    return 0


def cmd_open(a, root):
    branch = named_branch(a.branch)
    sha = resolve(root, branch)
    remote = git(root, "ls-remote", "--heads", "origin", branch, check=False).stdout.split()
    if not remote or remote[0] != sha:
        raise Failed(f"origin does not hold {branch} at {sha[:10]}; push it first")
    out = gh(root, "pr", "create", *repo_args(root), "--base", "main", "--head", branch, "--title", a.title, "--body", a.body)
    if out.returncode:
        log_action(root, "open", branch=branch, head=sha, result="failed")
        raise Failed(scrub(f"gh pr create failed: {out.stderr.strip()[:200]}"))
    number = re.search(r"/pull/(\d+)|#(\d+)", out.stdout)
    pr = int((number.group(1) or number.group(2))) if number else None
    log_action(root, "open", branch=branch, head=sha, pr=pr, result="ok")
    say(f"opened PR #{pr} for {branch} at {sha[:10]}")
    return 0


def pr_view(root, number: int, fields: str) -> dict:
    out = gh(root, "pr", "view", str(number), *repo_args(root), "--json", fields)
    if out.returncode:
        raise Failed(scrub(f"gh pr view {number} failed: {out.stderr.strip()[:200]}"))
    return json.loads(out.stdout)


def cmd_merge(a, root):
    pr = pr_view(root, a.pr, "state,baseRefName,headRefName,headRefOid")
    head = pr["headRefOid"]
    named_branch(pr["headRefName"])
    def refuse(reason, text):
        log_action(root, "merge", pr=a.pr, head=head, result="refused", reason=reason)
        raise Refused(f"refused: {text}")
    if pr["state"] != "OPEN":
        refuse("not-open", f"PR #{a.pr} is {pr['state']}")
    if pr["baseRefName"] != "main":
        refuse("base-not-main", f"PR #{a.pr} does not target main")
    if head != a.head_sha:
        refuse("head-moved", f"the head of PR #{a.pr} is {head[:10]}, not the {a.head_sha[:10]} that was scanned")
    if not check_recorded(root, head):
        refuse("no-passing-check", f"no passing check is recorded for head {head[:10]}; nothing unscanned is merged")
    out = gh(root, "pr", "merge", str(a.pr), *repo_args(root), "--merge", "--match-head-commit", head)
    if out.returncode:
        log_action(root, "merge", pr=a.pr, head=head, result="failed")
        raise Failed(scrub(f"gh pr merge refused or failed: {out.stderr.strip()[:200]}"))
    merged = pr_view(root, a.pr, "state,mergeCommit")
    sha = (merged.get("mergeCommit") or {}).get("oid")
    log_action(root, "merge", pr=a.pr, head=head, merge_commit=sha, result="ok")
    say(f"merged PR #{a.pr}: head {head[:10]} into main as merge commit {(sha or '?')[:10]}")
    return 0


def cmd_readback(a, root):
    if a.pr:
        pr = pr_view(root, a.pr, "headRefName,headRefOid,mergeCommit,state")
        branch_head, merge = pr["headRefOid"], (pr.get("mergeCommit") or {}).get("oid")
    else:
        branch_head, merge = resolve(root, named_branch(a.branch)), a.merge_sha
    if not merge:
        raise Failed("no merge commit to read back")
    if not fetch_main(root):
        raise Failed("origin unreachable: cannot read main back")
    parents = git(root, "rev-list", "--parents", "-n", "1", merge).stdout.split()[1:]
    tree_equal = git(root, "rev-parse", f"{merge}^{{tree}}").stdout == git(root, "rev-parse", f"{branch_head}^{{tree}}", check=False).stdout
    ancestor = git(root, "merge-base", "--is-ancestor", branch_head, "origin/main", check=False).returncode == 0
    merge_on_main = git(root, "merge-base", "--is-ancestor", merge, "origin/main", check=False).returncode == 0
    facts = {"merge_commit": merge[:10], "parents": len(parents), "branch_head_is_a_parent": branch_head in parents,
             "tree_equals_branch_tree": tree_equal, "branch_head_ancestor_of_main": ancestor, "merge_on_main": merge_on_main}
    ok = len(parents) == 2 and facts["branch_head_is_a_parent"] and ancestor and merge_on_main and tree_equal
    for k, v in facts.items():
        say(f"  {k}: {v}")
    say(f"readback: {'OK' if ok else 'DIFFERS'}")
    log_action(root, "readback", pr=a.pr, head=branch_head, merge_commit=merge, parents=len(parents), tree_equal=tree_equal,
               ancestor=ancestor, result="ok" if ok else "differs")
    return 0 if ok else 1


def build_parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--root", default=".", help="the repository (default: the current one)")
    sub = p.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("status")
    s.add_argument("--json", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("branch")
    c.add_argument("--seat", required=True, help="the author's seat key in TEAM.yaml, for the write-scope check")
    c.add_argument("--base", default="origin/main")
    c.add_argument("--test", action="append", help="a test folder of a touched tool, run in the clean worktree (repeatable)")
    c.add_argument("--lint-gate", default="", help="lint_gate.py to use (default: the sibling lint-gate folder)")
    pu = sub.add_parser("push")
    pu.add_argument("branch")
    o = sub.add_parser("open")
    o.add_argument("branch")
    o.add_argument("--title", required=True)
    o.add_argument("--body", default="")
    m = sub.add_parser("merge")
    m.add_argument("pr", type=int)
    m.add_argument("--head-sha", required=True, help="the head the check scanned; a moved head is refused")
    r = sub.add_parser("readback")
    r.add_argument("pr", type=int, nargs="?")
    r.add_argument("--branch")
    r.add_argument("--merge-sha")
    return p


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    try:
        refuse_flags(argv)
        a = build_parser().parse_args(argv)
        root = repo_top(a.root)
        return {"status": cmd_status, "check": cmd_check, "push": cmd_push, "open": cmd_open, "merge": cmd_merge,
                "readback": cmd_readback}[a.cmd](a, root)
    except Refused as error:
        say(str(error))
        return 3
    except Failed as error:
        say(f"integrator: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
