Feature: Login Feature

  Background:
    Given I am on the login page

  @wrong_credentials
  Scenario: Login with wrong credentials
    When I enter "robert123" in username field
    And I enter "123robert" in password field
    And I press login button
    Then I should see an internal error message

  @empty_username_and_password
  Scenario: Login with both empty username and password
    When I leave both username and password fields empty
    And I press login button
    Then I should see an error message

  @correct_credentials
  Scenario: Login with correct credentials
    When I enter "assq@123" in username field
    And I enter "assq" in password field
    And I press login button
    Then I should be redirected to the dashboard

  @empty_username_field
  Scenario: Login with empty username field
    When I leave username field empty
    And I enter "storm20" in password field
    And I press login button
    Then I should see an error message

