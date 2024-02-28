from selenium.webdriver.common.by import By


class CustomercareLocators:
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
