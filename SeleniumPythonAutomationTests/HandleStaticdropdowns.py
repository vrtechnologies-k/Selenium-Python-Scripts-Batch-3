import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

Select(driver.find_element(By.ID,'exampleFormControlSelect1')).select_by_visible_text("Female")

time.sleep(2)

dropdown = driver.find_elements(By.XPATH,"//select[@id='exampleFormControlSelect1']/option")

print(len(dropdown))

driver.quit()