Feature: Add candidate

  Scenario: Add candidate successfully
    Given I am logged in as an admin
    When I navigate to the "Add candidate" section
    And I click on the "Add" button in the module
    And I fill out the candidate form with the following details: "Carlos" "Rodriguez" "carlos@correo.com"
    And I submit the form
    Then I should see a confirmation message that the candidate was added successfully
