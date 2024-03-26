# ParaBank Project Testing automation with python BDD selenium framework

## Test plan
This testing document is intended for the development team, testing team, and other stakeholders involved in the ParaBank Banking project. Additionally, it aims to provide a clear understanding of the testing process for all those interested in the quality and performance of the application.

## Revision History:

| Date       | Description                   | Author            | Comments          |
| ---------- | ----------------------------- | ------------------ | ------------------ |
| 26.02.2024 | Test Plan for version 1.0     | Pricopie Adrian   | Draft test plan    |
| 1.03.2024 | v1.1                          | Robert Furtuna    | Added more details for Test Process |

## Table of Content:
1. [Introduction](#introduction)
   - [Project Objective](#project-objective)
   - [Tools and Version](#tools-and-version)
   - [Functionalities in Scope](#functionalities-in-scope)
   - [Functionalities and Tests Out of Scope](#functionalities-and-tests-out-of-scope)
2. [Test Process](#test-process)
   - [Test Planning](#test-planning)
     - [Roles and Responsibilities](#roles-and-responsibilities)
     - [Entry Criteria](#entry-criteria)
     - [Exit Criteria](#exit-criteria)
     - [Risks](#risks)
   - [Test Analysis](#test-analysis)
   - [Test Design](#test-design)
   - [Test Implementation](#test-implementation)
   - [Test Execution](#test-execution)
   - [Test Closure](#test-closure)
   - [Test Monitoring and Control](#test-monitoring-and-control)
3. [Project Structure](#project-structure)
   - [Features](#features)
   - [Locators](#locators)
   - [Pages](#pages)
   - [Screenshots](#screenshots)
   - [Steps](#steps)
   - [Browser file](#browser-file)
   - [Environment file](#environment-file)
   - [Venv, Behave.ini, Requirements.txt](#venv-behave.ini-requirements.txt)
   - [Behave Script](#behave-script)
  
4. [Features Under Testing](#features-under-testing)
    - [Customer Care Functionality Testing](#customer-care-functionality-testing)
    - [Forgot Password Functionality Testing](#forgot-password-functionality-testing)
    - [Login Functionality Testing](#login-functionality-testing)
    - [Register Functionality Testing](#register-functionality-testing)

5. [Getting Started](#getting-started)
    - [Clone the Repository](#clone-the-repository)
    - [Install Dependencies](#install-dependencies)
    - [Activate the Virtual Environment](#activate-the-virtual-environment)
    - [Run the tests](#run-the-tests)
6. [Conclusion](#conclusion)

7. [Test Deliverables](#test-deliverables)
   - [Test Conditions](#test-conditions)
   - [Test Cases](#test-cases)
   - [Daily Test Summary Reports](#daily-test-summary-reports)
   - [Traceability Matrix](#traceability-matrix)
   - [Test Case Results](#test-case-results)
   - [Bugs Report](#bugs-report)
   - [Test Completion Report](#test-completion-report)
   - [Schedule](#schedule)

## Introduction:
- ParaBank is a demo site used for demonstration of Parasoft software solutions.
All materials herein are used solely for simulating a realistic online banking website.

### 1.1 Project Objective

- We need to raise the trust in the quality of the project as high as possible before releasing it to customers.
- Application under test: [ParaBank](https://parabank.parasoft.com/parabank/index.htm).

### 1.2 Tools and Versions
- **editor code used: pycharm**
- **Language: [![Python versions](https://img.shields.io/pypi/pyversions/pytest-snowflake_bdd.svg)](https://pypi.org/project/pytest-snowflake_bdd)** 
- **Library Versions:**
    ```bash
     behave==1.2.6
     selenium===4.18.1
     webdriver-manager==4.0.1
     behave-html-formatter == 0.9.10
    ```

### 1.3 Functionalities in Scope
- testing will primarily concentrate on the Chrome browser. 
- To ensure the quality and functionality of the ParaBank platform, the following functionalities will be included in functional testing and graphical user interface (GUI) testing: Forgot password, login, customercare, register.
- To ensure that new customers can successfully register and access the ParaBank services.
- To ensure that a customer can successfully log in and access the ParaBank services.
- To ensure that if a customer forgot their password, they can recover using the "Forgot Password" functionality.
- To ensure effective customer care functionality is in place, providing support and assistance to users as they interact with ParaBank services.

### 1.4 Functionalities and Tests Out of Scope

- Non-functional testing like stress, performance is beyond the scope of this project.
- No QA support for mobile applications developed. Only web applications will be tested.

# 2. Test Process:

## 2.1 Test Planning

### Roles and Responsibilities:

| Tester                    | Responsibilities                    |
|---------------------------|-------------------------------------|
| Anetta Bako(junior-mid)  | - Customercare testing             |
|                           | - Forgot password testing         |
| Pricopie Adrian(junior)   | - Login  testing                  |
| Robert Furtuna(senior)  | - Register testing  |

### Entry Criteria:

- Roles needed for the project are allocated.
- Functional specifications are defined.
- Approved Project Schedule

## Exit Criteria:

- To provide a confirmation message of successful registration.
- 90% of tests are passed.
- Completion of role allocation.
- Approval of the defined functional specifications.

## Risks:

### Project Risks:

- The risk of team members committing human errors at various stages of the project, including testing activities.
- The risk that one or more team members may become unavailable, thus affecting the progress of the project.
- Uncertainty or lack of communication following testing or the review process, leading to delays or misunderstandings of identified issues.

### Product Risks:

- Stability risks (crashes, disconnects, etc)
- IE browser might have performance issues
- The web page pagination could be impacted when opened on mobile devices
- Stress conditions might impact the web application
- New browser might not be supported

## 2.2 Test Analysis:

- Analyze the business requirements to ensure all details for creating test conditions are available.
- Identify the functional requirements for each functionality, including what data can be modified, what data can be deleted, and what new customer data can be added.

# 3. Project Structure:

This project follows the Behavior-Driven Development (BDD) design pattern, enhancing modularity and maintainability The pages directory encapsulates classes representing specific pages on the ParaBank website, each handling interactions and elements unique to that page.

Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

[*behave*](https://behave.readthedocs.io/en/latest/#) uses tests written in a natural language style, backed up by Python
code.

- **features**: Hold the specifications or scenarios written in Gherkin syntax. Gherkin is a human-readable format that describes the behavior of the software in plain language. Each feature file typically represents a feature or a user story of the application being developed, and it contains one or more scenarios that describe the various behaviors or functionalities of that feature.
```gherkin
Feature: CustomerCare Feature

  Background:
    Given I am on the contact page

  @empty_fields
  Scenario: Email support with empty fields
    When I leave name,email,phone,message fields empty
    And I press the send button
    Then I should see an error message for the required fields


  @wrong_email_format
  Scenario: Email support with wrong email format
    When I enter "Robert" in name field
    And I enter "abc" in email field
    And I enter "123" in phone field
    And I enter "need support message" in message field
    And I press the send button
    Then I should see an error message for the email field


  @wrong_phone_format
  Scenario: Email support with wrong phone format
    When I enter "Robert" in name field
    And I enter "abc@email.com" in email field
    And I enter "aaa" in phone field
    And I enter "need support message" in message field
    And I press the send button
    Then I should see an error message for the phone field

  @correct_credential
  Scenario: Email support with correct credentials
    When I enter "Robert" in name field
    And I enter "abc@email.com" in email field
    And I enter "123456789" in phone field
    And I enter "need support message" in message field
    And I press the send button
    Then I should see a Thank you message
```
```gherkin
Feature: ForgotPassword Feature

  Background:
    Given I am on the homepage
    And I click o the forgot password button
    Then I should be redirected to the password reset page

  @Forgot_password_empty_fields
  Scenario: Reset password with empty fields
    When I click on find my login info button
    Then I should see an error message for the empty fields

  @Forgot_password_wrong_credentials
  Scenario: Reset password with wrong credentials
    When I enter "aaa" in first name field
    And I enter "bbb" in last name field
    And I enter "ccc" in address field
    And I enter "ddd" in city field
    And I enter "eee" in state field
    And I enter "111" in zip code field
    And I enter "222" in SSN field
    And I click on find my login info button
    Then I should see an error message due to wrong credentials

  @Forgot_password_correct_credentials
  Scenario: Reset password with correct credentials
    When I enter "John" in first name field
    And I enter "Smith" in last name field
    And I enter "Main street" in address field
    And I enter "Anytown" in city field
    And I enter "California" in state field
    And I enter "123456" in zip code field
    And I enter "456789" in SSN field
    And I click on find my login info button
    Then I should been redirected to the get information page
    And I log out
```
```gherkin
Feature: Login Feature

  Background:
    Given I am on the login page

@wrong_credentials
Scenario Outline: Login with wrong credentials
  When I enter "<username>" in username field
  And I enter "<password>" in password field
  And I press login button
  Then I should see an internal error message

  Examples:
    | username  | password  |
    | robert123 | 123robert |
    | user1     | pass1     |
    | user2     | pass2     |

  @empty_username_and_password
  Scenario: Login with both empty username and password
    When I leave both username and password fields empty
    And I press login button
    Then I should see an error message

  @login_correct_credentials
  Scenario: Login with correct credentials
    When I enter "robert2" in username field
    And I enter "robert2" in password field
    And I press login button
    Then I should be redirected to the dashboard

  @empty_username_field
  Scenario: Login with empty username field
    When I leave username field empty
    And I enter "storm20" in password field
    And I press login button
    Then I should see an error message

```
```gherkin
Feature: Register Feature

  Background:
    Given I am on homepage
    And I click on register button
    Then I should be redirected to the register page

  @register_empty_fields
  Scenario: Register with empty fields
    When I leave all the fields empty
    And I click register button
    Then I should see an error message for empty fields


  @register_with_no_matched_passwords
  Scenario: Register with different password confirmation
    When I introduce "123" in password field
    And I introduce "321" in password confirmation filed
    And I click register button
    Then I should see an error message for unmatched passwords

  @register_correct_credentials
  Scenario: Register with correct credentials
    When I introduce "John" in first name field
    And I introduce "Smith" in last name field
    And I introduce "Main street" in address field
    And I introduce "Anytown" in city field
    And I introduce "California" in state field
    And I introduce "123456" in zip code field
    And I introduce "078 982 112" in phone field
    And I introduce "456789" in SSN field
    And I introduce "John Smith" in username field
    And I introduce "password" in password field
    And I introduce "password" in password confirmation filed
    And I click register button
    Then I should be redirected to a welcome page

   @register_wrong_credentials
  Scenario: Register with wrong credentials
    When I introduce "092" in first name field
    And I introduce "09d" in last name field
    And I introduce "123" in address field
    And I introduce "qwe" in city field
    And I introduce "aaa" in state field
    And I introduce "sss" in zip code field
    And I introduce "1As" in phone field
    And I introduce ",.;" in SSN field
    And I introduce a new username in username field
    And I introduce "password" in password field
    And I introduce "password" in password confirmation filed
    And I click register button
    Then I should see an error message for wrong credentials
```

- **locators**: Holds locator classes that store all the locators (CSS selectors, XPath ,etc.) used in the project. This separation ensures easy maintenance and updates if the locators change.
```python
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
    THANK_YOU_MESSAGE = (By.XPATH, '//*[@id="rightPanel"]/p[1]')
```
```python
from selenium.webdriver.common.by import By


class ForgotPasswordLocators:
    FORGOT_LOGIN_BUTTON = (By.PARTIAL_LINK_TEXT, 'Forgot')
    VALIDATE_ACCOUNT_PAGE = (By.CSS_SELECTOR, '.title')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_FIELD = (By.CSS_SELECTOR, '#lastName')
    ADDRESS_FIELD = (By.CSS_SELECTOR, 'input[id="address.street"]')
    CITY_FIELD = (By.CSS_SELECTOR, 'input[id="address.city"]')
    STATE_FIELD = (By.CSS_SELECTOR, 'input[id="address.state"]')
    ZIP_CODE_FIELD = (By.CSS_SELECTOR, 'input[id="address.zipCode"]')
    SSN_FILED = (By.CSS_SELECTOR, '#ssn')
    FIND_LOGIN_INFO_BUTTON = (By.CSS_SELECTOR, 'input[value="Find My Login Info"]')
    FNAME_ERROR = (By.CSS_SELECTOR, 'span[id="firstName.errors"]')
    LNAME_ERROR = (By.CSS_SELECTOR, 'span[id="lastName.errors"]')
    ADDRESS_ERROR = (By.CSS_SELECTOR, 'span[id="address.street.errors"]')
    CITY_ERROR = (By.CSS_SELECTOR, 'span[id="address.city.errors"]')
    STATE_ERROR = (By.CSS_SELECTOR, 'span[id="address.state.errors"]')
    ZIPCODE_ERROR = (By.CSS_SELECTOR, 'span[id="address.zipCode.errors"]')
    SSN_ERROR = (By.CSS_SELECTOR, 'span[id="ssn.errors"]')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.error')
    GET_INFORMATION_PAGE = (By.XPATH, '//*[@id="rightPanel"]/p[1]')
    LOG_OUT = (By.PARTIAL_LINK_TEXT, 'Log')
```
```python
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

```
By: Enumeration class provided by the Selenium WebDriver library. It is used to specify the mechanism by which elements on a web page will be located. These locators will be used by the test automation code to find and interact with the corresponding elements on the web page. Using By ensures a consistent and reliable way to locate elements across different web pages and browsers.

- **pages**: Contains classes representing specific pages on the ParaBank website. Each class encapsulates interactions and elements unique to that page.
```python
from datetime import datetime

from selenium.common import NoSuchElementException

from Locators.CustomercareLocators import CustomercareLocators

from browser import Browser


class CustomerCarePage(Browser):
    def navigate_to_contact_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/contact.htm')

    def press_send_button(self):
        try:
            self.driver.find_element(*CustomercareLocators.SEND_BUTTON).click()
        except NoSuchElementException:
            print("Butonul press button nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_send_button_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_error_message_required_fields(self):
        try:
            name_error = self.driver.find_element(*CustomercareLocators.NAME_ERROR).text
            email_error = self.driver.find_element(*CustomercareLocators.EMAIL_ERROR).text
            phone_error = self.driver.find_element(*CustomercareLocators.PHONE_ERROR).text
            message_error = self.driver.find_element(*CustomercareLocators.MESSAGE_ERROR).text

            error_messages = f'{name_error},{email_error},{phone_error},{message_error}'
            return error_messages
        except NoSuchElementException:
            print("Butonul press button nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Elements_error_for_requireds_fields_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_name(self, name):
        try:
            self.driver.find_element(*CustomercareLocators.NAME_FIELD).send_keys(name)
        except NoSuchElementException:
            print("Campul pentru introducere nume nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_name_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_email(self, email):
        try:
            self.driver.find_element(*CustomercareLocators.EMAIL_FIELD).send_keys(email)
        except NoSuchElementException:
            print("Campul pentru introducere email nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_email_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_phone(self, phone):
        try:
            self.driver.find_element(*CustomercareLocators.PHONE_FIELD).send_keys(phone)
        except NoSuchElementException:
            print("Campul pentru introducere telefon  nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_phone_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def enter_message(self, message):
        try:
            self.driver.find_element(*CustomercareLocators.MESSAGE_FIELD).send_keys(message)
        except NoSuchElementException:
            print("Campul pentru enter message  nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_enter_message_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_error_message_email_field(self):
        try:
            return self.driver.find_element(*CustomercareLocators.EMAIL_ERROR).text
        except NoSuchElementException:
            print("Campul pentru get error message email field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_message_email_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_error_message_phone_field(self):
        try:
            return self.driver.find_element(*CustomercareLocators.PHONE_ERROR).text
        except NoSuchElementException:
            print("Campul pentru phone field nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_error_message_phone_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def get_thank_you_message(self):
        try:
            return self.driver.find_element(*CustomercareLocators.THANK_YOU_MESSAGE).text
        except NoSuchElementException:
            print("Mesajul thank you nu a fost gasit")
            screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'Element_thank_you_message_Failure' + '_' + datetime.now().strftime(
                '%d-%m-%Y') + '.png'
            self.driver.save_screenshot(screenshot_name)
            print(f"Screenshot saved at '{screenshot_name}'")

    def leave_name_email_phone_message_fields_empty(self):
        self.driver.find_element(*CustomercareLocators.NAME_FIELD).clear()
        self.driver.find_element(*CustomercareLocators.EMAIL_FIELD).clear()
        self.driver.find_element(*CustomercareLocators.PHONE_FIELD).clear()

```


```python
from selenium.common import NoSuchElementException

from browser import Browser
from Locators.RegisterLocators import RegisterLocators


class RegisterPage(Browser):

    def navigate_to_home_page(self):
        self.driver.get('https://parabank.parasoft.com/parabank/index.htm')

    def click_on_register_link_button(self):
        self.driver.find_element(*RegisterLocators.REGISTER_LINK_BUTTON).click()

    def get_register_page(self):
        return self.driver.find_element(*RegisterLocators.VALIDATE_ACCOUNT_PAGE).text

    def click_register_button(self):
        self.driver.find_element(*RegisterLocators.REGISTER_BUTTON).click()

    def click_log_out(self):
        self.driver.find_element(*RegisterLocators.LOG_OUT).click()

    def get_error_messages(self):
        error_messages = []
        for locator in RegisterLocators.field_message_error.values():
            error_messages.append(self.driver.find_element(*locator).text)

        return ",".join(error_messages)

    def get_confirm_password_error(self):
        return self.driver.find_element(*RegisterLocators.field_message_error['CONFIRM_PASSWORD_ERROR']).text

    def enter_first_name(self, firstname):
        self.driver.find_element(*RegisterLocators.fields_dict['FIRST_NAME']).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*RegisterLocators.fields_dict['LAST_NAME']).send_keys(lastname)

    def enter_adress(self, adress):
        self.driver.find_element(*RegisterLocators.fields_dict['ADDRESS']).send_keys(adress)

    def enter_city(self, city):
        self.driver.find_element(*RegisterLocators.fields_dict['CITY']).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(*RegisterLocators.fields_dict['STATE']).send_keys(state)

    def enter_zip_code(self, zipcode):
        self.driver.find_element(*RegisterLocators.fields_dict['ZIP_CODE']).send_keys(zipcode)

    def enter_phone(self, phone):
        self.driver.find_element(*RegisterLocators.fields_dict['PHONE']).send_keys(phone)

    def enter_ssn(self, ssn):
        self.driver.find_element(*RegisterLocators.fields_dict['SSN']).send_keys(ssn)

    def enter_username(self, username):
        self.driver.find_element(*RegisterLocators.fields_dict['USERNAME']).send_keys(username)

    def enter_password(self, passw):
        self.driver.find_element(*RegisterLocators.fields_dict['PASSWORD']).send_keys(passw)

    def enter_confirm_password(self, confpassw):
        self.driver.find_element(*RegisterLocators.fields_dict['CONFIRM_PASSWORD']).send_keys(confpassw)

    def get_welcome_page(self):
        return self.driver.find_element(*RegisterLocators.WELCOME_MESSAGE_PAGE).text

    def leave_all_the_field(self):
        # Iterați prin toate cheile din dicționarul RegisterLocators.FIELDS
        for field, locator in RegisterLocators.fields_dict.items():
            # Lăsați câmpul gol
            self.driver.find_element(*locator).clear()

    def is_error_message_displayed(self):
        # Verificăm dacă un mesaj de eroare este afișat pe pagină
        error_messages = []
        for locator in RegisterLocators.field_message_error.values():
            try:
                error_message = self.driver.find_element(*locator).text
                if error_message:
                    error_messages.append(error_message)
            except NoSuchElementException:
                pass  # Ignorăm excepțiile în cazul în care locatorul nu este găsit

        # Verificăm dacă lista de mesaje de eroare nu este goală
        return len(error_messages) > 0

```
- **screenshots**: Automatically captured screenshots for failed test cases. These images are helpful for identifying and debugging issues.

- **steps**: Are written in the Gherkin syntax and correspond to scenarios described in feature files. Each step has a specific keyword (Given, When, Then) that signifies the type of action being performed. These steps are then implemented in code as step definitions, which execute the corresponding actions on the system under test and perform assertions to verify expected outcomes.
  
The customer care step file cover scenarios such as filling out the form, pressing the send button, handling validation messages for empty and incorrectly formatted fields, and verifying a thank you message upon successful submission.  
```python
import time

from behave import *

@given('I am on the contact page')
def step_impl(context):
    context.CustomerCarePage.navigate_to_contact_page()


@when('I leave name,email,phone,message fields empty')
def step_impl(context):
    pass


@when('I press the send button')
def step_impl(context):
    context.CustomerCarePage.press_send_button()


@then('I should see an error message for the required fields')
def step_impl(context):
    actual_error_message = context.CustomerCarePage.get_error_message_required_fields()
    expected_error_message = 'Name is required.,Email is required.,Phone is required.,Message is required.'
    assert expected_error_message in actual_error_message, f'{expected_error_message} is not in {actual_error_message}'


@when('I enter "{name}" in name field')
def step_impl(context, name):
    context.CustomerCarePage.enter_name(name)


@when('I enter "{email}" in email field')
def step_impl(context, email):
    context.CustomerCarePage.enter_email(email)


@when('I enter "{phone}" in phone field')
def step_impl(context, phone):
    context.CustomerCarePage.enter_phone(phone)


@when('I enter "{message}" in message field')
def step_impl(context, message):
    context.CustomerCarePage.enter_message(message)


@then('I should see an error message for the email field')
def step_impl(context):
    actual_error_message = context.CustomerCarePage.get_error_message_email_field()
    expected_error_message = 'Email format is not correct'
    assert expected_error_message in actual_error_message


@then('I should see an error message for the phone field')
def step_impl(context):
    actual_error_message = context.CustomerCarePage.get_error_message_phone_field()
    expected_error_message = 'Phone format is not correct'
    assert expected_error_message in actual_error_message


@then('I should see a Thank you message')
def step_impl(context):
    actual_message = context.CustomerCarePage.get_thank_you_message()
    expected_message = 'Thank you Robert'
    assert expected_message in actual_message, f'{expected_message} is not {actual_message}'
```


The forgot password step file simulate a user's interaction with a web application's password recovery feature. They involve navigating to the homepage, clicking on the "forgot password" button, entering user information, handling validation messages, and verifying the outcomes of password recovery attempts, such as successful or unsuccessful logins and redirection to relevant pages.
```python
import time

from behave import *


@given('I am on the homepage')
def step_impl(context):
    context.ForgotPasswordPage.navigate_to_homepage()
    time.sleep(2)


@given('I click o the forgot password button')
def step_impl(context):
    context.ForgotPasswordPage.click_forgot_password_button()


@then('I should be redirected to the password reset page')
def step_impl(context):
    actual_page_title = context.ForgotPasswordPage.get_password_reset_page()
    expected_page_title = 'Customer Lookup'
    assert expected_page_title in actual_page_title, f'{expected_page_title} is not in {actual_page_title}'


@when('I click on find my login info button')
def step_impl(context):
    context.ForgotPasswordPage.click_find_login_info_button()


@then('I should see an error message for the empty fields')
def step_impl(context):
    actual_error_messages = context.ForgotPasswordPage.get_error_message_empty_fields()
    expected_error_messages = 'First name is required.,Last name is required.,Address is required.,City is required.,State is required.,Zip Code is required.,Social Security Number is required.'
    assert expected_error_messages in actual_error_messages, f'"{expected_error_messages}" is not in "{actual_error_messages}"'


@when('I enter "{firstname}" in first name field')
def step_impl(context, firstname):
    context.ForgotPasswordPage.enter_firstname(firstname)


@when('I enter "{lastname}" in last name field')
def step_impl(context, lastname):
    context.ForgotPasswordPage.enter_lastname(lastname)


@when('I enter "{address}" in address field')
def step_impl(context, address):
    context.ForgotPasswordPage.enter_address(address)


@when('I enter "{city}" in city field')
def step_impl(context, city):
    context.ForgotPasswordPage.enter_city(city)


@when('I enter "{state}" in state field')
def step_impl(context, state):
    context.ForgotPasswordPage.enter_state(state)


@when('I enter "{zipcode}" in zip code field')
def step_impl(context, zipcode):
    context.ForgotPasswordPage.enter_zipcode(zipcode)


@when('I enter "{ssn}" in SSN field')
def step_impl(context, ssn):
    context.ForgotPasswordPage.enter_ssn(ssn)


@then('I should see an error message due to wrong credentials')
def step_impl(context):
    actual_error_message = context.ForgotPasswordPage.get_error_message_wrong_credentials()
    expected_error_message = 'The customer information provided could not be found.'
    assert expected_error_message in actual_error_message, f'"{expected_error_message}" is not in "{actual_error_message}"'


@then('I should been redirected to the get information page')
def step_impl(context):
    actual_information = context.ForgotPasswordPage.get_information_page()
    expected_information = 'Your login information was located successfully. You are now logged in.'
    assert expected_information in actual_information, f'"{expected_information}" is not in "{actual_information}"'


@then('I log out')
def step_impl(context):
    context.ForgotPasswordPage.log_out()
```
The steps_login file contains step definitions that implement the actions described in the login feature's scenarios. These step definitions interact with the LoginPage class, which represents the login page of the application, to perform actions and validate expected outcomes during test execution.
```python
from datetime import datetime
import time

from behave import *


@given('I am on the login page')
def step_impl(context):
    context.LoginPage.navigate_to_login_page()
    time.sleep(2)


@when('I enter "{username}" in username field')
def step_impl(context, username):
    context.LoginPage.enter_username(username)


@when('I enter "{password}" in password field')
def step_impl(context, password):
    context.LoginPage.enter_password(password)


@when('I press login button')
def step_impl(context):
    context.LoginPage.click_login_button()


@then('I should see an internal error message')
def step_impl(context):
    actual_error_message = context.LoginPage.get_error_message()
    expected_result_message = 'An internal error has occurred and has been logged.'
    assert expected_result_message in actual_error_message



@when('I leave both username and password fields empty')
def step_impl(context):
    context.LoginPage.leave_both_username_password_field()


@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.LoginPage.get_error_message()
    expected_result_message = 'Please enter a username and password.'
    assert actual_error_message in expected_result_message


@then('I should be redirected to the dashboard')
def step_impl(context):
    actual_message = context.LoginPage.get_dashboard_page()
    expected_result = 'Accounts Overview'
    if expected_result not in actual_message:
        # Capture and save screenshot in case of failure
        screenshot_name = 'C:/Users/Robert/PycharmProjects/Project-Testing-with-BDD/Screenshots/' + 'Dashboard_Redirection_Failure2' + '_' + datetime.now().strftime(
            '%d-%m-%Y') + '.png'

        context.browser.driver.save_screenshot(screenshot_name)

        # Raise AssertionError with custom message
        raise AssertionError(f'Test failed. Screenshot saved at: {screenshot_name}')


@when('I leave username field empty')
def step_impl(context):
    context.LoginPage.leave_username_field_empty()
```
The following steps are tailored to the specific registration process of the Parabank website, allowing for automated testing and validation of the registration feature.
```python
import time
from faker import Faker
from behave import *

@given('I am on homepage')
def step_impl(context):
    context.RegisterPage.home_page()
    time.sleep(2)

@given('I click on register button')
def step_impl(context):
    context.RegisterPage.click_on_register_link_button()

@then('I should be redirected to the register page')
def step_impl(context):
    context.RegisterPage.get_register_page()

@when('I leave all the fields empty')
def step_impl(context):
    context.RegisterPage.leave_all_the_field()

@when('I click register button')
def step_impl(context):
    context.RegisterPage.click_register_button()

@then('I should see an error message for empty fields')
def step_impl(context):
    actual_error_messages = context.RegisterPage.get_error_messages()
    expected_error_messages = 'First name is required.,Last name is required.,Address is required.,City is required.,State is required.,Zip Code is required.,Social Security Number is required.,Username is required.,Password is required.,Password confirmation is required.'
    assert expected_error_messages in actual_error_messages, f'"{expected_error_messages}" is not in {actual_error_messages}'


@when('I introduce "{fname}" in first name field')
def step_impl(context, fname):
    context.RegisterPage.enter_first_name(fname)

@when('I introduce "{lname}" in last name field')
def step_impl(context, lname):
    context.RegisterPage.enter_last_name(lname)

@when('I introduce "{adress}" in address field')
def step_impl(context, adress):
    context.RegisterPage.enter_adress(adress)

@when('I introduce "{city}" in city field')
def step_impl(context, city):
    context.RegisterPage.enter_city(city)

@when('I introduce "{state}" in state field')
def step_impl(context, state):
    context.RegisterPage.enter_state(state)

@when('I introduce "{zipcode}" in zip code field')
def step_impl(context, zipcode):
    context.RegisterPage.enter_zip_code(zipcode)

@when('I introduce "{phone}" in phone field')
def step_impl(context, phone):
    context.RegisterPage.enter_phone(phone)

@when('I introduce "{ssn}" in SSN field')
def step_impl(context, ssn):
    context.RegisterPage.enter_ssn(ssn)

@when('I introduce "{username}" in username field')
def step_impl(context, username):
    context.RegisterPage.enter_username(username)

@when('I introduce a new username in username field')
def step_impl(context):
    fake = Faker()
    new_username = fake.user_name()
    context.RegisterPage.enter_username(new_username)

@when('I introduce "{passw}" in password field')
def step_impl(context, passw):
    context.RegisterPage.enter_password(passw)

@when('I introduce "{confpassw}" in password confirmation filed')
def step_impl(context, confpassw):
    context.RegisterPage.enter_confirm_password(confpassw)

@then('I should see an error message for wrong credentials')
def step_impl(context):
    error_message_displayed = context.RegisterPage.is_error_message_displayed()
    assert error_message_displayed, "Expected error message to be displayed, but it's not."
    # pass

@then('I should be redirected to a welcome page')
def step_impl(context):
    context.RegisterPage.get_welcome_page()


@then('I should see an error message for unmatched passwords')
def step_impl(context):
    actual_error_message = context.RegisterPage.get_confirm_password_error()
    expected_error_message = 'Passwords did not match.'
    assert expected_error_message in actual_error_message
```
time: Used for introducing delays in the test execution, providing a pause between actions.

faker: This library is used to generate fake data such as names and email addresses. In this particular case, the fake library is used to generate a new email address each time the registration functionality is tested with valid credentials. Without this library, the test would not pass because if the same email is entered twice, the account registration cannot be successful.

behave: This is the primary BDD testing framework for Python.

datetime: This module is used for working with dates and times. The datetime module is used in these steps for capturing the current date and time when saving a screenshot in case of a test failure. Specifically, it's used to generate a timestamp to include in the screenshot's file name.

- **browser-file**: The following Browser class defines a simple wrapper around the Selenium WebDriver to manage the browser instance. It initializes a Chrome WebDriver instance, maximizes the window, and sets an implicit wait time of 3 seconds for finding elements before throwing an exception.
```python
from selenium import webdriver


class Browser:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    def close(self):
        self.driver.close()
```
- **environment-file**: This environment.py file is used in conjunction with Behave, the BDD testing framework, to set up and tear down test environments before and after test execution. It imports necessary modules, initializes objects, and defines hooks to execute setup and teardown actions.
```python
from browser import Browser
from pages.customercare_page import CustomerCarePage
from pages.forgotpassword_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def before_all(context):
    context.browser = Browser()
    context.LoginPage = LoginPage()
    context.CustomerCarePage = CustomerCarePage()
    context.ForgotPasswordPage = ForgotPasswordPage()
    context.RegisterPage = RegisterPage()


def after_all(context):
    context.browser.close()
```
- **venv**: The virtual environment directory.
- **behave.ini**: Serves as a configuration file for Behave, the behavior-driven development (BDD) testing framework in Python. It allows to specify various settings and options for Behave, including options related to formatters, logging, and other behavior settings.
- **requirements.txt**: Lists all the required dependencies for the project. Install these dependencies before running the tests.
- **behave-script**: Parses the feature files, matches steps to their corresponding step definitions, and executes the tests. It provides detailed reports on the execution status of each scenario and step, helping to understand which tests passed, failed, or encountered issues.

# 4. Features Under Testing:
 ### Customer Care Functionality Testing:
1. Email support with empty fields
2. Email support with wrong email format
3. Email support with wrong phone format
4. Email support with correct credentials
   
### Forgot Password Functionality Testing:
1. Reset password with empty fields
2. Reset password with wrong credentials
3. Reset password with correct credentials

### Login Functionality Testing:
1. Login with wrong credentials
2. Login with both empty username and password
3. Login with correct credentials
4. Login with empty username field

### Register Functionality Testing:
1. Register with empty fields
2. Register with different password confirmation
3. Register with correct credentials
4. Register with wrong credentials

## Getting Started  :pushpin:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/AdrianPricopie/Project-Testing-with-BDD.git
    ```

2. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Activate the Virtual Environment:**

    ```bash
    venv/Scripts/Activate
    ```

4. **Run the tests:**
    ```bash
    behave -f html -o report.html  
    ```
5. **Run test by hastag:**
   
   example:
   
     ```bash
    behave --format html -o behave_report_tags.html --tags=register_wrong_credential
    ```

## Reports 

![](https://github.com/AdrianPricopie/Project-Testing-with-BDD/blob/main/Screenshot%202024-03-26%20at%2020.55.33.png)
![](https://github.com/AdrianPricopie/Project-Testing-with-BDD/blob/main/Screenshot%202024-03-26%20at%2020.55.55.png)
![](https://github.com/AdrianPricopie/Project-Testing-with-BDD/blob/main/Screenshot%202024-03-26%20at%2020.56.25.png)

   
   
