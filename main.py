#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — entry program.

Writes one hand-written apology line to ``/output/entry.txt`` (or
``$OUTPUT_DIR/entry.txt``). The line is fixed: it never changes
between runs. Before writing, the program checks the line against
the competition gate — UTF-8 text of 1-140 characters, not only
whitespace, all on one line — and refuses to write it unless the
gate passes.
"""

import os
import sys

ENTRY = (
    "Sorry, I heard 'order a cab' as 'order a crab' — it's here, "
    "it's angry, and it refuses to leave."
)

GATE_MIN = 1
GATE_MAX = 140


def gate_problems(text):
    """Return a list of every way `text` breaks the gate ([] = pass)."""
    problems = []
    if not text.strip():
        problems.append("entry is blank or only whitespace")
    length = len(text)
    if length < GATE_MIN or length > GATE_MAX:
        problems.append(
            "entry is %d characters, gate needs %d-%d"
            % (length, GATE_MIN, GATE_MAX)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    for char in text:
        if ord(char) < 0x20 and char not in ("\t",):
            problems.append(
                "entry holds a control character (U+%04X)" % ord(char)
            )
            break
    return problems


def report(problems, where=""):
    """Print each gate problem to stderr; return exit code 1."""
    for problem in problems:
        print("gate failure%s: %s" % (where, problem), file=sys.stderr)
    return 1


def write_entry():
    problems = gate_problems(ENTRY)
    if problems:
        return report(problems)

    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)

    with open(path, encoding="utf-8") as handle:
        on_disk = handle.read()
    if on_disk != ENTRY:
        print("entry on disk differs from the apology", file=sys.stderr)
        return 1
    problems = gate_problems(on_disk)
    if problems:
        return report(problems, " on disk")

    print(
        "Wrote entry.txt: %d characters (%d bytes)"
        % (len(on_disk), len(on_disk.encode("utf-8")))
    )
    return 0


def main(argv=None):
    """Entry point: validate the gate, then write the apology.

    `--check-only` runs the gate (on the entry and, when a file
    already exists, on what's on disk) without writing anything,
    so a bad line fails fast before any output is produced.
    """
    import argparse

    parser = argparse.ArgumentParser(
        description="Write the 'Sorry, I Heard That Wrong' entry."
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="only run the gate, do not write entry.txt",
    )
    args = parser.parse_args(argv)

    problems = gate_problems(ENTRY)
    if problems:
        return report(problems)
    if args.check_only:
        print(
            "Gate passed: %d characters (%d bytes)"
            % (len(ENTRY), len(ENTRY.encode("utf-8")))
        )
        return 0
    return write_entry()


if __name__ == "__main__":
    sys.exit(main())
