#!/usr/bin/env python3
"""Resource map for the Last War account.

Keeps an append-only snapshot history (_tools_/state/resources.jsonl) of
every resource a run reads off the HUD, and checks the newest snapshot
against the floors in _tools_/resources.json so a stretched resource
(coin at 565K on 2026-10-25) is flagged instead of discovered late.

Usage:
  resource_map.py snap food=276.9M iron=267.6M coin=565.1K [--note TEXT]
  resource_map.py show     latest snapshot with floor flags
  resource_map.py check    only the warnings (silent when all healthy)
"""
import argparse, json, os, sys
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
DEFS = os.path.join(ROOT, "resources.json")
HIST = os.path.join(ROOT, "state", "resources.jsonl")

def parse_amount(text):
    text = text.strip().replace(",", "")
    mult = 1
    if text[-1:] in "Mm":
        mult, text = 1_000_000, text[:-1]
    elif text[-1:] in "Kk":
        mult, text = 1_000, text[:-1]
    return int(float(text) * mult)

def load_defs():
    with open(DEFS) as f:
        return json.load(f)["resources"]

def snapshots():
    if not os.path.exists(HIST):
        return []
    with open(HIST) as f:
        return [json.loads(line) for line in f if line.strip()]

def flags(values):
    defs = load_defs()
    out = []
    for key, val in values.items():
        d = defs.get(key)
        if not d:
            out.append((key, val, "unknown resource - add it to resources.json"))
            continue
        if d.get("crit_below") is not None and val < d["crit_below"]:
            out.append((key, val, "CRITICAL - below " + str(d["crit_below"]) +
                        "; push from: " + "; ".join(d["push_sources"][:2])))
        elif d.get("warn_below") is not None and val < d["warn_below"]:
            out.append((key, val, "low - below " + str(d["warn_below"])))
    return out

def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("snap")
    p.add_argument("pairs", nargs="+")
    p.add_argument("--note", default="")
    sub.add_parser("show")
    sub.add_parser("check")
    args = ap.parse_args()
    if args.cmd == "snap":
        values = {}
        for pair in args.pairs:
            key, _, raw = pair.partition("=")
            values[key] = parse_amount(raw)
        rec = {"at": datetime.now().isoformat(timespec="seconds"),
               "note": args.note, "values": values}
        os.makedirs(os.path.dirname(HIST), exist_ok=True)
        with open(HIST, "a") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print("snapshot saved:", rec["at"])
        for key, val, why in flags(values):
            print(f"FLAG {key} = {val:,} - {why}")
        return 0
    snaps = snapshots()
    if not snaps:
        print("no snapshots yet")
        return 0
    latest = snaps[-1]
    print(f"Latest snapshot {latest['at']} - {latest.get('note','')}")
    defs = load_defs()
    for key, val in latest["values"].items():
        label = defs.get(key, {}).get("label", key)
        print(f"  {key:16} {val:>14,}  {label}")
    fl = flags(latest["values"])
    if args.cmd == "check" or fl:
        for key, val, why in fl:
            print(f"FLAG {key} = {val:,} - {why}")
        if not fl:
            print("all resources above their floors")
    return 0

if __name__ == "__main__":
    sys.exit(main())
