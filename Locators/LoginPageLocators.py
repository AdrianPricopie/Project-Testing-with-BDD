from selenium.webdriver.common.by import By


class LoginPageLocators:
    USERNAME_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[type="text"]')
    PASSWORD_FIELD_SELECTOR = (By.CSS_SELECTOR, 'input[type="password"]')
    LOGIN_BUTTON_SELECTOR = (By.CSS_SELECTOR, 'input[type="submit"]')
    TITLE_ERROR_LOGIN_SELECTOR = (By.CSS_SELECTOR, '.error')
    LOGIN_DASHBOARD = (By.CSS_SELECTOR, 'h1.title')
    LOG_OUT_BUTTON = (By.PARTIAL_LINK_TEXT, 'Log')