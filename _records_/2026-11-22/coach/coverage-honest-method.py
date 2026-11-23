#!/usr/bin/env python3
"""Honest serves coverage of executed units. Read-only. Usage:
  coverage-honest-method.py --now 2026-11-23T17:22Z [--hours 12] [--since 2026-11-23T09:51Z] [--created-since]
Classes by the rule in _tools_/queue.py forecast_class: ranked id (a plan item id with a row in the newest forecast ledger),
ranked name (the fill idle slot phrase), exempt (exactly upkeep, snapshot or baseline), other wording (anything else), no serves
line (empty frontmatter). Coverage = ranked / executed, by units and by unit-hours (result duration, else est_minutes).
Not ranked (the conformance tool's "serving nothing") = exempt + other wording + no serves line, in units and hours. Hours serving nothing, strict: other wording plus no serves line; lenient: the same minus lines that start with an exempt word
(snapshot ..., baseline ...). --cutover reads _tools_/state/strategy-cutover.json for --since; --since keeps units executed after that instant; with --created-since only those also created after it."""
import sys,re,csv,os,importlib.util,datetime as dt,collections,argparse
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,"..","..",".."))
spec=importlib.util.spec_from_file_location("queue_parse",os.path.join(H,"queue-parse.py")); q=importlib.util.module_from_spec(spec); spec.loader.exec_module(q)
ids={r["plan_item"] for r in csv.DictReader(open(os.path.join(ROOT,"_records_/2026-11-22/strategy/forecast-ledger.csv")))}
EX=("upkeep","snapshot","baseline"); FILL=re.compile(r"^fill[- ]idle[- ]slot\b",re.I)
def klass(serves):
    s=" ".join((serves or "").split())
    if not s: return "no serves line"
    parts=[" ".join(p.split()) for p in re.split(r"[;,]",s) if p.strip()]
    if any(not(p.lower() in EX or FILL.match(p) or p in ids) for p in parts): return "other wording"
    if all(p.lower() in EX for p in parts): return "exempt"
    return "ranked name" if any(FILL.match(p) for p in parts) and not any(p in ids for p in parts) else "ranked id"
def text(u): return open(u["path"],encoding="utf-8",errors="ignore").read()
def fld(u,k):
    m=re.search(r"(?m)^%s:[ \t]*(\S*)"%k,text(u)); return m.group(1) if m else ""
def hours(u):
    t=text(u); m=re.search(r"(?m)^  duration_seconds:\s*(\d+)",t)
    if m: return int(m.group(1))/3600
    m=re.search(r"(?m)^est_minutes:\s*(\d+)",t); return int(m.group(1))/60 if m else 0.0
def fmt(s):
    s=s.replace("Z","")
    return dt.datetime.strptime(s,"%Y-%m-%dT%H:%M:%S" if s.count(":")==2 else "%Y-%m-%dT%H:%M")
def main():
    a=argparse.ArgumentParser(); a.add_argument("--now",required=True); a.add_argument("--hours",type=float); a.add_argument("--since"); a.add_argument("--cutover",action="store_true"); a.add_argument("--created-since",action="store_true"); a=a.parse_args()
    import json
    if a.cutover: a.since=json.load(open(os.path.join(ROOT,"_tools_/state/strategy-cutover.json")))["since"]
    now=fmt(a.now); lo=fmt(a.since) if a.since else now-dt.timedelta(hours=a.hours or 12)
    ex=[]
    for u in q.load():
        if u["folder"]=="done" and u.get("r_status") in ("done","partial","failed") and q.T(u.get("r_finished_at","")) and lo<=q.T(u["r_finished_at"])<=now:
            if a.created_since:
                c=q.T(fld(u,"created_at"))
                if not c or c<lo: continue
            ex.append(u)
    c=collections.Counter(); h=collections.Counter(); lenient=0.0
    for u in ex:
        s=u.get("serves","") if u.get("serves_where")=="frontmatter" else ""; k=klass(s); c[k]+=1; hh=hours(u); h[k]+=hh
        if k=="other wording" and not any(" ".join(p.split()).lower().startswith(("snapshot","baseline")) for p in re.split(r"[;,]",s)): lenient+=hh
        if k=="no serves line": lenient+=hh
    n=len(ex); T=sum(h.values()); rk=c["ranked id"]+c["ranked name"]; rh=h["ranked id"]+h["ranked name"]
    strict=h["other wording"]+h["no serves line"]; notrk=n-rk; notrh=T-rh
    row=[f"{lo:%m-%d %H:%MZ} to {now:%m-%d %H:%MZ}"+(" (created since)" if a.created_since else ""),n,c["ranked id"],c["ranked name"],c["exempt"],c["other wording"],c["no serves line"],
         f"{rk/n:.0%}" if n else "n/a",f"{rh/T:.0%}" if T else "n/a",round(T,2),round(strict,2),round(lenient,2),f"{notrk} units {notrh:.2f} h not ranked"]
    print(*row,sep=" | ")
if __name__=="__main__": main()
