#!/usr/bin/env python3
"""Check that an idea or script says who would send it and what they would type.

Sends carry a reel past the creator's followers, so every idea needs a share block:
  {"share": {"driver": ..., "recipient": ..., "sendLine": ..., "portableFact": ...}}

Usage:
  python share_check.py idea.json [--script script.txt]
Exit code 0 = passes, 1 = problems listed. With --script, every number in portableFact must be said in the script.
Standard library only.
"""
import argparse
import json
import re
import sys

DRIVERS = ("social_currency", "practical_utility", "relatability", "perspective_flip", "high_arousal")
FACT_DRIVERS = {"social_currency", "practical_utility", "perspective_flip"}

VAGUE_RECIPIENTS = {
    "friend", "friends", "anyone", "someone", "somebody", "people", "everyone", "everybody", "others", "peers",
    "followers", "audience", "viewers", "their friends", "their network", "colleagues", "a friend", "a peer",
    "a colleague", "other creators", "other people", "their followers",
}
WEAK_LINES = {
    "lol", "lmao", "nice", "wow", "omg", "so true", "this", "same", "check this out", "watch this", "look at this",
    "must watch", "you need to see this", "you have to see this", "this is cool", "this is so cool",
    "this is amazing", "this is useful", "so useful",
}
NUMBER = re.compile(r"\d[\d,]*(?:\.\d+)?")


def _norm(text):
    return re.sub(r"[^\w\s]", "", str(text or "")).strip().lower()


def problems(share, spoken_text=None):
    if not isinstance(share, dict):
        return ["share block missing: add share {driver, recipient, sendLine, portableFact}"]
    found = []
    driver = re.sub(r"[\s\-/]+", "_", str(share.get("driver") or "").strip().lower())
    if driver not in DRIVERS:
        found.append(f"driver {share.get('driver')!r} is not one of {', '.join(DRIVERS)}")

    recipient = _norm(share.get("recipient"))
    bare = re.sub(r"^(?:a|an|the|your|their|my)\s+", "", recipient)
    if len(recipient.split()) < 3 or recipient in VAGUE_RECIPIENTS or bare in VAGUE_RECIPIENTS:
        found.append(f"recipient {share.get('recipient')!r} is not a specific person: say who, with the "
                     "problem or trait that makes them the one you'd send it to")

    line = _norm(share.get("sendLine"))
    if len(line.split()) < 4 or line in WEAK_LINES:
        found.append(f"sendLine {share.get('sendLine')!r} is not a real send: write the exact message "
                     "they'd type, carrying the reason")

    fact = str(share.get("portableFact") or "").strip()
    if driver in FACT_DRIVERS:
        if len(fact.split()) < 4:
            found.append(f"portableFact is required for {driver}: the one concrete fact or number the "
                         "sender can repeat without the video")
        elif spoken_text is not None:
            spoken = spoken_text.replace(",", "")
            missing = [n for n in NUMBER.findall(fact) if n.replace(",", "") not in spoken]
            if missing:
                found.append(f"portableFact cites {', '.join(missing)} but the script never says it")
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("file")
    parser.add_argument("--script")
    args = parser.parse_args(argv)
    with open(args.file, encoding="utf-8") as handle:
        data = json.load(handle)
    share = data.get("share") if isinstance(data, dict) and "share" in data else data
    spoken = open(args.script, encoding="utf-8").read() if args.script else None
    found = problems(share, spoken)
    if not found:
        print("PASS")
        return 0
    print("FAIL")
    for item in found:
        print(f"  - {item}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
