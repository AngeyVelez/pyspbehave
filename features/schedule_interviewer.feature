Feature: Schedule interviewer

  Scenario: Successful schedule interviewer with valid data
    Given the user must schedule an interview
    When enter valid data and submit form "Title interview" "a" "2024-12-12"
    Then the user should see a Successful message
