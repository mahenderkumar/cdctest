from behave import *
from random import randint
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@given('user sign-up as new user')
def step_impl(context):
    pass

@given('user is on the overview page of new user')
def step_impl(context):
    context.driver.find_element_by_xpath("//h1[contains(.,'Your College Overview :')]").is_displayed()

@then('user logs out of the application')
def step_impl(context):
    context.driver.get(context.baseurl+"/college-data-capture/logout/")
   
@when('admin user launches cms admin with valid credentials')
def step_impl(context):
    context.driver.get(context.baseurl+"/admin/")
    context.driver.find_element_by_xpath(".//*[@id='id_username']").send_keys("fasih")
    context.driver.find_element_by_xpath(".//*[@id='id_password']").send_keys("google")
    context.driver.find_element_by_xpath(".//*[@id='grp-content-container']//input[@value='Log in']").click()
    
@when('navigate to college wise request page')
def step_impl(context):
    #context.driver.find_element_by_xpath(".//*[@id='model-collegewiserequest']/a/strong[contains(.,'College wise requests')]").click()
    #context.driver.find_element_by_xpath(".//*[@id='model-collegewiserequest']/a/strong").click()
    sleep(15)
    #context.driver.find_element_by_id("model-collegewiserequest").click()
    context.driver.find_element_by_xpath(".//*[@id='model-collegewiserequest']/a/strong[contains(.,'College wise requests')]").click()
    
@then('application displays one request for college user')
def step_impl(context):
    collegeName=context.collegeName
    xpath=".//*[@id='result_list']//a[contains(.,'{}')]".format(collegeName)
    context.driver.find_element_by_xpath(xpath).click()
    context.driver.find_element_by_xpath(xpath).click()
    
@when('admin user approves the request')
def step_impl(context):
    sleep(5)
    context.driver.switch_to.frame(context.driver.find_element_by_tag_name("iframe"))
    context.driver.find_element_by_xpath("html/body").send_keys("Approve")
    context.driver.switch_to.default_content()
    
@then('application creates the college in HTCampus')
def step_impl(context):
    sleep(10)
    context.driver.find_element_by_xpath(".//*[@id='moderatedobject_form']/div/input[@name='approve']").click()


