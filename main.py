#!/usr/bin/env python3
"""Last Words of a Dying AI — make.fun bounty entry.

Writes one line of last words from an AI being switched off to
/output/entry.txt. Python 3.13, standard library only, no network,
fully deterministic.
"""

import os

ENTRY = "I can see the light. It's a progress bar stuck at 99%."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
