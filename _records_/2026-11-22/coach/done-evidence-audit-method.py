#!/usr/bin/env python3
"""Audit of DONE units for the evidence line (Steer A's closing rule, 2026-11-24T16:03Z).
A unit closes DONE when (a) the claim it was staged for was taken, or (b) a verified 'nothing to claim / nothing to do' state was
read in a frame and QUOTED in the result with what was read, in which frame and at what time. This script flags, for DONE units
finished in a window, whether the result text (summary + stats.achieved) carries: a clock time, a quoted or named state, and a
frame mention; then draws a seeded sample of five for a MANUAL read. The flags are crude; the manual read decides.
Usage: done-evidence-audit-method.py --since 2026-11-24T04:00Z --until 2026-11-24T16:03Z [--seed 20261124] [--n 5]"""
import sys,os,re,random,csv,datetime as dt,importlib.util
H=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location("cv",os.path.join(H,"coverage-honest-method.py")); cv=importlib.util.module_from_spec(sp); sp.loader.exec_module(cv)
a=sys.argv[1:]; g=lambda k,d: a[a.index(k)+1] if k in a else d
T=lambda s: dt.datetime.strptime(s.replace("Z",""),"%Y-%m-%dT%H:%M")
lo,hi=T(g("--since","2026-11-24T04:00Z")),T(g("--until","2026-11-24T16:03Z")); seed=int(g("--seed","20261124")); n=int(g("--n","5"))
TIME=re.compile(r"\b\d{1,2}:\d{2}(:\d{2})?(\.\d+)?Z?\b"); FRAME=re.compile(r"frame|step-?\d|screenshot|crop",re.I)
STATE=re.compile(r"already claimed|no train|no survivor|nothing (to|was)|reads? |read |shows?|showed|counter|no gift|none |full|greyed|'[^']{4,}'",re.I)
rows=[]
for u in cv.q.load():
    if u["folder"]!="done" or u.get("r_status")!="done": continue
    f=cv.q.T(u.get("r_finished_at",""))
    if not f or not (lo<=f<=hi): continue
    t=open(u["path"],encoding="utf-8",errors="ignore").read()
    m=re.search(r"(?m)^\s*summary:\s*(.*)$",t); ac=re.search(r"(?m)^\s*achieved:\s*(.*)$",t)
    txt=((m.group(1) if m else "")+" || "+(ac.group(1) if ac else ""))
    nothing=bool(re.search(r"nothing|no [a-z]+ (to|in|at)|already claimed|none|full|not due|no [a-z]+ ready",txt,re.I))
    rows.append((u["path"].split("/")[-1].replace(".md",""),f.strftime("%H:%MZ"),nothing,bool(TIME.search(txt)),bool(STATE.search(txt)),bool(FRAME.search(txt)),txt[:200]))
tot=len(rows); nt=[r for r in rows if r[2]]
strict=lambda r: r[3] and r[4] and r[5]; lenient=lambda r: r[3] and r[4]
print(f"DONE units {lo:%m-%d %H:%MZ} to {hi:%H:%MZ}: {tot}; 'nothing to do' type {len(nt)}")
print(f"carrying time + state + frame (strict): {sum(strict(r) for r in rows)} of {tot} = {sum(strict(r) for r in rows)/max(tot,1):.0%}; time + state (lenient): {sum(lenient(r) for r in rows)} of {tot} = {sum(lenient(r) for r in rows)/max(tot,1):.0%}")
if nt: print(f"among 'nothing to do' DONE units: strict {sum(strict(r) for r in nt)} of {len(nt)}, lenient {sum(lenient(r) for r in nt)} of {len(nt)}")
random.seed(seed); samp=random.sample(rows,min(n,tot)); print(f"SEEDED SAMPLE ({seed}) for the manual read:")
for r in samp: print(f"  {r[0]} {r[1]} | time {r[3]} state {r[4]} frame {r[5]} | {r[6][:170]}")
if "--csv" in a:
    csv.writer(open(os.path.join(H,"done-evidence-audit-"+hi.strftime("%Y-%m-%d")+".csv"),"w",newline="")).writerows([["unit","finished","nothing_to_do_type","has_time","has_state","has_frame","result_text"]]+[list(map(str,r)) for r in rows])
