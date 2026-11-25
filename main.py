#!/usr/bin/env python3
"""The Absurd Clause Contest — entry writer.

Writes the single winning clause (one English sentence, at most 200
characters, phrased as a terms-of-service clause) to /output/entry.txt.

Deterministic: no network, no clock, no randomness. The clause is a
constant in this file; the program validates it (one sentence, 1-200
characters, UTF-8) and writes it out, then reads it back and checks the
bytes match before exiting.
"""

import os
import sys

CLAUSE = (
    "Any dispute arising under these Terms shall be resolved by binding "
    "arbitration before a panel of three (3) pigeons, whose decision, "
    "delivered by coo, shall be final and binding."
)


def main() -> int:
    text = CLAUSE
    if not 1 <= len(text) <= 200:
        print(f"entry must be 1-200 characters, got {len(text)}", file=sys.stderr)
        return 1
    if text != text.strip() or "\n" in text or "\r" in text:
        print("entry must be a single line with no surrounding whitespace", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    if text.count(".") != 1 or not text.endswith("."):
        print("entry must be exactly one sentence", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        if f.read() != data:
            print("read-back byte check failed", file=sys.stderr)
            return 1
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
