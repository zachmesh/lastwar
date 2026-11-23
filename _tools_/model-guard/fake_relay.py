"""A stand-in for session-relay.py in the model_guard tests: sessions(), is_child(), inspect() and call() over a JSON state file of
seats (FAKE_GUARD_STATE). Each seat has a model, a running flag and optional switches: origin subagent, unreadable, refuse (the
host refuses selectModel), noop (selectModel does nothing). It records calls and never reads a cookie or token."""
import json
import os

STATE = os.environ["FAKE_GUARD_STATE"]


def _load():
    return json.load(open(STATE))


def _save(state):
    json.dump(state, open(STATE, "w"))


def sessions(allow_cache=False, timeout=None):
    return [{"sessionId": sid, "origin": s.get("origin"), "running": s.get("running", False)} for sid, s in _load()["seats"].items()]


def is_child(row):
    return row.get("origin") == "subagent"


def inspect(session_id, summary=None, timeout=60):
    state = _load()
    state["calls"].append({"inspect": session_id})
    _save(state)
    seat = state["seats"].get(session_id)
    if seat is None or seat.get("unreadable"):
        raise SystemExit("no session " + session_id + " Cookie: sid=abc123secret")
    return {"sessionId": session_id, "running": seat.get("running", False), "model": seat["model"]}


def call(method, args, timeout=60):
    state = _load()
    state["calls"].append({"call": method, "args": args})
    seat = state["seats"][args["request"]["sessionId"]]
    if seat.get("refuse"):
        _save(state)
        raise SystemExit("session/selectModel refused token=ghp_" + "a" * 20)
    if not seat.get("noop"):
        req = args["request"]
        seat["model"] = {"provider": req["provider"], "model": req["model"], "reasoningEffort": req["reasoningEffort"]}
    _save(state)
    return {}
