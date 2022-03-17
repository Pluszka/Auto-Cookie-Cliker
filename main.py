from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = r'C:\Users\pluus\dev_stuff\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
timecheck = int(time.time())
ids = driver.find_elements(By.CSS_SELECTOR, '#store div')
ids = [id.get_attribute('id') for id in ids][::-1]

while True:
    big_cookie = driver.find_element(By.ID, 'cookie')
    big_cookie.click()
    if (int(time.time()) - timecheck) % 5 == 0:
        for id in ids:
            if driver.find_element(By.ID, id).get_attribute('class') != 'grayed':
                driver.find_element(By.ID, id).click()

