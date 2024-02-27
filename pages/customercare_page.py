from selenium.webdriver.common.by import By

from browser import Browser


class CustomerCarePage(Browser):
    NAME_FIELD_SELECTOR = (By.CSS_SELECTOR, '#name')
    EMAIL_FIELD_SELECTOR = (By.CSS_SELECTOR, '#email')
    PHONE_FIELD_SELECTOR = (By.CSS_SELECTOR, '#phone')
    MESSAGE_FIELD_SELECTOR = (By.CSS_SELECTOR, '#message')
    SEND_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'input[value="Send to Customer Care"]')
    NAME_ERROR_SELECTOR = (By.CSS_SELECTOR, 'span[id="name.errors"]')
    EMAIL_ERROR_SELECTOR = (By.CSS_SELECTOR, 'span[id="email.errors"]')
    PHONE_ERROR_SELECTOR = (By.CSS_SELECTOR, 'span[id="phone.errors"]')
    MESSAGE_ERROR_SELECTOR = (By.CSS_SELECTOR, 'span[id="message.errors"]')
    THANK_YOU_MESSAGE_SELECTOR = (By.XPATH, '//*[@id="rightPanel"]/p[1]')

    def navigate_to_contact_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/contact.htm')

    def press_send_button(self):
        self.driver.find_element(*self.SEND_BUTTON_SELECTOR).click()

    def get_error_message_required_fields(self):
        name_error = self.driver.find_element(*self.NAME_ERROR_SELECTOR).text
        email_error = self.driver.find_element(*self.EMAIL_ERROR_SELECTOR).text
        phone_error = self.driver.find_element(*self.PHONE_ERROR_SELECTOR).text
        message_error = self.driver.find_element(*self.MESSAGE_ERROR_SELECTOR).text

        error_messages = f'{name_error},{email_error},{phone_error},{message_error}'
        return error_messages

    def enter_name(self,name):
        self.driver.find_element(*self.NAME_FIELD_SELECTOR).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.EMAIL_FIELD_SELECTOR).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*self.PHONE_FIELD_SELECTOR).send_keys(phone)

    def enter_message(self,message):
        self.driver.find_element(*self.MESSAGE_FIELD_SELECTOR).send_keys(message)

    def get_error_message_email_field(self):
        return self.driver.find_element(*self.EMAIL_ERROR_SELECTOR).text

    def get_error_message_phone_field(self):
        return self.driver.find_element(*self.PHONE_ERROR_SELECTOR).text

    def get_thank_you_message(self):
        return self.driver.find_element(*self.THANK_YOU_MESSAGE_SELECTOR).text


