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


