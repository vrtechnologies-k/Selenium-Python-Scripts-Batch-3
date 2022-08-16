import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.ID,'autocomplete').send_keys("ind")

time.sleep(5)

autoelements = driver.find_elements(By.CLASS_NAME,'ui-menu-item-wrapper')

print(len(autoelements))

for element in autoelements:
    country = element.text
    print(country)
    if country == "India":
        element.click()
        break

time.sleep(2)
driver.quit()