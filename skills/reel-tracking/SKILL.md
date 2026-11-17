---
name: reel-tracking
description: Log every posted reel with its real numbers and turn the log into lessons for the next script. Use after posting, when the user shares Insights numbers, or asks what they have learned from their recent reels.
---

# Reel tracking

A reel only teaches you something if its numbers are written down next to what you changed.

## The log
One row per reel in `reels.csv`:

`url, posted_at, idea, format, hook_type, length_sec, style, views_24h, views_7d, shares, saves, follows, notes`

- Numbers come from Instagram Insights, typed by the creator. Do not take them from a scrape: public likes and
  comments are not shares or follows.
- Leave a cell empty rather than guess.

## After each new row
1. Compare the reel to the account's median views (see outlier-finder) and to other reels with the same format
   and hook type.
2. Say what is different about this reel in one line.

## Lessons
- Write a lesson only when **three or more reels** support it. One or two is a hypothesis; label it that way.
- A lesson names the evidence (which reels) and what to do next time.
- If a new reel contradicts a lesson, say so and ask the creator whether to change or drop it.
- Keep lessons in `lessons.md`. Add or change one only after the creator says yes.

## Feed it back
Before writing the next script, read `lessons.md` and say which lessons the script follows or tests.
Never write "lesson 3 applied" without checking the script against it.
