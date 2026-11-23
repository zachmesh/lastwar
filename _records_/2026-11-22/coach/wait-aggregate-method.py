#!/usr/bin/env python3
"""Daily D-066 numbers: minutes waited per day by unit, and the builders' start against their free time.
  wait-aggregate-method.py [--day YYYY-MM-DD] [--waits PATH]
Reads the operator's wait rows (default _records_/2026-11-22/growth/0054-waits.csv; columns wait_requested_utc, idle_s_at_request,
wait_granted_utc, minutes_waited and a unit column when present; a refusal owner_active at the lock is a wait row). minutes_waited
is the operator's stated cost and is used as written: a unit with its own not_before can be granted later than the gate was met, so granted
minus requested can be larger; rows where the two differ are listed so the note can be read. Causes: idle 300 s or more at the request = the idle rule was met, the wait had another cause (another run holding the desktop, a
bridge restart). Idle under 300 s: SELF CLICK when the previous run's last click (column prev_run_last_click_utc) lies within 3 s of
request minus idle (the lock counts the harness's own clicks: not an owner-idle cost); OWNER IDLE when it does not (the last input
was not the harness's); UNCLASSIFIED when the column is empty. wait-cause-overrides.csv (unit, cause, evidence) overrides with a stated
evidence. Prints, for the UTC day, the rows, the minutes per unit and by cause, and the total. Builders: reads builders-start-vs-free.csv; minutes lost to waiting (granted minus
requested) and to claim or operator lag (requested minus the free time) are summed over the four builders: the headline."""
import csv,sys,os,datetime as dt,collections
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,"..","..",".."))
def t(s):
    s=s.strip().replace("Z","")
    for f in ("%Y-%m-%dT%H:%M:%S.%f","%Y-%m-%dT%H:%M:%S","%Y-%m-%dT%H:%M"):
        try: return dt.datetime.strptime(s,f)
        except ValueError: pass
    return None
a=sys.argv[1:]; g=lambda k,d=None: a[a.index(k)+1] if k in a else d
zero=t(g('--zero-since','2026-11-23T21:25:53Z'))
day=g("--day",dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")); path=g("--waits",os.path.join(ROOT,"_records_/2026-11-22/growth/0054-waits.csv"))
if not os.path.exists(path): print("no wait rows yet at",path); sys.exit(0)
per=collections.OrderedDict(); cause=collections.Counter(); n=0; bad=0; flags=[]
ov={}
op=os.path.join(H,"wait-cause-overrides.csv")
if os.path.exists(op):
    for r in csv.DictReader(open(op)): ov[r["unit"]]=r["cause"]
for r in csv.DictReader(open(path)):
    req=t(r.get("wait_requested_utc","")); gr=t(r.get("wait_granted_utc",""))
    if not req or not req.strftime("%Y-%m-%d")==day: continue
    stated=float(r.get("minutes_waited") or 0); calc=stated
    if gr and abs(((gr-req).total_seconds()/60)-stated)>0.2: bad+=1
    u=r.get("unit") or r.get("unit_id") or "(no unit named)"; per[u]=per.get(u,0)+calc; n+=1
    idle=float(r.get("idle_s_at_request") or 0); pc=t(r.get("prev_run_last_click_utc","") or "")
    if u in ov: c=ov[u]
    elif idle>=300: c="other (idle rule met)"
    elif pc is None: c="unclassified (under 300 s, previous click not logged)"
    else: c="self click" if abs(((req-dt.timedelta(seconds=idle))-pc).total_seconds())<=3 else "owner idle"
    cause[c]+=calc
    if req>=zero and calc>1.0:
        alert=" ALERT: refusal 'local input ... s ago' after the restart: the variable may be lost" if "local input" in (r.get("note","") or "") else " (read the note: another run on the desktop, a bridge restart, or the variable lost)"
        flags.append(f"  FLAG after the zero-wait restart {zero:%H:%M:%SZ}: {u} waited {calc:.2f} min (over 1)."+alert)
print(f"{day}: {n} wait rows, {sum(per.values()):.1f} minutes waited, {bad} rows whose stated minutes differ from granted minus requested (a not_before of the unit; read the note)")
for u,m in per.items(): print(f"  {u}: {m:.2f} min")
for c,m in cause.items(): print(f"  by cause, {c}: {m:.2f} min")
print(f"  rows after the zero-wait restart ({zero:%H:%M:%SZ}): flagged if over 1 minute:",len(flags)); [print(x) for x in flags]
