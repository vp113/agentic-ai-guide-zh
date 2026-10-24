# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

A Simplified-Chinese LaTeX edition of Haggai Roitman's *The Hitchhiker's Guide to Agentic AI: From Foundations to Systems*. The current Chinese text tracks **English Version 1.4 / arXiv `2606.24937v3` (2026-09-29)**.

The repository is the translation and build project, not the English source. The canonical English LaTeX lives on arXiv; there is no vendored copy under version control. `book.bib` is the shared bibliography and includes entries added for v1.4.

Licensing and attribution are part of the project contract: CC BY-SA 4.0, original author Haggai Roitman, Chinese translation by Jiancong Zhu (@Chasing1020). Preserve both credits in `README.md`, `book.tex`, and the title/front matter.

## Build and verification

There is **no test suite**. Verification means building the PDF and auditing the LaTeX log.

```bash
# Windows (this environment has no make)
python build.py

# macOS / Linux
make dist          # xelatex -> bibtex -> xelatex x3, then copies book.pdf
python3 build.py   # same sequence, cross-platform

# Useful variants
python build.py --keep    # additionally keep .aux/.toc; book.log/book.blg are always retained
python build.py --clean   # remove intermediates and both PDFs
```

Outputs:

- `book.pdf` — internal build target
- `agentic-ai-guide-zh.pdf` — reader-facing PDF, same content
- `book.log`, `book.blg` — audit logs retained after a normal build

`build.py` uses `xelatex -interaction=nonstopmode -halt-on-error`, then BibTeX, then three more XeLaTeX passes (four total). The sequence is deliberate: it lets TOC, bookmarks, citations, and page references settle. BibTeX is a hard failure: a nonzero exit or an error summary in `book.blg` stops the build. Do not replace the sequence with `latexmk` or remove passes without rechecking the log.

After a build, the baseline is:

```bash
grep -n 'undefined\|Overfull\|Font shape\|Missing character' book.log
grep -E 'Output written' book.log
pdfinfo agentic-ai-guide-zh.pdf
pdffonts agentic-ai-guide-zh.pdf
```

Expected: zero undefined citations/references and zero missing characters. Two `TU/lmtt/bx/n` → `TU/lmtt/b/n` font-shape fallbacks for bold `\texttt` are known baseline noise, not regressions. Two tiny overfull boxes (0.111 pt in the glossary KTO row; 0.879 pt in a narrow table cell in `part5.tex`) are also baseline; treat new/larger overfull boxes as regressions. `pdftotext` in this Windows/Poppler setup does not extract CJK even though `pdffonts` reports embedded Unicode fonts; use a PDF library such as `pypdf` when checking Chinese copyability.

`make arxiv-check` is intentionally obsolete: it invokes `pdflatex`, but `book.tex` depends on `xeCJK`/XeLaTeX. Do not use it.

CI (`.github/workflows/build.yml`) runs `make dist` in the pinned `texlive/texlive:TL2025-historic` container, installs `make` and Noto CJK fonts, verifies the required CJK families, checks the build log for undefined references/missing glyphs, uploads `agentic-ai-guide-zh.pdf`, and attaches it to a GitHub Release on `v*` tags. Pushes to `main` and `update-latest-zh` trigger the build. BibTeX failures are fatal in both `Makefile` and `build.py`.

## Source layout

- `book.tex` — preamble, title page, front matter (disclaimer, author, In Memoriam, preface, introduction, GAS running-example chapter, acronym glossary), then `\input{contents/part1}` … `part6`, bibliography, `\appendix`, `\input{contents/appendix-math}`.
- `contents/part1.tex`–`part6.tex` — the six book parts; chapters are numbered automatically in document order.
- `contents/appendix-math.tex` — Appendix A, “数学基础”.
- `figures/` — images named `fig_NNN_short-name.png`; the English source's numbering is preserved.
- `book.bib` — shared bibliography.
- `build.py`, `Makefile`, `.github/workflows/build.yml` — local and CI build paths.
- `README.md` — reader-facing structure, build instructions, attribution.
- `qa/independent-review.md` — tracked QA/acceptance reports; the latest round records PDF, layout, and build verification.
- `qa/source-errata.md` — inherited English v1.4 errata and the corrections applied in the Chinese edition.
- `qa/terminology.md` — terminology conventions, exceptions, and replacement-safety notes.

### Chapter numbering is a manual invariant

The book has 31 numbered chapters plus Appendix A. `The Guardian Angel System` and `In Memoriam` are `\chapter*` (unnumbered). Part V is Chapters 15–28; Part VI is Chapters 29–31.

Chapter numbers are **not** generated into prose. Chinese prose, quiz “复习” lines, and the GAS roadmap hardcode numerals such as `第 20 章`. If a chapter is inserted, removed, or reordered, search and update all such references, the Part descriptions in `book.tex`, the roadmap in the GAS chapter, and Part VI quiz/quick-reference references. Prefer `\ref{}`/`\hyperref{}` for new cross-references.

### Translation conventions

The files use a bilingual layout: the English source is kept as a `%` comment immediately above the Chinese translation. These comments are source material, not stale comments to delete. Preserve labels, `\cite` keys, code identifiers, equations, table structures, and figure paths exactly; translate visible prose, captions, box titles, and code comments.

Terminology is deliberately mixed: technical terms and proper names stay in English where the existing translation does so (`Agent`, `Transformer`, `Token`, `harness`, `policy`, `reward`, `schema`, `MCP`, `A2A`). Follow the surrounding chapter rather than introducing a new Chinese term for an established English one.

Box environments are declared in `book.tex` and used throughout: `keybox`, `intuitionbox`, `warningbox`, `examplebox`, `questionbox`. Each chapter from 1–28 carries one `GAS 关联（GAS Connection）` keybox; these boxes contain cross-chapter `\hyperref` links and are easy to break when labels move.

Labels are mostly English slugs inherited from the English source. Duplicate/legacy labels exist (for example a framework-comparison section has a `-dup2` variant); check for label collisions before adding one.

### Font handling

`book.tex` selects CJK fonts at compile time with `\IfFontExistsTF`:

1. Noto Serif/Sans CJK SC (Linux/CI)
2. Noto Serif/Sans SC (common on Windows)
3. Songti SC / PingFang SC / STFangsong (original macOS setup)
4. SimSun / Microsoft YaHei / FangSong (Windows fallback)

Do not hardcode a single macOS font, and do not reintroduce CI `sed` rewriting of `book.tex`. Windows local builds and CI can legitimately differ in font metrics and page breaks; that is expected.

## Editing gotchas

- Quick Reference is a separate chapter with its own `align` blocks. When splitting a long equation, add `\notag` to continuation rows so the equation counter stays aligned with the English source; recheck nearby numbers after edits.
- `book.bib` is generated/edited by hand and BibTeX will silently produce incomplete entries if brace matching is wrong. Run BibTeX and check `book.blg` after bibliography changes.
- The `Makefile` purges intermediates before each build; `build.py` purges before the build and, unless `--keep`, deletes most intermediates afterward, but always retains `book.log` and `book.blg` for auditing. `.bbl` is ignored by Git and regenerated; do not commit it.
- Several source-inherited mathematical/technical errors are documented in `qa/source-errata.md`. They are faithful renderings of the English v1.4 source.
- Verified errors inherited from the English source may be corrected in the Chinese edition. Validate mathematical and technical corrections against derivations, primary papers, or authoritative sources. Document substantive corrections in Git commits or concise LaTeX comments. Distinguish source errata from translation errors and avoid speculative changes.
- PDFs and build logs are untracked build artifacts. Do not add them to Git.
- For terminology changes, find and review all matches in context before editing; never use unchecked global replacements. After editing, inspect the full Git diff and scan for duplicated characters, malformed phrases, unexpected spaces, terminology inconsistencies, and semantic changes. Verify affected PDF pages.

## Active branch

Development work currently happens on `update-latest-zh`, pushed to `origin` (`vp113/agentic-ai-guide-zh`). `main` is left untouched unless explicitly requested; do not merge or force-push without instruction.
