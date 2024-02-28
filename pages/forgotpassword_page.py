import time

from selenium.webdriver.common.by import By

from browser import Browser


class ForgotPasswordPage(Browser):
    FORGOT_LOGIN_BUTTON_SELECTOR = (By.PARTIAL_LINK_TEXT, 'Forgot')
    VALIDATE_ACCOUNT_PAGE = (By.CSS_SELECTOR, '.title')
    FIRST_NAME_FIELD_SELECTOR = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_FIELD_SELECTOR = (By.CSS_SELECTOR, '#lastName')
    ADDRESS_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[id="address.street"]')
    CITY_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[id="address.city"]')
    STATE_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[id="address.state"]')
    ZIP_CODE_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[id="address.zipCode"]')
    SSN_FILED_SELECTOR = (By.CSS_SELECTOR, '#ssn')
    FIND_LOGIN_INFO_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'input[value="Find My Login Info"]')
    FNAME_ERROR = (By.CSS_SELECTOR, 'span[id="firstName.errors"]')
    LNAME_ERROR = (By.CSS_SELECTOR, 'span[id="lastName.errors"]')
    ADDRESS_ERROR = (By.CSS_SELECTOR, 'span[id="address.street.errors"]')
    CITY_ERROR = (By.CSS_SELECTOR, 'span[id="address.city.errors"]')
    STATE_ERROR = (By.CSS_SELECTOR, 'span[id="address.state.errors"]')
    ZIPCODE_ERROR = (By.CSS_SELECTOR, 'span[id="address.zipCode.errors"]')
    SSN_ERROR = (By.CSS_SELECTOR, 'span[id="ssn.errors"]')
    ERROR_MESSAGE_SELECTOR = (By.CSS_SELECTOR, '.error')
    GET_INFORMATION_PAGE = (By.XPATH, '//*[@id="rightPanel"]/p[1]')
    LOG_OUT_SELECTOR = (By.PARTIAL_LINK_TEXT, 'Log')

    def navigate_to_homepage(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def click_forgot_password_button(self):
        self.driver.find_element(*self.FORGOT_LOGIN_BUTTON_SELECTOR).click()

    def get_password_reset_page(self):
        return self.driver.find_element(*self.VALIDATE_ACCOUNT_PAGE).text

    def click_find_login_info_button(self):
        self.driver.find_element(*self.FIND_LOGIN_INFO_BUTTON_SELECTOR).click()

    def get_error_message_empty_fields(self):
        firstname_error = self.driver.find_element(*self.FNAME_ERROR).text
        lastname_error = self.driver.find_element(*self.LNAME_ERROR).text
        address_error = self.driver.find_element(*self.ADDRESS_ERROR).text
        city_error = self.driver.find_element(*self.CITY_ERROR).text
        state_error = self.driver.find_element(*self.STATE_ERROR).text
        zipcode_error = self.driver.find_element(*self.ZIPCODE_ERROR).text
        ssn_error = self.driver.find_element(*self.SSN_ERROR).text

        error_messages = f'{firstname_error},{lastname_error},{address_error},{city_error},{state_error},{zipcode_error},{ssn_error}'

        return error_messages

    def enter_firstname(self,firstname):
        self.driver.find_element(*self.FIRST_NAME_FIELD_SELECTOR).send_keys(firstname)

    def enter_lastname(self,lastname):
        self.driver.find_element(*self.LAST_NAME_FIELD_SELECTOR).send_keys(lastname)

    def enter_address(self,address):
        self.driver.find_element(*self.ADDRESS_FIELD_SELECTOR).send_keys(address)

    def enter_city(self,city):
        self.driver.find_element(*self.CITY_FIELD_SELECTOR).send_keys(city)

    def enter_state(self,state):
        self.driver.find_element(*self.STATE_FIELD_SELECTOR).send_keys(state)

    def enter_zipcode(self,zipcode):
        self.driver.find_element(*self.ZIP_CODE_FIELD_SELECTOR).send_keys(zipcode)

    def enter_ssn(self,ssn):
        self.driver.find_element(*self.SSN_FILED_SELECTOR).send_keys(ssn)

    def get_error_message_wrong_credentials(self):
        return self.driver.find_element(*self.ERROR_MESSAGE_SELECTOR).text

    def get_information_page(self):
        return self.driver.find_element(*self.GET_INFORMATION_PAGE).text

    def log_out(self):
        self.driver.find_element(*self.LOG_OUT_SELECTOR).click()
        time.sleep(2)

