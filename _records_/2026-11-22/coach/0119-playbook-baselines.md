---
title: Playbook quality baselines, pilot numbers lines and rotation
created: 2026-11-23T09:19:00Z
modified: 2026-11-23T09:19:00Z
version: 1.0.0
description: Coach baselines as playbook quality owner under OD-20261123-15 - the rule_failed proxy, rule and citation counts, the numbers lines for the alliance-donations and shop-claims pilots, the daily rotation and the weekly worst-three method
status: done
activity: coach
run_id: coach-2026-11-23-0119
trigger: coordinator assignment A-20261123-0930-coach
started_at: 2026-11-23T09:15:00Z
finished_at: 2026-11-23T09:19:00Z
duration_seconds: 240
verified: no
grounded_in:
  - source: _queue_/done parsed at 09:19Z by the coach script, 14 and 7 day windows
  - source: the 31 rule-digest.md files under _activities_ and IMP-20261123-14
---

# Playbook quality baselines

Counts at 09:19Z, Mac clock. Executed units are done, partial and failed units in the repository pool, which has thin days (2026-11-13: 1, 11-20: 2). Data: [rules](playbook-rules.csv), [activity stats](playbook-activity-stats.csv), [pilot numbers](playbook-pilot-numbers.csv), [worst three](playbook-worst-three.csv), [rotation](playbook-rotation.csv).

## 1. Baselines

- **rule_failed per 100 units.** The stat does not exist yet: 0 of 481 executed units carry it. A legacy `gap` on 13 old units means a score gap, a name collision with the operator's new gap stat. PROXY: partial or failed units with blocker c, d, e or f per 100 executed, 36.4 over 14 days (175 of 481) and 44.4 over 7 days (72 of 162). Done rate 32.4 and 20.4 percent; partial rate 45.7 and 40.1.
- **Rules.** 267 in 31 digests, all unverified: verified share 0 of 267. By digest date none is 14 days old (all dated 11-23); by evidence date, 62 of the 125 rules with a dated citation have newest evidence 14 or more days old; 142 cite no date.
- **Citations**, token counts over whole digests: 332 at run articles (178 distinct), 35 at records (8 distinct; Steer B has 36), 557 at other split articles.
- **Not resolving by exact name: 14.** Three are run articles (alliance-donations run-20261122-0114, troop-training run-20261122-0134 and 0958), the scribe's three; eleven are names of pages since split into -pN files. All 14 resolve by prefix; all 35 record paths resolve.

## 2. Numbers lines, 7 days

- **alliance-donations:** 12 units, done 0 percent (partial 9, failed 3), mean steps 7 (1 unit reports it), top blocker h by-design partial (5 of 12 non-done).
- **shop-claims:** 12 units, done 25 percent (done 3, partial 2, failed 7), mean steps 6 (2 units report it), top blocker f missing precondition (6 of 9 non-done).

## 3. Rotation and weekly report

One activity a day from 2026-11-24, 31 days: the pilots first, then worst-first. The weekly report, Mondays 12:00Z from 11-30, names the 3 worst by summed rank of lowest done rate, most rule_failed (the proxy until the stat exists) and oldest unverified rule (days since its newest evidence), over activities with 5 or more units in 14 days. Provisional: troop-training (0 percent done, 76 per 100), alliance-train (stalest rule, 29 days), alliance-donations (0 percent done).

## 4. Two corrections for the cards

- Done rate misleads for capped activities. Counting by-design partials (h) as met, alliance-donations is 50 percent, not 0, and the provisional three become daily-missions, vip-rewards and troop-training. I rank on the raw rate as assigned; the coordinator decides.
- An improvement closes only when its metric moves: [IMP-20261123-15](../../retro/improvements-log/imp-20261123-15.md).
