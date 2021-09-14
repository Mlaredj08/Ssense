class Locators():
    # LoginPage Elements

    Username_textbox_name = "email"
    Password_textbox_name = "password"
    LoginButton_xpath = "//form[@method='POST']//button[@type='submit']"

    # HomePage Elements
    Login_button_xpath = "/html/body/header/div[1]/div/div/div[2]/div/div/a[2]"

    # AccountPage Elements
    Add_Funds_button_xpath = "//a[text()=' Add Funds']"
    Paypal_button_xpath = "//img[@alt='paypal']"
    PayNow_button_xpath = "//button[text()='Pay Now ']"
    PaymentMsg_xpath="/html/body/section[1]/div/div[2]/div/div[1]/div/div/div[2]/p[2]"
    LogOut_button_xpath = "///html/body/div[1]/div/div[3]/ul/li[5]/a']"

    # PaymentPage Elements
    PP_Login_button_xpath = "/html/body/div[1]/div/div/div/div[1]"

    # Chekout_PaypalPage elements
    PPUsername_textbox_id = "email"
    PPNextButton_id = "btnNext"
    PPPassword_textbox_id = "password"
    PPLoginButton_id = "btnLogin"
    PPsubmitPayment_button_xpath = "//button[@id='payment-submit-btn']"
    PPacceptCoockies_id = "acceptAllButton"
