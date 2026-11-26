#!/usr/bin/env python3
"""Builds 1155-daily-report-2026-11-26.md. Every number is computed or read from the tools run on the window 11-25 12:00Z to 11-26 12:00Z
(productive-share-method.py, done-evidence-audit-method.py, strategy_conformance.py, coverage-honest-method.py, the queue done folder, the builder
idle segments from the timestamps of the records); only the donation count and the clock time come from the clock. Usage: python3 daily-report-build-2026-11-26.py"""
import datetime as dt
now=dt.datetime.now(dt.timezone.utc).replace(tzinfo=None,second=0,microsecond=0); hhmm=now.strftime("%H:%M")
cnt=min(30,1+int((now-dt.datetime(2026,11,26,4,17,56,800000)).total_seconds()//1200))
oil_days=(1_200_000-579_400)/1536/24
head=f"""---
title: Daily report 2026-11-26 12:00Z - the halt closed, the five numbers, both definitions, oil, duel, plunder and calibration
created: 2026-11-26T11:55:00Z
modified: 2026-11-26T11:55:00Z
version: 1.0.0
description: Coach daily report with data to the stated time - the header with both coverage and sweep definitions, the closed halt, the five numbers for 11-25 12:00Z to 11-26 12:00Z, oil, duel, plunder, foreground, donations and calibration.
status: done
activity: coach
run_id: coach-2026-11-26-1200
trigger: the 12:00Z daily report
started_at: 2026-11-26T11:41:00Z
finished_at: 2026-11-26T11:55:00Z
duration_seconds: 840
verified: no
grounded_in:
  - source: productive-share-method.py and done-evidence-audit-method.py with --since 2026-11-25T12:00Z --until 2026-11-26T12:00Z; strategy_conformance.py; coverage-honest-method.py --cutover; the queue done folder; idle-blocked-audit.csv; confirm-episodes-table.csv; own-priors-scored.csv; the records of the day.
---

"""
body=f"""# Daily report, data to {hhmm}Z

**The halt, closed.** The pool did not run from 11-25 12:00Z to 04:20Z (16 h): the game showed *active on a different device* from 06:25:52Z (the owner's phone). Steer A took it under OD-05 and OD-17: Confirms 04:20:55Z (held 43.8 min), 05:41:10.9Z (5 min 13 s), 07:47:01.5Z (held at least 3 h 27 min, frames to 11:14Z); the owner has not answered. **Realized:** a late duel rescue was worth 8,020 to 17,550 tags, not 35,650 (the cadence's stake); two dispatches (about 16M) and the lab idle went with it.

**Header, both definitions.** *Coverage:* A (unit-hours since the 11-23 cutover) **66.8 percent** of 17.32 h (limit 60; the tool's 12 h window 61.8); B (income regulars mapped, looks exempt) 100 percent of 2.01 h (0.61 h exempt). *Zero sweep:* no sweep unit ran. No day is compared across definitions.

**Five numbers, 11-25 12:00Z to 11-26 12:00Z.** (1) Ranked partial rate **27.8 percent** (5 of 18; the tool's growth partial 28 percent). (2) DONEs with *state_change: no* carrying a valid state_read: **10 of 10**; 0 of 23 DONEs carry no key. (3) Productive share **72.4 percent of units** (21 of 29; baseline 36.8) and **70.6 percent of hours** (1.85 of 2.62 h; baseline 46.2). (4) Idle minutes: builders at most 1,546 of 5,760 (26.8 percent): **owner present (phone) 1,350**, window or decision waits 126, startable by us 70; training 2,830 blocked by room of 4,320; labs 0; waits 0.75 min. (5) State_change disagreement **0 of 5** hand-judged (95 percent bound 45).

**Oil (binding).** HUD 579.4K at 11:12Z (600.0K at 05:22Z: the phone's research restarts cost about 35K, H112 prior 0.80); gap to 1.2M about 621K, **{oil_days:.1f} days** at 1,536 an hour.

**Duel.** 11-26 *Train Heroes*, chests 40,000, 150,000, 540,000: Skill Medals about 21.2K x 25 = 530,000, so the top chest needs one UR shard (the plan's Thursday application decides). The radar grants no duel points today.

**Plunder.** 14 of 14 guarded fights, 0 wounded; days without a dispatch by us: 11 of the 13 days (11-26 has two); quota loss not shown by any source. Two secret-task plunders took a flat EXP 123.9K each.

**Standing line:** daily chest 160 of 200 today (the Drill Ground upgrade did *Upgrade a Building*), 150 on days without a build start; other rows cost stamina or are PvP.

**Foreground.** Prompt-type alerts: four (new at 10:29Z; 2 of 4 follow the daily 08:02Z helper install). Chrome for Testing 10:00:07.9Z: my 0.55 hit. cu nightly: a seat suite hold 11:26Z to 11:29:46Z, not a nightly run.

**Donations.** No pass ran; the count is **{cnt}** at {hhmm}Z, cap 30 at 13:57:57Z.

**IMP-02** (tram badge): rule v2 holds on three entries; v3 badge-first; the dispatch down-grade test stays n = 2 (posterior 0.46). **IMP-03:** none. **Calibration:** 144 items, mean log score -0.57 against -0.72.
"""
p="1155-daily-report-2026-11-26.md"
open(p,"w").write(head+body); print("body words:",len(body.split()))
