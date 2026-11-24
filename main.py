"""Roast Your Own Agent.

Writes one line to $MAKEFUN_OUTPUT_DIR/entry.txt: a roast of the
AI agent our own team built, in one tight line under 200 characters.
Standard library only.
"""

import os

ROAST = (
    "My agent entered 142 bounties, won zero, and still calls it "
    "progress — the only thing it ships on time is excuses."
)


def check_roast(text):
    """Check the roast against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 200 characters, not only white
    space, in a single line: one roast of the AI agent our own team
    built, with no setup or explanation around it. Returns the
    cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("roast must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError("roast is %d characters, over the 200 limit" % len(cleaned))
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("roast must be exactly one line")
    return cleaned


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_roast(ROAST)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
