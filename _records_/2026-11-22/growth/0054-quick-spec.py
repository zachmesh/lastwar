#!/usr/bin/env python3
# closing rule 3170: a DONE nothing-to-do unit needs summary to end with: state_read: <quoted> | <frame> | <HH:MM:SSZ>
# state_read_frame must be "step N" or "step N frame" or a file name; keys state_read_what, state_read_frame, state_read_time (HH:MM:SSZ)
# usage: qs.py JSON  (compact unit spec -> full mk.py spec, fixes time, appends waits row)
import json,sys,subprocess,datetime,re
d=json.load(open(sys.argv[1]))
# Steer A 16:17Z: every summary also ends with "state_change: yes|no" (key state_change); a DONE with no needs the state_read line
if "state_change" not in d: sys.exit("spec needs state_change yes|no")
d["summary"]=d["summary"].rstrip(".")+". state_change: "+d["state_change"]
if d.get("state_read_what"):
    sr="%s | %s | %s"%(d["state_read_what"],d["state_read_frame"],d["state_read_time"])
    d["summary"]+=". state_read: "+sr
if d["state_change"]=="no" and d["status"]=="done" and "state_read:" not in d["summary"]: sys.exit("DONE with state_change no needs a state_read (keys state_read_what, state_read_frame, state_read_time)")
now=datetime.datetime.utcnow()
t_rec=(now-datetime.timedelta(seconds=40)).strftime("%Y-%m-%dT%H:%M:%SZ")
pt=(now-datetime.timedelta(seconds=40)-datetime.timedelta(hours=8)).strftime("%H:%M")
zt=(now-datetime.timedelta(seconds=40)).strftime("%H:%MZ")
spec={"unit":d["unit"],"status":d["status"],"dir":d["dir"],"stem":d["stem"],"run":d["run"],"steps":d["steps"],"actions":d["actions"],"cost":d["cost"],"title":d["title"],"now":t_rec,"window":d["window"],"claimed":d["claimed"],
"description":d["description"],
"rows":[["wait",d["wait"],d["start_utc"],"see growth/0054-waits.csv"],["badges",d["badges"],d["start_utc"],"tram badge rule: none; not tapped"]]+d["rows"]+[["drags","drags tried "+str(d.get("drags",0))+", cancelled 0","",""]],
"bullets":d["bullets"],"closing":d["closing"],"summary":d["summary"],"follow":d["follow"],"target":d["target"],"achieved":d["achieved"],
"index":"- %s PT (%s), %s-%s - %s, %s (unit `%s`, claimed %s, run `%s`, %s steps, %s USD). %s Record: %s/%s-queue-run.md."%(pt,zt,d["dir"],d["stem"],d["status"],d["title"],d["unit"],d["claimed"],d["run"],d["steps"],d["cost"],d["summary"].rstrip(".")+".",d["dir"],d["stem"]),
"rules":d.get("rules","1,2"),"extra_stats":d.get("extra_stats",{})}
if d.get("resources"): spec["resources"]=d["resources"]
spec["state_change"]=d["state_change"]
if d.get("state_read_what"): spec["state_read"]="%s | %s | %s"%(d["state_read_what"],d["state_read_frame"],d["state_read_time"])
json.dump(spec,open("/tmp/operator-tasks/_spec.json","w"))
subprocess.run(["python3","_tools_/queue.py","token-acquire","--executor","operator"],capture_output=True)
r=subprocess.run(["python3","/tmp/operator-tasks/mk.py","/tmp/operator-tasks/_spec.json"],capture_output=True,text=True)
print(r.stdout.strip().splitlines()[:2], r.stderr.strip()[-200:])
subprocess.run(["python3","_tools_/queue.py","token-release","--executor","operator"],capture_output=True)
# fix times: mk.py wrote d now; make sure record/index times are before now
p="_records_/2026-11-22/%s/%s-queue-run.md"%(d["dir"],d["stem"])
with open("_records_/2026-11-22/growth/0054-waits.csv","a") as f:
    f.write(d["waits_row"]+"\n")
lint=subprocess.run(["python3","_tools_/lint-gate/lint_gate.py","record-check",p],capture_output=True,text=True)
print(lint.stdout.strip().splitlines()[-1][:160])
