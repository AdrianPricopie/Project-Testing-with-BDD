from selenium.common import NoSuchElementException

from browser import Browser
from Locators.RegisterLocators import RegisterLocators


class RegisterPage(Browser):

    def navigate_to_home_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def click_on_register_link_button(self):
        self.driver.find_element(*RegisterLocators.REGISTER_LINK_BUTTON).click()

    def get_register_page(self):
        return self.driver.find_element(*RegisterLocators.VALIDATE_ACCOUNT_PAGE).text

    def click_register_button(self):
        self.driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    def click_log_out(self):
        self.driver.find_element(*RegisterLocators.LOG_OUT).click()

    def get_error_messages(self):
        error_messages = []
        for locator in RegisterLocators.field_message_error.values():
            error_messages.append(self.driver.find_element(*locator).text)

        return ",".join(error_messages)

    def get_confirm_password_error(self):
        return self.driver.find_element(*RegisterLocators.field_message_error['CONFIRM_PASSWORD_ERROR']).text

    def enter_first_name(self, firstname):
        self.driver.find_element(*RegisterLocators.fields_dict['FIRST_NAME']).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*RegisterLocators.fields_dict['LAST_NAME']).send_keys(lastname)

    def enter_adress(self, adress):
        self.driver.find_element(*RegisterLocators.fields_dict['ADDRESS']).send_keys(adress)

    def enter_city(self, city):
        self.driver.find_element(*RegisterLocators.fields_dict['CITY']).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*RegisterLocators.fields_dict['STATE']).send_keys(state)

    def enter_zip_code(self, zipcode):
        self.driver.find_element(*RegisterLocators.fields_dict['ZIP_CODE']).send_keys(zipcode)

    def enter_phone(self, phone):
        self.driver.find_element(*RegisterLocators.fields_dict['PHONE']).send_keys(phone)

    def enter_ssn(self, ssn):
        self.driver.find_element(*RegisterLocators.fields_dict['SSN']).send_keys(ssn)

    def enter_username(self, username):
        self.driver.find_element(*RegisterLocators.fields_dict['USERNAME']).send_keys(username)

    def enter_password(self, passw):
        self.driver.find_element(*RegisterLocators.fields_dict['PASSWORD']).send_keys(passw)

    def enter_confirm_password(self, confpassw):
        self.driver.find_element(*RegisterLocators.fields_dict['CONFIRM_PASSWORD']).send_keys(confpassw)

    def get_welcome_page(self):
        return self.driver.find_element(*RegisterLocators.WELCOME_MESSAGE_PAGE).text

    def leave_all_the_field(self):
        # Iterați prin toate cheile din dicționarul RegisterLocators.FIELDS
        for field, locator in RegisterLocators.fields_dict.items():
            # Lăsați câmpul gol
            self.driver.find_element(*locator).clear()

    def is_error_message_displayed(self):
        # Verificăm dacă un mesaj de eroare este afișat pe pagină
        error_messages = []
        for locator in RegisterLocators.field_message_error.values():
            try:
                error_message = self.driver.find_element(*locator).text
                if error_message:
                    error_messages.append(error_message)
            except NoSuchElementException:
                pass  # Ignorăm excepțiile în cazul în care locatorul nu este găsit

        # Verificăm dacă lista de mesaje de eroare nu este goală
        return len(error_messages) > 0
