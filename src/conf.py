"""
Sphinx configuration file.

Copyright (C) 2025 George K. Thiruvathukal.
"""

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "George K. Thiruvathukal's Blog"
copyright = "2025, George K. Thiruvathukal"  # noqa: A001
author = "George K. Thiruvathukal"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "ablog",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_togglebutton",
    "sphinxcontrib.bibtex",
    "sphinxcontrib.youtube",
]

templates_path = ["_templates"]
exclude_patterns = ["drafts/*", "archive/*"]

# Ablog configuration options
blog_authors = {
    "NMS": ("George K. Thiruvathukal", "https://gkthiruvathukal.github.io/"),
}
blog_default_author = "NMS"
blog_languages = {
    "en": ("English", None),
}
blog_default_language = "en"
post_show_prev_next = False
blog_title = "George K. Thiruvathukal's Blog"
blog_feed_fulltext = True

# Sphinx auto section label settings
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

# Sphinx BibTex settings
bibtex_bibfiles = [
    "bibliography/gkt-magazine.bib",
    "bibliography/gkt-misc.bib",
    "bibliography/gkt-incollection.bib",
    "bibliography/gkt-journal.bib",
    "bibliography/gkt-inproceedings.bib",
    "bibliography/gkt-books.bib",
    "bibliography/gkt-theses.bib",
    "bibliography/gkt-techreport.bib",
]

bibtex_default_style = "unsrt"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# Add ABlog's browsing widgets (tag cloud, categories, archives, recent
# posts) to the sidebar on blog pages only, alongside the theme's default
# nav/search templates.
html_sidebars = {
    "posts/**": [
        "navbar-logo.html",
        "icon-links.html",
        "search-button-field.html",
        "sbt-sidebar-nav.html",
        "ablog/recentposts.html",
        "ablog/tagcloud.html",
        "ablog/categories.html",
        "ablog/archives.html",
    ]
}

# Sphinx Book Theme Settings
html_theme_options = {
    "repository_url": "https://github.com/gkthiruvathukal/gkthiruvathukal.github.io",
    "use_repository_button": True,
    "show_navbar_depth": 0,
    "max_navbar_depth": 2,
    "collapse_navbar": True,
    "use_sidenotes": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/gkthiruvathukal",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "LinkedIn",
            "url": "https://www.linkedin.com/in/gkthiruvathukal",
            "icon": "fa-brands fa-linkedin",
        },
        {
            "name": "Google Scholar",
            "url": "https://scholar.google.com/citations?user=Ls7yS0IAAAAJ&hl=en",
            "icon": "fa-brands fa-google-scholar",
        },
        {
            "name": "Key Links",
            "url": "https://keylinks.gkt.sh",
            "icon": "fa-solid fa-link",
        },
    ],
    "extra_footer": (
        '<p>More key links: <a href="https://keylinks.gkt.sh">keylinks.gkt.sh</a></p>'
    ),
}
html_title = project
html_logo = "_static/images/headshot.png"
html_favicon = "_static/images/favicon.png"
