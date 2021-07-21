from selenium import webdriver
import time, threading

def isPrime2(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n%i==0:
            return False    
    return True

def stop():
    exit()

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://isthisprime.com/game/')

start = driver.find_element_by_id('start')
yes = driver.find_element_by_id('yes')
no = driver.find_element_by_id('no')
n = driver.find_element_by_id('n')

driver.implicitly_wait(5)

start.click()

while True:
    number = n.text.strip()
    try:
        if isPrime2(int(number)):
            yes.click()
        else:
            no.click()
    except:
        pass


