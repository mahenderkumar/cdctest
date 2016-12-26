from selenium.webdriver.support.ui import WebDriverWait
import requests

def cw(pageobj,driver):
    if WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_xpath(pageobj).is_displayed()):
        return True
    else:
        return False

def httpResponse(url):
    try:
        r = requests.head(url)
        print(r.status_code)
    except requests.ConnectionError:
        print("failed to connect")

