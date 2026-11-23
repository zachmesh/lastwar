---
title: Missions, mail and alliance
created: 2026-11-23T08:37:49Z
modified: 2026-11-23T08:37:49Z
version: 0.1.0
sequence: 6
description: Daily activity chests - daily-missions.
---
### Missions, mail and alliance

14. **Daily activity chests** - daily-missions. The Mission
    panel is opened, the activity points total and every chest
    state are read live, completed tasks are claimed one by one
    with a re-check after each, and every reached chest is
    claimed. This line was unscheduled on both audited days -
    the type had metadata but no regular - and is a regular
    since the 2026-10-31 fix.
15. **Mail, six categories** - mail. Claim All per category; a
    category closes on its claimed list or on the live
    no-rewards answer. Mail that evidences an unworked source -
    the Glittering Market Unclaimed mail above all - is flagged
    to that source line, never counted as the source worked.
16. **Alliance gifts** - gifts. Claim All on the Regular and
    Premium tabs, closing counts read live.
17. **Alliance donations, 30 of 30** - donations. The daily
    target is the full 30 coin donations. Closes only on a live
    Donation Count read in the closing unit - the count is a
    remaining count, so done reads 0 remaining. The full rule,
    including the timer-hidden fallback, is in the
    alliance-donations metadata. Checkpoints under rule R3 of
    the queue design at six and two hours before the reset.

