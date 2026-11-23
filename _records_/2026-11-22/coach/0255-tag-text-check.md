---
title: Tag text check - building reads carry the tag they were read from
created: 2026-11-23T10:57:00Z
modified: 2026-11-23T10:57:00Z
version: 1.0.0
description: The conformance check for the building-read tag rule decided on Steer A's proposal - its definition, the baseline from the growth sidecar CSVs and who carries the rule into briefs and digests
status: done
activity: coach
run_id: coach-2026-11-23-0255
trigger: coordinator decision on Steer A's tag-text proposal
started_at: 2026-11-23T10:52:00Z
finished_at: 2026-11-23T10:57:00Z
duration_seconds: 300
verified: no
grounded_in:
  - source: the 12 reading CSVs under _records_/2026-11-22/growth, counted by the coach script
  - source: coordinator decision of 2026-11-23 on the tag-text rule
---

# Tag text check

**Rule.** Every read of a building records the tag text it was read from, the name and level shown above the building after the tap, next to every number taken from its panel. A number with no tag text is [G].

**Why.** Two tap-identity errors in one day: a hospital read as Barracks Lv.20, and a base map showing two grounds and no Lv.28 that the later read corrected to four grounds, parade fields and a Tavern inside the compound.

**Check (g) in the conformance report.** The share of building-read rows that carry their tag text. A building-read row is a row of a growth or scout sidecar CSV that names a building and carries a number taken from its panel. It carries the tag text when the row has the name and level as displayed, in a `tag_text` column once the briefs ask for it, and until then in the building field. A row without it is counted as [G].

**Baseline at 10:57Z.** 26 of 67 rows carry name and level, 39 percent, over 12 CSVs ([by file](building-read-tag-check.csv)). The best files are the 11-23 troop read (6 of 7), the Drill Ground read (5 of 6) and the base map (8 of 11). Six files carry none: the inventory, the stocks, two stores reads, the drone wall and the decoration read. The count is a proxy by name-and-level pattern, so a few non-building rows may enter it; the target is 100 percent.

**Who carries it.** The planner writes it into the unit briefs for every building read; the scribe writes it into the digests and the snapshot protocol; the operator records the tag text in each row; the coach counts the share in each report and names the CSVs below 100 percent.
