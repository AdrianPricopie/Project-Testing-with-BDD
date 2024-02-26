import time

from behave import *


@given('I am on the login page')
def step_impl(context):
    context.LoginPage.navigate_to_login_page()
    time.sleep(4)


@when('I enter a wrong username')
def step_impl(context):
    context.LoginPage.enter_wrong_username()


@when('I enter a wrong password')
def step_impl(context):
    context.LoginPage.enter_wrong_password()


@when('I press login button')
def step_impl(context):
    context.LoginPage.click_login_button()


@then('I should see an error message')
def step_impl(context):
    actual_error_message = context.LoginPage.get_error_message()
    expected_result_message = 'An internal error has occurred and has been logged.'
    assert expected_result_message in actual_error_message
