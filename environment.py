from browser import Browser
from pages.customercare_page import CustomerCarePage
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.LoginPage = LoginPage()
    context.CustomerCarePage = CustomerCarePage()


def after_all(context):
    context.browser.close()
