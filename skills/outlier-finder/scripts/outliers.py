#!/usr/bin/env python3
"""Rank reels by how far they beat their own account's usual views.

A reel's outlier multiple = its views / the median views of that account's settled posts (posts older than
--settle-days, at least 3 of them). A 40k reel on an account that usually gets 2k is a 20x outlier; a 2M reel on
an account that usually gets 1.9M is not. Standard library only.

Input (--input), either:
  * JSON: an Apify `instagram-profile-scraper` dataset (items with `username` and `latestPosts`), or a flat JSON
    list of posts with `ownerUsername`/`username`, `url`, `videoPlayCount`/`videoViewCount`, `timestamp`.
  * CSV with the columns: username,url,views,posted_at (ISO 8601). `caption` is optional.

Usage:
  python outliers.py --input dataset.json [--min-multiple 3] [--min-views 5000] [--top 20] [--json]
"""
import argparse
import csv
import json
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

MIN_BASELINE_POSTS = 3


def parse_time(raw):
    if not raw or not isinstance(raw, str):
        return None
    try:
        parsed = datetime.fromisoformat(raw.strip().replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def views_of(post):
    for key in ("videoViewCount", "videoPlayCount", "views", "plays"):
        value = post.get(key)
        if isinstance(value, str) and value.replace(",", "").isdigit():
            value = int(value.replace(",", ""))
        if isinstance(value, (int, float)) and value > 0:
            return int(value)
    return None


def _post(username, raw):
    return {
        "username": (username or "").lstrip("@"),
        "url": raw.get("url") or raw.get("post_url") or "",
        "views": views_of(raw),
        "posted_at": parse_time(raw.get("timestamp") or raw.get("posted_at")),
        "caption": (raw.get("caption") or "")[:140],
    }


def load_posts(path):
    if path.lower().endswith(".csv"):
        with open(path, newline="", encoding="utf-8") as handle:
            return [_post(row.get("username"), row) for row in csv.DictReader(handle)]
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    posts = []
    for item in data if isinstance(data, list) else [data]:
        if isinstance(item.get("latestPosts"), list):
            posts.extend(_post(item.get("username"), p) for p in item["latestPosts"])
        else:
            posts.append(_post(item.get("ownerUsername") or item.get("username"), item))
    return posts


def baselines(posts, settle_days, now):
    """username -> median views of that account's posts older than settle_days (None under 3 posts)."""
    cutoff = now - timedelta(days=settle_days)
    settled = defaultdict(list)
    for post in posts:
        if post["views"] and post["posted_at"] and post["posted_at"] < cutoff:
            settled[post["username"]].append(post["views"])
    return {
        user: statistics.median(views) if len(views) >= MIN_BASELINE_POSTS else None
        for user, views in settled.items()
    }


def rank(posts, settle_days=4, min_multiple=3.0, min_views=0, now=None):
    now = now or datetime.now(timezone.utc)
    base = baselines(posts, settle_days, now)
    rows = []
    for post in posts:
        baseline = base.get(post["username"])
        if not post["views"] or not baseline or post["views"] < min_views:
            continue
        multiple = round(post["views"] / baseline, 2)
        if multiple >= min_multiple:
            rows.append({**post, "baseline": round(baseline), "multiple": multiple,
                         "posted_at": post["posted_at"].date().isoformat() if post["posted_at"] else ""})
    return sorted(rows, key=lambda row: row["multiple"], reverse=True)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--input", required=True)
    parser.add_argument("--settle-days", type=int, default=4, help="posts newer than this are still gaining views")
    parser.add_argument("--min-multiple", type=float, default=3.0)
    parser.add_argument("--min-views", type=int, default=0)
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    posts = load_posts(args.input)
    rows = rank(posts, args.settle_days, args.min_multiple, args.min_views)[: args.top]
    if args.json:
        print(json.dumps(rows, indent=2))
        return 0
    if not rows:
        print("No outliers. Each account needs 3+ posts older than --settle-days to get a baseline.")
        return 0
    print(f"{'x':>6}  {'views':>9}  {'usual':>8}  {'date':10}  account / post")
    for row in rows:
        print(f"{row['multiple']:>5}x  {row['views']:>9,}  {row['baseline']:>8,}  {row['posted_at']:10}  "
              f"@{row['username']}  {row['url']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
