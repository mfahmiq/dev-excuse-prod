#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line excuse a developer gives when code breaks
in production to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Deterministic, Python standard library only. Self-verifies the gate
before writing: UTF-8 text, 1-200 characters, a single line, and not
only whitespace. Exits non-zero on any failure.
"""

import os
import sys

ENTRY = "My code works perfectly \u2014 it's production that keeps running it in front of witnesses."


def main() -> int:
    # Validate the entry against the competition gate.
    if not ENTRY:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if ENTRY.strip() == "":
        print("error: entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(ENTRY) > 200:
        print(
            "error: entry is %d characters, over the 200 limit" % len(ENTRY),
            file=sys.stderr,
        )
        return 1

    # Encoding check: must be valid UTF-8.
    try:
        data = ENTRY.encode("utf-8")
    except UnicodeEncodeError as exc:
        print("error: entry is not valid UTF-8: %s" % exc, file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    out_path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)

    # Read back and confirm the file holds exactly the entry.
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != data:
        print("error: written file does not match the entry", file=sys.stderr)
        return 1
    if written.decode("utf-8") != ENTRY:
        print("error: round-trip decode mismatch", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (out_path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
