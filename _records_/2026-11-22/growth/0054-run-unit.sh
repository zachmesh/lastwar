#!/bin/bash
# usage: run_unit.sh UNIT TASKFILE MAXSTEPS
cd /Users/zhenchen/zachmesh/lastwar || exit 9
UNIT=$1; TASK=$2; STEPS=$3
node /Users/zhenchen/dtadpole/computer-use/_environments_/macos-desktop/run-lock.mjs status | grep -q '"run":null' || { echo "DESKTOP BUSY"; node /Users/zhenchen/dtadpole/computer-use/_environments_/macos-desktop/run-lock.mjs status; exit 2; }
python3 _tools_/queue.py token-acquire --executor operator || exit 1
python3 _tools_/queue.py claim --unit "$UNIT" --executor operator || { echo "CLAIM REFUSED"; python3 _tools_/queue.py token-release --executor operator; exit 1; }
CLAIMED=$(date -u +%T)
killall -9 UserNotificationCenter NotificationCenter 2>/dev/null
F=$(lsappinfo info -only name "$(lsappinfo front)" | head -1)
case "$F" in *LastWar*) ;; *) echo "FRONT NOT LASTWAR: $F"; exit 3;; esac
OUT=$(python3 _tools_/cu_bridge.py start --app com.lastwar.ios --model claude-gateway/claude-sonnet-5-5 --max-steps "$STEPS" --max-cost 0.5 --task "$(cat "$TASK")")
RID=$(echo "$OUT" | python3 -c "import sys,json; print(json.JSONDecoder().raw_decode(sys.stdin.read())[0]['run_id'])")
echo "claimed $CLAIMED run $RID"
for i in $(seq 1 40); do
  sleep 8
  F=$(lsappinfo info -only name "$(lsappinfo front)" | head -1 | cut -d: -f1)
  S=$(python3 _tools_/cu_bridge.py status 2>&1 | python3 -c "
import sys,json
d,_=json.JSONDecoder().raw_decode(sys.stdin.read()); print(d['state'],d['steps'])" 2>/dev/null)
  case "$F" in *LastWar*) ;; *) echo "FOREGROUND SWITCH to $F at $(date -u +%T)"; python3 _tools_/cu_bridge.py control --run-id "$RID" --command stop 2>&1 | head -2; exit 4;; esac
  case "$S" in finished*|failed*|stopped*) break;; esac
done
python3 _tools_/cu_bridge.py status 2>&1 | python3 -c "
import sys,json
d,_=json.JSONDecoder().raw_decode(sys.stdin.read())
r=d.get('result') or {}
print('STATE',d['state'],'steps',d['steps'],'actions',r.get('actions'),'cost',r.get('usage',{}).get('costUsd'))
print(r.get('finalMessage'))
"
echo "front: $(lsappinfo info -only name "$(lsappinfo front)" | head -1 | cut -d: -f1) at $(date -u +%T)"
python3 _tools_/queue.py token-release --executor operator
