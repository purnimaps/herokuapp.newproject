from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AccountRegistrationPage:

    drop_down = "//*[@id='dropdown']"
    dropdownHomePage = 'Dropdown'
    abTestingTextMsg = ''

    def __init__(self,driver):
        self.driver = driver
    def clickDropDown(self):
        self.driver.find_element(By.LINK_TEXT,self.dropdownHomePage).click()

    def chooseDropDown(self):
        select = Select(self.driver.find_element(By.XPATH,self.drop_down))
        for i in select.options:
            print("value is {} ".format(i.text))

    def getABTesting(self):
        ele = self.driver.find_element(By.TAG_NAME,"h3").text
        print("text of the element: " ,ele)
