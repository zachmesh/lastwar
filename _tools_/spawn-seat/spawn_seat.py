#!/usr/bin/env python3
"""spawn_seat: the only way to spawn a roster seat (owner orders 2026-11-23 and 2026-11-25: the approved model and effort in TEAM.yaml, persisted;
Claude Sonnet 5.5, xhigh on 11-23, high since the owner's request of 11-25 - the effort is read from the file, never a constant here).

`session-relay spawn` defaults to claude-opus-5-5, so a bare spawn brings a seat up on the wrong model (the operator did, at
09:07Z). This wraps it with the model, effort and provider FIXED from TEAM.yaml (`coordination.execution.approved_model`,
`approved_effort`, `approved_provider`): there is no --model, --effort or --provider option, and passing one is a usage error.

  spawn_seat.py --title TITLE [--prompt-file F] [--goal-file F] [--workspace DIR] [--team TEAM.yaml] [--dry-run]

It spawns the seat through the relay's own spawn, READS THE MODEL BACK with inspect, runs `session/selectModel` once when the
read-back differs and the seat is idle, reads back again, and FAILS LOUDLY (exit 1, a message on stderr) if it still differs, a
spawn step failed, or the model cannot be read. On success it prints the new session id and the read-back model, nothing else:
no token, cookie, URL or relay output. Exit 0 spawned and verified, 1 spawned but not verified (the id is still printed) or the
spawn failed, 2 the policy keys or an argument are unusable. The relay is `~/dtadpole/reflection/_tools_/session-relay/
session-relay.py` unless SESSION_RELAY_MODULE names another file (the tests do).
"""
from __future__ import annotations

import argparse
import contextlib
import importlib.util
import io
import os
import re
import sys
import time
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
DEFAULT_RELAY = "~/dtadpole/reflection/_tools_/session-relay/session-relay.py"
SESSION_ID = re.compile(r"^session-[0-9a-f][0-9a-f-]{6,}$")
SECRET = re.compile(r"(gh[pousr]_[A-Za-z0-9]{16,}|github_pat_[A-Za-z0-9_]{16,}|(?i:cookie|token|authorization)[=: ]+\S+)")


class Usage(Exception):
    pass


def scrub(text: str) -> str:
    return SECRET.sub("[redacted]", str(text))


def load_policy(team: Path) -> dict:
    """The approved model, effort and provider from TEAM.yaml, read with yaml.safe_load; a missing key is a usage error."""
    try:
        data = yaml.safe_load(team.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        raise Usage(f"cannot read {team}: {type(exc).__name__}")
    execution = ((data or {}).get("coordination") or {}).get("execution") or {}
    policy = {k: execution.get(f"approved_{k}") for k in ("model", "effort", "provider")}
    missing = [f"approved_{k}" for k, v in policy.items() if not (isinstance(v, str) and v.strip())]
    if missing:
        raise Usage(f"{team} lacks coordination.execution.{', '.join(missing)}: the policy cannot be read")
    return {k: v.strip() for k, v in policy.items()}


def load_relay():
    path = Path(os.environ.get("SESSION_RELAY_MODULE") or DEFAULT_RELAY).expanduser()
    if not path.is_file():
        raise Usage(f"no relay module at {path}")
    os.environ.setdefault("DSH_WEB_URL", "http://localhost:8080")
    os.environ.setdefault("SESSION_RELAY_JAR", "/tmp/dsh-gate.cj")
    spec = importlib.util.spec_from_file_location("session_relay_for_spawn", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["session_relay_for_spawn"] = module
    spec.loader.exec_module(module)
    return module


def read_back(relay, sid: str, attempts: int, pause: float):
    """(view, error): the seat's view with its model, retried a few times because the host's projection can lag a spawn."""
    last = "no attempt"
    for n in range(max(1, attempts)):
        try:
            view = relay.inspect(sid)
            if (view.get("model") or {}).get("model"):
                return view, None
            last = "the host reports no model for the seat"
        except BaseException as exc:                      # the relay exits with SystemExit on a host error
            last = f"inspect failed: {scrub(exc)[:120]}"
        if n + 1 < attempts:
            time.sleep(pause)
    return None, last


def differs(model: dict, policy: dict) -> list[str]:
    out = []
    if model.get("model") != policy["model"]:
        out.append(f"model {model.get('model')} (policy {policy['model']})")
    if model.get("reasoningEffort") != policy["effort"]:
        out.append(f"effort {model.get('reasoningEffort')} (policy {policy['effort']})")
    if model.get("provider") not in (None, policy["provider"]):
        out.append(f"provider {model.get('provider')} (policy {policy['provider']})")
    return out


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--title", required=True)
    p.add_argument("--prompt-file")
    p.add_argument("--goal-file")
    p.add_argument("--workspace", help="folder to open the seat in (default: the repository holding TEAM.yaml)")
    p.add_argument("--team", default=str(HERE.parent.parent / "TEAM.yaml"), help="the roster holding the policy keys")
    p.add_argument("--dry-run", action="store_true", help="print the fixed policy and stop; spawn nothing")
    p.add_argument("--settle-attempts", type=int, default=4, help="read-back attempts after the spawn")
    p.add_argument("--settle-seconds", type=float, default=2.0, help="pause between read-back attempts")
    a = p.parse_args(argv)
    try:
        team = Path(a.team)
        policy = load_policy(team)
        for name in ("prompt_file", "goal_file"):
            path = getattr(a, name)
            if path and not Path(path).expanduser().is_file():
                raise Usage(f"--{name.replace('_', '-')} {path} is not a file")
        workspace = Path(a.workspace or team.resolve().parent).expanduser()
        if a.dry_run:
            print(f"would spawn {a.title!r} in {workspace} on {policy['model']} {policy['effort']} {policy['provider']}")
            return 0
        relay = load_relay()
    except Usage as exc:
        print(f"spawn_seat: {scrub(exc)}", file=sys.stderr)
        return 2
    ns = argparse.Namespace(workspace=str(workspace), title=a.title, prompt_file=a.prompt_file, goal_file=a.goal_file,
                            provider=policy["provider"], model=policy["model"], effort=policy["effort"], no_full_access=False)
    out = io.StringIO()
    try:
        with contextlib.redirect_stdout(out):
            relay.cmd_spawn(ns)
    except BaseException as exc:
        print(f"spawn_seat: FAILED: the spawn did not complete: {scrub(exc)[:160]}", file=sys.stderr)
        return 1
    lines = [ln.strip() for ln in out.getvalue().splitlines() if ln.strip()]
    sid = lines[-1] if lines else ""
    failed_steps = [re.sub(r"^FAIL\s+", "", ln).split(":")[0] for ln in lines if ln.startswith("FAIL")]
    if not SESSION_ID.match(sid):
        print("spawn_seat: FAILED: the spawn returned no session id", file=sys.stderr)
        return 1
    print(f"session {sid}")
    problems = [f"spawn step failed: {name}" for name in failed_steps]
    view, error = read_back(relay, sid, a.settle_attempts, a.settle_seconds)
    if view is None:
        problems.append(f"the model could not be read back ({error})")
    else:
        wrong = differs(view["model"], policy)
        if wrong and not view.get("running"):
            try:
                relay.call("session/selectModel", {"request": {"sessionId": sid, "provider": policy["provider"],
                                                               "model": policy["model"], "reasoningEffort": policy["effort"]}})
            except BaseException as exc:
                problems.append(f"selectModel refused: {scrub(exc)[:100]}")
            view, error = read_back(relay, sid, a.settle_attempts, a.settle_seconds)
            wrong = differs(view["model"], policy) if view else [f"unreadable after selectModel ({error})"]
        elif wrong:
            problems.append("the seat is running, so its model cannot be changed now; model_guard --apply corrects it when idle")
        if wrong:
            problems.append("model differs: " + "; ".join(wrong))
        if view:
            model = view["model"]
            print(f"model {model.get('model')} {model.get('reasoningEffort')} {model.get('provider') or policy['provider']} (read back)")
    if problems:
        for problem in problems:
            print(f"spawn_seat: FAILED: {problem}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
