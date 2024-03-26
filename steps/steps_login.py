from datetime import datetime
from behave import *


@given('I am on the login page')
def step_impl(context):
    context.LoginPage.navigate_to_login_page()


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
    expected_result_message = 'The username and password could not be verified.'
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
        screenshot_name = '/Users/adrianpricopie/PythonBDD/Project-Testing-with-BDD/Screenshots/' + 'error_dashboard_page' + '_' + datetime.now().strftime(
            '%d-%m-%Y') + '.png'

        context.browser.driver.save_screenshot(screenshot_name)

        # Raise AssertionError with custom message
        raise AssertionError(f'Test failed. Screenshot saved at: {screenshot_name}')

    # clean UP (Log out)
    context.LoginPage.log_out()

@when('I leave username field empty')
def step_impl(context):
    context.LoginPage.leave_username_field_empty()
