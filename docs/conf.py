# -*- coding: utf-8 -*-

import os
import sys


# -- General configuration ------------------------------------------------

_projectpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

sys.path.insert(0, _projectpath)

from sphinx_navtree import __version__

extensions = ['sphinx_navtree']

navtree_maxdepth = {'Overview': 1, 'Demo Section': 2}
navtree_shift = True
navtree_root_links = True

source_suffix = '.rst'
source_encoding = 'utf-8'

master_doc = 'toc'

exclude_patterns = ['_build']
templates_path = ['_templates']

project = 'sphinx-navtree'
copyright = '2016 Kalle Tuure'
author = 'Kalle Tuure'

_basename = 'sphinx_navtree'
_title = 'sphinx-navtree documentation'
_subtitle = 'Navigation tree customization for Sphinx'
_project_url = 'https://github.com/bintoro/sphinx-navtree'
_doc_url = 'https://sphinx-navtree.readthedocs.org/'

version = __version__
release = __version__

language = 'en'

today = ''
today_fmt = '%B %d, %Y'

default_role = None
add_function_parentheses = True
add_module_names = False

highlight_language = 'none'
pygments_style = 'sphinx'

modindex_common_prefix = []


# -- Options for HTML output ----------------------------------------------

if not os.environ.get('READTHEDOCS'):
    html_theme = 'sphinx_rtd_theme'

html_theme_options = {}

html_title = '%s %s documentation' % (project, version)
html_short_title = _title

_context_config = {
    'master_doc': 'index',
    'display_github': False,
    'display_bitbucket': False,
}

html_logo = None
html_favicon = None

html_static_path = ['_static']
html_extra_path = []

html_last_updated_fmt = None
html_use_smartypants = True
html_add_permalinks = False

html_additional_pages = {}

html_domain_indices = False
html_use_index = False
html_split_index = False

html_copy_source = True
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

html_search_language = 'en'


# -- Options for EPUB output ----------------------------------------------

epub_author = author
epub_publisher = author
epub_identifier = _project_url
epub_scheme = 'URL'
epub_uid = 'pub-uid'

epub_show_urls = 'footnote'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'preamble': '',
    'figure_align': 'htbp',
}

# (source start file, target name, title, author, documentclass, toctree_only)
latex_documents = [
    (master_doc, _basename + '.tex', _title, author, 'manual', False),
]

latex_use_parts = True
latex_domain_indices = False
latex_show_urls = 'footnote'


# -- Options for manual page output ---------------------------------------

# (source start file, name, description, authors, manual section)
man_pages = [
    (master_doc, _basename, _subtitle, [author], 1)
]

man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
    (master_doc, _basename, _title, author, project, _subtitle, 'Miscellaneous'),
]

texinfo_domain_indices = False
texinfo_show_urls = 'footnote'


# -- Customization --------------------------------------------------------

def setup(app):
    app.add_stylesheet('https://static.goodtimes.fi/css/bintoro_rtd.css')
    app.connect('html-page-context', html_page_context)

def html_page_context(app, pagename, templatename, context, doctree):
    context.update(_context_config)

