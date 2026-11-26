---
title: Mail: Event and Alliance Claim All paid nothing, Mail dot cleared 1150
created: 2026-11-26T11:58:26Z
modified: 2026-11-26T11:58:26Z
version: 1.0.0
description: Unit mail-2026-11-26-0230 (version 1.0.366(908); front LastWar at the start 11:50:34Z; the different-device dialog never on screen; no UserNotificationCenter; owner gate: the second run was refused at 11:51:45Z because this Mac had local input 49 s earlier (a person at the Mac about 11:50:56Z): HOLD, read-only polling until idle 316 s at 11:56:12Z, then the run started at 11:56:45Z with idle 349 s) - FIRST FRAME (11:50:41.3Z; Warzone Duel timer 14:09:20): the tram icon bare; the MAIL button with a red dot; HUD: food 48.6M, iron 682.7M, coin 14.6M, diamonds 10,673; THE MAIL RAIL (the envelope (670,785)): Battle Report (no mark), Alliance (a gift icon), Event (a gift icon), System (none), Regular (a red dot), In-app Purchases (a red dot), Favorite (none); THE EVENT LIST (read twice, not scrolled): six rows, all unread before: an ally's 'Mega Ex...' mail 1h ago, an ally's 'train has ...' mail 1h ago, an ally's 'train...' mail 3h ago, an ally's 'Mega Exp...' mail 5h ago, an ally's 'train...' mail 5h ago, 'Code 87 Individual Reward' 6h ago (already read): NO mail titled 'Train arrival reward!', 'UNCLAIMED ARMS RACE EVENT' or 'GLITTERING MARKET UNCLAIMED' in the visible rows (the list below the sixth row was not scrolled: unread); no gift icon or green Claim on any row; the buttons Delete All, Claim All, Search; CLAIM ALL pressed ONCE on the Event list (553,932) at 11:56:54.7Z: no popup, the rows turned read (greyed, open envelopes); the HUD unchanged (food 48.6M, iron 682.7M, coin 14.6M): nothing paid; CLAIM ALL pressed ONCE on the Alliance list (553,932) at 11:57:18.6Z: the list (Daily Donation Rankings, Alliance Exercise, three New Alliance Marker mails, more) all read, no popup, nothing paid; the REGULAR list (390,575): Victory reports 'Lv.30 Doom Elite' 4h to 8h ago, no gift icon: Claim All NOT pressed; Delete All, Read All, mail rows and the In-app Purchases list never pressed; the Mail screen left by its back arrow (113,934), no TIPS popup; THE MAIL BUTTON'S RED DOT CLEARED: absent on the base at 11:58:10.4Z (it showed a dot at 11:50:41.3Z); HUD at 11:58:10Z: food 48.6M, iron 682.7M, coin 14.6M, diamonds 10,673 (unchanged); the tram icon bare; drags 0; the claims named by the unit (the Train arrival reward, the Arms Race unclaimed mail, the Glittering Market row quote) could not be worked: the mails are not in the visible Event rows
status: done
grounded_in:
  - source: cu_bridge run 20261126T115645Z-43afd0, final report read by the operator, 2026-11-26T11:50Z to 11:58Z
  - source: unit brief mail-2026-11-26-0230 and the mail-rewards rule digest
---

# Mail: Event and Alliance Claim All paid nothing, Mail dot cleared 1150

Rows in [1150-queue-run.csv](1150-queue-run.csv). Claimed 11:50:34Z; no different-device dialog.

- **Owner gate.** A person used the Mac about 11:50:56Z: the next start was refused at 11:51:44Z (idle 48 s); read-only polling until idle 316 s (11:56:12Z); the run started at 11:56:45Z.
- **Event list.** Six rows (an ally's Mega Exp and train mails, Code 87): none is 'Train arrival reward!', 'UNCLAIMED ARMS RACE EVENT' or 'GLITTERING MARKET UNCLAIMED'; no gift icon on a row; the list was not scrolled.
- **Claim All once** on the Event list and once on the Alliance list: no popup, nothing paid (HUD unchanged: food 48.6M, iron 682.7M, coin 14.6M, diamonds 10,673); the mails turned read.
- **The Mail button's red dot cleared** (dot at 11:50:41.3Z, gone at 11:58:10.4Z). Regular (Victory reports) has no gift icon: not pressed. Delete All never pressed; drags 0.
- **Run.** One run, 24 steps, 13 actions, 0.305127 USD, cap 0.5; 0 refused; foreground stayed LastWar.
- **Closing state.** The base, no panel; token released 11:58:19Z.
