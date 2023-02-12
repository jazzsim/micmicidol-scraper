import wget

def get_links(driver, query):
    driver.get("https://www.micmicidol.com/search?q=" + query + "&max-results=10")
    
    """Check if empty result"""
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
    content = driver.find_elements("xpath", "//div[@class='post-body entry-content']//a[@href]")
    image_links = []
    for a_tag in content:
        link = a_tag.get_attribute('href')
        image_links.append(link)
    return image_links

def download_image(folder_path, destination, image):
    try:
        wget.download(image, out=destination)
        print('\nDownloaded image to ' + folder_path + ' ✅')
    except:
        print('Image at ' + image + ' couldn\'t be downloaded')