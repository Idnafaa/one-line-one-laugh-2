#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes exactly one funny line to /output/entry.txt.
Standard library only; no network, no input files.
"""

LINE = (
    "My smartwatch congratulated me on burning 400 calories today; "
    "380 of them were reaching for the remote."
)


def main() -> int:
    # Enforce the bounty gate ourselves before writing: one line,
    # 1-200 characters, not only whitespace, no trailing whitespace.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line is {len(text)} chars, must be 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be exactly one line")
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
