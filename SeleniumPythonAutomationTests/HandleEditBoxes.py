import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()


name_editbox = driver.find_element(By.NAME,'name')
name_editbox.send_keys("venkat")
time.sleep(5)

name_value = name_editbox.get_attribute('value')

print(name_value)

driver.quit()