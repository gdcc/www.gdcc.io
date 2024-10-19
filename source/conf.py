# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'GDCC'
copyright = '2024, GDCC Members'
author = 'GDCC Members'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser"]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_logo = '_static/_images/gdcc-logo.png'
html_static_path = ['_static']
html_theme_options = {
  "show_prev_next": False,
  "header_links_before_dropdown": 6,
  # see https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/source-buttons.html
  "use_edit_page_button": True,
}
html_context = {
    "github_user": "gdcc",
    "github_repo": "www.gdcc.io",
    "github_version": "main",
    "doc_path": "source",
}
# see use_edit_page_button, which we use instead
html_show_sourcelink = False
