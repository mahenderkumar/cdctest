from behave import *
from random import randint
from a2collegeDataCapture import *
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

# from nose.tools import assert_false, assert_true
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

@given('user launches the cms admin site')
def step_impl(context):
    pass

@given('user is on the college request page')
def step_impl(context):
    context.driver.get(context.baseurl+"/admin/content_moderation/collegewiserequest/")
    collegeNameList=".//*[@id='result_list']//a[contains(.,'{}')]".format(context.collegeName)
    context.driver.find_element_by_xpath(collegeNameList).click()

@when('application counts the number of raised request which are in submitted status')
def step_impl(context):
    raisedRequestList=context.driver.find_elements_by_xpath(".//*[@id='result_list']/tbody//td[contains(.,'Submitted/Waiting for approval')]")
    global numberOfRaisedRequest
    numberOfRaisedRequest= len(raisedRequestList)
    assert numberOfRaisedRequest>=9

@then('application should display total number of raised request from cdc frontend is equal to cms admin')
def step_impl(context):
    pass
    # assert noOfRequest==numberOfRaisedRequest

@then('application should display the number of models request')
def step_impl(context):
    modelTypeRequestRaisedList=context.driver.find_elements_by_xpath(".//*[@id='result_list']/tbody//td[contains(.,'Submitted/Waiting for approval')]/parent::*/td[2]")
    modelListOfAvailableRequest=['college spoc','journalist','domestic financial detail','college album','domestic faculties','domestic placement','domestic infrastructure','domestic course','domestic college']
    modelListFromRaisedRequest=[]
    ItemsNotAvailableInTheRequest=[]
    for items in modelTypeRequestRaisedList:
        a=items.text
        modelListFromRaisedRequest.append(a)
    def comp(modelListOfAvailableRequest, modelListFromRaisedRequest):
        for val in modelListOfAvailableRequest:
            if val in modelListFromRaisedRequest:
                return True
            else:
                ItemsNotAvailableInTheRequest.append(val)
        print (ItemsNotAvailableInTheRequest)
