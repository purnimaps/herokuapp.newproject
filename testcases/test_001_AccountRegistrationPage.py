import os

from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage

class Test_001_AccountReg:
    baseURL = "https://the-internet.herokuapp.com/"

    def test_account_reg(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.hp = HomePage(self.driver)
        self.hp.clickCheckbox()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg19.png")
        self.driver.back()
        self.dd = AccountRegistrationPage(self.driver)
        print("------------clicking on home page drop down hyperlink------------")
        self.dd.clickDropDown()
        print("------------selecting and storing the drop down values-------------")
        self.dd.chooseDropDown()
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_account_reg20.png")
        self.driver.back()
        print("------------clicking on ab testing element-----------")
        self.hp.clickabTesting()
        print("------------printing the ab testing text element---------")
        self.dd.getABTesting()
        print("------close the application-----")
        assert 4 == 5



        # self.driver.implicitly_wait(20)
        # self.hp.clickRegister()
        # self.regpage = AccountRegistrationPage(self.driver)

        # self.regpage.setFirstName("John")
        # self.regpage.setLastName("Canedy")
        # self.email=randomeString.random_string_generator()+'gmail.com'
        # self.regpage.setEmail(self.email)
        # self.regpage.setEmail(self.email)
        # self.regpage.setTelephone("678900653321")





