from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID,'email').send_keys("hello")
ele = driver.find_element(By.XPATH,'//*[@type = "submit"]').text
print(ele)
driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_reg344.png")
ele1 = driver.find_element(By.XPATH,'//*[@class = "_42ft _4jy0 _6lti _4jy6 _4jy2 selected _51sy"]').text
print(ele1)
driver.save_screenshot(os.path.abspath(os.curdir) + "\\reports\\" + "sc90oii.png")
print("text element ",driver.find_element(By.XPATH,"//*[@class = '_8eso']").text)