#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day (make.fun).

Writes a single original roast line to /output/entry.txt.
Deterministic: stdlib only, no randomness, no time, no network.
"""

import os

ROAST = (
    "My smartwatch gives me a standing ovation for standing up, then says "
    "nothing when I sit back down \u2014 the world's tiniest fair-weather friend."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
