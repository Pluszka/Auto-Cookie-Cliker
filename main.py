from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r'C:\Users\pluus\dev_stuff\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
timecheck = int(time.time())
big_cookie = driver.find_element(By.ID, 'cookie')
ids = driver.find_elements(By.CSS_SELECTOR, '#store div')
ids = [id.get_attribute('id') for id in ids][::-1]

while True:
    big_cookie.click()
    if (int(time.time()) - timecheck) % 5 == 0:
        for id in ids:
            element = driver.find_element(By.ID, id)
            print(element.text)
            if element.get_attribute('class') != 'grayed':
                element.click()

