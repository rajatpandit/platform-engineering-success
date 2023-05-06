# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Platform Engineering Success'
copyright = '2023, Rajat Pandit'
author = 'Rajat Pandit'

# The full version, including alpha/beta/rc tags
release = '0.0.1'
fixed_sidebar = True


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx.ext.githubpages',
    'sphinx.ext.autodoc',
    'rst2pdf.pdfbuilder',
    'sphinxext.opengraph',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

html_favicon = '_static/favicon.ico'
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
canonical_url = 'https://rajatpandit.com/platform-engineering-success/'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_theme_options = {
    'logo': 'logo.png',
    'logo_name': False,
    'github_user': 'rajatpandit',
    'github_repo': 'platform-engineering-success',
    'github_banner': True,
    'github_button': True,
    'description': 'Setting up and running a well adopted platform engineering team',
    'show_powered_by': False,
    'sidebar_collapse': True,
    'show_relbars': True,
    # 'donate_url': 'https://rajatpandit.com/'
}
html_css_files = [
    'custom.css',
]

html_sidebars = {
    '**': [
        'about.html',
        'searchbox.html',
        'navigation.html',
        'relations.html',
        'donate.html',
    ]
}

html_baseurl = "https://rajatpandit.com/platform-engineering-success/"
ogp_site_url = "https://rajatpandit.com/platform-engineering-success/"
ogp_image = "https://rajatpandit.com/platform-engineering-success/_static/logo.png"
ogp_description_length = 300
ogp_type = "article"
ogp_use_first_image = True

ogp_custom_meta_tags = [
    '<meta property="twitter:creator" content="@rajatpandit" >'
    '<meta property="twitter:site" content="@rajatpandit" >',
    '<meta property="twitter:card" content="summary" >',
]