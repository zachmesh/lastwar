---
title: Playbook test T3 result 1511
created: 2026-11-23T15:20:00Z
modified: 2026-11-23T15:20:00Z
version: 1.0.0
description: Unit passes-playbook-t3-2026-11-23-001 - one foreground click on the check-in Go swiped the banner and brought Google Chrome to the front at 15:11:15Z; no in-game reward, so digest rule 9 is supported; closed needs-owner because focus did not return
status: needs-owner
grounded_in:
  - source: cu_bridge run 20261123T151100Z-91131b (frames step-0001 and step-0002, events and the consent request), 2026-11-23T15:11Z
  - source: a front-app log sampled every 0.5 s from 15:11:00Z, then by hand to 15:16:06Z
  - source: unit brief passes-playbook-t3-2026-11-23-001 and _records_/2026-11-22/research/checkin-go-test.md
---

# Playbook test T3 result

Rows in [1511-queue-run.csv](1511-queue-run.csv); one ledger row. Claimed 15:10:45Z; LastWar was frontmost and no different-device dialog showed.

- **Route.** The cart icon opens the shop on Official Event, which is itself the check-in page; there is no Hot Deals tab, so no tab tap was needed. Go was grounded from the screenshot at about (395,925).
- **The click.** **ONE** foreground click on Go at **15:11:14.951Z**, no second click. At once the banner moved to its second slide, "Claim points and redeem great rewards", POINTS 1000, with Go showing its click animation. **No reward popup, no Claimed state, no counter change.**
- **Focus lost.** The front log reads LastWar until 15:11:15 and **Google Chrome from 15:11:15**, still in front at 15:16:06 (4 min 51 s), unlike the self-recovering flash of 11-22. The harness raised a consent request (class new_app, Chrome) at 15:11:20.718Z. The operator did **not** answer it (human-only), stopped the run at 15:11:50.714Z (recorded as declined) and touched nothing in Chrome; the Chrome page was never looked at.
- **Verdict for the researcher.** Go does not pay in game and it opens the web store: digest rule 9 is **supported by one click** and not refuted. The +3 s screenshot of the test was never taken.
- **Needs-owner.** The card says the owner clicks the LastWar Dock icon. The operator asked the coordinator at 15:13Z whether to run `_tools_/mac_lastwar_front.sh` (osascript activate; no game input) and pressed nothing while waiting. Chrome may now sit on a purchase surface; it was not touched.
- **Run.** `claude-gateway/claude-sonnet-5-5`, 3 steps, 0.034873 USD against a stated cap of 0.5; nothing spent, nothing bought, no price, Renew or Take All tapped.
- **Closing state.** Chrome in front, LastWar behind it with the shop open on Official Event; token still held.
