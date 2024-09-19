Feature: Add candidate

  Scenario: Add candidate successfully
    Given the user is logged in as an admin
    When the user navigate to the "Add candidate" section
    And the user click on the "Add" button in the module
    And the user fill out the candidate form with the following details: "Andrew" "Gil" "mail@email.com"
    And the user submit the form
    Then the user should see a confirmation message that the candidate was added successfully
