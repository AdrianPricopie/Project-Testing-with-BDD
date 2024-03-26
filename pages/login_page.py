from datetime import datetime
from selenium.common import NoSuchElementException
from browser import Browser
from Locators.LoginPageLocators import LoginPageLocators


class LoginPage(Browser):

    def navigate_to_login_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm?ConnType=JDBC')

    def enter_username(self, username):
        try:
            self.driver.find_element(*LoginPageLocators.USERNAME_FIELD_SELECTOR).send_keys(username)
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_for_enter_username_login_page_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_password(self, password):
        try:
            self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD_SELECTOR).send_keys(password)
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_for_enter_password_login_page_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def click_login_button(self):
        try:
            self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON_SELECTOR).click()
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_for_login_button_login_page_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_error_message(self):
        try:
            return self.driver.find_element(*LoginPageLocators.TITLE_ERROR_LOGIN_SELECTOR).text
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_for_login_selector_from_page_login_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def leave_both_username_password_field(self):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD_SELECTOR).clear()
        self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD_SELECTOR).click()

    def leave_username_field_empty(self):
        self.driver.find_element(*LoginPageLocators.USERNAME_FIELD_SELECTOR).clear()

    def get_dashboard_page(self):
        try:
            return self.driver.find_element(*LoginPageLocators.LOGIN_DASHBOARD).text
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_get_dashboarrd_selector_from_page_login_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def log_out(self):
        try:
            self.driver.find_element(*LoginPageLocators.LOG_OUT_BUTTON).click()
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_for_login_click_button_from_page_login_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")
