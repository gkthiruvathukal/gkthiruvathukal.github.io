# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

A personal/academic blog for George K. Thiruvathukal, built with **Sphinx + ABlog**. Content is written in reStructuredText (`.rst`). The site is deployed to GitHub Pages at `gkt.sh`.

## Commands

```bash
make serve        # Live-reloading local dev server (sphinx-autobuild)
make build        # Full production build (sphinx-build --fresh-env)
make clean        # Remove build/ directory
make create-dev   # First-time setup: install pre-commit hooks + uv sync
```

Package manager is **uv**. Python 3.13 required. After cloning, run `make create-dev`.

## Architecture

- `src/conf.py` — Sphinx configuration (extensions, ABlog settings, BibTeX files, theme)
- `src/posts/` — Blog posts as `.rst` files (ABlog manages archives, feeds, tags)
- `src/pages/` — Static pages (about, works, funding, prospective-students)
- `src/drafts/` — Excluded from build via `exclude_patterns` in `conf.py`
- `src/bibliography/` — BibTeX files (`gkt-journal.bib`, `gkt-inproceedings.bib`, etc.) loaded by `sphinxcontrib.bibtex`
- `src/_static/` — Custom CSS (`custom.css`), images, favicon
- `tools/get-zotero-bibtex.sh` — Fetches `.bib` files from Zotero API (run by CI before build)
- `data/zotero-bibs.txt` — List of Zotero group URLs for the fetch script

## Creating a New Post

Create a `.rst` file in `src/posts/` with this frontmatter at the top:

```rst
:blogpost: true
:date: Month DD, YYYY
:category: Blog Post, Topic Category One, Topic Category Two
:tags: Tag One, Tag Two, Venue Acronym
:nocomments:

:bdg-primary:`Blog Post` :bdg-primary-line:`Tag One`

Post Title
==========
```

- `:category:` is a list: keep `Blog Post` (used by site-wide postlist filters) plus one or more topic categories (e.g., `Artificial Intelligence`, `Software Engineering`, `Music`) — these drive ABlog's auto-generated category archive pages.
- `:tags:` holds finer-grained, content-specific tags plus the publication venue acronym (e.g., `EMSE`, `ICSE`, `MSR`) when the post covers a paper. Chronological browsing comes from ABlog's built-in year archives (based on `:date:`), not from a tag — don't add a date-formatted tag.
- `:nocomments:` suppresses the comment section.
- Badge directives (`:bdg-primary:`) come from `sphinx_design`.
- Footnote-style citations (`.. [1]`) are used for inline references; BibTeX citations use `sphinxcontrib.bibtex` syntax for academic references.

## Key Extensions

| Extension | Purpose |
|-----------|---------|
| `ablog` | Blog post routing, archives, RSS feed |
| `sphinxcontrib.bibtex` | Academic citations from `.bib` files |
| `sphinx_design` | Badge/card/grid directives |
| `sphinx_togglebutton` | Collapsible content |
| `sphinxcontrib.youtube` | Embed YouTube videos |

## CI/CD

`.github/workflows/build.yml` runs on push to `main`:
1. Downloads fresh BibTeX from Zotero via `tools/get-zotero-bibtex.sh`
2. Builds with `sphinx-build`
3. Adds `CNAME` file (`gkt.sh`)
4. Deploys to GitHub Pages via `actions/deploy-pages`

## Linting

Pre-commit hooks (`.pre-commit-config.yaml`) run `ruff` (format + check), `isort`, and `bandit` on Python files. Config is in `ruff.toml` (line length 88). Run `pre-commit run --all-files` to check manually.
