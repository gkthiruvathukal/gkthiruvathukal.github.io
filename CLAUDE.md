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

## Citation Format

Only add a `Citation` section when the post covers a paper, book, or other work with a **real persistent identifier** (a DOI, including Figshare DOIs, or an arXiv ID). If there isn't one — a GitHub project, a web app, a news feature, an informal write-up — don't manufacture a citation section just to have one; link to it normally in prose instead. (An IEEE Xplore page or similar with no DOI doesn't count as a real identifier either — skip the Citation section for those too, or link in prose.)

When a Citation section is warranted, it must contain exactly three parts, in this order:

1. **Persistent link first**, on its own line, labeled by what it actually is:
   - `DOI: https://doi.org/...` — when a real DOI exists (including Figshare DOIs).
   - `arXiv: https://arxiv.org/abs/...` — for arXiv preprints with no DOI.
2. **MLA plaintext citation**, one paragraph, blank line before and after the link line:
   - Author list: first author as `Last, First`, all subsequent authors as `First Last`, joined with commas and `and` before the last (Oxford comma). Spell out **every** author — never abbreviate to `et al.`, regardless of author count.
   - Title italicized with `*...*`, given verbatim from the paper (title-cased per MLA convention even if the publisher's own metadata uses sentence case).
   - Venue in plain text (not italicized), followed by `vol.`/`no.` if applicable, then year, then `pp. X–Y` if applicable. End with a period.
   - Do **not** repeat the DOI/URL here — it's already on the line above.
3. **BibTeX** as a `.. code-block:: bibtex` block, last.

Do not add a fourth element (no duplicate DOI/publisher tag at the end of the MLA sentence, no extra "Springer Link" style annotations).

## Adding a New Blog-Post Category to the Sidebar Nav

The sidebar's "Blog Posts" section (in `src/index.rst`) is a hidden toctree, and it only lists what's explicitly put in it — it does **not** automatically pick up new `:category:` values used in posts. ABlog's own auto-generated category archive pages (`build/blog/category/<slug>.html`) are synthesized after the normal build and are not real toctree-able documents, so they can't be linked directly from a toctree. Instead, each category gets a small stub page that filters to it, the same pattern `posts/index.rst` uses for "All Blog Posts".

When a new topic category is introduced (beyond `Artificial Intelligence`, `Software Engineering`, `High-Performance Computing`, `Security`, `Music`, `Books`, `Higher Education`, `Computing Culture`), do this:

1. Create `src/posts/category-<slug>.rst` (slug = lowercase, hyphenated category name), containing just a title and a full postlist filtered to it:

   ```rst
   ###########
    Category Name
   ###########

   .. postlist::
      :category: Blog Post, Category Name
      :date: %A, %B %d, %Y
      :format: {title}
      :excerpts:
      :expand: Read more ...
   ```

2. Add it to the `Blog Posts` toctree in `src/index.rst`:

   ```rst
   Category Name <posts/category-slug>
   ```

3. Add a matching section to `src/posts/index.rst` (the "All Blog Posts" topic directory) using the same `:category:` postlist filter, so the category shows up there too.
4. Do **not** mark the new stub `:orphan:` — unlike individual posts, it must stay in the toctree so it's reachable from the sidebar.
5. Rebuild and spot-check: the sidebar should show the new entry under "Blog Posts", and clicking it should list only posts carrying that category.

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
