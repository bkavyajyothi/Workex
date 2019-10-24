from Base.selenium_driver import SeleniumDriver

class SearchJobsPage(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)

    #Locators
    expected_title="Jobs - Recruitment - Hiring - Job Search- Job Vacancies - Workex"



    def pageTitle(self):
        result=None
        actual_title=self.getPageTitle()
        if self.expected_title== actual_title:
            result=True
        else:
            result=False

        return result

