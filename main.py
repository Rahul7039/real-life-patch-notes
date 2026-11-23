"""Real-Life Patch Notes: The Comedy Changelog.

Writes the chosen one-line patch note to /output/entry.txt.
Pure stdlib, Python 3.13.
"""

import os

ENTRY = "v1.9.3: fixed a bug where the human brain filed every embarrassing memory under 'urgent' and replayed it at 3 a.m."


def main() -> None:
    line = ENTRY
    assert line, "entry must not be empty"
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert len(line) <= 160, f"entry is {len(line)} chars, over the 160 limit"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
