from tkinter import messagebox

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.Locators import Locators


class PP_Payment_Page:
    def __init__(self, driver):
        self.driver = driver
        self.Paypal_button = Locators.PP_Login_button_xpath

    def get_username(self):
        PPuser = self.driver.find_element_by_xpath("//p[contains(text(),'Email')]").text
        PPusername=PPuser.split(":")[1].strip()
        return PPusername

    def get_password(self):
        PPpwrd = self.driver.find_element_by_xpath("//p[contains(text(),'Password')]").text
        PPpassword = PPpwrd.split(":")[1].strip()
        return PPpassword

    def login_to_Paypal(self):
        self.driver.find_element_by_xpath(self.Paypal_button).click()





