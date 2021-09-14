import time
from tkinter import messagebox

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from Utilities.ReadProperties import ReadConfig
from Utilities.Logger import LogGen
from Pages.AccountPage import AccountPage
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Pages.Payment_PaypalPage import PP_Payment_Page
from Pages.Checkout_PaypalPage import Checkout_PaypalPage

logger = LogGen.loggen()


def connect_to_website(self, driver):
    self.logger.info("*************** Test_001_Login *****************")
    self.logger.info("****Started Connect to the website ****")
    self.driver = driver
    self.logger.info("****Opening URL****")
    self.driver.get(ReadConfig.getApplicationURL())
    act_title = self.driver.title

    if act_title == "PHPTRAVELS - PHPTRAVELS":
        self.logger.info("**** Home page title test passed ****")
        assert True
    else:
        self.logger.error("**** Home page title test failed****")
        self.driver.save_screenshot(".\\Screenshots\\" + "homePage.png")
        self.driver.close()
        assert False


def navigate_to_login_page(self, driver):
    home = HomePage(driver)
    self.logger.info("****Click on the login button ****")
    home.click_on_login_button()
    self.driver = driver
    self.logger.info("****Opening the login page****")
    act_title = self.driver.title

    if act_title == "Login - PHPTRAVELS":
        self.logger.info("**** Opening the login page passed ****")
        assert True
    else:
        self.logger.error("**** Opening the login page failed****")
        self.driver.save_screenshot(".\\Screenshots\\" + "loginPage.png")
        self.driver.close()
        assert False


def enter_credentials(self, driver, username, password):
    self.logger.info("****Entering credentials ****")
    login = LoginPage(driver)
    login.enter_username(username)
    login.enter_password(password)


def click_on_login_button(self, driver):
    self.logger.info("****Clicking on login button ****")
    login = LoginPage(driver)
    login.click_on_the_login_button(driver)
    self.logger.info("****Opening the account page****")
    act_title = self.driver.title

    if act_title == "Dashboard - PHPTRAVELS":
        self.logger.info("**** Opening the account page passed ****")
        assert True
    else:
        self.logger.error("**** Opening the account page failed****")
        self.driver.save_screenshot(".\\Screenshots\\" + "accountPage.png")
        self.driver.close()
        assert False


def adding_funds(self, driver):
    account = AccountPage(driver)
    account.click_on_addfunds_button(driver)
    self.logger.info("****Opening Add funds page****")
    act_title = WebDriverWait(driver, 20).until(
        expected_conditions.visibility_of_all_elements_located((By.XPATH, "//h3[contains(@class,'title')]")))
    titles = []
    for title in act_title:
        titles.append(title.text)

    if titles[0] == "Add Funds":
        self.logger.info("**** Opening Add funds page passed ****")
        assert True
    else:
        self.logger.error("**** Opening Add funds page failed****")
        self.driver.save_screenshot(".\\Screenshots\\" + "AddFunds.png")
        self.driver.close()
        assert False


def acceding_paypal(self, driver):
    account = AccountPage(driver)
    account.Paypal_Payment(driver)
    self.logger.info("**** Opening PayPalLogin page ****")



def PP_login(self, driver):
    PP_payment = PP_Payment_Page(driver)
    PP_payment.login_to_Paypal()
    self.logger.info("**** Opening PayPal page ****")
    Paypal_window = driver.window_handles[1]
    driver.switch_to_window(Paypal_window)
    driver.maximize_window()
    act_title = self.driver.title

    if act_title == "PayPal":
        self.logger.info("**** Opening PayPal page passed ****")
        assert True
    else:
        self.logger.error("**** Opening PayPal page failed ****")
        self.driver.save_screenshot(".\\Screenshots\\" + "PayPalPage.png")
        self.driver.close()
        assert False


def enter_PPCredentials(self, driver, username, password):
    self.logger.info("**** Logging to PayPal page ****")
    Check_PP = Checkout_PaypalPage(driver)
    Check_PP.enter_PPusername(username)
    Check_PP.click_on_next_button(driver)
    Check_PP.enter_PPpassword(password)
    Check_PP.click_on_the_login_button(driver)
    Check_PP.make_payment(driver)


def Payment_validation_and_logout(self, driver):
    account = AccountPage(driver)
    ValidationMsg = account.payment_succes(driver)

    if ValidationMsg == "Your funds has been added to your account":
        self.logger.info("**** Add Funds passed ****")
        self.driver.close()
        assert True
    else:
        self.logger.error("**** Add Funds failed ****")
        self.driver.save_screenshot(".\\Screenshots\\" + "PaymentUnsuccessfull.png")
        self.driver.close()
        assert False
