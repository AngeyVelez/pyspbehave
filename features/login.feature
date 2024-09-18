Feature: Login

  Scenario: Successful login with valid credentials
    Given the user launch the login page
    When enter valid credentials and submit form "Admin" "admin123"
    Then the user should see the user dashboard
