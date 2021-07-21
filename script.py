# in command prompt, type "pip install pynput" to install pynput.
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()
driver.get('https://isthisprime.com/game/')
assert "Python" in driver.title
elem = driver.find_element_by_id("n")
while(True):
    elem.send_keys(Keys.LEFT)

time.sleep(1000)

#time.sleep(2)
#keyboard.press(key)
#keyboard.release(key)
