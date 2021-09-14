from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.Locators import Locators


class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.Login_button_xpath = Locators.Login_button_xpath

    def click_on_login_button(self):
        self.driver.find_element_by_xpath(self.Login_button_xpath).click()
