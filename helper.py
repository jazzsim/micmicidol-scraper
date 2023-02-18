import wget
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def get_links(driver, query, max_results):
    driver.get("https://www.micmicidol.club/search?q=" + query + "&max-results=" + max_results)
    handle_alert(driver)
    # Check if empty result
    try:
        driver.find_elements("class name", "date-outer")
    except:
        return []
    
    titles = driver.find_elements("xpath", "//h3[@class='post-title entry-title']/a")
    links = []
    for title in titles:
        href = title.get_attribute('href');
        links.append(href)
    return links

def get_image_link(driver, link):
    driver.get(link)
    handle_alert(driver)
    content = driver.find_elements("xpath", "//div[@class='post-body entry-content']//a[@href]")
    image_links = []
    for a_tag in content:
        link = a_tag.get_attribute('href')
        image_links.append(link)
    return image_links

def make_folderpath(os, foldername):
    image_folder = os.path.realpath('images')
    # Create Images folder if not exist
    if (not os.path.exists(image_folder)):
        os.mkdir(image_folder)
        
    # Create path from query and url
    folder_path = os.path.join(image_folder, foldername)
    if (not os.path.exists(folder_path)):
        os.mkdir(folder_path)
    
    return folder_path

def download_image(driver, links, os, folder_path):
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
            # Get image extension
            ext = os.path.splitext(image)[1]
            if not ext:
                ext = '.jpg'
            destination = destination + ext
            try:
                wget.download(image, out=destination)
                print('\nDownloaded image to ' + folder_path + ' ✅')
            except:
                print('Image at ' + image + ' couldn\'t be downloaded')
            image_index += 1
        
def handle_alert(driver):
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for ' +
                                    'confirmation popup to appear.')
        alert = driver.switch_to.alert
        alert.accept()
        print("Alert accepted.")
    except TimeoutException:
        print("No alert found. Proceeding...")