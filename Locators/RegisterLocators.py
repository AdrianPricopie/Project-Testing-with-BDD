from selenium.webdriver.common.by import By


class RegisterLocators:
    REGISTER_LINK_BUTTON = (By.PARTIAL_LINK_TEXT, 'Register')
    VALIDATE_ACCOUNT_PAGE = (By.CSS_SELECTOR, '.title')
    fields_dict = {
        'FIRST_NAME': (By.CSS_SELECTOR, 'input[id="customer.firstName"]'),
        'LAST_NAME': (By.CSS_SELECTOR, 'input[id="customer.lastName"]'),
        'ADDRESS': (By.CSS_SELECTOR, 'input[id="customer.address.street"]'),
        'CITY': (By.CSS_SELECTOR, 'input[id="customer.address.city"]'),
        'STATE': (By.CSS_SELECTOR, 'input[id="customer.address.state"]'),
        'ZIP_CODE': (By.CSS_SELECTOR, 'input[id="customer.address.zipCode"]'),
        'PHONE': (By.CSS_SELECTOR, 'input[id="customer.phoneNumber"]'),
        'SSN': (By.CSS_SELECTOR, 'input[id="customer.ssn"]'),
        'USERNAME': (By.CSS_SELECTOR, 'input[id="customer.username"]'),
        'PASSWORD': (By.CSS_SELECTOR, 'input[id="customer.password"]'),
        'CONFIRM_PASSWORD': (By.CSS_SELECTOR, '#repeatedPassword'),
    }
    field_message_error = {
        'FNAME_ERROR': (By.CSS_SELECTOR, 'span[id="customer.firstName.errors"]'),
        'LNAME_ERROR': (By.CSS_SELECTOR, 'span[id="customer.lastName.errors"]'),
        'ADDRESS_ERROR': (By.CSS_SELECTOR, 'span[id="customer.address.street.errors"]'),
        'CITY_ERROR': (By.CSS_SELECTOR, 'span[id="customer.address.city.errors"]'),
        'STATE_ERROR': (By.CSS_SELECTOR, 'span[id="customer.address.state.errors"]'),
        'ZIPCODE_ERROR': (By.CSS_SELECTOR, 'span[id="customer.address.zipCode.errors"]'),
        'SSN_ERROR': (By.CSS_SELECTOR, 'span[id="customer.ssn.errors"]'),
        'USERNAME_ERROR': (By.CSS_SELECTOR, 'span[id="customer.username.errors"]'),
        'PASSWORD_ERROR': (By.CSS_SELECTOR, 'span[id="customer.password.errors"]'),
        'CONFIRM_PASSWORD_ERROR': (By.CSS_SELECTOR, 'span[id="repeatedPassword.errors"]'),
    }
    WELCOME_MESSAGE_PAGE = (By.CSS_SELECTOR, '.title')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[value="Register"]')
    LOG_OUT = (By.PARTIAL_LINK_TEXT, 'Log')
