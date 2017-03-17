import unittest
from selenium import webdriver
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class verifyResults(unittest.TestCase):

    def test_search_in_jysk_ua(self):
        self.setUp()
        main_page = MainPage()
        main_page.search_text_element()
        main_page.click_go_button()
        main_page.check_results()

	def tearDown(self):
		self.driver.close()


class BasePage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.jysk.ua")


class MainPage(BasePage):
    def search_text_element(self):
        inputElement = self.driver.find_element_by_name("query")
        inputElement.send_keys("RYSLINGE")

    def click_go_button(self):
        clickElement = self.driver.find_element_by_name("op")
        clickElement.click()

    def check_results(self):
        WebDriverWait(self.driver, 20).until(EC.title_contains("JYSK"))
        xpathResult = self.driver.find_element_by_xpath("//div[@class = 'view-header']/h1/span")
        result = xpathResult.text
        print 'Count of RYSLINGE = ' + result
        print 'ssss'
        assert (int(result) == 8)


#if __name__ == "__main__":
#    test_search_in__jysk_ua()
