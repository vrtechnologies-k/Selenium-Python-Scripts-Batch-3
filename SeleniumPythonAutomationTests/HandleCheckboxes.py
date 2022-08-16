from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

checkbox = driver.find_element(By.ID,'exampleCheck1')
checkbox.click()

#assert checkbox.is_selected()

if checkbox.is_selected():
    print("check box is selected")
else:
    print("check box is not selected")
driver.quit()
