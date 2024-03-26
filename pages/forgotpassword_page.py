import time

from Locators.ForgotPasswordLocators import ForgotPasswordLocators

from browser import Browser


class ForgotPasswordPage(Browser):

    def navigate_to_homepage(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')
        time.sleep(2)

    def click_forgot_password_button(self):
        self.driver.find_element(*ForgotPasswordLocators.FORGOT_LOGIN_BUTTON).click()

    def get_password_reset_page(self):
        return self.driver.find_element(*ForgotPasswordLocators.VALIDATE_ACCOUNT_PAGE).text

    def click_find_login_info_button(self):
        self.driver.find_element(*ForgotPasswordLocators.FIND_LOGIN_INFO_BUTTON).click()

    def get_error_message_empty_fields(self):
        firstname_error = self.driver.find_element(*ForgotPasswordLocators.FNAME_ERROR).text
        lastname_error = self.driver.find_element(*ForgotPasswordLocators.LNAME_ERROR).text
        address_error = self.driver.find_element(*ForgotPasswordLocators.ADDRESS_ERROR).text
        city_error = self.driver.find_element(*ForgotPasswordLocators.CITY_ERROR).text
        state_error = self.driver.find_element(*ForgotPasswordLocators.STATE_ERROR).text
        zipcode_error = self.driver.find_element(*ForgotPasswordLocators.ZIPCODE_ERROR).text
        ssn_error = self.driver.find_element(*ForgotPasswordLocators.SSN_ERROR).text

        error_messages = f'{firstname_error},{lastname_error},{address_error},{city_error},{state_error},{zipcode_error},{ssn_error}'

        return error_messages

    def enter_firstname(self, firstname):
        self.driver.find_element(*ForgotPasswordLocators.FIRST_NAME_FIELD).send_keys(firstname)

    def enter_lastname(self, lastname):
        self.driver.find_element(*ForgotPasswordLocators.LAST_NAME_FIELD).send_keys(lastname)

    def enter_address(self, address):
        self.driver.find_element(*ForgotPasswordLocators.ADDRESS_FIELD).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(*ForgotPasswordLocators.CITY_FIELD).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*ForgotPasswordLocators.STATE_FIELD).send_keys(state)

    def enter_zipcode(self, zipcode):
        self.driver.find_element(*ForgotPasswordLocators.ZIP_CODE_FIELD).send_keys(zipcode)

    def enter_ssn(self, ssn):
        self.driver.find_element(*ForgotPasswordLocators.SSN_FILED).send_keys(ssn)

    def get_error_message_wrong_credentials(self):
        return self.driver.find_element(*ForgotPasswordLocators.ERROR_MESSAGE).text

    def get_information_page(self):
        return self.driver.find_element(*ForgotPasswordLocators.GET_INFORMATION_PAGE).text

    def log_out(self):
        self.driver.find_element(*ForgotPasswordLocators.LOG_OUT).click()
        time.sleep(2)

