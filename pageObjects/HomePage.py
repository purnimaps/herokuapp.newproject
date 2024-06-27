from selenium.webdriver.common.by import By

class HomePage:

    checkboxes = "//a[contains(text(),'Checkboxes')]"
    nestedFrame = "Nested Frames"
    abTesting = "//*[text()='A/B Testing']"

    def __init__(self,driver):
        self.driver = driver

    def clickCheckbox(self):
        ele = self.driver.find_element(By.XPATH,self.checkboxes)
        ele.click()

    def nestedFramesEnablement(self):
        isdispl = self.driver.find_element(By.LINK_TEXT,self.nestedFrame).isdisplayed()
        return isdispl

    def clickabTesting(self):
        self.driver.find_element(By.XPATH,self.abTesting).click()








