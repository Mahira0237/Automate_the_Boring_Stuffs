#! python3
# ImageSiteDownloader.py - Downloads every single image of search result.
#Downloads only 5 instead

import requests, os, bs4,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse, urlunparse
import pathlib
import urllib.parse

options = Options()
options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=options)
search='Lake'
os.makedirs('ImageResults', exist_ok=True)
# Download the page.
searchPage='https://www.freepik.com/search?format=search&last_filter=query&last_value='+search+'&query='+search
print('Downloading page %s...' % searchPage)
browser.get(searchPage)
i=0
# Find the images.
searchRes = browser.find_elements(By.XPATH, "//img[contains(@alt,'lake')]")   
if searchRes == []:
    print('Could not find images.')
else:
    for results in searchRes:      
        theUrl = results.get_attribute('src')
        # Download the image.
        print('Downloading image %s...' % (theUrl))
        image = requests.get(theUrl)

        # Save the image to ./ImageResults.
        parsed_url = urllib.parse.urlparse(theUrl)
        filename = pathlib.Path(parsed_url.path).name
        imageFile = open(os.path.join('ImageResults', filename),'wb')
        for chunk in image.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        i+=1
        if i>=5:
            break
time.sleep(1)
print('Done.')