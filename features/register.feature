Feature: Register Feature

  Background:
    Given I am on homepage
    And I click on register button
    Then I should be redirected to the register page

  @register_empty_fields
  Scenario: Register with empty fields
    When I leave all the fields empty
    And I click register button
    Then I should see an error message for empty fields

  @register_with_no_matched_passwords
  Scenario: Register with different password confirmation
    When I introduce "123" in password field
    And I introduce "321" in password confirmation filed
    And I click register button
    Then I should see an error message for unmatched passwords
#
  @register_correct_credentials
  Scenario: Register with correct credentials
    When I introduce "John" in first name field
    And I introduce "Smith" in last name field
    And I introduce "Main street" in address field
    And I introduce "Anytown" in city field
    And I introduce "California" in state field
    And I introduce "123456" in zip code field
    And I introduce "078 982 112" in phone field
    And I introduce "456789" in SSN field
    And I introduce "John Smith" in username field
    And I introduce "password" in password field
    And I introduce "password" in password confirmation filed
    And I click register button
    Then I should be redirected to a welcome page

@register_wrong_credentials
  Scenario: Register with wrong credentials
    When I introduce "092" in first name field
    And I introduce "09d" in last name field
    And I introduce "123" in address field
    And I introduce "qwe" in city field
    And I introduce "aaa" in state field
    And I introduce "sss" in zip code field
    And I introduce "1As" in phone field
    And I introduce ",.;" in SSN field
    And I introduce a new username in username field
    And I introduce "password" in password field
    And I introduce "password" in password confirmation filed
    And I click register button
    Then I should see an error message for wrong credentials




