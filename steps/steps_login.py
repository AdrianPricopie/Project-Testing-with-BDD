import time

from behave import *


@given('I am on the login page')
def step_impl(context):
    context.LoginPage.navigate_to_login_page()
    time.sleep(4)


@when('I enter a wrong username')
def step_impl(context):
    pass


@when('I enter a wrong password')
def step_impl(context):
    pass


@when('I press login button')
def step_impl(context):
    pass


@then('I should see an error message')
def step_impl(context):
    pass
