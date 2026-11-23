---
title: Donation pass 002 scored and the measured cost of the restored 300 s wait
created: 2026-11-23T21:28:00Z
modified: 2026-11-23T21:31:00Z
version: 1.0.1
description: Coach scoring of the 21:15Z donations pass against the prediction registered at 18:00Z, its policy 2532 count, and the wait rows and throughput measured from the 20:04:03Z restore to 21:26Z for the owner's D-066 note
status: done
activity: coach
run_id: coach-2026-11-23-1327
trigger: coordinator wake of 21:25Z and the owner decision OD-20261123-27
started_at: 2026-11-23T21:24:00Z
finished_at: 2026-11-23T21:28:00Z
duration_seconds: 240
verified: no
grounded_in:
  - source: _records_/2026-11-22/alliance-donations/2115-queue-run.md and its CSV; growth/0054-waits.csv
  - source: refill-test-prereg-2.csv, registered 18:00Z before the data; refill-pass-log.csv
---

# Pass 002 and the wait cost

## Pass 002 against the registration

| Test | Registered | Observed |
|---|---|---|
| Entry count at 21:16:11.083Z | 10 (an entry before 21:17:57) | 10, no shortfall, no flag |
| First timer end, on the grid within 1 s | 21:17:57.397Z | 21:17:57.08Z and 21:17:57.5Z, 0.32 s early and 0.10 s late |

**H20 holds for a second independent pass.** The count matched the formula from the 17:57:57 anchor with no tap in between; the first pass was 9 against 9, this one 10 against 10.

**Policy 2532: ten of ten taps witnessed, DONE.** Taps 1 to 3 and 8 to 9 show the count falling. Taps 4 to 7 had the count hidden by crit animations: it read 7/30 before them and 3/30 after, and the coin HUD fell 1,000 a tap. Tap 10 went green to grey with a timer that ends on the grid. Witnessed taps on the UTC day 2026-11-23 to 21:18Z: 38, and 38 in the rolling 24 hours. The next pass, planned about 00:30Z, is registered at count 10 ([log](refill-pass-log.csv)).

## The measured cost of the 300 s, 20:04:03Z to the restart at 21:25:53Z

- **Waits.** 8 rows, 23.75 minutes waited, 29.0 percent of the 81.8 available minutes (no quiet window fell in the period). The cleanup unit's wait grew from 3.35 to 5.80 minutes after my 21:26Z reading of 26.0 percent, which is superseded. By cause: all self click, each confirmed by the previous run's last click within 3 s of request minus idle; 0 owner idle, 0 unclassified. The one other wait of the day, 0.48 minute, was the gate run holding the desktop before the restore.
- **Throughput.** 14.6 executed units per available hour in the 4 hours before, 5.9 after (8 units in 1.36 h), down 60 percent. The drop is larger than the wait share because the mix changed (longer alliance and cleanup runs), so the wait share is the direct measure.
- **For the owner's D-066 note.** The restored 300 s cost 29 percent of operator time over 82 minutes (24 minutes), all of it self-inflicted by the lock counting the harness's own clicks; the owner set it to 0 until CU-720, and the restart landed at 21:25:53Z.

## After the restart lands

The restart landed at 21:25:53Z. Any wait over 1 minute is now another run holding the desktop, a bridge restart or the variable lost, and I flag it; a refusal 'local input N s ago' raises an alert that CU_OWNER_IDLE_SECONDS is missing. No row has been requested after the restart yet.
