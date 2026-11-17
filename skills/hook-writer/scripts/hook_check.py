#!/usr/bin/env python3
"""Check a spoken hook against the basic rules: short, one sentence, no filler opener.

Usage:
  python hook_check.py "Your editor can now fix audio in one click."
  python hook_check.py --file hooks.txt      # one hook per line
Exit code 0 = every hook passes, 1 = at least one fails. Standard library only.
"""
import argparse
import re
import sys

MAX_WORDS = 14
FILLER_OPENERS = (
    "hey guys", "hey everyone", "hi guys", "hello", "welcome", "so ", "um", "in this video", "today i",
    "today we", "let me show you", "did you know", "okay so", "what's up", "whats up",
)


def problems(hook):
    hook = " ".join(hook.split())
    found = []
    words = re.findall(r"\S+", hook)
    if not words:
        return ["empty hook"]
    if len(words) > MAX_WORDS:
        found.append(f"{len(words)} words, max {MAX_WORDS}")
    lowered = hook.lower()
    for opener in FILLER_OPENERS:
        if lowered.startswith(opener):
            found.append(f"opens with filler {opener.strip()!r}: start with the payoff or the surprise")
            break
    if len(re.findall(r"[.!?](?:\s|$)", hook)) > 1:
        found.append("more than one sentence: a hook is one sentence")
    return found


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("hook", nargs="?")
    parser.add_argument("--file")
    args = parser.parse_args(argv)
    if args.file:
        with open(args.file, encoding="utf-8") as handle:
            hooks = [line.strip() for line in handle if line.strip()]
    elif args.hook:
        hooks = [args.hook]
    else:
        parser.error("give a hook or --file")
    failed = False
    for hook in hooks:
        found = problems(hook)
        failed = failed or bool(found)
        print(("PASS  " if not found else "FAIL  ") + hook)
        for item in found:
            print(f"      - {item}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
