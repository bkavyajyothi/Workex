import Utilities.custom_logger as cl
import logging
from Base.selenium_driver import SeleniumDriver

class NavigationPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    Workex_logo="//a[@title='Explore Jobs on Workex' and contains(text(),'Search Jobs')]"
    Search_jobs="//a[@title='Explore Jobs on Workex' and contains(text(),'Search Jobs')]"

    def navigateToHomePage(self):

        self.clickElement(self.Workex_logo, locatorType="xpath")

    def navigateToSearchPage(self):
        self.clickElement(self.Search_jobs, locatorType="xpath")