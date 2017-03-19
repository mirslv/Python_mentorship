from selenium import webdriver
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_in_jysk_ua():
    driver = set_driver()
    main_page = MainPage(driver)
    main_page.search_text_element("RYSLINGE")
    main_page.click_go_button()
    assert main_page.check_results() == 8

def tearDown(self):
    self.driver.close()


def set_driver():
    driver = webdriver.Chrome()
    driver.get("http://www.jysk.ua")
    return driver


class MainPage(object):
    def __init__(self, webdriver):
        self.driver = webdriver
        
    def search_text_element(self, text):
        inputElement = self.driver.find_element_by_name("query")
        inputElement.send_keys(text)

    def click_go_button(self):
        clickElement = self.driver.find_element_by_name("op")
        clickElement.click()

    def check_results(self):
        WebDriverWait(self.driver, 20).until(EC.title_contains("JYSK"))
        xpathResult = self.driver.find_element_by_xpath("//div[@class = 'view-header']/h1/span")
        result = xpathResult.text
        print 'Count of RYSLINGE = ' + result
        return int(result)


#if __name__ == "__main__":
#    test_search_in__jysk_ua()
