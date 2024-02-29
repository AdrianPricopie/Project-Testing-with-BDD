from browser import Browser
from Locators.RegisterLocators import RegisterLocators

class RegisterPage(Browser):


    def home_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def click_on_register_link_button(self):
        self.driver.find_element(*RegisterLocators.REGISTER_LINK_BUTTON).click()

    def get_register_page(self):
        self.driver.find_element(*RegisterLocators.VALIDATE_ACCOUNT_PAGE).text

    def click_register_button(self):
        self.driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    def get_error_messages(self):
        firstname_error = self.driver.find_element(*RegisterLocators.FNAME_ERROR).text
        lastname_error = self.driver.find_element(*RegisterLocators.LNAME_ERROR).text
        address_error = self.driver.find_element(*RegisterLocators.ADDRESS_ERROR).text
        city_error = self.driver.find_element(*RegisterLocators.CITY_ERROR).text
        state_error = self.driver.find_element(*RegisterLocators.STATE_ERROR).text
        zipcode_error = self.driver.find_element(*RegisterLocators.ZIPCODE_ERROR).text
        ssn_error = self.driver.find_element(*RegisterLocators.SSN_ERROR).text
        username_error = self.driver.find_element(*RegisterLocators.USERNAME_ERROR).text
        password_error = self.driver.find_element(*RegisterLocators.PASSWORD_ERROR).text
        confirm_password_error = self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD_ERROR).text

        error_messages_fields = f'{firstname_error},{lastname_error},{address_error},{city_error},{state_error},{zipcode_error},{ssn_error},{username_error},{password_error},{confirm_password_error}'

        return error_messages_fields

    def enter_first_name(self, firstname):
        self.driver.find_element(*RegisterLocators.FIRST_NAME_FIELD).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*RegisterLocators.LAST_NAME_FIELD).send_keys(lastname)

    def enter_adress(self, adress):
        self.driver.find_element(*RegisterLocators.ADDRESS_FIELD).send_keys(adress)

    def enter_city(self, city):
        self.driver.find_element(*RegisterLocators.CITY_FIELD).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*RegisterLocators.STATE_FIELD).send_keys(state)

    def enter_zip_code(self, zipcode):
        self.driver.find_element(*RegisterLocators.ZIP_CODE_FIELD).send_keys(zipcode)

    def enter_phone(self, phone):
        self.driver.find_element(*RegisterLocators.PHONE_FIELD).send_keys(phone)

    def enter_ssn(self, ssn):
        self.driver.find_element(*RegisterLocators.SSN_FILED).send_keys(ssn)

    def enter_username(self, username):
        self.driver.find_element(*RegisterLocators.USERNAME_FIELD).send_keys(username)

    def enter_password(self, passw):
        self.driver.find_element(*RegisterLocators.PASSWORD_FIELD).send_keys(passw)

    def enter_confirm_password(self, confpassw):
        self.driver.find_element(*RegisterLocators.CONFIRM_PASSWORD_FIELD).send_keys(confpassw)

    def get_welcome_page(self):
        self.driver.find_element(*RegisterLocators.WELCOME_MESSAGE_PAGE).text


