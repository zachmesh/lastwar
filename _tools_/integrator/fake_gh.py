#!/usr/bin/env python3
"""A stand-in for `gh` in the integrator tests: pull requests live in a JSON state file and merges happen in a local bare
repository. It records every argument vector (never the environment) so a test can prove which flags were used."""
import json
import os
import subprocess
import sys
import tempfile

STATE, REMOTE = os.environ["FAKE_GH_STATE"], os.environ["FAKE_GH_REMOTE"]
state = json.load(open(STATE)) if os.path.exists(STATE) else {"prs": [], "calls": []}
args = sys.argv[1:]
state["calls"].append(args)


def save():
    json.dump(state, open(STATE, "w"))


def git_remote(*a):
    return subprocess.run(["git", "--git-dir", REMOTE, *a], capture_output=True, text=True).stdout.strip()


def head_of(pr):
    return git_remote("rev-parse", f"refs/heads/{pr['headRefName']}")


def flag(name):
    return args[args.index(name) + 1] if name in args else None


def view(pr, keys):
    full = {"number": pr["number"], "state": pr["state"], "baseRefName": pr["base"], "headRefName": pr["headRefName"],
            "headRefOid": head_of(pr), "mergeCommit": ({"oid": pr["merge"]} if pr.get("merge") else None),
            "mergeable": "MERGEABLE", "isDraft": False,
            "files": [{"path": p} for p in git_remote("diff", "--name-only", f"main...refs/heads/{pr['headRefName']}").split()]}
    return {k: full[k] for k in keys.split(",")}


if os.environ.get("FAKE_GH_LEAK") and args[:2] == ["pr", "create"]:
    save()
    print("error: bad credentials " + os.environ.get("GH_TOKEN", ""), file=sys.stderr)
    sys.exit(1)
if args[:2] == ["pr", "list"]:
    print(json.dumps([view(p, flag("--json")) for p in state["prs"] if p["state"] == "OPEN"]))
elif args[:2] == ["pr", "create"]:
    number = len(state["prs"]) + 1
    state["prs"].append({"number": number, "headRefName": flag("--head"), "base": flag("--base"), "title": flag("--title"),
                         "state": "OPEN"})
    print(f"https://github.com/example/repo/pull/{number}")
elif args[:2] == ["pr", "view"]:
    pr = next(p for p in state["prs"] if p["number"] == int(args[2]))
    print(json.dumps(view(pr, flag("--json"))))
elif args[:2] == ["pr", "merge"]:
    pr = next(p for p in state["prs"] if p["number"] == int(args[2]))
    if any(f in args for f in ("--squash", "--rebase", "--delete-branch", "--admin")) or "--merge" not in args:
        save()
        print("forbidden merge flags", file=sys.stderr)
        sys.exit(1)
    if flag("--match-head-commit") != head_of(pr):
        save()
        print("Head branch was modified. Review and try the merge again.", file=sys.stderr)
        sys.exit(1)
    work = tempfile.mkdtemp(prefix="fake-gh-")
    run = lambda *a: subprocess.run(["git", "-C", work, "-c", "user.email=m@example.org", "-c", "user.name=m", *a],
                                    capture_output=True, text=True, check=True)
    subprocess.run(["git", "clone", "-q", REMOTE, work], check=True, capture_output=True)
    run("checkout", "-q", "main")
    run("merge", "--no-ff", "-q", "-m", f"Merge pull request #{pr['number']}", f"origin/{pr['headRefName']}")
    run("push", "-q", "origin", "main")
    pr["merge"], pr["state"] = run("rev-parse", "HEAD").stdout.strip(), "MERGED"
else:
    print("unsupported", args, file=sys.stderr)
    sys.exit(2)
save()
