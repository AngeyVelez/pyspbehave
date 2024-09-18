Feature: Login

  Scenario: Successful login with valid credentials
    Given I launch the login page
    When I enter valid credentials and submit form "Admin" "admin123"
    Then I should see the user dashboard
