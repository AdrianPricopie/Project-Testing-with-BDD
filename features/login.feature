Feature: Login Feature

  Background:
    Given I am on the login page

  Scenario: Login with wrong credentials
    When I enter a wrong username
    And I enter a wrong password
    And I press login button
    Then I should see an error message

  Scenario: Login with both empty username and password
    When I leave both username and password fields empty
    And I press login button
    Then I should see an error message for both empty fields

  Scenario: Login with correct credentials
    When I enter a correct username
    And I enter a correct password
    And I press login button
    Then I should be redirected to the dashboard

  Scenario: Login with empty username field
    When I leave username field empty
    And I enter a correct password
    Then I should see an error message

