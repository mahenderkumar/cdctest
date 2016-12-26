from behave import *
from random import randint
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

# from nose.tools import assert_false, assert_true
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
# from selenium.webdriver import  ActionChains

global ColgAddress, aboutCollege, pincode, contactNo, email, website
global courseName, courseDescription
global facilityDetails, infrastructureSummary
global placementSummary, campusJournalist,aluminiName,testimonialName,albumName,videoName,noOfRequest
ColgAddress="My address of college"
pincode="123456"
contactNo="987123456"
email="abc@abc.com"
website="https://www.htcampus.com/"
aboutCollege="Best education is our moto"
b=randint(100000, 999999)
courseName='{}{}'.format("Course ",b)
courseDescription= "Course Description"
facilityDetails="College facility details"
infrastructureSummary="College Infrastructure details"
placementSummary="College Placement Summary"
campusJournalist='{}{}'.format("campusJournalist ",b)
aluminiName='{}{}'.format("Alumini ",b)
testimonialName='{}{}'.format("Testimonial ",b)
albumName='{}{}'.format("AlbumName ",b)
videoName='{}{}'.format("VideoName ",b)

@given('application displays the Overview Tab')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Your College Overview')]").is_displayed())
    except:
        context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Overview')]").click()
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Your College Overview')]").is_displayed())


@when('user enters address of the college in the "Address of College" field')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='allias']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='allias']").send_keys("abc")
    # context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'About the college')]/parent::*/div[@class='jqte']/div[@class='jqte_editor']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'About the college')]/parent::*/div[@class='jqte']/div[@class='jqte_editor']").send_keys(aboutCollege)
    # context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Address of College')]/parent::*/div[@class='jqte']/div[@class='jqte_editor']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Address of College')]/parent::*/div[@class='jqte']/div[@class='jqte_editor']").send_keys(ColgAddress)
    
@when('user enters pincode in the pincode field')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='pincode']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='pincode']").send_keys(pincode)


@when('user enters contact number in the contact number field')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='contact_number']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='contact_number']").send_keys(contactNo)

@when('user enters email id in the email id field')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@name='email']").clear()
    context.driver.find_element_by_xpath(".//*[@name='email']").send_keys(email)

@when('user enters website in the website field')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@name='website']").clear()
    context.driver.find_element_by_xpath(".//*[@name='website']").send_keys(website)

@when('user clicks on save button')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='save_request']").click()

@then('application redirects the user to the Course page')
def step_impl(context):
    sleep(2)
    context.driver.find_element_by_xpath("//h1[contains(.,'Courses Offered by Your College/Institute')]").is_displayed()

@when('user tries to verify the changes in the overview tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='tab_name']/li[1]/a[contains(.,'Overview')]").click()

@then('application displays changes for address,about college, pincode, contactNo, emailId, website')
def step_impl(context):
    assert context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='allias']").get_attribute("value")=="abc"
    assert context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'About the college')]/parent::*/div[@class='jqte']/div[@class='jqte_editor']").text==aboutCollege
    assert(context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Address of College')]/parent::*/div[@class='jqte']/div[@class='jqte_editor']").text==ColgAddress)
    assert(context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='pincode']").get_attribute("value")==pincode)
    assert(context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='contact_number']").get_attribute("value")==contactNo)
    assert(context.driver.find_element_by_xpath(".//*[@name='email']").get_attribute("value")==email)
    assert(context.driver.find_element_by_xpath(".//*[@name='website']").get_attribute("value")==website)

@when('user clicks on Overview tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='tab_name']/li[2]/a[contains(.,'Course')]").click()

@when('user enters course details')
def step_impl(context):
    sleep(2)
    # context.driver.find_element_by_xpath(".//*[@id='coursecomp']/div/div[1]/div[2]/button").click()
    context.driver.execute_script("$('.btn.btn-success.pull-right').click()")
    # context.driver.find_element_by_css_selector(".btn.btn-success.pull-right").click()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Course Title']").send_keys(courseName)
    Select(context.driver.find_element_by_id("select_div_1")).select_by_visible_text("Yes")
    Select(context.driver.find_element_by_id("select_div_2")).select_by_visible_text("Full Time - Class Room")
    # Select(context.driver.find_element_by_id("select_div_2")).select_by_visible_text("Full Time - Class Room")
    context.driver.find_element_by_xpath(".//*[@id='mCSB_1_container']/ul/li[1]/label[contains(.,'Fashion / Textile Design')]/input").click()
    context.driver.find_element_by_xpath(".//*[@id='mCSB_1_container']/ul/li[1]/label[contains(.,'AgriBusiness / Rural')]/input").click()
    Select(context.driver.find_element_by_id("select_div_3")).select_by_visible_text("PG Courses")

    context.driver.find_element_by_xpath(".//*[@id='mainform']//label[text()='Course Description']/parent::*//div[@class='jqte_editor']").send_keys(courseDescription)
    context.driver.find_element_by_xpath(".//*[@id='mainform']//label[text()='Course Description']/parent::*//div[@class='jqte_editor']").send_keys("1")
    Select(context.driver.find_element_by_id("select_div_3")).select_by_visible_text("PG Courses")
    Select(context.driver.find_element_by_id("select_div_4")).select_by_visible_text("2")
    Select(context.driver.find_element_by_id("select_div_5")).select_by_visible_text("2")
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='in Lakhs']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='in Lakhs']").send_keys("2")
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='in Thousands']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='in Thousands']").send_keys("2")
    Select(context.driver.find_element_by_id("select_div_9")).select_by_visible_text("AIPA")
    Select(context.driver.find_element_by_id("select_div_10")).select_by_visible_text("A.P. Nurses, Midwives Council")

@when('click on Save button')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='save_request']").click()
    sleep(5)

@then('application displays the course name in the course list')
def step_impl(context):
    sleep(3)
    xpath = "//li/div[contains(.,'{}')]".format(courseName)
    context.driver.find_element_by_xpath(xpath).is_displayed()

@when('user tries to verify the changes in the a particular course')
def step_impl(context):
    xpath1 = "//li/div[contains(.,'{}')]/span[contains(@class,'edit_icon')]".format(courseName)
    context.driver.find_element_by_xpath(xpath1).click()
    assert context.driver.find_element_by_xpath("//input[@id='exampleInputEmail1' and @placeholder='Enter Course Title']").get_attribute("value")==courseName
    context.driver.find_element_by_xpath("//div[@class='form-group']/div[@class='selectdiv']/div[@class='out' and contains(.,'Yes')]").is_displayed()
    context.driver.find_element_by_xpath("//div[@class='form-group']/div[@class='selectdiv']/div[@class='out' and contains(.,'Full Time - Class Room')]").is_displayed()
    context.driver.find_element_by_xpath("//div[@class='form-group']/div[@class='selectdiv']/div[@class='out' and contains(.,'PG Courses')]").is_displayed()
    assert context.driver.find_element_by_xpath(".//*[@id='mainform']//label[text()='Course Description']/parent::*//div[@class='jqte_editor']").text==courseDescription
    context.driver.find_element_by_xpath(".//*[@id='select_div_4']/parent::*/div[contains(.,'2')]").is_displayed()
    context.driver.find_element_by_xpath(".//*[@id='select_div_5']/parent::*/div[contains(.,'2')]").is_displayed()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='in Lakhs']").get_attribute("value")=="2"
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='in Thousands']").get_attribute("value")=="2"
    context.driver.find_element_by_xpath(".//*[@id='select_div_9']/parent::*/div[contains(.,'AIPA')]").is_displayed()
    context.driver.find_element_by_xpath(".//*[@id='select_div_10']/parent::*/div[contains(.,'A.P. Nurses, Midwives Council')]").is_displayed()
    # context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Infrastructure')]").click()

@then('application displays all the saved records')
def step_impl(context):
    pass

@when('application click on "Save" button from the right panel')
def step_impl(context):
    context.driver.find_element_by_xpath("//button[@id='save_request']").click()

@then('application closes the edit option of the course')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath("//div[@id='mainform']//label[contains(.,'Course Title')]").is_displayed()
    except NoSuchElementException:
        assert True

@then('application redirects the user to the Infrastructure tab')
def step_impl(context):
    try:
        if context.driver.find_element_by_xpath("//h1[contains(.,'Infrastructure and Facilities')]").is_displayed()==True:
            pass
        else:
            context.driver.find_element_by_xpath("//button[@id='save_request']").click()
    except(NoSuchElementException):
        try:
            context.driver.find_element_by_xpath("//button[@id='save_request']").click()
            context.driver.find_element_by_xpath("//h1[contains(.,'Infrastructure and Facilities')]").is_displayed()
        except(NoSuchElementException):
            context.driver.find_element_by_xpath("//button[@id='save_request']").click()
            # context.driver.find_element_by_xpath("//h1[contains(.,'Infrastructure and Facilities')]").is_displayed()

@given('user is on the Infrastructure tab')
def step_impl(context):
    sleep(3)
    context.driver.find_element_by_xpath("//*[@id='tab_name']//a[contains(.,'Infrastructure')]").click()
    assert context.driver.find_element_by_xpath("//h1[contains(.,'Infrastructure and Facilities')]").is_displayed()

@when('user clicks on edit option corresponding to any facility')
def step_impl(context):
    sleep(4)
    context.driver.find_element_by_xpath("//div[contains(.,'Hostel')]/parent::*/div/span[contains(@class,'edit_icon')]").click()

@when('user adds a hostel facility in the infrastructure tab')
def step_imp(context):
    sleep(3)
    # addNewButtonIsDisplayed=context.driver.find_element_by_xpath(".//*[@id='infracomp']//button[contains(.,'Add New')]").is_displayed()
    try:
        context.driver.find_element_by_xpath("//div[contains(.,'Hostel')]/parent::*/div/span[contains(@class,'edit_icon')]").is_displayed()
        context.driver.find_element_by_xpath("//div[contains(.,'Hostel')]/parent::*/div/span[contains(@class,'edit_icon')]").click()
    except(NoSuchElementException):
        context.driver.find_element_by_xpath(".//*[@id='infracomp']//button[contains(.,'Add New')]").click()
        Select(context.driver.find_element_by_xpath(".//*[@id='select_div_1']")).select_by_visible_text("Hostel")
        facilityCheckboxList=context.driver.find_elements_by_id("inlineCheckBox1")
        for items in facilityCheckboxList:
            items.click()

@then('application opens up the edit option for the corresponding facility')
def step_impl(context):
    assert(context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1']").get_attribute("value")=="Hostel")

@when('user enters facility details information')
def step_impl(context):
    abc = context.driver.find_element_by_xpath(".//*[@id='infracomp']//label[text()='Facility Details']/parent::*//div[@class='jqte_editor']")
    abc.click()
    abc.clear()
    sleep(2)
    abc.send_keys(facilityDetails)
    abc.send_keys("1")
    sleep(2)

@then('application closes the edit option for the corresponding tab')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath(".//*[@id='infracomp']//h2[contains(.,'Add/Edit Facility')]").is_displayed()
    except NoSuchElementException:
        pass

@when('application enters "Infrastructure Summary"')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='infraSummaryComp']//label[text()='Infrastructure Summary']/parent::*//div[@class='jqte_editor']").click()
    context.driver.find_element_by_xpath(".//*[@id='infraSummaryComp']//label[text()='Infrastructure Summary']/parent::*//div[@class='jqte_editor']").clear()
    context.driver.find_element_by_xpath(".//*[@id='infraSummaryComp']//label[text()='Infrastructure Summary']/parent::*//div[@class='jqte_editor']").send_keys(infrastructureSummary)
    context.driver.find_element_by_xpath(".//*[@id='infraSummaryComp']//label[text()='Infrastructure Summary']/parent::*//div[@class='jqte_editor']").send_keys("1")

@then('application redirects the user to the "Placements" tab')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath(".//*[@id='college_overview']//h1[contains(.,'Placements')]").is_displayed())
    except:
        context.driver.find_element_by_xpath(".//*[@id='save_request']").click()
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath(".//*[@id='college_overview']//h1[contains(.,'Placements')]").is_displayed())

@when('application tries to verify all the infrastructure details entered by the user')
def step_impl(context):
    sleep(5)
    # assert (context.driver.find_element_by_xpath(".//*[@id='infraSummaryComp']//label[text()='Infrastructure Summary']/parent::*//div[@class='jqte_editor']").get_attribute("value")==infrastructureSummary)
    context.driver.find_element_by_xpath("//div[contains(.,'Hostel')]/parent::*/div/span[contains(@class,'edit_icon')]").click()
    assert (context.driver.find_element_by_xpath(".//*[@id='infracomp']//label[text()='Facility Details']/parent::*//div[@class='jqte_editor']").text==facilityDetails)

@then('application displays all the information are correctly entered')
def step_impl(context):
    pass

@given('user is on the placement tab')
def step_impl(context):
    try:
        context.driver.find_element_by_xpath(".//*[@id='college_overview']//h1[contains(.,'Placements')]").is_displayed()
    except NoSuchElementException:
        context.driver.find_element_by_xpath("//*[@id='tab_name']//a[contains(.,'Placements')]").click()
        context.driver.find_element_by_xpath(".//*[@id='college_overview']//h1[contains(.,'Placements')]").is_displayed()

@when('user tries to enter information in the placements tab')
def step_impl(context):
    # context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Placement Summary')]/parent::*//div[@class='jqte_editor']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Placement Summary')]/parent::*//div[@class='jqte_editor']").send_keys(placementSummary)
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='students_placed']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='students_placed']").send_keys("20")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='total_offers']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='total_offers']").send_keys("20")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='average_salary']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='average_salary']").send_keys("20")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='median_salary']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='median_salary']").send_keys("20")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='highest_salary']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='highest_salary']").send_keys("20")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='year']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='year']").send_keys("2016")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='visiting_companies_count']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='visiting_companies_count']").send_keys("20")

@then('application redirects the user to the faculty tab')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath(".//*[@id='college_overview']//h1[contains(.,'Faculty Information')]").is_displayed())
    except:
        context.driver.find_element_by_xpath(".//*[@id='save_request']").click()
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath(".//*[@id='college_overview']//h1[contains(.,'Faculty Information')]").is_displayed())

@when('application tries to verify the entered information in the placement tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Placement Summary')]/parent::*//div[@class='jqte_editor']").text==placementSummary
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='students_placed']").get_attribute("value")=="20"
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='total_offers']").get_attribute("value")=="20"
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='average_salary']").get_attribute("value")=="20"
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='median_salary']").get_attribute("value")=="20"
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='highest_salary']").get_attribute("value")=="20"
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='year']").get_attribute("value")=="2016"
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='visiting_companies_count']").get_attribute("value")=="20"

@given('user is on the faculty tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Faculty')]").click()

@when('application tries to enter information in the faculty tab')
def step_impl(context):
    Select(context.driver.find_element_by_xpath(".//*[@id='college_overview']//select[@name='designation']")).select_by_visible_text("Dean")
    context.driver.find_element_by_xpath("//input[@id='exampleInputEmail1' and @name='name']").clear()
    context.driver.find_element_by_xpath("//input[@id='exampleInputEmail1' and @name='name']").send_keys("Name of the senior member")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//textarea[@name='profile']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//textarea[@name='profile']").send_keys("Profile of senior member")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//textarea[@name='message']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//textarea[@name='message']").send_keys("Message from the senior member")
    # context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Faculty Details')]/parent::*//div[@class='jqte_editor']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Faculty Details')]/parent::*//div[@class='jqte_editor']").send_keys("Summary of the faculty")
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='permanent_faculty_count']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='permanent_faculty_count']").send_keys("20")
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='visiting_faculty_count']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='visiting_faculty_count']").send_keys("20")

@then('application redirects the user to the gallery tab')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Gallery')]").is_displayed())
    except:
        context.driver.find_element_by_xpath(".//*[@id='save_request']").click()
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Gallery')]").is_displayed())

@when('application tries to verify the entered information in the faculty tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//select[@name='designation']/parent::*/div[contains(.,'Dean')]").is_displayed()
    assert context.driver.find_element_by_xpath("//input[@id='exampleInputEmail1' and @name='name']").get_attribute("value")=="Name of the senior member"
    assert context.driver.find_element_by_xpath(".//*[@id='college_overview']//textarea[@name='profile']").get_attribute("value")=="Profile of senior member"
    assert context.driver.find_element_by_xpath(".//*[@id='college_overview']//textarea[@name='message']").get_attribute("value")=="Message from the senior member"
    assert context.driver.find_element_by_xpath(".//*[@id='college_overview']//label[contains(.,'Faculty Details')]/parent::*//div[@class='jqte_editor']").text=="Summary of the faculty"
    assert context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='permanent_faculty_count']").get_attribute("value")=="20"
    assert context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @name='visiting_faculty_count']").get_attribute("value")=="20"

@given('user is on the financial detail tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Financial Details')]").click()

@when('application tries to enter information in the financial detail')
def step_impl(context):
    context.driver.find_element_by_xpath("//*[@id='scholorship1']").click()
    context.driver.find_element_by_xpath(".//*[@id='scholorship_detail']//label[text()='Scholarship Detail']/parent::*//div[@class='jqte_editor']").clear()
    context.driver.find_element_by_xpath(".//*[@id='scholorship_detail']//label[text()='Scholarship Detail']/parent::*//div[@class='jqte_editor']").send_keys("Scholarship details of the college")
    chooseCourseOption = context.driver.find_elements_by_xpath(".//*[@id='mCSB_1_container']/ul/li")
    # NoOfChooseCourseOption = len(context.driver.find_elements_by_xpath(".//*[@id='mCSB_1_container']/ul/li"))
    a=1;
    for items in chooseCourseOption:
        try:
            xpathForCheckedCheckBox=".//*[@id='mCSB_1_container']/ul/li[{}]/input[@checked='checked']".format(a)
            context.driver.find_element_by_xpath(xpathForCheckedCheckBox)
            a+=1
        except NoSuchElementException:
            xpathForUnCheckedCheckBox=".//*[@id='mCSB_1_container']/ul/li[{}]/input".format(a)
            b= context.driver.find_element_by_xpath(xpathForUnCheckedCheckBox)
            b.click()
            a+=1

@then('application redirects the user to the "Point of Contact" page')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Point of Contact')]").is_displayed())
    except:
        context.driver.find_element_by_xpath(".//*[@id='save_request']").click()
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Point of Contact')]").is_displayed())

@when('application tries to verify the entered information in the financial details tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='scholorship1' and @checked='checked']").is_displayed()
    assert context.driver.find_element_by_xpath(".//*[@id='scholorship_detail']//label[text()='Scholarship Detail']/parent::*//div[@class='jqte_editor']").text=="Scholarship details of the college"

@given('user is on the "point of contact" tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Point of Contact')]").click()

@when('user enters all the spoc information')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='name' and @name='name']").clear()
    context.driver.find_element_by_xpath(".//*[@id='name' and @name='name']").send_keys("Name of college Spoc")
    context.driver.find_element_by_xpath(".//*[@id='designation' and @name='designation']").clear()
    context.driver.find_element_by_xpath(".//*[@id='designation' and @name='designation']").send_keys("Designation of college Spoc")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='email']").clear()
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='email']").send_keys("abc@abc.com")
    context.driver.find_element_by_xpath(".//*[@id='contact_number']").clear()
    context.driver.find_element_by_xpath(".//*[@id='contact_number']").send_keys("9876543210987,987876768")

@when('user click on "Add New" button corresponding to "Campus Journalist" section')
def step_impl(context):
    sleep(2)
    context.driver.find_element_by_xpath(".//*[@id='journalistcomp']//button[contains(.,'Add New')]").click()

@when('user enters "Campus Journalist" information')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Name']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Name']").send_keys(campusJournalist)
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Email']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Email']").send_keys("abc@abc.com")
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Contact Number']").clear()
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Contact Number']").send_keys("9876543210")

@when('application tries to verify the entered information in the "Point of Contact" details tab')
def step_impl(context):
    sleep(3)
    assert context.driver.find_element_by_xpath(".//*[@id='name' and @name='name']").get_attribute("value")==("Name of college Spoc")
    context.driver.find_element_by_xpath(".//*[@id='designation' and @name='designation']").get_attribute("value")==("Designation of college Spoc")
    context.driver.find_element_by_xpath(".//*[@id='college_overview']//input[@name='email']").get_attribute("value")==("abc@abc.com")
    context.driver.find_element_by_xpath(".//*[@id='contact_number']").get_attribute("value")==("9876543210987,987876768")
    xpathForJournalistNameEditIcon=".//*[@id='journalistcomp']//div[contains(.,'{}')]/span[contains(@class,'edit_icon')]".format(campusJournalist)
    context.driver.find_element_by_xpath(xpathForJournalistNameEditIcon).click()
    sleep(2)
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Name']").get_attribute("value")==(campusJournalist)
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Email']").get_attribute("value")==("abc@abc.com")
    context.driver.find_element_by_xpath(".//*[@id='exampleInputEmail1' and @placeholder='Enter Contact Number']").get_attribute("value")==("9876543210")

@then('application redirect the user to the "Alumni & Testimonials" tab')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Alumni & Testimonials')]").is_displayed())
    except:
        context.driver.find_element_by_xpath(".//*[@id='save_request']").click()
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath("//h1[contains(.,'Alumni & Testimonials')]").is_displayed())

@given('user is on the "alumini & testimonial" tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Alumni & Testimonials')]").click()

@when('user entered alumini details')
def step_impl(context):
    sleep(5)
    context.driver.find_element_by_xpath("//div[@id='alumcomp']//button").click()
    context.driver.find_element_by_xpath("//div[@class='col-md-12']/div/input").send_keys(aluminiName)
    context.driver.find_element_by_xpath("//ul[contains(@class,'form-list')]/li[2]/div/input").send_keys("2011")
    Select(context.driver.find_element_by_xpath(".//select[@id='select_div_1']")).select_by_visible_text("CAPGEMINI")
    context.driver.find_element_by_xpath("//button[contains(.,'Save Alumni')]").click()

@when('user entered testimonial details')
def step_impl(context):
    sleep(12)
    context.driver.find_element_by_xpath(".//*[@id='testimonialcomp']//button").click()
    context.driver.find_element_by_xpath(".//*[@class='col-md-12']/li[1]/div/input").send_keys(testimonialName)
    context.driver.find_element_by_xpath(".//*[@class='col-md-12']/li[2]/div/input").send_keys("Testimonial Message")
    context.driver.find_element_by_xpath("//div[@class='col-md-12']/parent::*/ul/li[2]/div/input").send_keys("2011")
    Select(context.driver.find_element_by_xpath(".//*[@id='select_div_2']")).select_by_index(1)
    context.driver.find_element_by_xpath(".//*[@id='testimonialcomp']//button[contains(.,'Save Testimonials')]").click()

@then('application redirect the user to the "Overview" tab')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Overview')]").is_displayed())
    except:
        context.driver.find_element_by_xpath(".//*[@id='save_request']").click()
        WebDriverWait(context.driver, 10).until(lambda driver: context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Overview')]").is_displayed())


@when('application tries to verify the entered information in the "Alumini & Testimonial" details tab')
def step_impl(context):
    sleep(2)
    xpathForeditingAluminiCreated=".//*[@id='alumcomp']//div[contains(.,'{}')]/span[contains(@class,'edit_icon')]".format(aluminiName)
    context.driver.find_element_by_xpath(xpathForeditingAluminiCreated).click()
    sleep(4)
    context.driver.find_element_by_xpath("//div[@class='col-md-12']/div/input").get_attribute("value")==(aluminiName)
    context.driver.find_element_by_xpath("//ul[contains(@class,'form-list')]/li[2]/div/input").get_attribute("value")==("2011")
    context.driver.find_element_by_xpath(".//*[@id='select_div_1']/parent::*/div[@class='out' and contains(.,'CAPGEMINI')]").is_displayed()
    sleep(2)
    # xpathForEditTestimonialCreated=".//*[@id='testimonialcomp']//div[contains(.,'{}')]/span[contains(@class,'edit_icon')]".format(testimonialName)
    # context.driver.find_element_by_xpath(xpathForEditTestimonialCreated).click()
    # sleep(4)
    # context.driver.find_element_by_xpath(".//*[@class='col-md-12']/li[1]/div/input").get_attribute("value")==(testimonialName)
    # context.driver.find_element_by_xpath(".//*[@class='col-md-12']/li[2]/div/input").get_attribute("value")==("Testimonial Message")
    # context.driver.find_element_by_xpath("//div[@class='col-md-12']/parent::*/ul/li[2]/div/input").get_attribute("value")==("2011")

@given('user is on the "Gallery" tab')
def step_impl(context):
    context.driver.find_element_by_xpath(".//*[@id='tab_name']//a[contains(.,'Gallery')]").click()

@when('user creates a album')
def step_impl(context):
    sleep(4)
    context.driver.find_element_by_xpath(".//*[@id='imagecomp']/div/div[2]/a").click()
    context.driver.find_element_by_xpath("//label[contains(.,'Album Name')]/parent::*/input").send_keys(albumName)
    context.driver.find_element_by_xpath(".//*[@id='imagecomp']//button").click()

@then('application displays the album name in the list')
def step_impl(context):
    sleep(10)
    XpathalbumName=".//*[@id='imagecomp']//h4[contains(.,'{}')]".format(albumName)
    context.driver.find_element_by_xpath(XpathalbumName).is_displayed()

@when('user creates a "video gallery"')
def step_impl(context):
    sleep(3)
    context.driver.find_element_by_xpath(".//*[@id='videocomp']//button").click()
    sleep(2)
    context.driver.find_element_by_xpath("//label[contains(.,'Video Title')]/parent::*/input").send_keys(videoName)
    context.driver.find_element_by_xpath("//label[contains(.,'Video Link')]/parent::*/input").send_keys("https://www.google.com")
    Select(context.driver.find_element_by_xpath(".//*[@id='album']")).select_by_index(1)
    context.driver.find_element_by_xpath(".//*[@id='videocomp']//button[contains(.,'Save Video')]").click()

@then('application displays the video name in the list')
def step_impl(context):
    sleep(10)
    xpathForVideo=".//*[@id='videocomp']//div[contains(.,'{}')]/span[contains(@class,'edit_icon')]".format(videoName)
    context.driver.find_element_by_xpath(xpathForVideo).is_displayed()

@when('user click on submit button from any tab')
def step_impl(context):
    global noOfRequest
    noOfRequest=context.driver.find_element_by_xpath("//ul[@id='tab_name']//span[@class='update-count']").text
    context.driver.find_element_by_xpath(".//*[@id='submit_request' and contains(.,'Final Submit')]").click()
    sleep(2)
    try:
        alert = context.driver.switch_to_alert()
        alert.accept()
    except(NoAlertPresentException):
        pass
    sleep(5)

@then('application raises request for all the save records')
def step_impl(context):
    totalNotificationRequest=context.driver.find_element_by_xpath("//ul[@id='tab_name']//span[@class='update-count']").text
    global noOfRequestRaised
    noOfRequestRaised=int(totalNotificationRequest)-int(noOfRequest)
    assert noOfRequestRaised >=9
