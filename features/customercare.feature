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