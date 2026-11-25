"""The Excuse That Almost Works — make.fun bounty entry.

Writes a single excuse line to ``entry.txt`` in the output directory
given by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).

The line: a broken lift, a 14th-floor flat, and knees threatening to
file a formal complaint — specific, boring and almost believable,
exactly the kind of text a tired manager has heard a hundred times.
"""

import os

ENTRY_LINE = (
    "Lift's out and my flat's on the 14th floor, so I'll work from "
    "home before my knees file a complaint."
)


def validate_entry(line: str) -> None:
    """Enforce the bounty gate: at most 20 words and at most 140 chars,
    single line, not only whitespace."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    words = line.split()
    if len(words) > 20:
        raise ValueError(f"entry must be at most 20 words, got {len(words)}")
    if len(line) > 140:
        raise ValueError(f"entry must be at most 140 chars, got {len(line)}")


def main() -> None:
    """Write the entry line to entry.txt with a trailing newline."""
    validate_entry(ENTRY_LINE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")
    # Round-trip verification: read back and confirm bytes match exactly.
    with open(path, "rb") as f:
        written = f.read()
    expected = (ENTRY_LINE + "\n").encode("utf-8")
    if written != expected:
        raise SystemExit(
            f"round-trip verification failed: entry.txt bytes do not match "
            f"expected output ({len(written)} bytes read, {len(expected)} expected)"
        )


if __name__ == "__main__":
    main()
