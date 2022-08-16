from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.maximize_window()

driver.find_element(By.NAME,'name').send_keys("venkat")

driver.find_element(By.NAME,'email').send_keys("venkat@gmail.com")

driver.find_element(By.ID,"exampleInputPassword1").send_keys("Venkat@123")

driver.find_element(By.ID,"exampleCheck1").click()

Select(driver.find_element(By.ID,"exampleFormControlSelect1")).select_by_visible_text("Female")

driver.find_element(By.ID,"inlineRadio2").click()

driver.find_element(By.NAME,"bday").send_keys("01-08-1988")

driver.find_element(By.CLASS_NAME,"btn-success").click()

alertmessage = driver.find_element(By.CLASS_NAME,"alert-success").text

print(alertmessage)

assert "Success!" in alertmessage

driver.quit()