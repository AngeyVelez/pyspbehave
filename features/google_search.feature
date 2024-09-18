Feature: Google search

  Scenario: Perform a search on Google
    Given the user is on the Google homepage
    When the user searches for "Screenplay Pattern"
    Then the user should see search results
