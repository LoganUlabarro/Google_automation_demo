from base.selenium_driver_util import seleniumDriver
import utilities.custom_logger as cl
import logging

class homePage(seleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log.info('*+' * 35)

    #locators
    _search_bar = '.gLFyf'
    _google_btn = '//img[@alt="Google"]'

    def verifyGoogleLogo(self):
        self.waitForElementVisible(self._google_btn, 'xpath')
        if self.isElementPresent(self._google_btn, 'xpath'):
            return True
        else:
            return False

    def searchGoogle(self, searchTerm):
        self.waitForElementVisible(self._search_bar, 'css')
        try:
            self.clearValue(self._search_bar, 'css')
            self.setValue(searchTerm, self._search_bar, 'css')
            self.pressEnter(self._search_bar, 'css')
        except():
            print('failed to search for ' + searchTerm)

    