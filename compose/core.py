#!/usr/bin/env python

"""
Entry point
"""

import os
import io
import click
import base64
import tempfile
import webbrowser as browser
import matplotlib.pyplot as plt
from jinja2 import Environment, FileSystemLoader
from http.server import BaseHTTPRequestHandler, HTTPServer


def generate_sample_graph():
    """Visualisation generation"""
    x_data = range(1, 45)
    y_idx = list(range(1, 45))
    sample_data = lambda x: x * 0.256 + x**2 + 35
    y_data = list(map(sample_data, y_idx))
    plt.figure(figsize=(15, 5))
    plt.plot(x_data, y_data, marker="+")
    # -- Create buffer
    plt_buffer = io.BytesIO()
    plt.savefig(plt_buffer, format="png", bbox_inches="tight",)
    plt_buffer.seek(0)
    plt_data = b''.join(plt_buffer)
    encoded = base64.b64encode(plt_data)
    output = encoded.decode("utf-8")
    return output


def render_template():
    """Render and populate the template"""
    #TODO: Flexible file system loader for custom templates
    env = Environment(loader=FileSystemLoader("."),)
    
    # Get css path as a custom path
    css_location = "./static/styles.css"
    full_css_path = os.path.realpath(css_location)

    # Custom data goes here
    doc_title = "Sample Report"
    
    # Generating Sample Graph
    sample_graph = generate_sample_graph()
    
    # TODO: Flexible template location or type
    template = env.get_template("./templates/report.html")
    rendered = template.render(
        title=doc_title,
        stylesheet_url=full_css_path,
        sample_graph=sample_graph,
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