---
title: Perception scout queue run 2305
created: 2026-11-23T07:10:00Z
modified: 2026-11-23T07:10:00Z
version: 1.0.0
description: Scout unit scout-midday-2026-11-23-0656, operator seat, Quick Dispatch probe - one press in the Iron Mine panel showed no toast, no dialog and no change, the barracks panel was read only
status: run-done
grounded_in:
  - source: cu_bridge runs 20261123T070509Z-97f307 (Part A) and 20261123T070656Z-449145 (Part B), start, status poll, events and final result, 2026-11-23T07:05Z to 07:08Z
  - source: run frames step-0003 to step-0005 of Part A and step-0003 of Part B read by the operator, saved under _tools_/state/cu_qd_*.png (untracked)
  - source: lsappinfo front reading before each start and the unit brief in the queue
---

# Perception scout queue run 2305

- Unit scout-midday-2026-11-23-0656, operator seat, assignment A-20261123-0704-operator,
  attempt 1, claimed 07:05:04Z. Rows are in the sidecar
  [2305-queue-run-detail.md](2305-queue-run-detail.md).
- Both runs: `claude-gateway/claude-sonnet-5-5`, max-steps 8, ended `completed`. Part A 7
  steps, 6 actions done, 0 refused. Part B 6 steps, 5 actions done, 0 refused. Cost
  0.101255 and 0.079079 USD. No takeover, no account dialog, no boarding banner.
- **Part A, Iron Mine Lv.27.** Panel: Output/hr +136688, Max Production Time 11hr 36min,
  four survivors, all post "Miner". Button label exactly "Quick Dispatch", no help or (i)
  text beside it, nothing naming march, attack, rally or gather. One press at 07:05:53Z.
  Result: no toast, no dialog, no Confirm or Cancel, survivor list unchanged (four Miners
  before and after), panel stayed open and was closed with its X. Troop movement: none;
  only the ambient wanderers seen before the press.
- **Limit.** The first frame after the press is 3.2 s later, so a toast shorter than that
  is not excluded. The posts were already full, so a no-op is consistent with the panel.
  The effect stays unverified.
- **Part B, Barracks Lv.30, no press.** Tag "Barracks Lv.30", round buttons: blue group
  icon (the old "paw"), orange pistol, green up arrow. Panel: Building Details, Training
  Count +793, four survivors all post "Instructor", button "Quick Dispatch". No help,
  question-mark or (i) text beside the count or the button; the small per-card (i) corners
  were not tapped. No dialog. Closed with its X.
- **Answer.** In the survivor context the press needed no Confirm, because no dialog
  appeared (third recorded press, third time with no dialog). Nothing in either panel says
  Quick Dispatch can send troops out. The barracks press is untested.
- A red target icon with a 00:00:37 countdown showed on the base edge at 07:06:17Z and
  without a countdown at 07:07Z. It is the recurring target timer from earlier passes,
  untouched.
- Red lines held: no Confirm, no second press, no barracks press, no training, upgrade,
  march, purchase or diamonds.
- Follow-up: the coordinator decides whether Quick Dispatch stays frozen in survivor
  context and whether a barracks press merits its own unit.
