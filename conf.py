# -*- coding: utf-8 -*-


# sphinx settings
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'repoze.sphinx.autointerface',
]

source_suffix = '.rst'
master_doc = 'index'
pygments_style = 'sphinx'
html_last_updated_fmt = '%b %d, %Y'
todo_include_todos = True
autodoc_member_order = 'bysource'
exclude_patterns = ['**/.repo', '**/lib']

# general substitutions
project = 'Senic Developer Documentation'
copyright = '2017'
version = release = "0.0.0"

# theme setup
html_theme = "senic"
html_theme_path = ["./themes"]
