import os.path

from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from helper import get_links, get_image_link, download_image

# add options
options = Options()
options.add_argument('headless');

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(1.5) # seconds

while True:
    query = ''
    while not query:
        query = input("Search by model/magazine name (Enter EXIT to close the program): ")
    if query == 'EXIT':
        break
    
    
    print('\nSearching... This could take awhile ⌛️')
    # get links
    links = get_links(driver, query)
    if not links:
        print('No results found.')
    else:
        """Found Results"""
        results_count = len(links)
        print(f'\nFound {results_count} result(s)')
        
        image_folder = os.path.realpath('Images')
        """Create Images folder if not exist"""
        if (not os.path.exists(image_folder)):
            os.mkdir(image_folder)
            
        """Create path from query and url"""
        folder_path = os.path.join(image_folder, query)
        if (not os.path.exists(folder_path)):
            os.mkdir(folder_path)

        for link in links:
            print(f'\nWorking on {link} ⌛️')
            filename = os.path.split(link)[1]
            filename = filename.replace('.html', '')
            
            base_destination = os.path.join(folder_path, filename)
            
            image_links = get_image_link(driver, link)
            image_count = len(image_links)
            print(f'\nFound {image_count} images. Start downloading... ⬇️')
            
            image_index = 1
            for image in image_links:
                print(f'\n{image_index} / ' + str(len(image_links)))
                destination = base_destination + f' ({image_index})'
                """Get image extension"""
                ext = os.path.splitext(image)[1]
                if not ext:
                    ext = '.jpg'
                destination = destination + ext
                download_image(folder_path, destination, image)
                image_index += 1
                
driver.close()
