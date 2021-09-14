import pytest
import optparse
from selenium import webdriver

@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path="C:/App/chromedriver.exe")
    print("Launching chrome browser.........")
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


# @pytest.fixture()
# def browser(brws):
#     if browser == 'chrome':
#         driver = webdriver.Chrome(executable_path="C:/App/chromedriver.exe")
#         print("Launching chrome browser.........")
#     elif browser == 'firefox':
#         driver = webdriver.Firefox()
#         print("Launching firefox browser.........")
#     return driver
#
#
# def pytest_addoption(parser):  # This will get the value from CLI /hooks
#     parser.addoption("--brws")
#
#
# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--brws")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'SSENSE'
    config._metadata['Module Name'] = 'PHP Travel - Add funds'
    config._metadata['Tester'] = 'Mohammed Laredj'


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
