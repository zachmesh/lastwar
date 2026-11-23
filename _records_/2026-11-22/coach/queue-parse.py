import os, re, glob, datetime as dt, collections, json
root="/Users/zhenchen/zachmesh/lastwar/_queue_"
def parse(path):
    txt=open(path,encoding="utf-8",errors="ignore").read()
    m=re.match(r"---\n(.*?)\n---\n(.*)",txt,re.S)
    if not m: return None
    fm,body=m.group(1),m.group(2)
    u={"path":path,"folder":os.path.basename(os.path.dirname(path)),"body":body}
    # top-level scalars
    for line in fm.splitlines():
        if re.match(r"^[a-z_]+:",line):
            k,_,v=line.partition(":"); u[k.strip()]=v.strip()
    # result block fields
    for k in ("status","started_at","finished_at","duration_seconds","executor","summary"):
        mm=re.search(r"(?m)^  %s: (.*)$"%k,fm); 
        if mm: u["r_"+k]=mm.group(1).strip()
    mm=re.search(r"(?m)^    blocker_category: (.*)$",fm)
    if mm: u["blocker"]=mm.group(1).strip()
    mm=re.search(r"(?m)^    verified: (.*)$",fm)
    if mm: u["verified"]=mm.group(1).strip()
    sv=re.search(r"(?m)^serves:\s*(.*)$",fm)
    if sv: u["serves"]=sv.group(1).strip(); u["serves_where"]="frontmatter"
    else:
        sb=re.search(r"(?m)^\s*serves:\s*(.*)$",body)
        if sb: u["serves"]=sb.group(1).strip(); u["serves_where"]="body"
    return u
def load():
    units=[]
    for d in ("inbox","claimed","done","completed"):
        for p in glob.glob(f"{root}/{d}/*.md"):
            if p.endswith("INDEX.md"): continue
            u=parse(p)
            if u: units.append(u)
    return units
def T(s):
    try: return dt.datetime.strptime(s,"%Y-%m-%dT%H:%M:%SZ")
    except: return None
if __name__=="__main__":
    units=load(); print("parsed",len(units),collections.Counter(u["folder"] for u in units))
    now=dt.datetime(2026,11,23,8,30)
    for h in (6,24):
        ex=[u for u in units if u["folder"]=="done" and T(u.get("r_finished_at",""))and T(u["r_finished_at"])>=now-dt.timedelta(hours=h)]
        print(h,"h executed",len(ex),collections.Counter(u.get("r_status") for u in ex))
    inbox=[u for u in units if u["folder"]=="inbox"]
    print("inbox",len(inbox),"with serves",sum(1 for u in inbox if "serves" in u),"chains",collections.Counter(u.get("chain_id","-") for u in inbox).most_common(8))
