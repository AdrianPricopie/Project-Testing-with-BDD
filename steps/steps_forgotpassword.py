from behave import *


@given('I am on the homepage')
def step_impl(context):
    context.ForgotPasswordPage.navigate_to_homepage()


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
