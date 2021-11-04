from selenium.common.exceptions import NoSuchElementException


class FindCompanyUrl:
    def leverWebsite(self, jobLink):
        self.driver.get(jobLink)
        try:
            companyUrl = jobLink = self.driver.find_element_by_css_selector(
                'body > div.main-footer.page-full-width > div > p > a').get_attribute('href')
        except NoSuchElementException:
            companyUrl = False
        return companyUrl

    def greenhouseWebsite(self, jobLink):
        self.driver.get(jobLink)
        try:
            companyUrl = jobLink = self.driver.find_element_by_css_selector(
                '#logo > a').get_attribute('href')
        except NoSuchElementException:
            companyUrl = False
        return companyUrl
