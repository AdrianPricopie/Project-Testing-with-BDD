Feature: ForgotPassword Feature

  Background:
    Given I am on the homepage
    And I click o the forgot password button
    Then I should be redirected to the password reset page

  @Forgot_password_empty_fields
  Scenario: Reset password with empty fields
    When I leave empty all the fields
    And I click on find my login info button
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


