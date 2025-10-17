# pylint: skip-file

import time
from pathlib import Path

# -- Project information -----------------------------------------------------

def get_project_name_from_index():
    with open(Path(__file__).parent / 'index.md', 'r', encoding='utf-8') as f:
        return f.readline().strip()[2:].strip()

project = get_project_name_from_index()
author = 'Ez Adlin Waez'
copyright = f'{time.localtime().tm_year}, {author}'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    ]

source_suffix = '.md'
numfig = True

templates_path = ['_templates']
exclude_patterns = []

myst_enable_extensions = [
    "colon_fence",
    "substitution",
    "deflist",
    "tasklist",
    "attrs_inline",
    "fieldlist",
    "html_image",
    "linkify",
    "strikethrough",
    "replacements",
    "dollarmath",
    "html_admonition",
    "attrs_block",
]
myst_fence_as_directive = ["mermaid"]

mermaid_output_format = 'svg'
mermaid_pdfcrop = 'pdfcrop'
mermaid_params = ['--width', '800', '--height', '600']

# -- Options for HTML output -------------------------------------------------

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['css/custom.css']

# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'pdflatex'
latex_show_urls = 'footnote'
latex_toplevel_sectioning = 'section'
latex_documents = [(
    'index',  # startdocname
    f'{project.upper().replace(" ", "_")}.tex',  # targetname
    f'{project}',  # title
    author,  # author
    'howto',  # theme
)]
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'geometry': r'\usepackage{geometry} \geometry{outer=2cm}',
    'babel': '',
    'fontpkg': '',
    'figure_align': 'H',
    'fncychap': '',
    'preamble': r'''
        \usepackage{graphicx}
        \usepackage{geometry}
        \usepackage{booktabs}
        \usepackage{listings}
        \usepackage{xcolor}
        \usepackage[version=4]{mhchem}
        \usepackage{amsmath}
        \usepackage{amssymb}
    ''',
    'tableofcontents': '\\tableofcontents\\newpage',
    'printindex': '',
}
