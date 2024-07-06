from selenium.webdriver.common.by import By

class Input:
    inputLocator = 'Inputs'
    numberXpath = "//input[@type='number']"

    def __init__(self,driver):
        self.driver = driver

    def clickInput(self):
        self.driver.find_element(By.LINK_TEXT,self.inputLocator).click()

