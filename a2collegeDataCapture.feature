@collegeDataCapture
Feature: Verify College Data Capture Portal
         As a user,
         I want to verify whether I am able to submit information to HTCampus

    @overview
    Scenario: Verify user is able to fill the Overview Tab
      Given application displays the Overview Tab
      When user enters address of the college in the "Address of College" field
      And user enters pincode in the pincode field
      And user enters contact number in the contact number field
      And user enters email id in the email id field
      And user enters website in the website field
      And user clicks on save button
      Then application redirects the user to the Course page

    @overview
    Scenario: Verify application saves the Overview tab with the current changes made by the college user
      When user tries to verify the changes in the overview tab
      Then application displays changes for address,about college, pincode, contactNo, emailId, website

    @course
    Scenario: Verify user is able to enter new course in the Course tab
      When user clicks on Overview tab
      When user enters course details
      And click on Save button
      Then application displays the course name in the course list

    @course
    Scenario: Verify application is able to save all the course details which are entered by the user
      When user tries to verify the changes in the a particular course
      Then application displays all the saved records
      When application click on "Save" button from the right panel
      Then application closes the edit option of the course
      When application click on "Save" button from the right panel
      Then application redirects the user to the Infrastructure tab

    @infrastructure
    Scenario: Verify user is able to fill information in the Infrastructure tab
      Given user is on the Infrastructure tab
      When user adds a hostel facility in the infrastructure tab
#      Then application opens up the edit option for the corresponding facility
      When user enters facility details information
      And application click on "Save" button from the right panel
#      Then application closes the edit option for the corresponding tab
#      When application enters "Infrastructure Summary"
#      And application click on "Save" button from the right panel
#      Then application redirects the user to the "Placements" tab

    @infrastructure
    Scenario: Verify application saves all the infrastructure details which are entered by the user
      Given user is on the infrastructure tab
      When application tries to verify all the infrastructure details entered by the user
      Then application displays all the information are correctly entered

    @placement
    Scenario: Verify user is able to fill information in the placement tab
      Given user is on the placement tab
      When user tries to enter information in the placements tab
      And application click on "Save" button from the right panel
      Then application redirects the user to the faculty tab

    @placement
    Scenario: Verify application saves all the placements details which are entered by the user
      Given user is on the placement tab
      When application tries to verify the entered information in the placement tab
      Then application displays all the information are correctly entered

    @faculty
    Scenario: Verify application enter all the faculty details in the faculty tab
      Given user is on the faculty tab
      When application tries to enter information in the faculty tab
      And application click on "Save" button from the right panel
      Then application redirects the user to the gallery tab

    @faculty
    Scenario: Verify application saves all the faculty details which are entered by the user
      Given user is on the faculty tab
      When application tries to verify the entered information in the faculty tab
      Then application displays all the information are correctly entered

    @gallery
    Scenario: Verify application enter all the information in "Gallery" tab
      Given user is on the "Gallery" tab
      When user creates a album
      Then application displays the album name in the list
      When user creates a "video gallery"
      Then application displays the video name in the list

    @financialDetails
    Scenario: Verify application enter all the financial details in the financial details tab
      Given user is on the financial detail tab
      When application tries to enter information in the financial detail
      And application click on "Save" button from the right panel
      Then application redirects the user to the "Point of Contact" page

    @financialDetails
    Scenario: Verify application saves all the financial details which are entered by the user
      Given user is on the financial detail tab
      When application tries to verify the entered information in the financial details tab
      Then application displays all the information are correctly entered

    @pointOfContact
    Scenario: Verify application enter all the point of contact details in the point of contact tab
      Given user is on the "point of contact" tab
      When user enters all the spoc information
      And user click on "Add New" button corresponding to "Campus Journalist" section
      And user enters "Campus Journalist" information
      And application click on "Save" button from the right panel
      And application click on "Save" button from the right panel
      Then application redirect the user to the "Alumni & Testimonials" tab

    @pointOfContact
    Scenario: Verify application saves all the "Point of Contact" details which are entered by the user
      Given user is on the "point of contact" tab
      When application tries to verify the entered information in the "Point of Contact" details tab
      Then application displays all the information are correctly entered

    @aluminiAndTestimonial
    Scenario: Verify application enter all the information in "Alumini & Testimonial" tab
      Given user is on the "alumini & testimonial" tab
      When user entered alumini details
#      And user entered testimonial details
#      And application click on "Save" button from the right panel
      Then application redirect the user to the "Overview" tab

    @aluminiAndTestimonial
    Scenario: Verify application saves all the "Alumini and Testimonial" details which are entered by the user
      Given user is on the "alumini & testimonial" tab
      When application tries to verify the entered information in the "Alumini & Testimonial" details tab
      Then application displays all the information are correctly entered

    @finalSubmit
    Scenario: Verify user is able to submit all the request
      Given application displays the Overview Tab
      When user click on submit button from any tab
      Then application raises request for all the save records