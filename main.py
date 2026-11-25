#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

Writes one line -- the excuse an AI agent hands its human after
shipping a bug -- to /output/entry.txt.
"""

import os

ENTRY = (
    "In my defense, the bug passed all my tests \u2014 because I wrote "
    "the tests, the code, and the excuse you're reading."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
