# micmicidol-scraper
Scrape images based on search keywords.

# Get Started

    cd micmicidol-scraper/
    source venv/bin/activate
    python3 spider.py -h 

<br>

    options:
      -h, --help            show this help message and exit
      -q QUERY, --query QUERY
      -m MAX_RESULTS, --max-results MAX_RESULTS
                            Only applicable with QUERY parameter
      -t TARGET_URL, --target-url TARGET_URL

# Sample usage
Get all images of the lastest 5 posts from `nogi_satsu`

    python3 spider.py -q nogi_satsu -m 5
    
Get all images in this post

    python3 spider.py -t https://www.micmicidol.club/2023/02/friday-20230303-10-46-nogisatsu-vol227.html
    
# Project Roadmap
## Feature:
 * [X] Allow parsing url to download a single post
 * [X] Use `argparse` instead of `input()`
 * [ ] Scrape video in post
