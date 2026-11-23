#!/usr/bin/env python3
"""Refill entry-count check (rule 8: one count per 20 minutes on a fixed clock, cap 30). Usage:
  refill-check-method.py ENTRY_UTC [--observed N] [--anchor UTC] [--taps N]
ENTRY_UTC and UTC are YYYY-MM-DDTHH:MM:SS(.fff)Z. The anchor is the last timer end read in a pass that SPENT the pool (default: the
newest timer end in refill-pass-log.csv); --taps is the number of witnessed taps made since the anchor, own passes included.
  uncapped = 1 + floor((entry - anchor) / 1200 s) - taps_since_anchor
  predicted = max(0, min(30, uncapped))      an entry before the anchor (timer still running) gives 0
A pass that leaves counts behind reads no new timer end, so the old anchor stays valid and its taps are subtracted.
If uncapped reaches 30 the cap hides the answer: refills at the cap are lost and elsewhere use cannot show, so the prediction is an
upper bound only; keep the gap since the last spend under about 9 hours to test accrual. A smaller observed count is a shortfall:
counts used elsewhere (the owner's phone shares the count) or partial accrual, not a refutation of the grid."""
import sys,csv,os,datetime as dt
H=os.path.dirname(os.path.abspath(__file__))
def t(s): s=s.replace("Z",""); return dt.datetime.strptime(s,"%Y-%m-%dT%H:%M:%S.%f" if "." in s else "%Y-%m-%dT%H:%M:%S")
def predict(entry,anchor,taps=0):
    unc=1+int(((t(entry)-t(anchor)).total_seconds())//1200)-int(taps)
    p=max(0,min(30,unc)); hrs=(t(entry)-t(anchor)).total_seconds()/3600
    note="" if unc<30 else "upper bound only: the cap of 30 hides elsewhere use"
    if hrs>9 and not note: note="gap over 9 h since the anchor: close to the cap, a weak test"
    return p,unc,note
if __name__=="__main__":
    a=sys.argv[1:]; entry=a[0]
    g=lambda k,d=None: a[a.index(k)+1] if k in a else d
    obs=int(g("--observed")) if g("--observed") is not None else None; taps=int(g("--taps",0))
    anchor=g("--anchor")
    if not anchor:
        rows=list(csv.DictReader(open(H+"/refill-pass-log.csv"))); anchor=[r["timer_end_utc"] for r in rows if r["timer_end_utc"]][-1]
    p,unc,note=predict(entry,anchor,taps)
    print("anchor",anchor,"| taps since",taps,"| uncapped",unc,"| predicted",p,"| observed",obs if obs is not None else "-","| shortfall",(p-obs) if obs is not None else "-",("| "+note) if note else "")
