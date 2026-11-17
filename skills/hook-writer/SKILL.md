---
name: hook-writer
description: Write the first one to three seconds of a short-form video. Use when the user needs hooks for a reel, wants to fix a weak opening, or asks for ten options ranked. Includes a checker for length and filler openers.
---

# Hook writer

The hook is the first sentence the viewer hears and the first picture they see. It has one job: make a stranger
stay for the next three seconds.

## Inputs
The idea and its share block (see share-check), plus the findings (see research-first-script). The hook may only
use facts from the findings.

## Write ten, in five angles (two each)
1. **Result**: the outcome first ("I turned a 2-hour edit into 4 minutes").
2. **Surprise**: something that should not be true, and is.
3. **Cost**: a cheaper replacement for something paid, or what it saves in money or time.
4. **Viewer's problem**: the exact situation they are in right now.
5. **Contrarian**: a mild disagreement with what the niche believes. Never an insult.

## Rules
- One sentence, 14 words or fewer, payoff or surprise first, the tool named after it.
- Say something a person could repeat. No "Did you know", no "In this video", no "Hey guys".
- The picture at frame 0 must already be moving and must carry the same claim as the words, so it works on mute.
- No made-up numbers. A number in the hook needs a row in the findings.

## Check them
```
python scripts/hook_check.py --file hooks.txt
```
Drop any hook that fails. Rank the rest: put first the one a stranger would stop for, and say in one line why.
Give the top three with the exact frame-0 picture for each.
