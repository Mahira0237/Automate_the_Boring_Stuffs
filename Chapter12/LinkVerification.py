from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

import time, requests
browser = webdriver.Chrome()
page='https://www.wikihow.com/Play-UNO'
browser.get(page)

links=browser.find_elements(By.TAG_NAME, 'a')
for link in links:
    url=link.get_attribute('href')
    try:
        requests.get(url).raise_for_status()
    except Exception as exc:
        print('There is an error:%s'%exc)
print('Done Checking')


