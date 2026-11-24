#!/usr/bin/env python3
# usage: mk.py SPEC.json  -> writes the record md + csv, completes the unit, appends the day index
import json,sys,csv,os,subprocess
s=json.load(open(sys.argv[1]))
os.chdir("/Users/zhenchen/zachmesh/lastwar")
d=f"_records_/2026-11-22/{s['dir']}"
stem=s['stem']
with open(f"{d}/{stem}-queue-run.csv","w",newline="") as f:
    w=csv.writer(f); w.writerow(["item","value","read_utc","note"])
    for r in s["rows"]: w.writerow(r+[""]*(4-len(r)))
md=f"""---
title: {s['title']}
created: {s['now']}
modified: {s['now']}
version: 1.0.0
description: {s['description']}
status: {s['status']}
grounded_in:
  - source: cu_bridge run {s['run']}, final report read by the operator, {s['window']}
  - source: unit brief {s['unit']} and the {s['dir']} rule digest
---

# {s['title']}

Rows in [{stem}-queue-run.csv]({stem}-queue-run.csv). Claimed {s['claimed']}; no different-device dialog.

""" + "\n".join("- "+b for b in s["bullets"]) + f"""
- **Run.** One run, {s['steps']} steps, {s['actions']} actions, {s['cost']} USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** {s['closing']}
"""
open(f"{d}/{stem}-queue-run.md","w").write(md)
j={"unit":s["unit"],"status":s["status"],"dir":s["dir"],"stem":stem,"run":s["run"],"steps":s["steps"],"actions":s["actions"],"cost":s["cost"],
 "summary":s["summary"],"follow":s["follow"],"target":s["target"],"achieved":s["achieved"],"resources":s.get("resources","none"),
 "index_text":s["index"],"rules":s.get("rules","1"),"extra_stats":s.get("extra_stats",{}),"state_change":s.get("state_change",""),"state_read":s.get("state_read","")}
json.dump(j,open(sys.argv[1]+".done.json","w"))
print(subprocess.run(["python3","/tmp/operator-tasks/done.py",sys.argv[1]+".done.json"],capture_output=True,text=True).stdout.strip()[:300])
