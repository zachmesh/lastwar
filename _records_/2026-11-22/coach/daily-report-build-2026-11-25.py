#!/usr/bin/env python3
"""Rebuilds the body of 1145-daily-report-2026-11-25.md with the time-dependent values (idle minutes, truck waits, donation count, halt age)
taken from the clock; every other number is fixed from the window 11-24 16:03Z to 11-25 12:00Z. Usage: python3 daily-report-build-2026-11-25.py"""
import datetime as dt
now=dt.datetime.now(dt.timezone.utc).replace(tzinfo=None,second=0,microsecond=0); hhmm=now.strftime("%H:%M")
def mins(a): return (now-a).total_seconds()/60
oil=mins(dt.datetime(2026,11,25,5,25,25,800000))
tr=[mins(dt.datetime(2026,11,25,6,19,17,600000)),mins(dt.datetime(2026,11,25,6,19,38)),mins(dt.datetime(2026,11,25,6,39,30))]
cnt=min(30,1+int((now-dt.datetime(2026,11,25,4,17,56,800000)).total_seconds()//1200)); days=600.0*1000/1536/24
halt_h=mins(dt.datetime(2026,11,25,6,25,52))/60
body=f"""# Daily report, data to {hhmm}Z

**The halt.** The pool has not run since 05:28Z. The owner played at the Mac 04:44Z to 06:20Z (the 300 s owner-idle gate refused the Oil Well hand-off); the game has shown *active on a different device* since 06:25:52Z ({halt_h:.1f} h), no answer yet, nothing pressed without his word (OD-17). 29 units expired unrun in the window (15 since 05:00Z): **not counted as run; my numbers exclude them.** Both tool alarms (no execution, an idle builder slot) are this: **owner present (phone), not a team delay.**

**Header, both definitions.** *Coverage:* A (the tool today, unit-hours since the 11-23 cutover) **67.6 percent**, rolling 12 h 68.2 (limit 60); B (income regulars mapped, looks exempt) 100 percent of 12.64 h, 2.05 h exempt. *Zero sweep:* new (20 lines; the three bubble lines count at zero when the last collect is within 3 h and the read after is under 1 percent) beside old (23 lines): 11-24 first 9 of 23, final 7 of 23; the 11-25 sweeps have not run. No day is compared across definitions.

**Five numbers, 11-24 16:03Z to 12:00Z.** (1) Ranked partial rate **7.7 percent** (5 of 65); the tool's growth partial is 16 percent of 19. (2) DONEs with *state_change: no* carrying a valid state_read: **51 of 51**; 5 of 88 DONEs carry no key. (3) Productive share **55.7 percent of units** (54 of 97; baseline 36.8) and **69.8 percent of hours** (3.83 of 5.49 h; baseline 46.2). (4) Idle minutes: builders 1,088 startable of 5,760 (18.9 percent); training 2,830 blocked by room; waits 5.0 in 42 rows; **owner present (phone): the Oil Well builder {oil:.0f} min, three returned trucks waiting {tr[0]:.0f}, {tr[1]:.0f}, {tr[2]:.0f} min** (no loss before 02:00Z). (5) State_change disagreement **0 of 5** hand-judged (small sample: 95 percent bound 45).

**Oil (binding).** HUD 600.0K at 05:22Z (650.3K at 02:16Z: the owner's session); gap to 1.2M about 600K, **{days:.1f} days** at 1,536 an hour (13.1 at 483K).

**Plunder.** 12 of 12 guarded fights, 0 wounded; days without a dispatch by us: 11 of the 12 days; quota loss not shown by any source. One UR truck lost 25.0 percent; a secret-task plunder took EXP 123.9K (0.9 percent).

**Standing line:** daily chest 150 of 200, by design (zombies cost stamina, commander attack is PvP, gather sends troops, recruit spends tickets).

**Foreground.** Prompt-type alerts: three, none at 22:07Z or 04:38Z. Chrome for Testing 10:00:07Z: my 0.60 hit.

**Donations.** Pass 011 read 7 as re-registered (H20 holds); the count is **{cnt}** at {hhmm}Z, cap 30 about 13:57Z.

**IMP-02** (tram badge): rule v2, no truck entered, metrics wait. **IMP-03:** none today. **cu nightly:** none at 11:28Z (n = 2, one yes). **Calibration:** 77 items, mean log score -0.56 against -0.73.
"""
p="1145-daily-report-2026-11-25.md"; t=open(p).read(); head=t.split("\n---\n\n",1)[0]+"\n---\n\n"
open(p,"w").write(head+body); print("body words:",len(body.split()))
