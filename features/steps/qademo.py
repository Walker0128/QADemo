from behave import *
from selenium import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

use_step_matcher("re")

@given("search keyword on google")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    text = "list of cloud platform"
    context.browser.get("https://www.google.co.uk")
    time.sleep(5)
    context.browser.find_element_by_xpath("//*[contains(test()='agree')]").click()
    searchBar = context.browser.find_element_by_name("q")
    searchBar.clear()
    searchBar.send_keys(text)
    searchBar.send_keys(Keys.ENTER)


@then("we should get result on ZDnet")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.browser.find_element_by_xpath(
        "//*[contains(text(),'Top cloud providers: AWS, Microsoft Azure, and ... - ZDNet')]").click()

@given("list of cloud platform on ZDNet")
def step_impl(context: object):
    """
    :type context: behave.runner.Context
    """
    try:
        context.browser.get(
        "https://www.zdnet.com/article/the-top-cloud-providers-of-2021-aws-microsoft-azure-google-cloud-hybrid-saas/")
        time.sleep(3)
        cookingButton = context.browser.find_element_by_id("onetrust-reject-all-handler")
        if cookingButton:
            cookingButton.click()
    except:
        pass


@when("we check the list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        context.browser.listOfPlatForm = context.browser.find_elements_by_class_name('precap-hed')
        context.browser.listOfName = []
        for i in context.browser.listOfPlatForm:
            context.browser.listOfName.append(i.get_attribute("textContent").strip())
    except:
        raise NotImplementedError(u'STEP: When we check the list')



@then("we should find (?P<name>.+)")
def step_impl(context, name):
    """
    :type context: behave.runner.Context
    :type name: str
    """
    try:
        assert name in context.browser.listOfName
        # assert name in context.browser.page_source
    except:
        raise NotImplementedError(u'STEP: When we we should find name')


@Given("click on View now at AWS button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    name = 'Amazon Web Services'
    context.handle = context.browser.current_window_handle
    if name in context.browser.listOfName:
        context.browser.find_element_by_xpath("//*[contains(text(),'View now at AWS')]").click()
        time.sleep(3)


@then("it opens up a new tab within the same browser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        handles = context.browser.window_handles
        if len(handles) > 1:
            context.browser.switch_to.window(handles[1])
            assert True
        else:
            assert False
    except:
        raise NotImplementedError(u'STEP: Then it opens up a new tab within the same browser')


@step("it opens up AWS page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        expectURL = "aws.amazon.com/what-is-aws"
        currentURL = context.browser.current_url
        assert expectURL in currentURL
    except:
        raise NotImplementedError(u'STEP: And it opens up AWS page')


@step("it lands to the page which shows AWS title")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    try:
        expectTitle = "Cloud computing with AWS"
        # currentTitle = context.browser.title
        # assert expectTitle in currentTitle
        assert expectTitle in context.browser.page_source
    except:
        raise NotImplementedError(u'STEP: And it lands to the page which shows “Cloud computing with AWS “')


