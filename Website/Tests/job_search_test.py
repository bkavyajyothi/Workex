from selenium import webdriver
from Utilities.test_status import TestStatus
from Pages.search_jobs_page import SearchJobsPage
from Pages.navigation_page import NavigationPage
import unittest
import time
import pytest

@pytest.mark.usefixtures("oneTimeSetUp")
class SearchJobTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.sjp = SearchJobsPage(self.driver)
        self.np = NavigationPage(self.driver)
        self.ts=TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_JobSearch(self):
        self.np.navigateToSearchPage()
        time.sleep(8)
        result = self.sjp.pageTitle()
        self.ts.markFinal("Search page navigation", result, "Search page navigation successful")


