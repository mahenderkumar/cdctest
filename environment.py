from selenium import webdriver
from behave import *
from selenium.webdriver.support.ui import WebDriverWait
import os
import os.path
import zipfile
import glob
import datetime
from time import time
#from pyvirtualdisplay import Display
import sys
import csv
from selenium.webdriver.support.ui import Select
from time import sleep
from random import randint
from selenium.common.exceptions import NoSuchElementException, TimeoutException

#baseurl = "http://desertrose.htcampus.com"
baseurl = "http://cms.staging.htcampus.com"
#baseurl = "http://localhost:8000"
#baseurl = "http://dev.cms.staging.htcampus.com"
aboutCollege="Test College User "
b=randint(100000, 999999)
collegeName="{}{}".format(aboutCollege,b)
global FEATURE_FAILED_STATUS_COUNT
FEATURE_FAILED_STATUS_COUNT=0
#FEATURE_PASSED_STATUS_COUNT=0
# collegeName="Test College User 831633"
#debug = False
headless = False

# USE: behave -D debug      (to enable  debug-on-error)
# USE: behave -D debug=yes     (to enable  debug-on-error)
# USE: behave -D debug=no      (to disable debug-on-error)

#def setup_debug(userdata):
   # global debug
    #debug = userdata.getbool("debug")

#def setup_headless(userdata):
    #global headless
    #headless = userdata.getbool("headless")

# method for browser selection
def browser_sel(browser):
        # Create a new instance of the Chrome driver
    if browser == 'c' or browser == 'chrome':
        return webdriver.Chrome()
        # defining a browser agent for phantomjs
    elif browser == 'h' or browser == 'headless':
        browser_info = dict(webdriver.DesiredCapabilities.PHANTOMJS)
        browser_info["phantomjs.page.settings.useragent"] =\
            ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
             "Chrome/43.0.2357.130 Safari/537.36")

        # Create a new instance of the Headless (PhantomJS) driver
        return webdriver.PhantomJS(desired_capabilities=browser_info)
        # run after execution of phantomjs "pgrep phantomjs | xargs kill"
    else:
        # Create a new instance of the Firefox driver
        fp = webdriver.FirefoxProfile()
        fp.set_preference("network.proxy.type", 0)
        #fp.add_extension(extension='reports/firebug-2.0-fx.xpi')
        #fp.add_extension(extension='reports/JSErrorCollector.xpi')
        #fp.set_preference("extensions.firebug.currentVersion", "2.0") #Avoid startup screen
        #fp.set_preference("extensions.firebug.console.enableSites", "true")
        #fp.set_preference("extensions.firebug.net.enableSites", "true")
        #fp.set_preference("extensions.firebug.script.enableSites", "true")
        #fp.set_preference("extensions.firebug.allPagesActivation", "On")
        return webdriver.Firefox(firefox_profile=fp)
        

def login_application(context):
    context.driver.get(baseurl+"/college-data-capture/login/")
    try:
        sleep(6)
        Select(context.driver.find_element_by_id("id_state")).select_by_visible_text("Andhra Pradesh")
        sleep(3)
        Select(context.driver.find_element_by_id("id_city")).select_by_visible_text("Chittoor")
        sleep(3)
        Select(context.driver.find_element_by_id("id_institute")).select_by_visible_text(collegeName)
        context.driver.find_element_by_id("id_password").send_keys("12345")
        context.driver.find_element_by_xpath(".//*[@id='id_login_form']/ul/li[5]/input").click()
    except(NoSuchElementException,TimeoutException):
        try:
            sleep(4)
            Select(context.driver.find_element_by_id("id_state")).select_by_visible_text("Andhra Pradesh")
            sleep(3)
            Select(context.driver.find_element_by_id("id_city")).select_by_visible_text("Chittoor")
            sleep(3)
            Select(context.driver.find_element_by_id("id_institute")).select_by_visible_text(collegeName)
            context.driver.find_element_by_id("id_password").send_keys("12345")
            context.driver.find_element_by_xpath(".//*[@id='id_login_form']/ul/li[5]/input").click()
        except(NoSuchElementException,TimeoutException):
            raise

def admin_user_login(context):
    context.driver.get(baseurl+"/admin/")
    WebDriverWait(context.driver, 15).until(lambda driver: context.driver.find_element_by_xpath(".//*[@id='id_username']").is_displayed())
    context.driver.find_element_by_xpath(".//*[@id='id_username']").send_keys("fasih")
    context.driver.find_element_by_xpath(".//*[@id='id_password']").send_keys("google")
    context.driver.find_element_by_xpath(".//*[@id='grp-content-container']//input[@value='Log in']").click()
    
def new_college_user(context):
    context.driver.get(baseurl+"/college-data-capture/register/")
    try:
        sleep(7)
        Select(context.driver.find_element_by_id("id_state")).select_by_visible_text("Andhra Pradesh")
        sleep(5)
        Select(context.driver.find_element_by_id("id_city")).select_by_visible_text("Chittoor")
        sleep(4)
        context.driver.find_element_by_id("id_institute").send_keys(collegeName)
        context.driver.find_element_by_id("id_password").send_keys("12345")
        context.driver.find_element_by_xpath(".//*[@id='id_register_form']/ul/li[5]/input").click()
    except(NoSuchElementException,TimeoutException):
        try:
            sleep(7)
            Select(context.driver.find_element_by_id("id_state")).select_by_visible_text("Andhra Pradesh")
            sleep(5)
            Select(context.driver.find_element_by_id("id_city")).select_by_visible_text("Chittoor")
            sleep(4)
            context.driver.find_element_by_id("id_institute").send_keys(collegeName)
            context.driver.find_element_by_id("id_password").clear()
            context.driver.find_element_by_id("id_password").send_keys("12345")
            context.driver.find_element_by_xpath(".//*[@id='id_register_form']/ul/li[5]/input").click()
        except(NoSuchElementException,TimeoutException):
            raise

#def before_all(context):
    #global startTimeOfTest
    #startTimeOfTest = time()
    #setup_debug(context.config.userdata)
    #setup_headless(context.config.userdata)
    #screenshot_method()
    #if headless == True:
        #global display
        #display = Display(visible=0, size=(1366, 768)) #for desktop view
        #display.start()

#def screenshot_method():
    #date_time_now = datetime.datetime.utcnow()
    #delta = datetime.timedelta(5)
    #delete_files = date_time_now - delta
    #basedir = os.path.dirname(os.path.dirname(__file__))
    #snapshotsfile = glob.glob(os.path.join(basedir, 'reports/screenshot/*'))
    #snapshotsfile = glob.glob(os.path.join(basedir, 'results/static/screenshot/*'))
    #for f in snapshotsfile:
        #if os.path.isfile(f):
            #t = os.path.getmtime(f)
            #date_time_now = datetime.datetime.utcfromtimestamp(t)
            #if date_time_now <= delete_files:
                #try:
                   # os.remove(f)
                #except OSError:
                    #pass

def before_feature(context,feature):
    browser = context.config.userdata.get("browser")
    context.driver = browser_sel(browser)
    context.driver.maximize_window()
    #jsError(context)
    context.baseurl = baseurl
    context.collegeName = collegeName
    var = context.feature.name
    if var=="Verify new college user is created":
         new_college_user(context)
    elif var=="Verify College Data Capture Portal":
         login_application(context)
    elif var=="Verify cms admin captures all the request":
          admin_user_login(context)
          
#def after_step(context, step):
    #if step.status =="failed":
        #os.makedirs(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports/screenshot'));
        #now = datetime.datetime.now().strftime("%I:%M%p-on-%B-%d,%Y")
        #context.driver.get_screenshot_as_file('reports/screenshot/screenshot-%s.png' % now)
        #context.driver.get_screenshot_as_file('results/static/screenshot/screenshot-%s.png' % now)
        #jsError(context)
            # -- ENTER DEBUGGER: Zoom in on failure location.
            # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        #if debug and step.status == "failed":
            #import ipdb
            #ipdb.post_mortem(step.exc_traceback)

#def jsError(context):
    #basedir = os.path.dirname(os.path.dirname(__file__))
    #csvfile = os.path.join(basedir, 'reports', 'error.csv')
    #error = context.driver.execute_script("return window.console.error()")
    #errors = context.driver.execute_script("return window.JSErrorCollector_errors ? window.JSErrorCollector_errors.pump() : []")
    ##writing errors in a file csv
    #jserr = open(csvfile, 'a+')
    #now = datetime.datetime.now().strftime("%I:%M%p-on-%B-%d,%Y")
    #err = csv.writer(jserr)
    #for error in errors:
        #err.writerow([now, context.driver.current_url]+ error.values())
    #jserr.close()

#def after_feature(context, feature):
   # if feature.status=="failed":
       # global FEATURE_FAILED_STATUS_COUNT
       # FEATURE_FAILED_STATUS_COUNT+=1
    #context.driver.quit()

#def after_all(context):
    #if headless==True:
        #display.stop()
    #global FEATURE_FAILED_STATUS_COUNT
    #File=open("DataFile.txt","w")
    #File.write("Failed_Status={}".format(FEATURE_FAILED_STATUS_COUNT))
    #File.close()
    #endTimeOfTest = time()
    #global TestExecutionTime
    #TestExecutionTime = endTimeOfTest - startTimeOfTest
    #sys.stdout.write(str(datetime.timedelta(seconds=TestExecutionTime)))
