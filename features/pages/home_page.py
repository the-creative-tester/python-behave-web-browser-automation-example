from selenium.webdriver.common.by import By
from features.browser import Browser

class HomePageLocator(object):
    # Home Page Locators

    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "search")
    SUBMIT_BUTTON = (By.CLASS_NAME, "fa-search")


class HomePage(Browser):
    # Home Page Actions

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)
