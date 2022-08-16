import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.ID, 'openwindow').click()

# driver.find_element(By.ID,'opentab').click()

parentwindow = driver.window_handles[0]

print(parentwindow)

childwindow = driver.window_handles[1]

print(childwindow)

allwindows = driver.window_handles

print(allwindows)

driver.switch_to.window(childwindow)

driver.maximize_window()

time.sleep(3)

# driver.find_element(By.NAME,'email').send_keys("venkat@gmail.com")

titletext = driver.find_element(By.TAG_NAME, 'h3').text

print(titletext)

assert "TESTING" in titletext

time.sleep(2)

driver.close()

driver.switch_to.window(parentwindow)

driver.quit()
