"""The Dog Ate My Homework: Funniest Excuse — make.fun bounty entry.

Writes one excuse line (62 chars) to entry.txt in
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
deterministic: the same bytes on every run.

The line turns the oldest excuse in history inside out: the dog ate
the homework on purpose, so that the kid's excuse would finally be
true. The dog is not sorry — it believes it did the kid a favour,
and says so with a smug "You're welcome."
"""

import os
import sys

ENTRY = (
    "I ate it so your excuse would finally be true. "
    "You're welcome."
)


def main():
    line = ENTRY
    if not line or not line.strip():
        sys.exit("entry line is blank")
    if "\n" in line or "\r" in line:
        sys.exit("entry line must be a single line")
    if not 1 <= len(line) <= 199:
        sys.exit("entry line must be 1-199 characters, got %d" % len(line))
    if line != line.strip():
        sys.exit("entry line must not start or end with whitespace")
    if not line.endswith("You're welcome."):
        # The punch is the dog taking credit for the favour: it must
        # never silently go missing from the line.
        sys.exit("entry line must end with the smug You're welcome.")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = line.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Re-read and verify the file is exactly the gated line, no newline.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        sys.exit("entry.txt does not match the gated line")
    print("wrote %s (%d chars, %d bytes)" % (path, len(line), len(data)))


if __name__ == "__main__":
    main()
