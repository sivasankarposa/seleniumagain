
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(executable_path="C:\\Users\\siva sankar\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()

products=driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    title=product.find_element_by_xpath("div/h4/a").text
    if title=="Blackberry":
        product.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_xpath("//a[@class='nav-link btn btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
wait=WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)


