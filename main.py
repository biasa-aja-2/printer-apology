"""The Printer Apology.

The one-line apology note an office printer writes to the people who
keep jamming it, feeding it cheap paper and swearing at it.

Why this line: the printer owns the jam, then lists its real grievances
-- discount paper, swearing in three languages, and still being asked
for colour -- with the punch landing on the last word. A sarcastic
apology that indicts its users, not a grovelling one, and a fresh angle:
no "out of paper" or "PC LOAD LETTER" joke, no self-pity.
Pure stdlib, no network, no secrets.
"""

import os
import sys

LINE = "Sorry I jammed again \u2014 you fed me discount paper, swore at me in three languages, and still expected colour."
# One sentence only: the em dash carries the pause, so the gate's
# exactly-one-sentence rule still holds and the punch stays at the end.


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
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)

    # Byte-exact read-back verification.
    with open(path, "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != LINE:
        sys.exit("verification failed: read-back differs from LINE")
    print("wrote %d chars to %s" % (len(LINE), path))


if __name__ == "__main__":
    main()
