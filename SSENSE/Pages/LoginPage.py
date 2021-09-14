from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.Locators import Locators


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.Username_textbox_name = Locators.Username_textbox_name
        self.Password_textbox_name = Locators.Password_textbox_name
        self.LoginButton_xpath = Locators.LoginButton_xpath

    def enter_username(self, user):
        self.driver.find_element_by_name(self.Username_textbox_name).clear()
        self.driver.find_element_by_name(self.Username_textbox_name).send_keys(user)

    def enter_password(self, pwd):
        self.driver.find_element_by_name(self.Password_textbox_name).clear()
        self.driver.find_element_by_name(self.Password_textbox_name).send_keys(pwd)

    def click_on_the_login_button(self, driver):
        element = WebDriverWait(driver, 10).until(expected_conditions.
                                                  element_to_be_clickable((By.XPATH, self.LoginButton_xpath)))
        element.click()
