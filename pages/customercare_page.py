from datetime import datetime

from selenium.common import NoSuchElementException

from Locators.CustomercareLocators import CustomercareLocators

from browser import Browser


class CustomerCarePage(Browser):
    def navigate_to_contact_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/contact.htm')

    def press_send_button(self):
        try:
            self.driver.find_element(*CustomercareLocators.SEND_BUTTON).click()
        except NoSuchElementException:
            print("Butonul press button nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_send_button_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_error_message_required_fields(self):
        try:
            name_error = self.driver.find_element(*CustomercareLocators.NAME_ERROR).text
            email_error = self.driver.find_element(*CustomercareLocators.EMAIL_ERROR).text
            phone_error = self.driver.find_element(*CustomercareLocators.PHONE_ERROR).text
            message_error = self.driver.find_element(*CustomercareLocators.MESSAGE_ERROR).text

            error_messages = f'{name_error},{email_error},{phone_error},{message_error}'
            return error_messages
        except NoSuchElementException:
            print("Butonul press button nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Elements_error_for_requireds_fields_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_name(self, name):
        try:
            self.driver.find_element(*CustomercareLocators.NAME_FIELD).send_keys(name)
        except NoSuchElementException:
            print("Campul pentru introducere nume nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_name_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_email(self, email):
        try:
            self.driver.find_element(*CustomercareLocators.EMAIL_FIELD).send_keys(email)
        except NoSuchElementException:
            print("Campul pentru introducere email nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_email_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_phone(self, phone):
        try:
            self.driver.find_element(*CustomercareLocators.PHONE_FIELD).send_keys(phone)
        except NoSuchElementException:
            print("Campul pentru introducere telefon  nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_phone_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_message(self, message):
        try:
            self.driver.find_element(*CustomercareLocators.MESSAGE_FIELD).send_keys(message)
        except NoSuchElementException:
            print("Campul pentru enter message  nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_message_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_error_message_email_field(self):
        try:
            return self.driver.find_element(*CustomercareLocators.EMAIL_ERROR).text
        except NoSuchElementException:
            print("Campul pentru get error message email field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_message_email_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_error_message_phone_field(self):
        try:
            return self.driver.find_element(*CustomercareLocators.PHONE_ERROR).text
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_message_phone_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_thank_you_message(self):
        try:
            return self.driver.find_element(*CustomercareLocators.THANK_YOU_MESSAGE).text
        except NoSuchElementException:
            print("Mesajul thank you nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_thank_you_message_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def leave_name_email_phone_message_fields_empty(self):
        self.driver.find_element(*CustomercareLocators.NAME_FIELD).clear()
        self.driver.find_element(*CustomercareLocators.EMAIL_FIELD).clear()
        self.driver.find_element(*CustomercareLocators.PHONE_FIELD).clear()
