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

project = 'GIANI'
copyright = '2019-2025, GIANI docs authors'
author = 'Dave Barry'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    #'myst_parser',
    'sphinx_rtd_theme',
    #'sphinx_panels',
    #'sphinx.ext.autosectionlabel',
    #'sphinx_search.extension'
]

# Add any paths that contain templates here, relative to this directory.
#templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


html_theme_options = {
    'style_nav_header_background': '#343131'
}

#html_css_files = [
#    'css/custom.css',
#]

master_doc = 'index'

#rst_prolog = """
#.. |br| raw:: html
#  <br/>
  
#.. |vertical_ellipsis| unicode:: 0x22EE
#.. |copyright| unicode:: 0xA9
#"""


#highlight_language = 'groovy'

html_logo = 'docs/overview/images/Icon.png'

#html_favicon = 'docs/images/QuPath.ico'

#release = '0.3.0'
version = '3.4.9'
