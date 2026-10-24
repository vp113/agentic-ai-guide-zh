#!/usr/bin/env python3
"""Build the Chinese PDF with XeLaTeX + BibTeX on Windows, macOS, and Linux.

Usage:
    python build.py            # full build -> book.pdf + agentic-ai-guide-zh.pdf
    python build.py --clean    # remove intermediates and both PDFs
    python build.py --keep     # keep .aux/.toc as well; book.log/book.blg are always retained

Requires xelatex and bibtex on PATH (MiKTeX or TeX Live).
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAIN = "book"
BOOK_PDF = ROOT / f"{MAIN}.pdf"
DIST_PDF = ROOT / "agentic-ai-guide-zh.pdf"
BLG = ROOT / f"{MAIN}.blg"

INTERMEDIATES = [
    f"{MAIN}.aux", f"{MAIN}.log", f"{MAIN}.out", f"{MAIN}.toc",
    f"{MAIN}.fls", f"{MAIN}.fdb_latexmk", f"{MAIN}.synctex.gz",
    f"{MAIN}.blg", f"{MAIN}.bbl", f"{MAIN}.bcf", f"{MAIN}.run.xml",
    f"{MAIN}.xdv",
]
AUDIT_LOGS = {f"{MAIN}.log", f"{MAIN}.blg"}


def run(cmd: list[str]) -> None:
    print("+ " + " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)


def clean(remove_pdfs: bool = True) -> None:
    for name in INTERMEDIATES:
        (ROOT / name).unlink(missing_ok=True)
    if remove_pdfs:
        BOOK_PDF.unlink(missing_ok=True)
        DIST_PDF.unlink(missing_ok=True)


def ensure_tools() -> None:
    missing = [tool for tool in ("xelatex", "bibtex") if shutil.which(tool) is None]
    if missing:
        sys.exit(
            "Missing required tool(s): "
            + ", ".join(missing)
            + "\nInstall MiKTeX (Windows) or TeX Live (macOS/Linux) and retry."
        )


def check_bibtex_log() -> None:
    """Fail on BibTeX error summaries, matching the Makefile/CI gate."""
    if not BLG.exists():
        sys.exit("BibTeX did not produce book.blg")
    text = BLG.read_text(encoding="utf-8", errors="replace")
    match = re.search(r"There (?:was|were) ([1-9][0-9]*) error", text)
    if match:
        print(text, file=sys.stderr)
        sys.exit(f"BibTeX reported {match.group(1)} error(s); see book.blg")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build agentic-ai-guide-zh.pdf")
    parser.add_argument("--clean", action="store_true", help="remove intermediates and PDFs, then exit")
    parser.add_argument("--keep", action="store_true", help="keep .aux/.toc too; book.log/book.blg are always retained")
    args = parser.parse_args()

    if args.clean:
        clean(remove_pdfs=True)
        print("Removed build intermediates and PDFs.")
        return

    ensure_tools()
    clean(remove_pdfs=False)

    # Four XeLaTeX passes plus BibTeX: TOC, bookmarks, and citations settle.
    run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"{MAIN}.tex"])
    run(["bibtex", MAIN])
    check_bibtex_log()
    for _ in range(3):
        run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"{MAIN}.tex"])

    if not BOOK_PDF.exists():
        sys.exit("Build finished without producing book.pdf")
    shutil.copyfile(BOOK_PDF, DIST_PDF)

    if not args.keep:
        for name in INTERMEDIATES:
            if name in AUDIT_LOGS:
                continue
            (ROOT / name).unlink(missing_ok=True)
        # book.log/book.blg stay for the documented post-build audit.

    print(f"\nBuilt: {DIST_PDF}")


if __name__ == "__main__":
    main()
