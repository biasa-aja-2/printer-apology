"""The Printer Apology.

A sarcastic apology in the printer's own voice: it owns the jam, then lists its real grievances — discount paper, swearing, and the demand for colour — with the punch landing on the last word. Fresh angle: the printer apologises while indicting its users.
Pure stdlib, no network, no secrets.
"""

import os
import sys

LINE = 'Sorry I jammed again — you fed me discount paper, swore at me in three languages, and still expected colour.'


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    # MAKEFUN_OUTPUT_DIR may be a directory or a file path.
    if out_dir.endswith(".txt"):
        path = out_dir
        directory = os.path.dirname(path) or "."
    else:
        directory = out_dir
        path = os.path.join(directory, "entry.txt")
    os.makedirs(directory, exist_ok=True)

    # Self-check gate: 1-120 chars, single line, not whitespace-only.
    if not (1 <= len(LINE) <= 120):
        sys.exit("gate failed: length %d not in 1..120" % len(LINE))
    if LINE.strip() == "":
        sys.exit("gate failed: line is whitespace-only")
    if "\n" in LINE or "\r" in LINE:
        sys.exit("gate failed: line is not a single line")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        sys.exit("gate failed: not exactly one sentence")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)

    # Byte-exact read-back verification.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != LINE:
        sys.exit("verification failed: read-back differs from LINE")
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
