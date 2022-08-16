from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

tablerows = driver.find_elements(By.XPATH,"//div[@class='tableFixHead']/table[@id='product']/tbody/tr")

print(len(tablerows))

for i in range(1, len(tablerows)+1):
    tablecolumns = driver.find_elements(By.XPATH,"//div[@class='tableFixHead']/table[@id='product']/tbody/tr["+str(i)+"]/td")

    print(len(tablecolumns))

    for j in range(1, len(tablecolumns)+1):
        content = driver.find_element(By.XPATH,"//div[@class='tableFixHead']/table[@id='product']/tbody/tr["+str(i)+"]/td["+str(j)+"]").text

        print(content)

driver.quit()