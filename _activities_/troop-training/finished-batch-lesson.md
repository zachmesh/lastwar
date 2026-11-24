---
title: Troop training finished batch lesson
created: 2026-11-24T04:15:43Z
modified: 2026-11-24T04:18:34Z
version: 0.2.0
description: The dated lesson of 2026-11-24 - a Drill Ground Full toast does not mean idle, because a finished batch can wait behind it; one pistol press per barracks per read when room could exist
---

# Troop training finished batch lesson

Dated 2026-11-24, from the Coach's audit (`_records_/2026-11-22/coach/idle-blocked-audit.csv`) and evidence (`_records_/2026-11-22/coach/1215-partial-collect-evidence.md`).

## The rule

Press the pistol once per barracks per read whenever room could exist. The toast "Drill Ground Full" at room 0 fits both an empty queue and a finished batch, so a read classifies each barracks as EMPTY QUEUE, FINISHED BATCH WAITING (with its size) or BLOCKED BY THE TOAST in this read, and records the ready bubble and its digits per tent. A toast alone is never "idle". A collect admits what fits and leaves the rest waiting [D].

## The precedents

On 2026-11-10 (12:29 PT, `_records_/2026-11-10/troop-training/1229-queue-run.md`) the pistol collected the finished Lv.24 batch, and on 2026-11-22 (10:05 PT, `_records_/2026-11-22/arms-race/1005-queue-run.md`) a finished batch of 143 Lv.8. The 11-23 schema wrote "idle, blocked", and the card's entry of 2026-11-09 (day-20261031-p2) called Lv.27 "idle and blocked" from the toast alone: the card taught the wrong inference ([errata](errata.md)).

## The case of 2026-11-23

A Lv.24 barracks held a finished batch of 274 (+291,262) under four "idle, blocked" reads, and a Lv.27 one held 726. Room was 0 until the siege freed it: the cost is the delay after room opened, 120 and 99 minutes, nothing permanent.

## The batch sizes [D]

Nobody queued the 274: Lv.24 was requeued T8 x666 on 11-10, 143 were collected on 11-22, about 523 remained, and 274 is exactly the room left after the 726 (1,000 - 726). So about 249 T8 (+264,687) probably still wait. It was not the owner's phone.

## Open

Registered before the data: 2026-11-26T21:10:37Z, one pistol press on Lv.24 collects 200 (+212,600, toast "200 Lv. 8 units are ready") and leaves 49; all-or-nothing predicts a refusal. Until then read digits of about 249 beside the Lv.24 tent. The Lv.30 tap at 11:18Z with room 0 is not informative: both models refuse.
