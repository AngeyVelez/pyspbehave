Feature: Shortlist candidate

  Scenario: Shortlist a candidate
    Given the user want to shortlist a newly created candidate
    When the user click on shortlist button
    Then the user should see a shortlist form
