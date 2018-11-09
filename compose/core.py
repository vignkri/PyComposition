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

    # Get css path as a custom path
    css_location = "./static/styles.css"
    full_css_path = os.path.realpath(css_location)

    # Custom data goes here
    doc_title = "Sample Report"
    
    # TODO: Flexible template location or type
    template = env.get_template("./templates/report.html")
    rendered = template.render(
        title=doc_title,
        stylesheet_url=full_css_path,
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