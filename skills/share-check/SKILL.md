---
name: share-check
description: Check that a reel idea or script has a real reason to be sent to someone. Use before scripting or filming an idea, when the user asks "will anyone share this", or to audit a script for a vague audience, a weak send line or numbers the video never says.
---

# Share check

Sends carry a reel past the creator's own followers. An idea passes only if you can say **who** would send it,
**what they would type**, and **what fact they repeat** without the video.

## The block

Every idea carries:

```json
{"share": {
  "driver": "practical_utility",
  "recipient": "a teammate still writing regex by hand",
  "sendLine": "you didn't know this tool writes the regex for you?",
  "portableFact": "It turns a plain sentence into a tested regex in one step"
}}
```

- `driver` is one of: `social_currency` (looks smart or early), `practical_utility` (you need this),
  `relatability` (this is literally you), `perspective_flip` (changes a mind), `high_arousal` (awe, anger, laughter).
- `recipient` is a specific person, at least 3 words. Never "friends", "anyone", "followers".
- `sendLine` is the exact message they type, at least 4 words. "lol" and "check this out" do not count.
- `portableFact` is required for `social_currency`, `practical_utility` and `perspective_flip`.

## Check it in code

```
python scripts/share_check.py idea.json --script script.txt
```

It exits 1 and lists the problems. With `--script`, every number in `portableFact` must be said in the script.

## Rules
- Rewrite and re-run until it passes. Do not argue the block past the checker.
- A block that passes only says the idea is sendable, not that it is good. Still judge the topic.
- Do not invent a fact to pass: the portable fact must come from the research (see research-first-script).
