from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
#from prime import isPrime
from prime import insertPrimes

import time


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://isthisprime.com/game/')
driver.maximize_window()

print("before")
WebDriverWait(driver, 10000).until(EC.visibility_of_element_located((By.CLASS_NAME, 'play')))
print('after')

keyboard = Controller()
primes = insertPrimes()
print(primes)

print(53 in primes)

startTime = time.time()
duration = 60

while True:
    number = driver.find_element(By.ID, 'n')
    currentTime = time.time()
    elapsedTime = currentTime - startTime
    if(elapsedTime > duration):
        print('done')
        break
    time.sleep(0.005)
    if(int(number.text) in primes):
        keyboard.tap(Key.left)
    else:
        keyboard.tap(Key.right)


#time.sleep(2)
#keyboard.press(key)
#keyboard.release(key)
