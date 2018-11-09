# Composition

A composer to create repeatable reports in HTML from single-point non-changing data sources. It creates single-page reports with custom-css support in the static folder.

## How-To

1. Set up virtual environment for python.
2. Install the library requisites.
3. Edit the `core.py` module to build required reporting structure. 
    1. Run `python core.py` to generate HTML
4. It automatically opens the default browser with the temporary html file.
    1. Save or print the file for persistence.

## Feature Ideas

- Write documents directly from markdown and configuration files for repeatable information.
- Tool to embed fonts in the CSS
- Use markdown to create graphs, information while making sure repeated.