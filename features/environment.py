# -- FILE: features/environment.py
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys



@fixture
def selenium_browser_chrome(context):
    chromeOption = Options()
    chromeOption.add_argument("--headless")
    # context.browser = webdriver.Chrome(options=chromeOption)
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(30)


# def getListofCloudPlatform(context):
#     context.browser.get("https://www.google.co.uk")
#     searchBar = context.browser.find_element_by_name('q')
#     searchBar.send_keys("list of cloud platform")
#     searchBar.send_keys(Keys.ENTER)


def before_feature(context, feature):
    selenium_browser_chrome(context)
    # getListofCloudPlatform(context)


def after_feature(context, feature):
    context.browser.quit()
