import argparse
import os.path

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from helper import get_links, get_image_link, download_image, make_folderpath

parser = argparse.ArgumentParser(prog= 'Micmicidol Scraper', description= 'Scrape images from micmicidol posts')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-q', '--query')
parser.add_argument('-m', '--max-results', help= 'Only applicable with QUERY parameter', default=10)
group.add_argument('-t', '--target-url')
args = parser.parse_args()

query = args.query
target_url = args.target_url
max_results = args.max_results

# add options
options = Options()
options.add_argument('headless');

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(1.5) # seconds

links = []

if query:
    print('\nSearching... This could take awhile ⌛️')
    # get links
    links = get_links(driver, query, max_results)
    if not links:
        print('No results found.')
    else:
        # Found Results
        results_count = len(links)
        print(f'\nFound {results_count} result(s)')
        
        image_folder = os.path.realpath('images')
        # Create Images folder if not exist
        if (not os.path.exists(image_folder)):
            os.mkdir(image_folder)
            
        # Create path from query and url
        folder_path = os.path.join(image_folder, query)
        if (not os.path.exists(folder_path)):
            os.mkdir(folder_path)
            
        download_image(driver, links, os, folder_path)
    driver.close()
else:
    # get all images
    image_links = get_image_link(driver, target_url)
    
    # use target_url as name 
    filename = os.path.split(target_url)[1]
    filename = filename.replace('.html', '')
    folder_path = make_folderpath(os, filename)
    
    links.append(target_url)
    download_image(driver, links, os, folder_path)
    driver.close()
