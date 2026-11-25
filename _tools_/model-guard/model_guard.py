#!/usr/bin/env python3
"""model_guard: every roster seat runs the approved model at the approved effort (owner orders 2026-11-23 and 2026-11-25: Claude Sonnet 5.5, xhigh on 11-23, high since 11-25 - the effort is read
from TEAM.yaml `approved_effort`, never a constant here).

From Steer A's 45-line v1, with the roster read by yaml.safe_load - the `seats` list and the `steward` block - and the policy read
from TEAM.yaml `coordination.execution.approved_model`, `approved_effort`, `approved_provider`. Each seat's model is read with
the relay's inspect and compared with the policy.

  model_guard.py [--apply] [--verbose] [--team TEAM.yaml]

Without --apply it only reports. With --apply an IDLE seat that drifted is corrected through session/selectModel and read back;
a RUNNING seat is left and retried on the next tick (the 15-minute loop). A child or subagent session is never touched (the host
refuses): it is listed as informational. It prints NOTHING when no seat drifted (so the tick stays quiet; --verbose prints the
table anyway). Exit 0 when no seat drifted or every drift was fixed; exit 1 on any unfixed drift - a dry run, a running seat,
a refused or failed correction, a session that cannot be read; exit 2 when the policy or the roster cannot be read. Output holds
seat keys, the first 16 characters of a session id, model names and states: no token, cookie, URL or relay output. The relay is
`~/dtadpole/reflection/_tools_/session-relay/session-relay.py` unless SESSION_RELAY_MODULE names another file (the tests do).
"""
from __future__ import annotations

import argparse
import importlib.util
import os
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DEFAULT_RELAY = "~/dtadpole/reflection/_tools_/session-relay/session-relay.py"
SECRET = re.compile(r"(gh[pousr]_[A-Za-z0-9]{16,}|github_pat_[A-Za-z0-9_]{16,}|(?i:cookie|token|authorization)[=: ]+\S+)")


class Usage(Exception):
    pass


def scrub(text) -> str:
    return SECRET.sub("[redacted]", str(text))


def load_team(path: Path):
    """(policy, seats): the approved model, effort and provider, and [(key, session_id)] for each seat and the steward."""
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise Usage(f"cannot read {path}: {type(exc).__name__}")
    execution = (data.get("coordination") or {}).get("execution") or {}
    policy = {k: execution.get(f"approved_{k}") for k in ("model", "effort", "provider")}
    missing = [f"approved_{k}" for k, v in policy.items() if not (isinstance(v, str) and v.strip())]
    if missing:
        raise Usage(f"{path} lacks coordination.execution.{', '.join(missing)}: the policy cannot be read")
    seats, seen = [], set()
    for seat in data.get("seats") or []:
        sid = seat.get("session_id") if isinstance(seat, dict) else None
        if not isinstance(sid, str) or not sid.startswith("session-") or seat.get("assignment") == "concluded" or sid in seen:
            continue
        seen.add(sid)
        seats.append((str(seat.get("key")), sid))
    steward = data.get("steward") or {}
    sid = steward.get("session_id") if isinstance(steward, dict) else None
    if isinstance(sid, str) and sid.startswith("session-") and sid not in seen:
        seats.append(("steward", sid))
    return {k: v.strip() for k, v in policy.items()}, seats


def load_relay():
    path = Path(os.environ.get("SESSION_RELAY_MODULE") or DEFAULT_RELAY).expanduser()
    if not path.is_file():
        raise Usage(f"no relay module at {path}")
    os.environ.setdefault("DSH_WEB_URL", "http://localhost:8080")
    os.environ.setdefault("SESSION_RELAY_JAR", "/tmp/dsh-gate.cj")
    spec = importlib.util.spec_from_file_location("session_relay_for_guard", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["session_relay_for_guard"] = module
    spec.loader.exec_module(module)
    return module


def drift_of(model: dict, policy: dict) -> list[str]:
    out = []
    if model.get("model") != policy["model"]:
        out.append("model")
    if model.get("reasoningEffort") != policy["effort"]:
        out.append("effort")
    if model.get("provider") not in (None, policy["provider"]):
        out.append("provider")
    return out


def children_of(relay, sids) -> set[str]:
    """The seat sessions the host lists as subagents; an unreadable list names none (inspect then decides)."""
    try:
        return {row["sessionId"] for row in relay.sessions(allow_cache=True) if row.get("sessionId") in sids and relay.is_child(row)}
    except BaseException:
        return set()


def check(relay, policy, seats, apply: bool):
    """(rows, unfixed): rows are (key, sid, model, effort, state) for every seat that drifted or could not be read, plus
    informational child rows; unfixed counts the drifts still standing."""
    rows, unfixed, info = [], 0, []
    kids = children_of(relay, {sid for _k, sid in seats})
    for key, sid in seats:
        if sid in kids:
            info.append((key, sid, "-", "-", "child session: informational, never touched (the host refuses)"))
            continue
        try:
            view = relay.inspect(sid)
        except BaseException as exc:
            rows.append((key, sid, "-", "-", f"UNREADABLE: {scrub(exc)[:50]}"))
            unfixed += 1
            continue
        model = view.get("model") or {}
        wrong = drift_of(model, policy)
        if not wrong:
            continue
        state = "DRIFT (dry run: pass --apply)"
        if apply and view.get("running"):
            state = "DRIFT (running: retry next tick)"
        elif apply:
            try:
                relay.call("session/selectModel", {"request": {"sessionId": sid, "provider": policy["provider"],
                                                               "model": policy["model"], "reasoningEffort": policy["effort"]}})
                after = (relay.inspect(sid) or {}).get("model") or {}
                state = "FIXED" if not drift_of(after, policy) else "FIX FAILED: still " + "/".join(drift_of(after, policy))
            except BaseException as exc:
                state = f"FIX REFUSED: {scrub(exc)[:50]}"
        if state != "FIXED":
            unfixed += 1
        rows.append((key, sid, model.get("model"), model.get("reasoningEffort"), state))
    return rows, info, unfixed


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--apply", action="store_true", help="correct idle seats through session/selectModel")
    p.add_argument("--verbose", action="store_true", help="print the table even when no seat drifted")
    p.add_argument("--team", default=str(HERE.parent.parent / "TEAM.yaml"), help="the roster holding the policy keys")
    a = p.parse_args(argv)
    try:
        policy, seats = load_team(Path(a.team))
        relay = load_relay()
    except Usage as exc:
        print(f"model_guard: {scrub(exc)}", file=sys.stderr)
        return 2
    rows, info, unfixed = check(relay, policy, seats, a.apply)
    if rows or a.verbose:
        print(f"{'seat':<12}{'session':<18}{'model':<22}{'effort':<8}state")
        for key, sid, model, effort, state in rows + info:
            print(f"{key:<12}{sid[:16]:<18}{str(model):<22}{str(effort):<8}{state}")
        fixed = sum(1 for r in rows if r[4] == "FIXED")
        print(f"seats {len(seats)} | drift {len(rows)} | fixed {fixed} | unfixed {unfixed} | policy {policy['model']} {policy['effort']}")
    return 1 if unfixed else 0


if __name__ == "__main__":
    sys.exit(main())
