from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By
import random
from random import randint
import time

browser=webdriver.Chrome()
page='https://play2048.co/'
browser.get(page)

# i=0
# Body=browser.find_element(By.TAG_NAME,'body')
# while i<100:
#     Body.send_keys(Keys.UP)
#     Body.send_keys(Keys.RIGHT)
#     Body.send_keys(Keys.DOWN)
#     Body.send_keys(Keys.LEFT)
#     i+=1

# time.sleep(5)

i=0
Body=browser.find_element(By.TAG_NAME,'body')
while i<500:
    move=random.randint(1,4)
    if move==1: Body.send_keys(Keys.UP)
    elif move==2: Body.send_keys(Keys.RIGHT)
    elif move==3: Body.send_keys(Keys.DOWN)
    else: Body.send_keys(Keys.LEFT)
    i+=1

time.sleep(5)



