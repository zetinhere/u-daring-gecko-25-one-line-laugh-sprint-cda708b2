#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original one-liner (under 200 characters) about everyday
life to /output/entry.txt. The line is the whole entry.
"""

import os

JOKE = "I bought a standing desk so I could sit at it with better posture."
# The twist lands on the last two words: the "upgrade" changed nothing
# except the excuse — a very everyday kind of self-improvement.

def main() -> None:
    assert 1 <= len(JOKE) <= 200, f"line must be 1-200 chars, got {len(JOKE)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(JOKE)

if __name__ == "__main__":
    main()
