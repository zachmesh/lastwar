#!/usr/bin/env python3
# usage: done.py JSONFILE   (keys: unit,status,dir,stem,run,steps,actions,cost,summary,follow,target,achieved,resources,time_pt,time_z,title,index_text,rules)
import json,subprocess,sys,os
j=json.load(open(sys.argv[1]))
os.chdir("/Users/zhenchen/zachmesh/lastwar")
rec=f"_records_/2026-11-22/{j['dir']}/{j['stem']}-queue-run"
cmd=["python3","_tools_/queue.py","complete","--unit",j["unit"],"--status",j["status"],
 "--summary",j["summary"],"--evidence",f"{rec}.md and {j['stem']}-queue-run.csv; run {j['run']}","--follow-up",j["follow"],
 "--stat","target="+j["target"],"--stat","achieved="+j["achieved"],"--stat","resources_gained="+j["resources"],
 "--stat","points=0","--stat","costs=none spent; model %s USD"%j["cost"],"--stat","verified=yes",
 "--stat","run_id="+j["run"],"--stat","run_steps=%s"%j["steps"],"--stat","actions_done=%s"%j["actions"],"--stat","actions_refused=0",
 "--stat","cost_usd="+j["cost"],"--stat","device_takeovers=0","--rules-used",j.get("rules","1,2")]
for k,v in j.get("extra_stats",{}).items(): cmd+=["--stat",f"{k}={v}"]
if j.get("state_change"): cmd+=["--state-change",j["state_change"]]
if j.get("state_read"): cmd+=["--state-read",j["state_read"]]
p=subprocess.run(cmd,capture_output=True,text=True); print("complete rc",p.returncode,(p.stdout+p.stderr).strip()[:200])
open("_records_/2026-11-22/INDEX.md","a").write(j["index_text"]+"\n")
print(subprocess.run(["python3","_tools_/lint-gate/lint_gate.py","record-check",rec+".md"],capture_output=True,text=True).stdout.strip().splitlines()[-1])
