from faker import Faker
from behave import *


@given('I am on homepage')
def step_impl(context):
    context.RegisterPage.navigate_to_home_page()


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


@then('I should be redirected to a welcome page')
def step_impl(context):
    context.RegisterPage.get_welcome_page()

    # clean up log out
    context.RegisterPage.click_log_out()


@then('I should see an error message for unmatched passwords')
def step_impl(context):
    actual_error_message = context.RegisterPage.get_confirm_password_error()
    expected_error_message = 'Passwords did not match.'
    assert expected_error_message in actual_error_message
