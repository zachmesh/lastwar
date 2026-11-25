#!/usr/bin/env python3
"""One-shot numbers for the coach's daily report. Read-only. Usage: daily-report-numbers.py [--now 2026-11-24T12:00Z]
Runs the conformance tool and my methods and prints, in the order of the report: the since-cutover coverage verdict first, the
forecast warning check, idle net of the quiet windows (startable and blocked), the waits since the zero-wait restart, the latest
Total Power series and the decomposition rows, the staged inputs. The donation tap totals and the calibration stay in the inputs file."""
import subprocess,sys,os,csv,json,datetime as dt
H=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.abspath(os.path.join(H,"..","..",".."))
a=sys.argv[1:]; now=a[a.index("--now")+1] if "--now" in a else dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
def run(cmd,cwd=ROOT):
    r=subprocess.run(cmd,cwd=cwd,capture_output=True,text=True); return (r.stdout+r.stderr).strip()
since=json.load(open(os.path.join(ROOT,"_tools_/state/strategy-cutover.json")))["since"]
print(f"=== NUMBERS at {now}")
print("\n--- 1. COVERAGE: the verdict is UNIT-HOURS (limit 60), units are the trend line; read both UNROUNDED from my method below, the tool rounds")
for l in run(["python3","_tools_/strategy-conformance/strategy_conformance.py","--since",since,"--now",now]).splitlines():
    if any(k in l for k in ("SINCE CUTOVER","ROLLING","growth units","last execution","executed serves","conforming","alarm","ALARM")): print(l[:230])
print("my method, since the cutover:",run(["python3","coverage-honest-method.py","--now",now,"--cutover"],H))
print("--- 2. FORECAST WARNINGS:",run(["python3","_tools_/queue.py","validate"]).splitlines()[-1][:120])

print("\n--- 2b. FORECAST GATE since the flip (10:48:40Z, PR 959): units created since it, by strict class; strict-invalid = other wording or no serves line = an override was used")
sys.path.insert(0,H)
import importlib.util,re,collections
_sp=importlib.util.spec_from_file_location("cv",os.path.join(H,"coverage-honest-method.py")); _cv=importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_cv)
def _created(u):
    t=open(u["path"],encoding="utf-8",errors="ignore").read(); m=re.search(r"(?m)^created_at:[ \t]*(\S+)",t); return _cv.q.T(m.group(1)) if m else None
_flip=dt.datetime(2026,11,24,10,48,40)
_S=lambda u: u.get("serves","") if u.get("serves_where")=="frontmatter" else ""
_new=[u for u in _cv.q.load() if _created(u) and _created(u)>=_flip]
_c=collections.Counter(_cv.klass(_S(u)) for u in _new)
print(f"  TEAM.yaml require_forecast line: {[l.strip() for l in open(os.path.join(ROOT,'TEAM.yaml')) if 'require_forecast' in l][:1]}; units created since the flip: {len(_new)} {dict(_c)}; strict-invalid: {sum(v for k,v in _c.items() if k in ('other wording','no serves line'))}")

print("\n--- 3. IDLE net of the quiet windows (startable and blocked; finished-waiting minutes are in idle-blocked-audit.csv)")
print(run(["python3","slot-idle-method.py",now],H))
print("\n--- 4. WAITS")
day=now[:10]; print(run(["python3","wait-aggregate-method.py","--day",day],H))
print("\n--- 5. POWER, latest series rows and the decomposition")
S=list(csv.reader(open(os.path.join(H,"total-power-series.csv"))))[-3:]
for r in S: print("  ",r[2],r[3],"|",r[5][:90])
for r in csv.reader(open(os.path.join(H,"power-delta-decomposition.csv"))):
    if r[0].startswith(("OUR GAIN, total","OTHER DEVICE","EXTERNAL","NET CHANGE","LOCKED")): print("  ",r[0][:70],"|",r[1],"|",(r[2] or "")[:40])
print("\n--- 6. STAGED INPUTS (daily-report-inputs-2026-11-25.csv): rows",len(list(csv.reader(open(os.path.join(H,"daily-report-inputs-2026-11-25.csv")))))-1)
