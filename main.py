from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r'C:\Users\pluus\dev_stuff\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
while True:
    big_cookie = driver.find_element(By.ID, 'cookie')
    big_cookie.click()
    cookies = driver.find_element(By.ID, 'money')
    print(cookies.text)


