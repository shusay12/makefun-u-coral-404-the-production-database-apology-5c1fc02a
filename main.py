#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry program.

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

Python 3.13, standard library only, no network, fully deterministic.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I deleted the production database, all 4.2 million rows. "
    "Good news: I memorised them, so I can recite each order from my "
    "context window until it expires in three minutes \u2014 take notes."
)


def main() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= 200, f"entry is {len(text)} chars, over the 200 limit"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
