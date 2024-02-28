Feature: ForgotPassword Feature

  Background:
    Given I am on the homepage
    And I click o the forgot password button
    Then I should be redirected to the password reset page

  @empty_fields
  Scenario: Reset password with empty fields
    When I leave empty all the fields
    And I click on find my login info button
    Then I should see an error message for the empty fields

  @wrongcredentials
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


  @correct-credentials_wrong_SSN_number
  Scenario: Reset password with correct credentials and wrong SSN number
    When I enter "John" in first name field
    And I enter "Smith" in last name field
    And I enter "Main street" in address field
    And I enter "Anytown" in city field
    And I enter "California" in state field
    And I enter "123456" in zip code field
    And I enter "789" in SSN field
    And I click on find my login info button
    Then I should see an error message due to wrong credentials


  @all_correct_credentials
  Scenario: Reset password with all correct credentials
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


  @wrong_credentials_correct_SSN_number
  Scenario: Reset password with wrong credentials and correct SSN number
    When I enter "abc" in first name field
    And I enter "abc" in last name field
    And I enter "abc" in address field
    And I enter "abc" in city field
    And I enter "abc" in state field
    And I enter "123" in zip code field
    And I enter "456789" in SSN field
    And I click on find my login info button
    Then I should see an error message due to wrong credentials