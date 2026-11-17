---
name: outlier-finder
description: Find the reels in a niche that beat their own account's usual views, then explain why they worked. Use when the user wants viral reels to learn from, "what is working in my niche", outliers, a watchlist of creators, or gives a scraped dataset or CSV of posts and asks which ones to study.
---

# Outlier finder

A reel is an outlier when its views are far above **that account's own usual views**, not when the raw number is
big. A 40k reel on an account that usually gets 2k (20x) tells you more than a 2M reel on an account that always
gets 2M. This skill ranks posts by that multiple, then studies the top few.

## Step 1: get the posts

Any of these works:
- An Apify `instagram-profile-scraper` dataset (JSON) for 20 to 100 creators in the niche. Ask the user for the
  usernames. If the Apify MCP server is connected, run the actor with
  `{"usernames": [...], "includeAboutSection": false}` and save the dataset to a file; say the run's cost first.
  If it is not connected, tell the user to connect it (an Apify account with its monthly credit is enough) or to paste a dataset file.
- A CSV with `username,url,views,posted_at`.

Do not guess usernames. If the user has no list, ask for 5 creators they already watch and start there.

## Step 2: rank

```
python scripts/outliers.py --input dataset.json --min-multiple 3 --min-views 5000 --top 20
```

- The usual views of an account = the median of its posts older than 4 days, and it needs at least 3 such posts.
  An account with fewer gets no baseline and is skipped: say so instead of ranking it.
- Posts newer than 4 days are still gaining views, so they are scored against the older posts but never used to
  set the baseline.

## Step 3: study the top 5

For each, watch or read the reel and write, in this order:
1. **Hook**: the first sentence and what is on screen at frame 0.
2. **Why it spread**: what a viewer would send it for (see the share-check skill).
3. **What is portable**: the topic, the shape or the angle you can reuse. Never the lines, never the footage.

End with a short table: account, multiple, hook, portable idea. Flag any outlier on an account under about 1,000
followers as noisy.

## Rules
- Public play counts only. Shares and saves are not public, so never claim a share rate from this data.
- Say how many accounts and posts the ranking is based on, and the date of the scrape.
- One outlier is a sample of one. A pattern needs three or more outliers that share it.
