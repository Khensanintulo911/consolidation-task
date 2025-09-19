# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
import django

# Add project to Python path
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../mysite'))
sys.path.insert(0, os.path.abspath('../blog'))
sys.path.insert(0, os.path.abspath('../polls'))
sys.path.insert(0, os.path.abspath('../personal'))

# Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
django.setup()

project = 'CONSOLIDATION TASK'
copyright = '2025, KHENSANI NTULO'
author = 'KHENSANI NTULO'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'en'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

