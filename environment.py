import time

from browser import Browser
from pages.customercare_page import CustomerCarePage
from pages.forgotpassword_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def before_all(context):
    context.browser = Browser()
    context.LoginPage = LoginPage()
    context.CustomerCarePage = CustomerCarePage()
    context.ForgotPasswordPage = ForgotPasswordPage()
    context.RegisterPage = RegisterPage()


def after_all(context):
    time.sleep(2)
    context.browser.driver.close()
