import time

from selenium.webdriver.common.by import By

from browser import Browser


class LoginPage(Browser):
    USERNAME_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[type="text"]')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'input[type="submit"]')
    TITLE_ERROR_LOGIN_SELECTOR = (By.CSS_SELECTOR, '.error')
    LOGIN_DASHBOARD = (By.CSS_SELECTOR, 'h1.title')
    LOG_OUT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Log')

    def navigate_to_login_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC')

    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_FIELD_SELECTOR).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON_SELECTOR).click()

    def get_error_message(self):
        return self.driver.find_element(*self.TITLE_ERROR_LOGIN_SELECTOR).text

    def leave_both_username_password_field(self):
        self.driver.find_element(*self.USERNAME_FIELD_SELECTOR).clear()
        self.driver.find_element(*self.PASSWORD_FIELD_SELECTOR).click()

    def leave_username_field_empty(self):
        self.driver.find_element(*self.USERNAME_FIELD_SELECTOR).clear()

    def get_dashboard_page(self):
        return self.driver.find_element(*self.LOGIN_DASHBOARD).text

    def log_out(self):
        self.driver.find_element(*self.LOG_OUT_BUTTON).click()
        time.sleep(2)
