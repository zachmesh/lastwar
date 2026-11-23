#!/usr/bin/env python3
"""Slot idle minutes with the quiet windows subtracted. Usage: slot-idle-method.py CUTOFF  (YYYY-MM-DDTHH:MMZ, Mac UTC).
Reads slot-idle-intervals.csv (idle slot intervals, an empty idle_to means open to the cutoff) and the rows of plan-triggers.csv
whose type is quiet-window (a row with the word daily in its event repeats every day from its start). For the 24 h and 6 h
windows ending at the cutoff it prints, by slot type: slot-minutes available, raw idle, idle inside quiet windows (not counted:
no input was allowed), adjusted idle and its share, of which blocked by capacity (the finished troops cannot be collected while the Drill Ground is full: the slot reads idle but nothing can start), and the startable idle that remains. Bases: builders 4 slots, labs 2, training barracks 3 (Lv.20 unprobed)."""
import csv,sys,os,datetime as dt
H=os.path.dirname(os.path.abspath(__file__))
fmt=lambda s: dt.datetime.strptime(s.replace("Z",""),"%Y-%m-%dT%H:%M:%S" if s.count(":")==2 else "%Y-%m-%dT%H:%M")
cut=fmt(sys.argv[1]) if len(sys.argv)>1 else dt.datetime(2026,11,23,15,5)
def ov(a0,a1,b0,b1): return max(0.0,(min(a1,b1)-max(a0,b0)).total_seconds()/60)
wins=[]
for r in csv.DictReader(open(H+"/plan-triggers.csv")):
    if r["type"]!="quiet-window": continue
    s,e=fmt(r["trigger_utc"]),fmt(r["end_utc"])
    if "daily" in r["trigger_event"]:
        d=0
        while s+dt.timedelta(days=d)<=cut+dt.timedelta(days=1): wins.append((s+dt.timedelta(days=d),e+dt.timedelta(days=d))); d+=1
    else: wins.append((s,e))
iv=list(csv.DictReader(open(H+"/slot-idle-intervals.csv")))
base={"builders":4,"labs":2,"training":3}
out=[["window","slot_type","slot_minutes","raw_idle","in_quiet_windows","adjusted_idle","adjusted_share","of_which_blocked_by_capacity","startable_idle","startable_share"]]
for label,hrs in (("24h",24),("6h",6)):
    lo=cut-dt.timedelta(hours=hrs); tot=[0,0,0,0]
    for t in ("builders","labs","training"):
        raw=q=bl=0.0
        for r in iv:
            if r["slot_type"]!=t: continue
            a0=fmt(r["idle_from"]); a1=fmt(r["idle_to"]) if r["idle_to"] else cut; n=int(r["slots"])
            ri=n*ov(a0,a1,lo,cut); qi=n*sum(ov(max(a0,lo),min(a1,cut),w0,w1) for w0,w1 in wins); raw+=ri; q+=qi
            if r.get('blocked_by_capacity')=='yes': bl+=ri-qi
        sm=base[t]*hrs*60; out.append([label,t,sm,round(raw),round(q),round(raw-q),f"{(raw-q)/sm:.1%}",round(bl),round(raw-q-bl),f"{(raw-q-bl)/sm:.1%}"])
        tot[0]+=sm; tot[1]+=raw; tot[2]+=q; tot[3]+=bl
    out.append([label,"ALL",tot[0],round(tot[1]),round(tot[2]),round(tot[1]-tot[2]),f"{(tot[1]-tot[2])/tot[0]:.1%}",round(tot[3]),round(tot[1]-tot[2]-tot[3]),f"{(tot[1]-tot[2]-tot[3])/tot[0]:.1%}"])
for r in out: print(*r,sep=" | ")
if len(sys.argv)>2: csv.writer(open(sys.argv[2],"w",newline="")).writerows(out)
