import pytest
from Steps.CommunSteps import connect_to_website, navigate_to_login_page, enter_credentials, click_on_login_button, \
    adding_funds, acceding_paypal, PP_login, enter_PPCredentials,Payment_validation_and_logout
from Pages.Payment_PaypalPage import PP_Payment_Page
from Utilities.ReadProperties import ReadConfig
from Utilities.Logger import LogGen
from Pages.conftest import browser


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()

    logger = LogGen.loggen()

    @pytest.mark.E2E
    def test_adding_funds_PHPTravels(self, browser):
        connect_to_website(self, browser)
        navigate_to_login_page(self, browser)
        username = ReadConfig.getUseremail()
        password = ReadConfig.getPassword()
        enter_credentials(self, browser, username, password)
        click_on_login_button(self, browser)
        adding_funds(self, browser)
        acceding_paypal(self, browser)
        PP_payment = PP_Payment_Page(browser)
        pp_username = PP_payment.get_username()
        pp_pswrd = PP_payment.get_password()
        PP_login(self, browser)
        enter_PPCredentials(self, browser,pp_username,pp_pswrd)
        Payment_validation_and_logout(self,browser)

