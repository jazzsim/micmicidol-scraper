# micmicidol-scraper
Scrape images based on search keywords.

This is a Selenium scraper with 1.5 seconds of implicit wait and the amount of results is capped at 10 results per search.

The images downloaded will be store in the Images folder with the keywrods as the folder name.

<img width="404" alt="Screenshot 2023-02-12 at 7 54 02 PM" src="https://user-images.githubusercontent.com/24294128/218309421-013f77d4-3004-4192-8210-4ca3678a45d3.png">

# Usage
To start the program

    cd micmicidol-scraper/
    source venv/bin/activate
    python3 spider.py

<img width="842" src="https://user-images.githubusercontent.com/24294128/218308457-3baf3668-2fb9-42c5-9001-ea9bdc7b2ddf.png">

To shutdown the program (note: EXIT is case sensitive)

    EXIT
    deactivate
    
<img width="500" alt="Screenshot 2023-02-12 at 7 56 46 PM" src="https://user-images.githubusercontent.com/24294128/218309559-6d37c1f0-1276-4911-948f-c67a8b7ceeb7.png">

# Showcase
You can continue to scrape after completion.

You will receive the "No results found." message when the website does not return any results.

<img width="842" src="https://user-images.githubusercontent.com/24294128/218308409-20a9810c-b3fd-431c-96de-dab37708b0c5.png">

# Project Roadmap
## Feature:
 * [ ] Allow parsing url to download a single post
 * [ ] Use `argparse` instead of `input()`
 * [ ] Scrape video in post
