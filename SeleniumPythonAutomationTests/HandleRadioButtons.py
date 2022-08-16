import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()


driver.find_element(By.ID,'inlineRadio1').click()

time.sleep(5)

buttons = driver.find_elements(By.NAME,'inlineRadioOptions')

# length of radio buttons
print(len(buttons))

# click on 2st radio button
buttons[1].click()

time.sleep(5)


driver.quit()