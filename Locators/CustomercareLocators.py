from selenium.webdriver.common.by import By


class CustomercareLocators:
    NAME_FIELD = (By.CSS_SELECTOR, '#name')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#email')
    PHONE_FIELD = (By.CSS_SELECTOR, '#phone')
    MESSAGE_FIELD = (By.CSS_SELECTOR, '#message')
    SEND_BUTTON = (By.CSS_SELECTOR, 'input[value="Send to Customer Care"]')
    NAME_ERROR = (By.CSS_SELECTOR, 'span[id="name.errors"]')
    EMAIL_ERROR = (By.CSS_SELECTOR, 'span[id="email.errors"]')
    PHONE_ERROR = (By.CSS_SELECTOR, 'span[id="phone.errors"]')
    MESSAGE_ERROR = (By.CSS_SELECTOR, 'span[id="message.errors"]')
    THANK_YOU_MESSAGE  = (By.XPATH, '//*[@id="rightPanel"]/p[1]')
