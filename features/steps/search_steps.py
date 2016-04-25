from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to the PyPi Home page')
def step_impl(context):
    context.home_page.navigate("https://pypi.python.org/pypi")
    assert_equal(context.home_page.get_page_title(), "PyPI - the Python Package Index : Python Package Index")

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)

@step('I am taken to the PyPi Search Results page')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Index of Packages Matching 'behave' : Python Package Index")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))