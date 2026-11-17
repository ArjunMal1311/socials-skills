import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/outlier-finder/scripts"))
sys.path.insert(0, str(ROOT / "skills/share-check/scripts"))

sys.path.insert(0, str(ROOT / "skills/hook-writer/scripts"))

import hook_check  # noqa: E402
import outliers  # noqa: E402
import share_check  # noqa: E402


def test_hook_check():
    assert hook_check.problems("Your editor can now fix audio in one click.") == []
    assert hook_check.problems("Hey guys, today I want to show you something that I found yesterday afternoon.")
    assert len(hook_check.problems("One two three four five six seven eight nine ten eleven twelve "
                                   "thirteen fourteen fifteen.")) == 1

NOW = datetime(2026, 11, 17, tzinfo=timezone.utc)


def post(user, views, day):
    return {"username": user, "url": f"https://x/{user}/{day}", "views": views, "caption": "",
            "posted_at": datetime(2026, 11, day, tzinfo=timezone.utc)}


def test_outlier_is_scored_against_own_median():
    posts = [post("small", 2000, d) for d in (1, 2, 3)] + [post("small", 40000, 15)]
    posts += [post("big", 2_000_000, d) for d in (1, 2, 3)] + [post("big", 2_100_000, 15)]
    rows = outliers.rank(posts, now=NOW)
    assert [r["username"] for r in rows] == ["small"]
    assert rows[0]["multiple"] == 20.0


def test_account_with_under_three_settled_posts_has_no_baseline():
    posts = [post("new", 1000, 1), post("new", 1000, 2), post("new", 90000, 15)]
    assert outliers.rank(posts, now=NOW) == []


def test_load_apify_profile_dataset(tmp_path):
    data = tmp_path / "d.json"
    data.write_text('[{"username":"a","latestPosts":[{"url":"u","videoPlayCount":5000,'
                    '"timestamp":"2026-11-01T10:00:00.000Z"}]}]')
    posts = outliers.load_posts(str(data))
    assert posts[0]["username"] == "a" and posts[0]["views"] == 5000


GOOD = {"driver": "practical_utility", "recipient": "a teammate still writing regex by hand",
        "sendLine": "you didn't know this writes the regex for you?",
        "portableFact": "It turns a plain sentence into a tested regex in 1 step"}


def test_good_share_block_passes():
    assert share_check.problems(GOOD) == []


def test_vague_share_block_fails():
    bad = {"driver": "practical_utility", "recipient": "friends", "sendLine": "check this out",
           "portableFact": ""}
    assert len(share_check.problems(bad)) == 3


def test_fact_number_must_be_spoken():
    assert share_check.problems(GOOD, "it does it in 1 step") == []
    assert share_check.problems(GOOD, "it does it fast")
