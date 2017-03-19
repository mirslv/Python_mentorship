#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    search_item = SearchPage(driver)
    search_item_text = "Стіл RYSLINGE + 4 стільці RYSLINGE"
    print search_item_text
    search_item.click_search_item(search_item_text)
    stilci = StilciRyslingePage(driver)
    a = stilci.check_header()
    print 'header = ' + a
    assert stilci.check_header() == search_item_text
    
"""    
def test_click_search_item():
    driver = set_driver()
    search_item = SearchPage(driver)
    search_item_text = u"Стіл RYSLINGE + 4 стільці RYSLINGE"
    search_item.click_search_item(search_item)
"""

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

class SearchPage(MainPage):    
    def click_search_item(self, text):
        searchElement = self.driver.find_elements_by_class_name("product-name")[0]
        itemName = searchElement.text.encode("utf-8")
        print itemName
        if itemName == text:
            searchElement.click()
        else:
            print 'There is no such item'
            
class StilciRyslingePage(SearchPage):
    def check_header(self):
        xpathResult = self.driver.find_element_by_xpath("//div[@class = 'product-name-sku']/h1")
        result = xpathResult.text.encode("utf-8")
        return result

#if __name__ == "__main__":
#    test_search_in__jysk_ua()
