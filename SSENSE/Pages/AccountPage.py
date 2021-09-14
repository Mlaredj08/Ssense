from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.Locators import Locators


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

        self.AddFunds_Button_xpath = Locators.Add_Funds_button_xpath
        self.Click_on_paypal_xpath = Locators.Paypal_button_xpath
        self.PayNow_button_xpath = Locators.PayNow_button_xpath
        self.PaymentMsg_xpath = Locators.PaymentMsg_xpath
        self.logout_button_xpath = Locators.LogOut_button_xpath

    def click_on_addfunds_button(self, driver):
        element = WebDriverWait(driver, 10).until(expected_conditions.
                                                  element_to_be_clickable((By.XPATH, self.AddFunds_Button_xpath)))
        element.click()

    def Paypal_Payment(self, driver):
        element = WebDriverWait(driver, 10).until(expected_conditions.
                                                  element_to_be_clickable((By.XPATH, self.Click_on_paypal_xpath)))
        element.click()

        btnPayNow = WebDriverWait(driver, 10).until(expected_conditions.
                                                    element_to_be_clickable((By.XPATH, self.PayNow_button_xpath)))
        btnPayNow.click()

    def payment_succes(self, driver):

        Account_window = driver.window_handles[0]
        driver.switch_to_window(Account_window)
        SuccesMsg = self.driver.find_element_by_xpath(self.PaymentMsg_xpath).text
        return SuccesMsg

    def logout(self, driver):
        element = WebDriverWait(driver, 10).until(expected_conditions.
                                                  element_to_be_clickable((By.XPATH, self.logout_button_xpath)))
        element.click()
