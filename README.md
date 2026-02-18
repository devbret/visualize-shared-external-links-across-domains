# Visualize Shared External Links Across Domains

!["Multiple websites scanned for internal and external links."](https://hosting.photobucket.com/images/i/bernhoftbret/two-websites.png)

Crawls websites to collect and structure internal and external link relationships into a JSON file, which a D3.js frontend then visualizes as an interactive, color-coded network graph with zoom, drag and hover features.

## Overview

The Python backend script crawls starting websites, recursively visiting internal links up to a specified maximum and collecting both internal and external hyperlinks. Internal links are tracked per base domain, while external links are stored along with the internal pages referencing them. Once crawling is complete, the collected link relationships are saved into a structured `links.json` file.

Whereas the JavaScript frontend portion uses D3.js to load the `links.json` file and render an interactive network graph in the browser. Each URL becomes a node, with internal pages colored aqua and external links colored magenta. The graph supports zooming, dragging nodes, hover highlighting of connected nodes and tooltip display of URLs.
