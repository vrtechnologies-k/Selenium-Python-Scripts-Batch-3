from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.title)

print(driver.current_url)

driver.back()

driver.forward()

driver.refresh()

driver.quit()