#!/usr/bin/env python3
"""Coach playbook quality statistics. Read-only on _queue_ and _activities_.
Windows end at the cutoff given as argv[1] (Mac UTC, YYYY-MM-DDTHH:MMZ). Executed units are done, partial and failed units
in _queue_/done (expired units are closures, not executions). Per activity (the unit's activity field):
 - done rate = done / executed; done-or-by-design rate = (done + partial with blocker letter h) / executed; the weekly
   ranking is on the second, both are reported.
 - rule_failed per 100 units: the unit stat `rule_failed` when the unit carries it (with `rules_used` and `rule_gap`; the
   legacy `gap` field of old duel and arms-race units is a score gap and is ignored). Until units carry the stat the proxy is
   used, and the output says which: partial or failed units whose blocker letter is c, d, e or f, per 100 executed.
 - oldest unverified rule: the largest age in days since the newest dated evidence of a rule in the activity's rule digest.
 - worst three: activities with 5 or more executed units in 14 days, ranked by the sum of three ranks (lowest done-or-by-design
   rate, highest rule_failed per 100, oldest unverified rule); ties by the done-or-by-design rate.
Numbers line, fixed format, the scribe uses it verbatim (written to playbook-pilot-numbers.csv):
 Numbers, 7 days to <YYYY-MM-DD>: <N> units; done <X>%; done-or-by-design <Y>%; partial <P>, failed <F>; mean steps <S or n/a> (<k> of <N> report it); top blocker <letter> <name> (<b> of <M> non-done).
 With no units: Numbers, 7 days to <YYYY-MM-DD>: 0 units.   With no non-done unit: top blocker none (0 of 0 non-done).
"""
import re,glob,collections,datetime as dt,statistics,csv,sys
import importlib.util,os
_spec=importlib.util.spec_from_file_location("queue_parse",os.path.join(os.path.dirname(os.path.abspath(__file__)),"queue-parse.py"))
q=importlib.util.module_from_spec(_spec); _spec.loader.exec_module(q)
NOW=dt.datetime.strptime(sys.argv[1],"%Y-%m-%dT%H:%MZ") if len(sys.argv)>1 else dt.datetime(2026,11,23,9,30)
OUT="/Users/zhenchen/zachmesh/lastwar/_records_/2026-11-22/coach/"
U=q.load()
def steps(u):
    t=open(u["path"],encoding="utf-8",errors="ignore").read()
    m=re.search(r"(?m)^    run_steps:\s*(\d+)",t); return int(m.group(1)) if m else None
ex=[u for u in U if u["folder"]=="done" and u.get("r_status") in ("done","partial","failed") and q.T(u.get("r_finished_at",""))]
for u in ex: u["steps"]=steps(u); u["fin"]=q.T(u["r_finished_at"])
rules=list(csv.DictReader(open(OUT+"playbook-rules.csv")))
RULEB=set("cdef")
def statnum(u,key):
    t=open(u["path"],encoding="utf-8",errors="ignore").read()
    m=re.search(r"(?m)^    %s:\s*(.*)$"%key,t)
    if not m: return None
    v=m.group(1).strip()
    if v.isdigit(): return int(v)
    return len([x for x in re.split(r"[;,]",v) if x.strip()]) if v else None
def stats(units):
    n=len(units); st=collections.Counter(u["r_status"] for u in units)
    def letter(u):
        m=re.match(r"^([a-i])(?![A-Za-z])",(u.get("blocker","") or "").strip()); return m.group(1) if m else "-"
    bl=collections.Counter(letter(u) for u in units if u["r_status"] in ("partial","failed"))
    rp=sum(v for k,v in bl.items() if k in RULEB)
    sv=[u["steps"] for u in units if u["steps"] is not None]
    rfv=[statnum(u,'rule_failed') for u in units]; rfv=[x for x in rfv if x is not None]
    return dict(n=n,done=st["done"],partial=st["partial"],failed=st["failed"],done_rate=st["done"]/n if n else None,partial_rate=st["partial"]/n if n else None,
                rule_proxy=rp,rf_units=len(rfv),rf_sum=sum(rfv),adj_rate=(st['done']+bl.get('h',0))/n if n else None,rule_proxy_per100=100*rp/n if n else None,bl=bl,steps_mean=statistics.mean(sv) if sv else None,steps_n=len(sv))
rows=[["activity","window_days","executed","done","partial","failed","done_rate","partial_rate","rule_proxy_units","rule_proxy_per_100","done_or_by_design_rate","blockers","mean_steps","steps_units","rules","oldest_unverified_rule_age_days","rules_older_than_14d"]]
S={}
acts=sorted({u.get("activity","?") for u in ex})
rbyact=collections.defaultdict(list)
for r in rules: rbyact[r["activity"]].append(r)
for W in (14,7):
    lo=NOW-dt.timedelta(days=W)
    for a in acts:
        us=[u for u in ex if u.get("activity")==a and u["fin"]>=lo]
        if not us: continue
        s=stats(us); S[(a,W)]=s
        rr=rbyact.get(a,[]); ages=[int(r["age_days_newest"]) for r in rr if r["age_days_newest"]!=""]
        rows.append([a,W,s["n"],s["done"],s["partial"],s["failed"],f"{s['done_rate']:.2f}",f"{s['partial_rate']:.2f}",s["rule_proxy"],f"{s['rule_proxy_per100']:.1f}",f"{s['adj_rate']:.2f}",
                     " ".join(f"{k}{v}" for k,v in sorted(s["bl"].items())),f"{s['steps_mean']:.1f}" if s["steps_mean"] is not None else "n/a",s["steps_n"],len(rr),max(ages) if ages else "",sum(a>=14 for a in ages)])
csv.writer(open(OUT+"playbook-activity-stats.csv","w",newline="")).writerows(rows)
# totals
for W in (14,7):
    lo=NOW-dt.timedelta(days=W); us=[u for u in ex if u["fin"]>=lo]; s=stats(us)
    print(f"ALL {W}d: executed {s['n']} done {s['done']} partial {s['partial']} failed {s['failed']} done rate {s['done_rate']:.1%} partial {s['partial_rate']:.1%}; rule proxy (c,d,e,f) {s['rule_proxy']} = {s['rule_proxy_per100']:.1f} per 100; blockers {dict(s['bl'])}; done-or-by-design {s['adj_rate']:.1%}; steps n {s['steps_n']}")
# pilots
for a in ("alliance-donations","shop-claims"):
    for W in (7,14):
        s=S.get((a,W))
        if s: print(f"PILOT {a} {W}d: units {s['n']} done {s['done']} partial {s['partial']} failed {s['failed']} done rate {s['done_rate']:.0%}; mean steps {s['steps_mean'] if s['steps_mean'] is None else round(s['steps_mean'],1)} (n={s['steps_n']}); blockers {dict(s['bl'])}; done-or-by-design {s['adj_rate']:.0%}; proxy/100 {s['rule_proxy_per100']:.1f}")
        else: print("PILOT",a,W,"no units")
# worst three on 14d with min 5 units
cand=[(a,S[(a,14)]) for a in acts if (a,14) in S and S[(a,14)]["n"]>=5]
def rank(key,rev):
    order=sorted(cand,key=lambda x:key(x),reverse=rev); return {a:i+1 for i,(a,_) in enumerate(order)}
r1=rank(lambda x:x[1]["done_rate"],False); r1b=rank(lambda x:x[1]["adj_rate"],False); r2=rank(lambda x:x[1]["rule_proxy_per100"],True)
age={a:(max([int(r["age_days_newest"]) for r in rbyact.get(a,[]) if r["age_days_newest"]!=""] or [-1])) for a,_ in cand}
order=sorted(cand,key=lambda x:-age[x[0]]); r3={a:i+1 for i,(a,_) in enumerate(order)}
comp=sorted(cand,key=lambda x:(r1b[x[0]]+r2[x[0]]+r3[x[0]],x[1]["adj_rate"]))
W3=[["rank","activity","executed_14d","done_or_by_design_rate","done_rate","rule_failed_per_100","rule_failed_source","oldest_unverified_rule_age_days","rank_done_or_by_design","rank_rule_failed","rank_staleness","rank_sum"]]
for i,(a,s) in enumerate(comp,1):
    src="stat" if s["rf_units"]>=s["n"]*0.5 else "proxy (blocker c,d,e,f)"
    W3.append([i,a,s["n"],f"{s['adj_rate']:.2f}",f"{s['done_rate']:.2f}",f"{s['rule_proxy_per100']:.1f}",src,age[a],r1b[a],r2[a],r3[a],r1b[a]+r2[a]+r3[a]])
csv.writer(open(OUT+"playbook-worst-three.csv","w",newline="")).writerows(W3)
print("candidates (>=5 executed in 14d):",len(cand)); 
for r in W3[:6]: print(r)

# ---- fixed-format numbers lines (7 days) for every activity with a rule digest ----
NAMES={"h":"by-design partial","f":"missing precondition","e":"repeated blocker","c":"tap method","d":"inference over live read",
       "a":"window closure","b":"crowding out","g":"red-line miss","i":"owner-named without escalation","-":"none given"}
def pct(x): return int(x*100+0.5)
def numbers_line(act):
    d=NOW.date().isoformat()
    s=S.get((act,7))
    if not s or s["n"]==0: return f"Numbers, 7 days to {d}: 0 units."
    nd=s["partial"]+s["failed"]
    if nd:
        top=sorted([(v,k) for k,v in s["bl"].items()],key=lambda x:(-x[0],x[1]))[0]
        tb=f"{top[1]} {NAMES[top[1]]} ({top[0]} of {nd} non-done)"
    else: tb="none (0 of 0 non-done)"
    ms="n/a" if s["steps_mean"] is None else (str(int(s["steps_mean"])) if abs(s["steps_mean"]-round(s["steps_mean"]))<0.05 else f"{s['steps_mean']:.1f}")
    return (f"Numbers, 7 days to {d}: {s['n']} units; done {pct(s['done_rate'])}%; done-or-by-design {pct(s['adj_rate'])}%; "
            f"partial {s['partial']}, failed {s['failed']}; mean steps {ms} ({s['steps_n']} of {s['n']} report it); top blocker {tb}.")
digest_acts=sorted({r["activity"] for r in rules})
csv.writer(open(OUT+"playbook-numbers-lines.csv","w",newline="")).writerows([["activity","numbers_line"]]+[[a,numbers_line(a)] for a in digest_acts])
csv.writer(open(OUT+"playbook-pilot-numbers.csv","w",newline="")).writerows([["activity","numbers_line"]]+[[a,numbers_line(a)] for a in ("alliance-donations","shop-claims")])
print("NUMBERS LINES:"); 
for a in ("alliance-donations","shop-claims"): print(" ",a,"|",numbers_line(a))
