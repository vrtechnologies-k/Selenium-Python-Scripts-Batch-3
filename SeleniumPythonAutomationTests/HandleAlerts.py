import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

driver.find_element(By.NAME,'enter-name').send_keys("Venkat")

driver.find_element(By.ID,'alertbtn').click()

alert = driver.switch_to.alert

alerttext = alert.text

print(alerttext)

assert "Venkat" in alerttext

alert.accept()

time.sleep(3)

driver.find_element(By.NAME,'enter-name').send_keys("Venkat")

driver.find_element(By.ID,'confirmbtn').click()

confirmText = alert.text

print(confirmText)

assert "Are you sure you want to confirm" in confirmText

alert.dismiss()

time.sleep(2)

driver.quit()


