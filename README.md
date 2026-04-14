# Visualize Shared External Links Across Domains

!["Multiple websites scanned for internal and external links."](https://hosting.photobucket.com/images/i/bernhoftbret/two-websites.png)

Crawls websites to collect and structure internal and external link relationships into a JSON file, which a D3.js frontend then visualizes as an interactive, color-coded network graph with zoom, drag and hover features.

## Overview

The Python backend script crawls starting websites, recursively visiting internal links up to a specified maximum and collecting both internal and external hyperlinks. Internal links are tracked per base domain, while external links are stored along with the internal pages referencing them. Once crawling is complete, the collected link relationships are saved into a structured `links.json` file.

Whereas the JavaScript frontend portion uses D3.js to load the `links.json` file and render an interactive network graph in the browser. Each URL becomes a node, with internal pages colored aqua and external links colored magenta. The graph supports zooming, dragging nodes, hover highlighting of connected nodes and tooltip display of URLs.

## Set Up Instructions

Below are the required software programs and instructions for installing and using this application on a Linux machine.

### Programs Needed

- [Git](https://git-scm.com/downloads)

- [Python](https://www.python.org/downloads/)

### Steps

1. Install the above programs

2. Open a terminal

3. Clone this repository using `git` by running the following command: `git clone git@github.com:devbret/shared-external-links.git`

4. Navigate to the repo's directory by running: `cd shared-external-links`

5. Create a virtual environment with this command: `python3 -m venv venv`

6. Activate your virtual environment using: `source venv/bin/activate`

7. Install the needed dependencies for running the script: `pip install -r requirements.txt`

8. Edit the `app.py` file `start_urls` variable (on line 61), these are the websites you would like to visit and visualize
   - Also edit the `app.py` file `max_links` variable (on line 10) which specifies how many pages or links you would like to crawl per website

9. Run the Python script with the command: `python3 app.py`

10. To view the website's connectome using the `index.html` frontend file you will need to run the following command in a terminal: `python3 -m http.server`

11. Access the visualization in a browser by visiting: `http://localhost:8000`

12. To exit the virtual environment, type this command in the terminal: `deactivate`

## Other Considerations

This project repo is intended to demonstrate an ability to do the following:

- Crawl websites to collect and categorize internal and external links, storing their relationships in a structured JSON format

- Visualize link structure as an interactive D3.js network graph, thereby allowing users to explore connections and open linked pages directly

If you have any questions or would like to collaborate, please reach out either on GitHub or via [my website](https://bretbernhoft.com/).
