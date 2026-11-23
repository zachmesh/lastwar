#!/usr/bin/env python3
"""Operator throughput before and after the restored 300 s idle wait, for Steer A's measurement. Read-only.
  throughput-method.py --now ISO [--restore ISO] [--span-hours 4]
Counts executed units (done, partial, failed, by result.finished_at) in the span before the restore and from the restore to now,
and divides by AVAILABLE hours: elapsed time minus the cu quiet windows (rows type quiet-window in plan-triggers.csv), when the
operator is idle by agreement. Prints units per available hour before and after, the change in percent, the minutes waited from
growth/0054-waits.csv in the after period (by cause) and that wait as a share of available minutes. The units run are not all alike
(growth reads, passes, fills), so the throughput change is an upper bound on what the wait alone costs; the wait share is the direct
measure."""
import sys,os,csv,re,importlib.util,datetime as dt
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,"..","..",".."))
sp=importlib.util.spec_from_file_location("queue_parse",os.path.join(H,"queue-parse.py")); q=importlib.util.module_from_spec(sp); sp.loader.exec_module(q)
def t(s):
    s=s.replace("Z","")
    for f in ("%Y-%m-%dT%H:%M:%S.%f","%Y-%m-%dT%H:%M:%S","%Y-%m-%dT%H:%M"):
        try: return dt.datetime.strptime(s,f)
        except ValueError: pass
a=sys.argv[1:]; g=lambda k,d=None: a[a.index(k)+1] if k in a else d
now=t(g("--now")); restore=t(g("--restore","2026-11-23T20:04:03Z")); span=float(g("--span-hours","4"))
wins=[]
for r in csv.DictReader(open(os.path.join(H,"plan-triggers.csv"))):
    if r["type"]!="quiet-window": continue
    s,e=t(r["trigger_utc"]),t(r["end_utc"])
    if "daily" in r["trigger_event"]:
        d=0
        while s+dt.timedelta(days=d)<=now: wins.append((s+dt.timedelta(days=d),e+dt.timedelta(days=d))); d+=1
    else: wins.append((s,e))
def avail(lo,hi):
    tot=(hi-lo).total_seconds()/60
    for w0,w1 in wins: tot-=max(0.0,(min(hi,w1)-max(lo,w0)).total_seconds()/60)
    return tot
U=[u for u in q.load() if u["folder"]=="done" and u.get("r_status") in ("done","partial","failed") and q.T(u.get("r_finished_at",""))]
def count(lo,hi): return sum(1 for u in U if lo<=q.T(u["r_finished_at"])<hi)
b0=restore-dt.timedelta(hours=span); nb=count(b0,restore); ab=avail(b0,restore); na=count(restore,now); aa=avail(restore,now)
rb=nb/(ab/60) if ab else float("nan"); ra=na/(aa/60) if aa>0 else float("nan")
print(f"before  {b0:%m-%d %H:%MZ} to {restore:%H:%MZ}: {nb} units in {ab/60:.2f} available h = {rb:.2f} units per available hour")
print(f"after   {restore:%m-%d %H:%MZ} to {now:%H:%MZ}: {na} units in {aa/60:.2f} available h = {ra:.2f} units per available hour" if aa>0 else "after: no available time yet")
if aa>0 and rb==rb: print(f"change  {(ra-rb)/rb:+.0%} ({ra-rb:+.2f} units an hour); Steer A's estimate: 5.5 to 3.8, -31%")
wp=os.path.join(ROOT,"_records_/2026-11-22/growth/0054-waits.csv"); w=0.0; n=0
if os.path.exists(wp):
    for r in csv.DictReader(open(wp)):
        x=t(r.get("wait_requested_utc","") or "")
        if x and restore<=x<=now: w+=float(r.get("minutes_waited") or 0); n+=1
print(f"waits   {n} rows, {w:.2f} minutes waited since the restore = {100*w/aa:.1f}% of available minutes" if aa>0 else "waits: none yet")
