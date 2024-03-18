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

5. [Test Deliverables](#test-deliverables)
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

- **features**: Hold the specifications or scenarios written in Gherkin syntax. Gherkin is a human-readable format that describes the behavior of the software in plain language. Each feature file typically represents a feature or a user story of the application being developed, and it contains one or more scenarios that describe the various behaviors or functionalities of that feature.
```python
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
```python
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
```python
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
```python
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
  

