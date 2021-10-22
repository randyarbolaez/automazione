from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager


class FindCompanyUrl:
    def findCompanyUrlInLeverWebsite(self, jobLink):
        self.driver.get(jobLink)
        try:
            companyUrl = jobLink = self.driver.find_element_by_css_selector(
                'body > div.main-footer.page-full-width > div > p > a').get_attribute('href')
        except NoSuchElementException:
            companyUrl = 'N/A'
        return companyUrl

    def findCompanyUrlInGreenhouseWebsite(self, jobLink):
        self.driver.get(jobLink)
        try:
            companyUrl = jobLink = self.driver.find_element_by_css_selector(
                '#logo > a').get_attribute('href')
        except NoSuchElementException:
            companyUrl = 'N/A'
        return companyUrl
