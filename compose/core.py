#!/usr/bin/env python

"""
Entry point
"""

import click
import webbrowser as browser
from jinja2 import Environment, FileSystemLoader
from http.server import BaseHTTPRequestHandler, HTTPServer


@click.command
def main():
    """Main function"""
    pass


if __name__ == "__main__":
    main()