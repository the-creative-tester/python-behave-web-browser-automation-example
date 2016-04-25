from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()

def after_all(context):
    context.browser.close()
