from Locators.CustomercareLocators import CustomercareLocators

from browser import Browser


class CustomerCarePage(Browser):
    def navigate_to_contact_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/contact.htm')

    def press_send_button(self):
        self.driver.find_element(*CustomercareLocators.SEND_BUTTON).click()

    def get_error_message_required_fields(self):
        name_error = self.driver.find_element(*CustomercareLocators.NAME_ERROR).text
        email_error = self.driver.find_element(*CustomercareLocators.EMAIL_ERROR).text
        phone_error = self.driver.find_element(*CustomercareLocators.PHONE_ERROR).text
        message_error = self.driver.find_element(*CustomercareLocators.MESSAGE_ERROR).text

        error_messages = f'{name_error},{email_error},{phone_error},{message_error}'
        return error_messages

    def enter_name(self,name):
        self.driver.find_element(*CustomercareLocators.NAME_FIELD).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*CustomercareLocators.EMAIL_FIELD).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*CustomercareLocators.PHONE_FIELD).send_keys(phone)

    def enter_message(self,message):
        self.driver.find_element(*CustomercareLocators.MESSAGE_FIELD).send_keys(message)

    def get_error_message_email_field(self):
        return self.driver.find_element(*CustomercareLocators.EMAIL_ERROR).text

    def get_error_message_phone_field(self):
        return self.driver.find_element(*CustomercareLocators.PHONE_ERROR).text

    def get_thank_you_message(self):
        return self.driver.find_element(*CustomercareLocators.THANK_YOU_MESSAGE).text


