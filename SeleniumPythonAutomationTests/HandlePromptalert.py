import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/alerts")

driver.maximize_window()

driver.execute_script("window.scrollBy(0,400)")

time.sleep(2)

driver.find_element(By.ID,'promtButton').click()

alert = driver.switch_to.alert

alert.send_keys("Venkat")

time.sleep(2)

textvalue = alert.__getattribute__

print(textvalue)

alert.accept()

time.sleep(2)

promptresult = driver.find_element(By.ID,'promptResult').text

assert "Venkat" in promptresult

driver.quit()


