#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import datetime

from calcifer import __version__

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

project = 'calcifer'
copyright = '{0.year}, Dramafever'.format(datetime.datetime.now())
version = release = __version__

needs_sphinx = '1.1'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.graphviz',
    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = []
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'
pygments_style = 'sphinx'
html_static_path = []
exclude_patterns = []
graphviz_output_format = 'svg'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme  # pylint: disable=C0413
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

intersphinx_mapping = {
    'python': ('https://docs.python.org/', None),
}
