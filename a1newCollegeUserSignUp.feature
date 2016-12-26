@a1newCollegeUserSignUp
Feature: Verify new college user is created
         As a user,
         I want to verify whether I am able to create a new college user in HTCampus

  Scenario: Verify application allows college user to register in CDC
    Given user sign-up as new user
    And user is on the overview page of new user
    Then user logs out of the application
    When admin user launches cms admin with valid credentials
    And navigate to college wise request page
    Then application displays one request for college user
    When admin user approves the request
    Then application creates the college in HTCampus
