#!/usr/bin/env python

"""
Entry point
"""

import click
import tempfile
import webbrowser as browser
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
from http.server import BaseHTTPRequestHandler, HTTPServer


def render_template():
    """Render and populate the template"""
    #TODO: Flexible file system loader for custom templates
    env = Environment(loader=FileSystemLoader("."),)

    # Custom commands go here
    doc_title = "Sample Report"
    
    # TODO: Flexible template location or type
    template = env.get_template("./templates/report.html")
    rendered = template.render(
        title=doc_title,
    )
    return rendered.encode("utf-8")


@click.command()
def main():
    """Main function"""
    # Get the rendered template
    page = render_template()

    # Create temporary file
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(page)
    f.seek(0)
    f.close()

    # Open the template in the browser
    browser.open(f.name)


if __name__ == "__main__":
    main()