#!/usr/bin/env python3
"""Read-only audit of _activities_/<activity>/run-*.md against the dated records.
Method (also in the coach note):
 1. File time: run-YYYYMMDD-HHMM[-suffix].md, local Pacific, as the records use.
 2. Candidate records: every primary file _records_/<date>/<folder>/HHMM-*.md whose HHMM is within 45 minutes of the
    article time (the neighbouring date is read when the time is within 45 minutes of midnight). Folders that only cite
    other records (knowledge-organization, pr-integration, pr-catchall, tool-development, integration, queue-planning,
    retro-review, coach) and INDEX.md are excluded.
 2b. Cited records: any _records_/<date>/<folder>/HHMM-*.md path named in the article body that exists is also a candidate,
    whatever its time gap. The class column uses window plus cited candidates; the note also gives the window-only counts.
 3. Numbers: comma-grouped numbers, decimals, numbers with a K, M, G or percent suffix, bare integers of 3 digits or of 5 or
    more digits; bare 4-digit integers (years, clock times), 1-2 digit integers and dates are ignored. Commas stripped.
 4. Shared-number share = |numbers(article) & numbers(record)| / |numbers(article)|, per distinct number. The best
    candidate is the one with the highest share (ties: smaller time gap, then same activity folder).
 5. Class: a = mapped and share >= 0.50; b = mapped with share < 0.50, or fewer than 3 numbers (nothing numeric to
    duplicate); c = no candidate record within 45 minutes (the reason says whether the activity has any record that date).
 6. Word overlap (few-number articles only): share of the article's distinct words of 6 or more letters found in the
    nearest same-activity record within 45 minutes (else the nearest record); shown in the reason, never used for the class.
 7. Rule signals: occurrences of rule, cadence, standing, stays, unverified, open, owed, next, never, do not in the body,
    written into the reason of b and c rows to help triage; the class never rests on them.
Nothing is moved, renamed or deleted."""
import os, re, csv, glob, collections, statistics, sys
ROOT=sys.argv[1] if len(sys.argv)>1 else "/Users/zhenchen/zachmesh/lastwar"
OUT=sys.argv[2] if len(sys.argv)>2 else ROOT+"/_records_/2026-11-22/coach"
EXCL={"knowledge-organization","pr-integration","pr-catchall","tool-development","integration","queue-planning","retro-review","coach"}
NUM=re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+(?:\.\d+)?[KMG%]?|\d+\.\d+[KMG%]?|\d+[KMG%])(?![\w])|(?<![\w.,])(\d{3}|\d{5,})(?![\w,])")
def nums(text):
    out=set()
    for m in NUM.finditer(text):
        tok=m.group(1) or m.group(2)
        tok=tok.replace(",","").lower()
        out.add(tok)
    return out
def body(p):
    t=open(p,encoding="utf-8",errors="ignore").read()
    m=re.match(r"---\n.*?\n---\n(.*)",t,re.S)
    return m.group(1) if m else t
def mins(h): return int(h[:2])*60+int(h[2:])
WORD=re.compile(r"[A-Za-z]{6,}")
def words_of(t): return set(w.lower() for w in WORD.findall(t))
# index primary records
recs=collections.defaultdict(list)
for p in glob.glob(ROOT+"/_records_/20??-??-??/*/[0-9][0-9][0-9][0-9]-*.md"):
    parts=p.split("/"); d=parts[-3]; fo=parts[-2]
    if fo in EXCL: continue
    recs[d].append({"path":p,"folder":fo,"m":mins(os.path.basename(p)[:4]),"nums":None})
def rnums(r):
    if r["nums"] is None: r["nums"]=nums(open(r["path"],encoding="utf-8",errors="ignore").read())
    return r["nums"]
import datetime as dt
def shift(d,k): return (dt.date.fromisoformat(d)+dt.timedelta(days=k)).isoformat()
CITE=re.compile(r"_records_/(\d{4}-\d{2}-\d{2})/([a-z0-9-]+)/(\d{4}-[A-Za-z0-9._-]*\.md)")
rows=[]; window_only=collections.Counter()
rel=lambda x:os.path.relpath(x,ROOT)
def classify(an,b,act,cands,actday):
    sig=len(re.findall(r"(?i)\b(rule|cadence|standing|stays|unverified|open|owed|next|never|do not)\b",b))
    best=None; mp=""; share=""
    if cands and len(an)>=1:
        scored=[]
        for r,gap,cited in cands:
            sh=len(an&rnums(r))/len(an)
            scored.append((sh,1 if cited else 0,-gap,1 if r["folder"]==act else 0,r,gap,cited))
        scored.sort(key=lambda x:(x[0],x[1],x[2],x[3]),reverse=True); best=scored[0]
    if best:
        mp=rel(best[4]["path"]); sh=best[0]; gap=best[5]; fo=best[4]["folder"]; ci=best[6]
        if len(an)>=3: share=f"{sh:.2f}"
        where=("cited record" if ci else f"record {gap} min away")+("" if fo==act else f" (folder {fo})")
    if len(an)<3 and cands:
        cs=sorted(cands,key=lambda x:(0 if x[2] else 1,x[1],0 if x[0]["folder"]==act else 1)); near=cs[0]
        rtxt=open(near[0]["path"],encoding="utf-8",errors="ignore").read(); aw=words_of(b)
        ov=len(aw&words_of(rtxt))/max(1,len(aw))
        if not mp: mp=rel(near[0]["path"])
        return mp,share,"b",f"{len(an)} numbers, nothing numeric to duplicate; word overlap {ov:.0%} with a {'cited record' if near[2] else str(near[1])+' min away record'}; rule signals {sig}"
    if best and len(an)>=3:
        if sh>=0.5: return mp,share,"a",f"{sh:.0%} of {len(an)} numbers appear in a {where}"
        return mp,share,"b",f"only {sh:.0%} of {len(an)} numbers appear in the nearest candidate ({where}); rule signals {sig}"
    return mp,share,"c",f"{len(an)} numbers; no record within 45 minutes or cited ("+("activity has a record that date" if actday else "nothing in the activity folder that date")+f"); rule signals {sig}"
for p in sorted(glob.glob(ROOT+"/_activities_/*/run-*.md")):
    act=p.split("/")[-2]; f=os.path.basename(p)
    m=re.match(r"run-(\d{4})(\d{2})(\d{2})-(\d{4})",f)
    d=f"{m.group(1)}-{m.group(2)}-{m.group(3)}"; tm=mins(m.group(4))
    b=body(p); words=len(b.split()); an=nums(b)
    cands=[]; actday=False
    for k in (-1,0,1):
        dd=shift(d,k); off=k*1440
        for r in recs.get(dd,[]):
            gap=abs((r["m"]+off)-tm)
            if gap<=45: cands.append((r,gap,False))
            if r["folder"]==act and (k==0 or gap<=45): actday=True
    cited=[]
    for cm in CITE.finditer(b):
        cp=f"{ROOT}/_records_/{cm.group(1)}/{cm.group(2)}/{cm.group(3)}"
        if os.path.exists(cp) and cm.group(2) not in EXCL and cp not in [c[0]["path"] for c in cands] and cp not in [c[0]["path"] for c in cited]:
            r={"path":cp,"folder":cm.group(2),"m":mins(cm.group(3)[:4]),"nums":None}
            dgap=abs((dt.date.fromisoformat(cm.group(1))-dt.date.fromisoformat(d)).days)*1440+abs(r["m"]-tm)
            cited.append((r,dgap,True))
    wmp,wsh,wcls,wreason=classify(an,b,act,cands,actday)
    window_only[wcls]+=1
    mp,share,cls,reason=classify(an,b,act,cands+cited,actday)
    if cited and cls!=wcls: reason+=f"; window-only class was {wcls}"
    rows.append([rel(p),act,words,mp,share,cls,reason])
os.makedirs(OUT,exist_ok=True)
with open(OUT+"/run-articles-audit.csv","w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["path","activity","words","mapped_record_path","shared_number_share","class","reason"]); w.writerows(rows)
tot=collections.defaultdict(lambda:collections.Counter())
for r in rows:
    t=tot[r[1]]; t["files"]+=1; t["words"]+=r[2]; t["class_"+r[5]]+=1; t["words_"+r[5]]+=r[2]
with open(OUT+"/run-articles-audit-totals.csv","w",newline="") as fh:
    w=csv.writer(fh); w.writerow(["activity","files","words","a_duplicate","b_unique","c_no_record","words_a","words_b","words_c"])
    for a in sorted(tot): t=tot[a]; w.writerow([a,t["files"],t["words"],t["class_a"],t["class_b"],t["class_c"],t["words_a"],t["words_b"],t["words_c"]])
    T=collections.Counter()
    for t in tot.values(): T.update(t)
    w.writerow(["ALL",T["files"],T["words"],T["class_a"],T["class_b"],T["class_c"],T["words_a"],T["words_b"],T["words_c"]])
sh=[float(r[4]) for r in rows if r[4]!=""]
mapped=[r for r in rows if r[3]!=""]
print("window-only classes",dict(window_only))
print("files",len(rows),"words",sum(r[2] for r in rows))
print("class",collections.Counter(r[5] for r in rows),"words by class",{c:sum(r[2] for r in rows if r[5]==c) for c in "abc"})
print("mapped",len(mapped),"with share",len(sh),"median share all",round(statistics.median(sh),3) if sh else None)
a=[float(r[4]) for r in rows if r[5]=="a"]; print("class a median share",round(statistics.median(a),3),"n",len(a))
print("titles What the ... added:",sum(1 for p in glob.glob(ROOT+"/_activities_/*/run-*.md") if re.search(r"(?m)^title: What the .* added",open(p,encoding="utf-8",errors="ignore").read(2000))))
