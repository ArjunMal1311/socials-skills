---
name: research-first-script
description: Write a short-form video script that only says what research backs. Use when the user gives a tool, repo, link, topic or idea and wants a reel script, or asks for a script with no made-up numbers, no invented experience and no assets that do not exist.
---

# Research-first script

The flow is **idea, research, script**, never idea, script. The creator says every line as themselves, so the
script may only contain what the research backed. Scripts written straight from an idea invent percentages,
"I built / I ran" experience and assets ("I put it all in a doc") that do not exist.

## Step 1: findings (before any script)

Write a FINDINGS block. Each row is one claim:

| Claim | Source (url or "ran it myself") | How checked | Date |
|---|---|---|---|

- Claims come from a primary source: the docs, the repo, the product page, or a run the creator really did.
- A number with no row here cannot appear in the script.
- If you cannot verify a claim, leave it out. Do not soften it into "reportedly".
- First person ("I found", "I ran") is only for what the creator did. Ask what they actually ran. Third person
  ("someone just built X") is fine when the source confirms it.

## Step 2: the share block

Fill `{driver, recipient, sendLine, portableFact}` from the findings, then run the share-check skill. Do not
write the script until it passes.

## Step 3: the script

- One run-on breath the creator can say in one take. Default 30 seconds, 105 words at most (3.5 words a second);
  use the length the user gives.
- Hook: one sentence, 14 words or fewer, payoff or surprise first, the tool named after it.
- Then: what it does in one line, 2 to 4 concrete steps, one counted number from the findings, one close.
- Plain spoken words and contractions. No stat lists, no staged "Let me show you".
- A visual cue next to each sentence (what is on screen), a new picture about every 3 seconds, readable text
  at frame 0.
- Close with one ask. Name only a link or thing that really exists. No link yet = "Follow for more".

## Step 4: audit before handing it over

Return JSON with `findings`, `script`, `share`, and `claims_check`: every number and every "I" sentence in the
script mapped to its findings row. Any line you cannot map is cut or rewritten. Say how many words and how many
seconds the script is.

## Rules
- Never copy another creator's lines. Model their structure, write your own words.
- No assets that do not exist, no results the creator did not get.
- If research turns up that the tool does not do what the idea says, say so and drop or change the idea.
