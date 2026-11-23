---
title: Secret missions queue run 0050
created: 2026-11-23T08:55:00Z
modified: 2026-11-23T08:55:00Z
version: 1.0.0
description: Secrets unit secrets-2026-11-23-0742, operator seat, the 4-hour UR task Capture the Oil Depot claimed about 8 seconds after the first Post frame, nothing plundered, popup tiles read
status: run-done
grounded_in:
  - source: cu_bridge start, status poll, events and final result on run 20261123T085051Z-a6cd12, 2026-11-23T08:50Z to 08:51Z
  - source: frames step-0002.png (CONGRATULATIONS popup) and step-0004.png (Your Tasks after the claim) read by the operator, the first saved as _tools_/state/cu_secrets_0050.png (untracked)
  - source: earlier claim record 2248-queue-run.md for the 06:51Z comparison
---

# Secret missions queue run 0050

- Unit secrets-2026-11-23-0742, operator seat, assignment A-20261123-0850-operator,
  attempt 1, claimed 08:50:49Z. Rows in the sidecar
  [0050-queue-run-detail.md](0050-queue-run-detail.md).
- Run `20261123T085051Z-a6cd12`, model `claude-gateway/claude-sonnet-5-5`, max-steps 8,
  ended `completed` after 6 steps. Actions done 10, refused 0. Model time 5.8 s per step.
  Cost 0.083334 USD. No takeover. The first frame was the base: no account dialog, no
  boarding banner, no loading screen.
- Route: the jeep tap at 08:50:59Z opened SECRET COMMAND POST on the first try, already on
  Your Tasks. UR Capture the Oil Depot showed a green Claim button on the first Post frame.
  One Claim tap at 08:51:08Z paid it. Nothing was plundered.
- **Popup tiles (the 4-hour UR task):** Iron 3.2M, Food 3.2M, Black Market Cash 40,
  Mystery Supply Box 67, Oil 6.0K x5 (30K), Treasure Map Fragment #5 x2, #2 x2, #4 x1,
  Hero EXP 4.1M. The first dismiss tap did not close it; a second tap in empty space did.
- **Against the 06:51Z claim** (the 2-hour UR task): that paid Resource Chest 300 and
  Upgrade Ore 800; this one paid raw iron and food and oil instead, and Fragment #5.
- **Black Market currency:** Black Market Cash +40 is the only balance seen; the account
  total was not read. The box count rises to about 366 (299 read at 08:13Z plus 67).
- After the claim: UR Capture the Oil Depot, UR Rescue Missing Agent and both SSR Train
  Refugees carry PERFECT, no Claim button. Assist Allies 5/5, Plunder Others 0/5. The red
  badge moved from Your Tasks to Hidden Treasures, not opened.
- Redeploy: Mega Refresh and Mega Deploy stayed greyed, so nothing was sent. Cards below
  the fourth were not read (no scrolling).
- Closing state: the base, no panel. HUD not re-read.
- Red lines held: no Plunder, diamonds, purchase, Mega or Go button.
- Follow-up: the next Secret Missions chance needs the idle-slot state; Mega Deploy
  greyed means no task is waiting to send.
