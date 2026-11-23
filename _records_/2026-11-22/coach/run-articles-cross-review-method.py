#!/usr/bin/env python3
"""Read-only review of the class-a rows of run-articles-audit.csv whose mapped record sits in another activity's folder.
Per row: (1) the record exists; (2) same-unit evidence: a unit id named in the article (regular-YYYY-MM-DD-HHMM) also
appears in the record, or the article cites the record path or its file name; (3) distinctive numbers: shared numbers that
occur in at most 30 primary records, counted against the article's own distinctive numbers; (4) activity mentions: the
record names the article's activity (distinguishing stem). Verdict: confirm = same-unit evidence; plausible = at least 3
distinctive shared numbers and an activity mention; weak = at least 2 distinctive shared numbers or an activity mention but
not both tests; wrong = neither. Rows weak or wrong are the ones not to mark superseded."""
import re,os,csv,glob,collections,sys
sys.path.insert(0,"/tmp/lw-coach")
ROOT="/Users/zhenchen/zachmesh/lastwar"; OUT=ROOT+"/_records_/2026-11-22/coach/"
NUM=re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+(?:\.\d+)?[KMG%]?|\d+\.\d+[KMG%]?|\d+[KMG%])(?![\w])|(?<![\w.,])(\d{3}|\d{5,})(?![\w,])")
def nums(t):
    return {(m.group(1) or m.group(2)).replace(",","").lower() for m in NUM.finditer(t)}
def body(p):
    t=open(p,encoding="utf-8",errors="ignore").read(); m=re.match(r"---\n.*?\n---\n(.*)",t,re.S); return m.group(1) if m else t
EXCL={"knowledge-organization","pr-integration","pr-catchall","tool-development","integration","queue-planning","retro-review","coach"}
df=collections.Counter(); rtext={}
for p in glob.glob(ROOT+"/_records_/20??-??-??/*/[0-9][0-9][0-9][0-9]-*.md"):
    if p.split("/")[-2] in EXCL: continue
    t=open(p,encoding="utf-8",errors="ignore").read(); rtext[p]=t
    for n in nums(t): df[n]+=1
RARE=30
UNIT=re.compile(r"\b([a-z][a-z-]*-20\d\d-\d\d-\d\d-\d{3,4})\b")
GENERIC={"alliance","daily","claims","tasks","queue","rewards","activities","collection"}
def stems(act):
    ws=[w for w in act.split("-") if w not in GENERIC and len(w)>=4] or [w for w in act.split("-") if len(w)>=4] or [act]
    return sorted({w[:5].lower() for w in ws})
rows=list(csv.DictReader(open(OUT+"run-articles-audit.csv")))
cross=[r for r in rows if r["class"]=="a" and r["mapped_record_path"].split("/")[2]!=r["activity"]]
res=[["path","activity","mapped_record_path","record_folder","exists","shared_share","same_unit_evidence","cites_record","distinctive_shared","article_distinctive","activity_mentions","article_cited_record_exists","verdict","one_line_reason","suggested_record"]]
for r in cross:
    ap=ROOT+"/"+r["path"]; rp=ROOT+"/"+r["mapped_record_path"]; ex=os.path.exists(rp)
    b=body(ap); rt=rtext.get(rp) or (open(rp,encoding="utf-8",errors="ignore").read() if ex else "")
    an=nums(b); rn=nums(rt); shared=an&rn
    dis_a={n for n in an if df[n]<=RARE}; dis_s=shared&dis_a
    uids=set(UNIT.findall(b)); same=sorted(u for u in uids if u in rt)
    base=os.path.basename(rp)[:-3]; cites=(r["mapped_record_path"] in b) or (base in b and base[:4].isdigit())
    mentions=sum(len(re.findall(re.escape(st),rt,flags=re.I)) for st in stems(r["activity"]))
    ruids=set(UNIT.findall(rt)); conflict=bool(uids and ruids and not (uids&ruids)) and not cites
    cp=[x.rstrip(".,;)`") for x in re.findall(r"_records_/\d{4}-\d{2}-\d{2}/[a-z0-9-]+/\d{4}-[A-Za-z0-9._-]*\.md",b)]
    cexists="none cited" if not cp else ("yes" if all(os.path.exists(ROOT+"/"+x) for x in cp) else "NO")
    if same or cites: v="confirm"; why=("same unit id "+same[0]) if same else "the article cites the record"
    elif conflict: v="wrong"; why=f"different unit: the article names {sorted(uids)[0]}, the record {sorted(ruids)[0]}"+("; the cited record is absent from the checkout" if cexists=="NO" else "")
    elif len(dis_s)>=3 or (len(dis_s)>=2 and dis_a and len(dis_s)/len(dis_a)>=0.66 and mentions>=1): v="plausible"; why=f"{len(dis_s)} of {len(dis_a)} distinctive numbers shared; the record names the activity {mentions}x"
    elif len(dis_s)>=2 or (mentions>=1 and len(dis_s)>=1): v="weak"; why=f"{len(dis_s)} of {len(dis_a)} distinctive numbers shared, activity named {mentions}x; evidence thin"
    else: v="wrong"; why=f"{len(dis_s)} of {len(dis_a)} distinctive numbers shared and the record never names the activity"
    res.append([r["path"],r["activity"],r["mapped_record_path"],r["mapped_record_path"].split("/")[2],"yes" if ex else "NO",r["shared_number_share"],"; ".join(same) if same else "no","yes" if cites else "no",len(dis_s),len(dis_a),mentions,cexists,v,why,(next((x for x in cp if os.path.exists(ROOT+"/"+x)),"") if v in ("weak","wrong") else "")])
csv.writer(open(OUT+"run-articles-cross-activity-review.csv","w",newline="")).writerows(res)
c=collections.Counter(x[12] for x in res[1:]); print("rows",len(res)-1,"exists",sum(1 for x in res[1:] if x[4]=="yes"),dict(c))
flag=[x for x in res if x[12] in ("weak","wrong")]
csv.writer(open(OUT+"run-articles-not-superseded.csv","w",newline="")).writerows([res[0]]+flag[1:] if flag and flag[0]==res[0] else [res[0]]+flag)
print("flagged",len([x for x in res[1:] if x[12] in ("weak","wrong")]))
b3=[x for x in res[1:] if x[1] in ("alliance-donations","shop-claims","troop-training")]
print("block1 rows",len(b3),dict(collections.Counter(x[12] for x in b3)))
