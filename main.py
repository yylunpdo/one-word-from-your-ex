#!/usr/bin/env python3
"""One Word From Your Ex — make.fun bounty entry.

Writes exactly ONE word to /output/entry.txt: the word my ex would use
to describe me. Pure Python stdlib, no dependencies.
"""

import os

# The word: "unreachable" — funny at first (always busy, always away),
# then brutally honest: the reason it ended. No calls returned,
# no plans kept, just... unreachable.
WORD = "unreachable"


def main():
    word = WORD.strip()
    assert " " not in word, "entry must be a single word"
    assert word.isalpha() and word.islower(), "entry must be one lowercase word"
    assert 1 <= len(word) <= 20, "entry must be 1-20 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word + "\n")


if __name__ == "__main__":
    main()
