#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, in the dog's own voice, to /output/entry.txt.
The dog does not apologise: it solved the problem by removing it.
"""
import os

LINE = "I ate the homework so the teacher can't mark it wrong. Problem solved, and I already ate the detention slip too."


def main():
    # The gate counts every character in the file: one line, no trailing
    # newline, plain ASCII so bytes == characters.
    text = LINE.strip()
    assert text == LINE, "entry must already be a single clean line"
    assert 1 <= len(text.encode("utf-8")) <= 200, "entry must be 1-200 bytes"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
