"""Real-Life Patch Notes: The Comedy Changelog.

Writes the chosen one-line patch note to /output/entry.txt.
Pure stdlib, Python 3.13.
"""

import os

ENTRY = "v1.9.3: fixed a bug where the human brain filed every embarrassing memory under 'urgent' and replayed it at 3 a.m."


def validate(line: str) -> str:
    """Return the line if it passes the entry gates, else raise.

    Explicit checks instead of assert, so validation still runs
    under `python -O`, where assert statements are stripped.
    """
    if not line:
        raise ValueError("entry must not be empty")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 160:
        raise ValueError(f"entry is {len(line)} chars, over the 160 limit")
    return line


def main() -> None:
    line = validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
