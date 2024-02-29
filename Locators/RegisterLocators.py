from selenium.webdriver.common.by import By


class RegisterLocators:
    REGISTER_LINK_BUTTON = (By.PARTIAL_LINK_TEXT, 'Register')
    VALIDATE_ACCOUNT_PAGE = (By.CSS_SELECTOR, '.title')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, 'input[id="customer.firstName"]')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, 'input[id="customer.lastName"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[id="customer.address.street"]')
    CITY_FIELD = (By.CSS_SELECTOR, 'input[id="customer.address.city"]')
    STATE_FIELD = (By.CSS_SELECTOR, 'input[id="customer.address.state"]')
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, 'input[id="customer.address.zipCode"]')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[id="customer.phoneNumber"]')
    SSN_FILED = (By.CSS_SELECTOR, 'input[id="customer.ssn"]')
    USERNAME_FIELD = (By.CSS_SELECTOR, 'input[id="customer.username"]')
    PASSWORD_FIELD = (By.CSS_SELECTOR, 'input[id="customer.password"]')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#repeatedPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'input[value="Register"]')
    FNAME_ERROR = (By.CSS_SELECTOR, 'span[id="customer.firstName.errors"]')
    LNAME_ERROR = (By.CSS_SELECTOR, 'span[id="customer.lastName.errors"]')
    ADDRESS_ERROR = (By.CSS_SELECTOR, 'span[id="customer.address.street.errors"]')
    CITY_ERROR = (By.CSS_SELECTOR, 'span[id="customer.address.city.errors"]')
    STATE_ERROR = (By.CSS_SELECTOR, 'span[id="customer.address.state.errors"]')
    ZIPCODE_ERROR = (By.CSS_SELECTOR, 'span[id="customer.address.zipCode.errors"]')
    SSN_ERROR = (By.CSS_SELECTOR, 'span[id="customer.ssn.errors"]')
    USERNAME_ERROR = (By.CSS_SELECTOR, 'span[id="customer.username.errors"]')
    PASSWORD_ERROR = (By.CSS_SELECTOR, 'span[id="customer.password.errors"]')
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, 'span[id="repeatedPassword.errors"]')
    WELCOME_MESSAGE_PAGE = (By.CSS_SELECTOR, '.title')




