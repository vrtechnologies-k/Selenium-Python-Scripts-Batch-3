from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

tablerows = driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr")

print(len(tablerows))

for i in range(2,len(tablerows)+1):

    tablecolumns = driver.find_elements(By.XPATH,"//table[@name='courses']/tbody/tr["+str(i)+"]/td")

    #print(len(tablecolumns))

    for j in range(1,len(tablecolumns)+1):
        course = driver.find_element(By.XPATH,"//table[@name='courses']/tbody/tr["+str(i)+"]/td["+str(j)+"]")
        #print(coursetext)
        if course.text == "WebServices / REST API Testing with SoapUI":
            price = course.find_element(By.XPATH,'following-sibling::td').text
            print(price)
            break


driver.quit()

