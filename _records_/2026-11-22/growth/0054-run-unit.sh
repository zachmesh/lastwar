#!/bin/bash
# usage: run-unit.sh UNIT|- TASKFILE MAXSTEPS MAXCOST   (new bridge tree, 2026-11-24; UNIT '-' = no claim; replaces the old run-lock.mjs version)
cd /Users/zhenchen/zachmesh/lastwar || exit 9
UNIT=$1; TASK=$2; STEPS=$3; COST=${4:-0.5}
python3 _tools_/cu_bridge.py lock 2>&1 | tail -1 | grep -q '"state": "free"' || { echo "DESKTOP BUSY: $(python3 _tools_/cu_bridge.py lock 2>&1 | tail -1)"; exit 2; }
python3 _tools_/queue.py token-acquire --executor operator | tail -1 || exit 1
if [ "$UNIT" != "-" ]; then python3 _tools_/queue.py claim --unit "$UNIT" --executor operator 2>&1 | tail -1 | tee /tmp/claim_out.txt; grep -q "^claimed" /tmp/claim_out.txt || { echo "CLAIM REFUSED"; python3 _tools_/queue.py token-release --executor operator | tail -1; exit 1; }; fi
killall -9 UserNotificationCenter NotificationCenter 2>/dev/null
F=$(lsappinfo info -only name "$(lsappinfo front)" | head -1)
case "$F" in *LastWar*) ;; *) echo "FRONT NOT LASTWAR: $F"; exit 3;; esac
T0=$(date -u +%T.%N | cut -c1-12); echo "start requested $T0 ; lock: $(python3 _tools_/cu_bridge.py lock 2>&1 | tail -1)"
OUT=$(python3 _tools_/cu_bridge.py start --app com.lastwar.ios --model claude-gateway/claude-sonnet-5-5 --max-steps "$STEPS" --max-cost "$COST" --task "$(cat "$TASK")" 2>&1)
RID=$(echo "$OUT" | python3 -c "import sys,json; t=sys.stdin.read(); print(json.JSONDecoder().raw_decode(t[t.index('{'):])[0]['run_id'])" 2>/dev/null)
[ -z "$RID" ] && { echo "START FAILED: $(echo "$OUT" | head -6 | cut -c1-300)"; python3 _tools_/queue.py token-release --executor operator | tail -1; exit 4; }
echo "run=$RID started $(date -u +%T.%N | cut -c1-12)"; echo "$OUT" | grep -i -E "approve|consent|control-link" | cut -c1-200
for i in $(seq 1 120); do sleep 5
  F=$(lsappinfo info -only name "$(lsappinfo front)" | head -1 | cut -d: -f1)
  case "$F" in *LastWar*) ;; *) echo "FOREGROUND SWITCH: $F at $(date -u +%T.%N | cut -c1-12)"; python3 _tools_/cu_bridge.py control --run-id $RID --command stop 2>&1 | head -2; break;; esac
  S=$(python3 _tools_/cu_bridge.py status --run-id $RID 2>/dev/null | python3 -c "
import sys,json
t=sys.stdin.read(); d,_=json.JSONDecoder().raw_decode(t[t.index('{'):]); print(d.get('state'), 'WAITING:'+json.dumps(d.get('waiting_for_person'))[:300] if d.get('waiting_for_person') else '')")
  case "$S" in *finished*|*failed*|*stopped*|*WAITING*|*error*) echo "$(date -u +%T) $S"; break;; esac
done
python3 - <<PY
import json
rid="$RID"
d=json.load(open(f"/Users/zhenchen/.computer-use/runs/{rid}/run.json"))
r=d.get("result") or {}
print("RESULT",r.get("status"),r.get("steps"),r.get("actions"),(r.get("usage") or {}).get("costUsd"),r.get("error"))
print(r.get("finalMessage"))
print("build",d.get("build"))
rows=[json.loads(l) for l in open(f"/Users/zhenchen/.computer-use/runs/{rid}/events.jsonl") if l.strip()]
for e in rows:
    k=e.get("kind")
    if k=="action" and e.get("status")=="done" and e["action"].get("type") in ("click","drag","scroll"): print("ACT",e["t"][11:23],e["step"],e["action"].get("type"),e["action"].get("x"),e["action"].get("y"))
    elif k=="observation": print("OBS",e["t"][11:23],e["step"])
    elif k=="note": print("note",e["t"][11:23])
    elif k=="consent": print("CONSENT",json.dumps(e)[:400])
PY
python3 _tools_/queue.py token-release --executor operator | tail -1
echo "front: $(lsappinfo info -only name "$(lsappinfo front)" | head -1 | cut -d: -f1) at $(date -u +%T)"
