from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#s = Service(executable_path="D:\\PythonProjects\\pythonProjectBatch3\\chromedriver.exe")
#driver = webdriver.Chrome(service = s)

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

print(driver.title)

print(driver.current_url)

driver.back()

driver.refresh()

driver.quit()



