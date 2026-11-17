# Paste-in prompts (no Claude Code needed)

Using claude.ai or any chat? Copy the prompt for the job, fill the [brackets], paste. Each one follows the same
rules as its skill. Anything marked "needs data" says what to paste, and Claude must say so when it is missing.

## start-here: one idea to a reel pack
```
Make me a reel pack for: [tool / repo / link / idea]. Audience: [one line]. How I talk: [one line]. What I have
really done or can show on screen: [list]. Length: [30] seconds.
Do these in order and do not skip any:
1. Research from primary sources. Give a FINDINGS table: claim | source | how checked | date. Drop any claim with no
   source. If fewer than 3 survive, stop and tell me.
2. A share block: driver (social_currency / practical_utility / relatability / perspective_flip / high_arousal),
   recipient (a specific person, 3+ words), sendLine (the exact message they'd type, 4+ words), portableFact.
3. Ten hooks (14 words or fewer, payoff first). Pick one, keep two spares, and give the exact frame-0 picture.
4. The script in one breath, within the length. Every number must be in the findings. "I" only for what I said I
   did. A visual for every line, a new picture about every 3 seconds.
5. Caption, 3-5 hashtags, first comment. A comment keyword only if the message behind it really exists.
6. A "Film this" list and a "Not verified" list.
Do not invent numbers, results or assets.
```

## outlier-finder (needs data)
```
Here are recent reels as CSV: username,url,views,posted_at. [paste 15-30+ rows across several accounts]
For each account, take the median views of its posts older than 4 days (needs at least 3, else skip it and say so).
A reel's multiple = its views / that median. List reels at 3x or more, best first. For the top 5: the hook, why
people would send it, and what is reusable (the shape, never the lines). Say how many accounts and posts you used.
Do not claim share rates: they are not public.
```

## reel-analyzer (needs a transcript)
```
Here is the transcript of a reel with timestamps: [paste]. What was on screen at frame 0, 1s, 2.5s and the end:
[describe or attach screenshots]. Give: hook, beats with start times, pacing, what is on screen per line, the close,
why people would send it, and what is reusable. Mark every guess as a guess. Do not claim why viewers stayed or left.
End with "Steal the shape:" in one line, with no quoted lines.
```

## content-audit (needs your numbers)
```
Here are my last 20-30 posts from Insights: url, date, format, topic, hook type, views, shares, saves, follows.
[paste]. Ignore posts under 4 days old. Give my median views first. For each format/topic/hook type with 3+ posts,
give its median vs mine. Then: Do more of, Stop, Test next (one change at a time). Say how many posts you used.
Fewer than 3 in a group is an anecdote. No "X caused Y".
```

## research-first-script
```
Idea: [idea]. Audience: [one line]. Voice: [one line]. What I really did or can show: [list]. Length: [30]s.
First give a FINDINGS table: claim | source | how checked | date. Drop unsourced claims. Then the script in one
breath, 14-word hook, every number from the table, "I" only for what I did, a visual per line, one honest ask.
End with claims_check: each number and each "I" line mapped to its finding. Cut anything you can't map.
```

## share-check
```
Here is my idea: [idea]. Write the share block and judge it:
driver (one of social_currency, practical_utility, relatability, perspective_flip, high_arousal),
recipient (a specific person, 3+ words, never "friends"), sendLine (4+ words, the exact message they'd type,
never "check this out"), portableFact (one concrete fact they can repeat without the video; needed for
social_currency, practical_utility, perspective_flip). Say PASS or FAIL for each part and rewrite until it passes.
Do not invent the fact.
```

## hook-writer
```
Topic: [topic]. Findings I can use: [facts]. Write 10 hooks in 5 angles, 2 each: result, surprise, cost, viewer's
problem, contrarian. 14 words or fewer, payoff first, one sentence, no "hey guys" / "in this video" / "did you know".
Give the top 3 with the exact frame-0 picture. Use no number that is not in my facts.
```

## carousel-builder
```
Idea: [idea]. Facts: [findings]. Make an 8-slide carousel: slide 1 the promise (8 words or fewer), slides 2-6 one
idea each with what real screenshot goes on it, slide 7 the main objection answered with a fact, slide 8 one ask.
Max 25 words a slide. Give a table: slide | text | what's on it | source. Add alt text. No number without a source.
```

## on-screen-text
```
Here is my script with timing: [paste]. Write the on-screen text: a frame-0 headline (6 words or fewer), captions in
chunks of 1-3 words timed to the voice, and callouts that appear when the line is said. Keep text in the middle of a
1080x1920 frame (not the top ~250 px or bottom ~420 px). Table: time | spoken | caption chunks | callout. Flag any
stretch over 3 seconds with no change on screen.
```

## reel-audit (describe the actual cut)
```
Audit my reel. Here is what it does second by second: [describe or paste transcript + notes on visuals]. Give PASS /
FIX / WAIVE with a timestamp for each: 1 frame 0 moving, 2 frame 0 carries the claim, 3 first word within ~0.5s,
4 claim by ~1.5s, 5 one idea, 6 picture changes about every 3s to match the line, 7 text large and in the middle,
8 every number true and sourced, 9 one ask that is really delivered, 10 clear audio at about -14 LUFS. Then the 3
fixes that matter most. If you can't tell from what I gave you, say so.
```

## caption-and-keyword
```
Reel: [what it says]. Goal: [comments and messages / reach]. Write a caption (line 1 is the hook, 2-4 short lines,
one ask), 3-5 hashtags and a first comment. Use a comment keyword ONLY if this is true: [the automated message
exists, is tested, and contains: ___]. If not, use a save or send ask instead. Say exactly what the automated
message will contain.
```

## content-calendar
```
I can make [N] posts a week with about [X] minutes each. Formats I can do: [list]. Approved ideas: [list with their
share blocks]. Plan [1/2] weeks. Do not repeat a topic or hook type back to back, cap a topic at 3 posts, change one
thing at a time against my recent posts, and mark which need my face. Table: date | format | idea | hook | share
driver | what to film | keyword or none | the one thing being tested. Never plan more than I said I can make.
```

## reel-tracking
```
Here is my reel log (url, posted_at, idea, format, hook_type, length_sec, views_24h, views_7d, shares, saves,
follows, notes): [paste]. For the newest reel, compare it to my median and to reels with the same format and hook
type, in one line. Propose a lesson only if 3 or more reels support it; otherwise label it a hypothesis. Name the
reels as evidence. Do not change my lessons file without my yes.
```
