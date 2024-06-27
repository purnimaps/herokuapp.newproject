import pytest
from selenium import webdriver

driver = None
@pytest.fixture()
def setup():
    global driver
    if driver is None:
        driver = webdriver.Chrome()
    return driver

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call" or report.when == 'setup':
        xfail = hasattr(report,'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::","_") + ",png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:340px;height:228px;" '\
                     'onclick="window.open(this.src)" align="right"/></div>' %file_name
                extras.append(pytest_html.extras.html(html))
        report.extras = extras


def pytest_html_report_title(report):
    report.title = "My very own title!"

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)





  # always add url to report
  #       extras.append(pytest_html.extras.url("http://www.example.com/"))
  #       xfail = hasattr(report, "wasxfail")
  #       if (report.skipped and xfail) or (report.failed and not xfail):
  #           # only add additional html on failure
  #           extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
  #       report.extras = extras