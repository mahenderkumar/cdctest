@cmsAdminRequest
Feature: Verify cms admin captures all the request
         As a user,
         I want to verify whether I am able to submit information to HTCampus

  @admin
  Scenario: Verify no of request raised in the admin
    Given user launches the cms admin site
    And user is on the college request page
    When application counts the number of raised request which are in submitted status
    Then application should display total number of raised request from cdc frontend is equal to cms admin
    And application should display the number of models request
