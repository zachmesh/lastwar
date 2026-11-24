#!/usr/bin/env python3
"""Productive share (Steer A, 2026-11-24T16:05Z): the share of executed units, and of the operator's hours, whose RESULT CHANGED THE GAME
STATE (a claim that paid, a build or research started, a batch collected, a truck dispatched or settled, a fight fought, a conversion made),
which cannot be raised by relabelling. Version 1 is a regex on the result block (resources_gained, claimed_count, points, achieved,
summary), audited by hand on a seeded five. Usage: productive-share-method.py --since 2026-11-24T04:00Z --until 2026-11-24T16:03Z [--seed N] [--csv]"""
import sys,os,re,random,csv,datetime as dt,importlib.util
H=os.path.dirname(os.path.abspath(__file__))
sp=importlib.util.spec_from_file_location("cv",os.path.join(H,"coverage-honest-method.py")); cv=importlib.util.module_from_spec(sp); sp.loader.exec_module(cv)
a=sys.argv[1:]; g=lambda k,d: a[a.index(k)+1] if k in a else d
T=lambda s: dt.datetime.strptime(s.replace("Z",""),"%Y-%m-%dT%H:%M")
lo,hi=T(g("--since","2026-11-24T04:00Z")),T(g("--until","2026-11-24T16:03Z")); seed=int(g("--seed","20261124"))
POS=re.compile(r"\b(claim tap|paid|collected|dispatched|settled|started|upgraded|queued|requeued|trained|opened|delivered|Mission Completed|loot|donat\w*|bought|converted|boarded|dug|dig made|taken in|Complete tap|completed by|plunder won|fight won|credited|Help All|cleared|points gained)\b",re.I)
CLAIMED=re.compile(r"(?<!already )(?<!Already )(?<!Free Supply )\bclaimed\b")   # lower-case action word only: 'Claimed' and 'already claimed' are card states
NEG=re.compile(r"^\s*(no |nothing|none|blocked|closed 'badge absent|stopped|not )",re.I)
def field(t,k):
    m=re.search(r"(?m)^\s*"+k+r":\s*(.*)$",t); return (m.group(1).strip() if m else "")
rows=[]
for u in cv.q.load():
    if u["folder"]!="done" or u.get("r_status") not in ("done","partial","failed"): continue
    f=cv.q.T(u.get("r_finished_at",""))
    if not f or not (lo<=f<=hi): continue
    t=open(u["path"],encoding="utf-8",errors="ignore").read()
    dur=float(field(t,"duration_seconds") or 0); summ=field(t,"summary"); ach=field(t,"achieved"); rg=field(t,"resources_gained"); cc=field(t,"claimed_count"); pts=field(t,"points")
    gained=bool(rg) and rg.lower() not in ("none","0","")
    cc_pos=bool(cc) and cc.isdigit() and int(cc)>0
    pts_pos=bool(pts) and re.match(r"^[1-9]",pts)
    text=summ+" || "+ach
    verbs=(bool(POS.search(text)) or bool(CLAIMED.search(text))) and not NEG.match(summ)
    prod=gained or cc_pos or bool(pts_pos) or verbs
    rows.append((u["path"].split("/")[-1].replace(".md",""),f.strftime("%H:%MZ"),u["r_status"],dur,prod,gained,cc_pos,verbs,summ[:170]))
n=len(rows); P=[r for r in rows if r[4]]; hrs=sum(r[3] for r in rows)/3600; phrs=sum(r[3] for r in P)/3600
span=(hi-lo).total_seconds()/3600
print(f"executed units {lo:%m-%d %H:%MZ} to {hi:%H:%MZ}: {n}; productive {len(P)} = {len(P)/max(n,1):.1%} of units")
print(f"operator hours in the units: {hrs:.2f} h, on productive units {phrs:.2f} h = {phrs/max(hrs,1e-9):.1%}; per hour of the window {phrs/span:.2f} h of {span:.1f} h; per 24 h about {phrs/span*24:.1f} h")
byreg={}
for r in rows:
    reg=re.sub(r"-\d{4}-\d{2}-\d{2}.*","",r[0]); d=byreg.setdefault(reg,[0,0,0.0]); d[0]+=1; d[1]+=r[4]; d[2]+=r[3]/3600
print("least productive regulars by hours (units, productive, hours):")
for reg,d in sorted(byreg.items(),key=lambda kv:-(kv[1][2]*(1-kv[1][1]/kv[1][0])))[:6]: print(f"  {reg}: {d[0]} units, {d[1]} productive, {d[2]:.2f} h")
random.seed(seed); samp=random.sample(rows,min(5,n)); print(f"SEEDED SAMPLE ({seed}) for the manual audit (flag, then judge):")
for r in samp: print(f"  {r[0]} {r[1]} {r[2]} prod={r[4]} (gained {r[5]}, claimed {r[6]}, verbs {r[7]}) | {r[8][:140]}")
if "--csv" in a:
    csv.writer(open(os.path.join(H,"productive-share-"+hi.strftime("%Y-%m-%d")+".csv"),"w",newline="")).writerows([["unit","finished","status","duration_s","productive","resources_gained","claimed_count_positive","positive_verbs","summary"]]+[list(map(str,r)) for r in rows])
