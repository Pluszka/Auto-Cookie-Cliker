from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PATHS = ['//*[@id="buyTime machine"]/b/text()[2]',
         '//*[@id="buyPortal"]/b/text()[2]',
         '//*[@id="buyAlchemy lab"]/b/text()[2]',
         '//*[@id="buyShipment"]/b/text()[2]',
         '//*[@id="buyMine"]/b/text()[2]',
         '//*[@id="buyFactory"]/b/text()[2]',
         '//*[@id="buyGrandma"]/b/text()[2]',
         '//*[@id="buyCursor"]/b/text()[2]']


def enoughMoney(money, price):
    price_block = driver.find_element(By.XPATH, price)
    if int(money.text) >= int(price_block.text):
        print(money.text, price_block.text)
        price_block.click()


chrome_driver_path = r'C:\Users\pluus\dev_stuff\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
timecheck = time.time()
while True:
    print(timecheck)
    big_cookie = driver.find_element(By.ID, 'cookie')
    big_cookie.click()
    cookies = driver.find_element(By.ID, 'money')
    if timecheck % 5 == 0:
        for path in PATHS:
            enoughMoney(cookies, path)
