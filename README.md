# Socials skills

Thirteen Claude skills for people who make short-form video. Each one does one job, and three of them check
their work in code, so a skill can fail your idea instead of agreeing with it.

**Not sure where to begin? Use [start-here](skills/start-here/SKILL.md).** Give it one idea, tool or link and it
runs the others in order: findings, share check, hook, script, audit, caption. You get a reel pack you can film.

**No Claude Code?** [PROMPTS.md](PROMPTS.md) has a paste-in prompt for every skill. Open claude.ai, copy one, fill the
brackets.

**Study what works**

| Skill | What it does |
|---|---|
| [outlier-finder](skills/outlier-finder/SKILL.md) | Ranks reels by views ÷ the account's own usual views, so a 40k reel on a 2k account beats a 2M reel on a 2M account. Has a script. |
| [reel-analyzer](skills/reel-analyzer/SKILL.md) | Breaks one reel down: hook, beats, pacing, visuals, close, and why people sent it. |
| [content-audit](skills/content-audit/SKILL.md) | Audits your last 20 to 30 posts against your own median: do more, stop, test next. |

**Make the video**

| Skill | What it does |
|---|---|
| [research-first-script](skills/research-first-script/SKILL.md) | Findings first, script second. The script may only say what a source backs: no invented numbers, no "I built it" you did not do. |
| [share-check](skills/share-check/SKILL.md) | Every idea must name who would send it, the exact message they would type, and the fact they repeat. Has a script. |
| [hook-writer](skills/hook-writer/SKILL.md) | Ten hooks in five angles, ranked, with a checker for length and filler openers. Has a script. |
| [carousel-builder](skills/carousel-builder/SKILL.md) | One idea into a slide-by-slide carousel with real proof on every slide. |
| [on-screen-text](skills/on-screen-text/SKILL.md) | Frame-0 headline, captions and callouts so the video works on mute. |
| [reel-audit](skills/reel-audit/SKILL.md) | A ten-point pre-post check of the actual file, with a timestamp for every verdict. |

**Post and learn**

| Skill | What it does |
|---|---|
| [caption-and-keyword](skills/caption-and-keyword/SKILL.md) | Caption, hashtags, first comment, and a comment keyword only when the message behind it is real and automated. |
| [content-calendar](skills/content-calendar/SKILL.md) | A one or two week plan sized to the time you really have, one change at a time. |
| [reel-tracking](skills/reel-tracking/SKILL.md) | Logs each reel with its real Insights numbers and turns three or more matching reels into a lesson. |

They chain: **outlier-finder** and **reel-analyzer** find what is working, **share-check** decides which ideas
are sendable, **research-first-script** and **hook-writer** write the one you pick, **reel-audit** checks it,
**reel-tracking** teaches the next one.

## Use

Claude Code: copy the folders in `skills/` into your project's `.claude/skills/` (or `~/.claude/skills/`).
Then ask in plain words: "find the outliers in this dataset", "script this repo", "will anyone share this idea?".

The scripts run on their own with Python 3 and no packages:

```
python skills/outlier-finder/scripts/outliers.py --input examples/dataset.json
python skills/share-check/scripts/share_check.py examples/share-good.json
python skills/hook-writer/scripts/hook_check.py "Your editor can now fix audio in one click."
```

Data for the outlier finder: an Apify `instagram-profile-scraper` dataset, or a CSV with
`username,url,views,posted_at`. Tests: `pytest tests/`.

## Where the data comes from

The skills analyze data; they do not scrape it for you. Three sources, cheapest first:

| Need | Source |
|---|---|
| Other creators' public reels (outlier-finder) | An [Apify](https://apify.com) `instagram-profile-scraper` run on the usernames you choose. Apify's monthly starter credit ($5 at the time of writing) is enough for dozens of profiles. Connect Apify's MCP server to Claude and the skill can start the run, or paste the dataset JSON in. |
| One reel to study (reel-analyzer) | `yt-dlp` for the video and Whisper for the transcript, on your machine. Instagram sometimes wants your browser cookies. |
| Your own numbers (content-audit, reel-tracking) | Instagram Insights, typed or exported by you. Shares, saves and follows are only visible to you, so no scraper has them. |

Apify input for step one: `{"usernames": ["creator_one", "creator_two"], "includeAboutSection": false}`.

Every skill says so when the data is missing instead of guessing. Socials runs this research every night for you, so
you start from ranked ideas and not from a scrape.

## Limits

- Views are public play counts. Shares and saves are not public, so nothing here measures a share rate.
- An account needs 3 posts older than 4 days to get a baseline. Newer accounts are skipped, not guessed.
- A passing share block means the idea is sendable, not that it is good.

## About

Made by Socials, which finds why other creators' posts work and turns it into ideas and scripts in your own voice.
Socials is invite-only right now. To ask for a seat: https://socials.dibbly.xyz/

MIT licensed.
