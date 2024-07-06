from datetime import datetime
import os

import pytest
from selenium import webdriver

# driver = None
@pytest.fixture()
def setup(browser):
    # global driver
    # if driver is None:
        if browser == "edge":
            driver = webdriver.Edge()
            print("lanunching edge browser")
        elif browser == "firefox":
            driver = webdriver.Firefox()
            print("launching firefox browser")
        else:
            driver = webdriver.Chrome()
            print("launching chrome browser")
        return driver

# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call" or report.when == 'setup':
#         xfail = hasattr(report,'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::","_") + '.png'
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:340px;height:228px;" '\
#                      'onclick="window.open(this.src)" align="right"/></div>' %file_name
#                 extras.append(pytest_html.extras.html(html))
#         report.extras = extras
#
#
# def pytest_html_report_title(report):
#     report.title = "Interesting Report!!!!!!!!!!!!!!"
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)


#this will get the value from CLI/Hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

# This will return the browser value to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

############################## pytest html report ##############################

#It is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Herokuapp'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Radhe'

#it is hook for delete/Modify environment info to html report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

#specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"

