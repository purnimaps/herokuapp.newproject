import os

import pytest

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_AccountReg:
    # baseURL = ReadConfig.getApplicationUrl()
    # baseURL = "https://the-internet.herokuapp.com/"
    baseURL = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_account_reg(self,setup):
        self.logger.info("************ starting the testcase **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickCheckbox()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg19.png")
        self.driver.back()
        self.dd = AccountRegistrationPage(self.driver)
        self.logger.info("************ clicking on home page drop down hyperlink **********")

        self.dd.clickDropDown()

        self.logger.info("************ selecting and storing the drop down values **********")

        self.dd.chooseDropDown()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg20,png")
        self.driver.back()
        self.logger.info("************ clicking on ab testing element **********")

        self.hp.clickabTesting()
        self.logger.info("************ printing the ab testing text element **********")

        self.dd.getABTesting()

        self.logger.info("************ close the application **********")






