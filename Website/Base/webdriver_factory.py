from selenium import webdriver
import os
class WebDriverFactory():
        def __init__(self, browser):

            self.browser = browser


        def getWebDriverInstance(self):
            """
           Get WebDriver Instance based on the browser configuration

            Returns:
                'WebDriver Instance'
            """
            baseURL = "https://workex.jobs/home"
            if self.browser == "iexplorer":
                # Set ie driver
                driver = webdriver.Ie()
            elif self.browser == "firefox":
                driver = webdriver.Firefox()
            elif self.browser == "chrome":
                # Set chrome driver
                chromepath = "/home/kavya/Downloads/chromedriver_linux64/chromedriver"
                os.environ["webdriver.chrome"] = chromepath
                driver = webdriver.Chrome(chromepath)
            else:
                driver = webdriver.Firefox()
            # Setting Driver Implicit Time out for An Element
            driver.implicitly_wait(3)
            # Maximize the window
            driver.maximize_window()
            # Loading browser with  URL
            driver.get(baseURL)
            return driver