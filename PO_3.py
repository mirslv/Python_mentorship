from selenium import webdriver
import pytest
from main_page import MainPage


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





