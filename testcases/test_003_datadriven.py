import pytest

from utilities.readProperties import ReadConfig
from pageObjects.Input import Input
from utilities.customLogger import LogGen
from utilities import XLUtils
import os


class Test_DataDriven:
    baseurl = ReadConfig.getApplicationUrl()
    logger =  LogGen.loggen()
    path = os.path.abspath(os.curdir) + "\\testdata\\t1.xlsx"

    @pytest.mark.sanity
    def test_datadriveninputs(self,setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.l1 = Input(self.driver)
        self.logger.info("----------clicking on the input element----------")
        self.l1.clickInput()
        self.r = XLUtils.getColumnCount(self.path,sheetName="Sheet1")
        y = self.l1.getElement()
        for i in range(1,self.r+1):
            p = XLUtils.readData(self.path,'Sheet1',1,i)
            y.send_keys(p)




