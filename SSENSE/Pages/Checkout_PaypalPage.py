import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.Locators import Locators


class Checkout_PaypalPage():
    def __init__(self, driver):
        self.driver = driver

        self.Username_textbox_id = Locators.PPUsername_textbox_id
        self.Password_textbox_id = Locators.PPPassword_textbox_id
        self.NextButton_id = Locators.PPNextButton_id
        self.LoginButton_id = Locators.PPLoginButton_id
        self.makePaymentButton_xpath = Locators.PPsubmitPayment_button_xpath
        self.AcceptCoockies_id = Locators.PPacceptCoockies_id

    def enter_PPusername(self, user):
        self.driver.find_element_by_id(self.Username_textbox_id).clear()
        self.driver.find_element_by_id(self.Username_textbox_id).send_keys(user)

    def click_on_next_button(self, driver):
        element = WebDriverWait(driver, 10).until(expected_conditions.
                                                  element_to_be_clickable((By.ID, self.NextButton_id)))
        element.click()

    def enter_PPpassword(self, pwd):
        self.driver.find_element_by_id(self.Password_textbox_id).clear()
        self.driver.find_element_by_id(self.Password_textbox_id).send_keys(pwd)

    def click_on_the_login_button(self, driver):
        element = WebDriverWait(driver, 10).until(expected_conditions.
                                                  element_to_be_clickable((By.ID, self.LoginButton_id)))
        element.click()

    def make_payment(self, driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_id(self.AcceptCoockies_id).click()

        bButtonExist = self.driver.find_element_by_xpath(self.makePaymentButton_xpath).is_displayed()
        WebDriverWait(driver, 60).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, self.makePaymentButton_xpath)))

        element = WebDriverWait(driver, 60).until(expected_conditions.
            element_to_be_clickable(
            (By.XPATH, self.makePaymentButton_xpath)))
        if bButtonExist:
            time.sleep(5)
            element.click()
        time.sleep(5)
