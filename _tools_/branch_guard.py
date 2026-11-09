#!/usr/bin/env python3
"""Guard a records-branch tip against a false severed-history verdict.

A records-branch delivery ends in a reconcile merge against the
remote tip, then a push. Twice in this repository's history a
reconcile concluded the histories were unrelated when they were
not:

* Issue #485 (2026-11-08): the daily retro merged the
  records/2026-11-08 tip 76f358efda with --allow-unrelated-histories,
  reporting it a root commit with no parents and no merge-base
  against the previous tip 78e34bfa23. The live object store proves
  the opposite: 76f358efda has two parents (023fb42b6, bd5f98a0c),
  both present, and ``git merge-base 78e34bfa23 76f358efda`` is
  78e34bfa23 itself - the push was a clean fast-forward introducing
  exactly four commits. The retro's local view did not hold the
  tip's parents, so ``merge-base`` could find no common ancestor
  and the reconcile misread "objects missing here" as "histories
  unrelated". The --allow-unrelated-histories merge was unnecessary
  but harmless; the false issue it filed cost a full investigation.

The failure mode is a missing distinction: a merge-base lookup
cannot tell "these histories are genuinely unrelated" from "this
repo does not hold the tip's parents". This tool makes the
distinction explicit, so a reconcile never again concludes
"unrelated" from an unverified local view.

One command, standard library only:

  check - fetch a branch tip from a remote into a private ref
          (``refs/remotes/branch-guard/<branch>``; no local branch
          is moved), then verify that the expected previous tip is
          an ancestor of the fetched tip. The tip's parent objects
          must all be present locally before any ancestry verdict
          is given: a missing parent means the ancestry cannot be
          verified, and the tool says so instead of reporting the
          histories unrelated. Exit 0 when the push is a
          fast-forward (previous tip is an ancestor of the new
          tip), 1 when it genuinely is not (all objects present,
          so the verdict is real - stop, never force), 2 when the
          ancestry cannot be verified (fetch failed, the previous
          tip is unknown here, or a tip parent object is missing).
          ``--no-fetch`` skips the fetch and checks the tip already
          held under the private ref (offline re-checks and tests).

Run every records-branch reconcile through this check before the
merge and before the push: a non-zero exit stops the delivery, and
a --allow-unrelated-histories merge is only ever considered after
this tool reports the tip a genuine root commit (zero parents) with
exit 1.

Usage:
  branch_guard.py check --repo PATH --branch BRANCH --previous SHA
                        [--remote REMOTE] [--no-fetch]
                        [--format text|json]
"""

import argparse
import json
import subprocess
import sys

TOOL_VERSION = "1.0.0"

PRIVATE_REF_PREFIX = "refs/remotes/branch-guard/"


def _run_git(args, cwd):
    """Run git and return the completed process (never raises)."""
    try:
        return subprocess.run(
            ["git"] + args, cwd=cwd, capture_output=True, text=True,
            timeout=120)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None


def _render(result, fmt):
    if fmt == "json":
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        for line in result["text"]:
            print(line)


def _resolve_commit(repo, rev):
    """Return the full SHA for rev, or None when it is not a commit."""
    proc = _run_git(["rev-parse", "--verify", rev + "^{commit}"], cwd=repo)
    if proc is None or proc.returncode != 0:
        return None
    return proc.stdout.strip()


def _object_present(repo, sha):
    proc = _run_git(["cat-file", "-e", sha], cwd=repo)
    return proc is not None and proc.returncode == 0


def _tip_parents(repo, tip):
    """Return the tip's parent SHAs, or None when the tip is unreadable."""
    proc = _run_git(["cat-file", "-p", tip], cwd=repo)
    if proc is None or proc.returncode != 0:
        return None
    parents = []
    for line in proc.stdout.splitlines():
        if line.startswith("parent "):
            parents.append(line.split(None, 1)[1].strip())
    return parents


def cmd_check(args):
    repo = args.repo
    branch = args.branch
    private_ref = PRIVATE_REF_PREFIX + branch

    proc = _run_git(["check-ref-format", private_ref], cwd=repo)
    if proc is None or proc.returncode != 0:
        print(f"error: branch {branch!r} does not form a valid ref",
              file=sys.stderr)
        return 2

    tip = None
    fetch_error = None
    if not args.no_fetch:
        proc = _run_git(
            ["fetch", "--no-tags", args.remote,
             f"{branch}:{private_ref}"],
            cwd=repo)
        if proc is None or proc.returncode != 0:
            detail = (proc.stderr.strip().splitlines() or [""])[-1] \
                if proc is not None else "git fetch could not run"
            fetch_error = (f"fetch of {branch} from {args.remote} "
                           f"failed: {detail}")
    if fetch_error is None:
        tip = _resolve_commit(repo, private_ref)
        if tip is None and args.no_fetch:
            # Offline re-check: fall back to a local branch of the
            # same name when the private ref was never fetched.
            tip = _resolve_commit(repo, branch)

    result = {
        "version": TOOL_VERSION,
        "branch": branch,
        "remote": args.remote,
        "previous": args.previous,
        "tip": tip,
        "fast_forward": False,
        "tip_is_root": None,
        "parents_present": None,
        "status": "unverifiable",
        "text": [],
    }

    if fetch_error is not None:
        result["text"] = [
            f"{branch}: CANNOT VERIFY - {fetch_error}",
            "Do not conclude the histories are unrelated; "
            "fix the fetch and re-run.",
        ]
        _render(result, args.format)
        return 2
    if tip is None:
        result["text"] = [
            f"{branch}: CANNOT VERIFY - no tip held locally under "
            f"{private_ref}" + (" (fetch was skipped)" if args.no_fetch
                                else ""),
            "Run without --no-fetch so the tip is fetched first.",
        ]
        _render(result, args.format)
        return 2

    previous = _resolve_commit(repo, args.previous)
    if previous is None:
        result["text"] = [
            f"{branch}: CANNOT VERIFY - previous tip "
            f"{args.previous} is not a commit in this repo",
            "Fetch the branch history first; do not conclude the "
            "histories are unrelated.",
        ]
        _render(result, args.format)
        return 2

    parents = _tip_parents(repo, tip)
    if parents is None:
        result["text"] = [
            f"{branch}: CANNOT VERIFY - tip {tip} cannot be read "
            "in this repo",
            "Do not conclude the histories are unrelated; "
            "re-fetch and re-run.",
        ]
        _render(result, args.format)
        return 2
    result["tip_is_root"] = len(parents) == 0

    missing = [p for p in parents if not _object_present(repo, p)]
    if missing:
        result["parents_present"] = False
        result["text"] = [
            f"{branch}: CANNOT VERIFY - tip {tip} has "
            f"{len(missing)} parent object(s) missing locally "
            f"({missing[0][:12]}...)",
            "The tip's ancestry cannot be checked from this repo: "
            "a missing parent is not evidence the histories are "
            "unrelated (issue #485). Re-fetch and re-run; never "
            "merge with --allow-unrelated-histories on this verdict.",
        ]
        _render(result, args.format)
        return 2
    result["parents_present"] = True

    proc = _run_git(["merge-base", "--is-ancestor", previous, tip],
                    cwd=repo)
    if proc is None:
        result["text"] = [
            f"{branch}: CANNOT VERIFY - git merge-base could not run",
            "Do not conclude the histories are unrelated.",
        ]
        _render(result, args.format)
        return 2
    if proc.returncode == 0:
        result["fast_forward"] = True
        result["status"] = "fast-forward"
        result["text"] = [
            f"{branch}: fast-forward - previous tip "
            f"{previous[:12]} is an ancestor of {tip[:12]}",
            "Safe to reconcile and push.",
        ]
        _render(result, args.format)
        return 0
    if proc.returncode == 1:
        result["status"] = "not-fast-forward"
        if result["tip_is_root"]:
            verdict = (f"tip {tip[:12]} is a genuine root commit "
                       "(zero parents, all objects verified)")
        else:
            verdict = (f"tip {tip[:12]} does not contain previous "
                       f"tip {previous[:12]} (all objects verified)")
        result["text"] = [
            f"{branch}: NOT A FAST-FORWARD - {verdict}",
            "Stop: do not push, never force. Reconcile by hand.",
        ]
        _render(result, args.format)
        return 1
    result["text"] = [
        f"{branch}: CANNOT VERIFY - git merge-base failed "
        f"(exit {proc.returncode}): "
        f"{(proc.stderr.strip().splitlines() or [''])[-1]}",
        "Do not conclude the histories are unrelated.",
    ]
    _render(result, args.format)
    return 2


def build_parser():
    parser = argparse.ArgumentParser(
        prog="branch_guard.py",
        description="Verify a records-branch tip is a fast-forward "
                    "over the previous tip before a reconcile merge "
                    "or push (issue #485).")
    parser.add_argument("--version", action="version",
                        version=f"%(prog)s {TOOL_VERSION}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser(
        "check",
        help="fetch a branch tip and verify the previous tip is "
             "its ancestor (exit 0 fast-forward, 1 not, "
             "2 cannot verify)")
    p_check.add_argument("--repo", required=True,
                         help="repository path (worktree or clone)")
    p_check.add_argument("--branch", required=True,
                         help="branch to check, e.g. records/2026-11-08")
    p_check.add_argument("--previous", required=True,
                         help="expected previous tip SHA (full or short)")
    p_check.add_argument("--remote", default="github",
                         help="remote to fetch the tip from "
                              "(default: github)")
    p_check.add_argument("--no-fetch", action="store_true",
                         help="check the tip already held locally "
                              "instead of fetching it")
    p_check.add_argument("--format", choices=["text", "json"],
                         default="text")
    p_check.set_defaults(func=cmd_check)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
