#!/usr/bin/env python3
"""Flag STE sheet violations in a markdown document.

The check ignores fenced code blocks. It counts inline code as one word.
Numbered steps use the procedural limit (20 words). Other sentences use the
descriptive limit (25 words). A descriptive paragraph may have 6 sentences.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

FILLERS = (
    "it is important to note",
    "it should be noted",
    "please note that",
    "as well as",
    "the fact that",
    "keep in mind",
)

# Unapproved word from the STE sheet, and the approved alternative.
UNAPPROVED = (
    (re.compile(r"\bin order to\b"), "to"),
    (re.compile(r"\bprior to\b"), "before"),
    (re.compile(r"\bcommenc\w*"), "start"),
    (re.compile(r"\bensur\w*"), "make sure"),
    (re.compile(r"\breplenish\w*"), "fill"),
    (re.compile(r"\butiliz\w*"), "use"),
    (re.compile(r"\bapproximately\b"), "about"),
    (re.compile(r"\bit is imperative\b"), "a direct command"),
)

FENCE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE = re.compile(r"`[^`\n]+`")
SENTENCE_END = re.compile(r"(?<=[.!?])\s+")
NUMBERED_STEP = re.compile(r"^\d+\.\s+(.*)$")
BULLET = re.compile(r"^[-*]\s+")
PARAGRAPH_LIMIT = 6


def visible_text(markdown: str) -> str:
    return FENCE.sub(" ", markdown)


def word_count(sentence: str) -> int:
    stripped = INLINE_CODE.sub(" code ", sentence)
    return len(stripped.split())


def sentence_parts(text: str) -> list[str]:
    return [part.strip() for part in SENTENCE_END.split(text) if part.strip()]


def check(markdown: str, max_words: int = 25, procedure_max: int = 20) -> list[str]:
    findings: list[str] = []
    visible = visible_text(markdown)
    lowered_lines = visible.lower().splitlines()

    for line_number, line in enumerate(lowered_lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        for filler in FILLERS:
            if filler in stripped:
                findings.append(f"filler:{line_number}: {filler}")
        for pattern, alternative in UNAPPROVED:
            match = pattern.search(stripped)
            if match:
                findings.append(f"unapproved:{line_number}: {match.group(0)} -> {alternative}")

    for line_number, line in enumerate(visible.splitlines(), start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        step = NUMBERED_STEP.match(stripped)
        bullet = BULLET.match(stripped)
        if step:
            body = step.group(1)
            limit = procedure_max
        elif bullet:
            body = stripped[bullet.end() :]
            limit = max_words
        else:
            body = stripped
            limit = max_words
        for sentence in sentence_parts(body):
            count = word_count(sentence)
            if count > limit:
                findings.append(f"too-long:{line_number}: {count} words: {sentence}")

    findings.extend(long_paragraphs(visible))
    return findings


def long_paragraphs(visible: str) -> list[str]:
    findings: list[str] = []
    block: list[tuple[int, str]] = []

    def flush() -> None:
        if not block:
            return
        text = " ".join(line for _, line in block)
        count = len(sentence_parts(text))
        if count > PARAGRAPH_LIMIT:
            start = block[0][0]
            findings.append(f"paragraph:{start}: {count} sentences")
        block.clear()

    for line_number, line in enumerate(visible.splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            flush()
            continue
        if (
            stripped.startswith("#")
            or NUMBERED_STEP.match(stripped)
            or BULLET.match(stripped)
        ):
            flush()
            continue
        block.append((line_number, stripped))
    flush()
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Markdown file to check")
    parser.add_argument("--max-words", type=int, default=25, help="Maximum words in a descriptive sentence")
    parser.add_argument("--procedure-max", type=int, default=20, help="Maximum words in a numbered step")
    args = parser.parse_args()

    if args.max_words < 1 or args.procedure_max < 1:
        print("limits must be at least 1", file=sys.stderr)
        return 2

    try:
        markdown = args.path.read_text(encoding="utf-8")
    except OSError as error:
        print(f"cannot read {args.path}: {error}", file=sys.stderr)
        return 2

    findings = check(markdown, args.max_words, args.procedure_max)
    if not findings:
        print("ok")
        return 0

    print("\n".join(findings))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
