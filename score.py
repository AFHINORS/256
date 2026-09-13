#!/usr/bin/env python3
"""Grade one local solution folder.

    python3 score.py challenge.b64 /path/to/your/repo
"""

from __future__ import annotations

import sys
from pathlib import Path

import evaluate


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        sys.stderr.write("usage: score.py challenge.b64 /path/to/your/repo\n")
        return 2
    evaluate.CHALLENGE = Path(argv[1]).resolve()
    sol = Path(argv[2]).resolve()
    if sol.is_file():
        sol = sol.parent
    row = evaluate.grade(sol)
    print()
    if row["status"] != "ok":
        print(f"  status       {row['status']}")
        print(f"  code         {row['code']:,} bytes")
        print(f"  time         {row['time']:.1f}s")
        print()
        return 1
    print(f"  compressed   {row['compressed']:,} bytes")
    print(f"  code         {row['code']:,} bytes")
    print(f"  SCORE        {row['score']:,} bytes")
    print(f"  time         {row['time']:.1f}s")
    print("  round trip   OK")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
