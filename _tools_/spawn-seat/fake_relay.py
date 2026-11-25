"""A stand-in for session-relay.py in the spawn_seat tests: the same four names the tool uses (cmd_spawn, inspect, call), a
JSON state file, and a mode that decides how the seat comes up. It records the arguments it receives and never reads a cookie
or token (the tests put fake ones in the environment and require that they never come back out)."""
import json
import os
import sys

STATE, MODE = os.environ["FAKE_RELAY_STATE"], os.environ.get("FAKE_RELAY_MODE", "ok")
SID = "session-00000000-aaaa-bbbb-cccc-111111111111"


def _load():
    return json.load(open(STATE)) if os.path.exists(STATE) else {"calls": [], "model": None, "running": False}


def _save(state):
    json.dump(state, open(STATE, "w"))


def cmd_spawn(a):
    state = _load()
    state["calls"].append({"spawn": {"provider": a.provider, "model": a.model, "effort": a.effort, "title": a.title,
                                     "workspace": a.workspace, "prompt_file": a.prompt_file, "goal_file": a.goal_file,
                                     "no_full_access": a.no_full_access}})
    if MODE == "spawn-fails":
        _save(state)
        raise SystemExit("workspace/create failed: Cookie: sid=abc123secret token=ghp_" + "a" * 20)
    if MODE in ("ok", "step-fails"):
        state["model"] = {"provider": a.provider, "model": a.model, "reasoningEffort": a.effort}
    else:                                             # the seat came up on the host default
        # what a bare `session-relay spawn` brings up (the host default, not the policy: the guard must correct both the model and the effort)
        state["model"] = {"provider": "meta-claude", "model": "claude-opus-5-5", "reasoningEffort": "xhigh"}
    state["running"] = MODE == "drift-running"
    _save(state)
    print(f"workspace ws-1 (created=False) session {SID}")
    print("  ok   session/selectModel ")
    if MODE == "step-fails":
        print("  FAIL session/rename: boom Cookie: sid=abc123secret")
    print(SID)


def inspect(session_id):
    state = _load()
    state["calls"].append({"inspect": session_id})
    _save(state)
    if MODE == "inspect-fails":
        raise SystemExit("no session " + session_id)
    if MODE == "no-model":
        return {"sessionId": session_id, "running": False, "model": {}}
    return {"sessionId": session_id, "running": state["running"], "model": state["model"]}


def call(method, args):
    state = _load()
    state["calls"].append({"call": method, "args": args})
    if method == "session/selectModel":
        if MODE == "selectmodel-refused":
            _save(state)
            raise SystemExit("session/selectModel refused: a child session")
        if MODE != "drift-unfixable":
            req = args["request"]
            state["model"] = {"provider": req["provider"], "model": req["model"], "reasoningEffort": req["reasoningEffort"]}
    _save(state)
    return {}
