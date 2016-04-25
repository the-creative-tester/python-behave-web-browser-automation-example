Feature: Search

  Scenario: Search PyPI
    Given I navigate to the PyPi Home page
    When I search for "behave"
    Then I am taken to the PyPi Search Results page
    And I see a search result "behave 1.2.5"