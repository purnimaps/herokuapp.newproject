from utilities.readProperties import ReadConfig
from testcases import conftest
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage

class Test_002:
    baseurl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()

    def test_file_download(self,setup):
        self.logger.info("-------------Testing download of a file-------------------")
        self.driver = setup
        self.logger.info("------------Entering the application--------------")
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("-------------clicking on the file download link-----------")
        self.ho = HomePage(self.driver)
        self.ho.clickFileDownload()
        self.logger.info("--------------click on the file-----------")
        self.ap = AccountRegistrationPage(self.driver)
        self.ap.clickJpgFile()
        self.logger.info("--------done with downloading part -------")
