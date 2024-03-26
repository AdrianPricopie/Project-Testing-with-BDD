import time

from behave import *


@given('I am on the contact page')
def step_impl(context):
    time.sleep(3)
    context.CustomerCarePage.navigate_to_contact_page()


@when('I leave name,email,phone,message fields empty')
def step_impl(context):
    context.CustomerCarePage.leave_name_email_phone_message_fields_empty()


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
    assert expected_error_message in actual_error_message, (f"Expected error message: '{expected_error_message}', "
                                                            f"but got: '{actual_error_message}'")


@then('I should see an error message for the phone field')
def step_impl(context):
    actual_error_message = context.CustomerCarePage.get_error_message_phone_field()
    expected_error_message = 'Phone format is not correct'
    assert expected_error_message in actual_error_message, (f"Expected error message: '{expected_error_message}', "
                                                            f"but got: '{actual_error_message}'")


@then('I should see a Thank you message')
def step_impl(context):
    actual_message = context.CustomerCarePage.get_thank_you_message()
    expected_message = 'Thank you Robert'
    assert expected_message in actual_message, f'{expected_message} is not {actual_message}'
