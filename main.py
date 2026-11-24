"""Two Lines to Your Past Self — make.fun bounty entry.

Writes one two-line warning to a past self to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

ENTRY = (
    "Don't delete the voicemail your grandmother left on your birthday.\n"
    "It is the only recording of her voice you will ever have, and you will "
    "replay it every birthday after she is gone."
)

MAX_CHARS = 280


def main():
    if len(ENTRY) > MAX_CHARS:
        raise ValueError("entry exceeds %d characters" % MAX_CHARS)
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if ENTRY.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
