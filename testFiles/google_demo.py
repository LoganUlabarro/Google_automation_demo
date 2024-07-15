# page objects
from pages.home_page import homePage

# utilities
from utilities.test_status import ResultHandler
from utilities.get_env_settings import getEnvSettings

# assertions and data
import unittest
import pytest

# get environment settings
envSettings = getEnvSettings()
testEnvironment = envSettings[2]
testDataType = envSettings[3]

# Uses one time setup and setup from conftest file
@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class SmokeTests(unittest.TestCase):

    # set up page object for all tests
    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        # set up page objects
        self.home = homePage(self.driver)
        # set up test status
        self.ts = ResultHandler(self.driver)

    # our login test, verifies that the mdmportal header appears after login
    @pytest.mark.run(order=1)
    def test_valid_login(self):
        # run login page steps
        print('running search tests')
        result1 = self.home.verifyGoogleLogo()
        self.ts.mark(result1, 'Navigated to google')
        self.home.searchGoogle('Pine Trees')
        result2 = True
        self.ts.markFinal('test_search_1', result2, 'Successfully searched for Desktop computers')
