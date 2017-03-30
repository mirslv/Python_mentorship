#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


def test_search_in_jysk_ua():
    driver = set_driver()
    main_page = MainPage(driver)
    main_page.search_text_element("RYSLINGE")
    main_page.click_go_button()
    assert main_page.check_results() == 8
   
def test_check_header():
    driver = set_driver()
    stilci = StilciRyslingePage(driver)
    stilci.search_text_element("RYSLINGE")
    stilci.click_go_button()    
    search_item_text = "Стіл RYSLINGE + 4 стільці RYSLINGE"
    print search_item_text
    stilci.click_search_item(search_item_text)
    a = stilci.check_header()
    print 'header = ' + a
    assert stilci.check_header() == search_item_text    

def test_check_description():
    driver = set_stilci_page()
    stilci = StilciRyslingePage(driver)
    description = "в комплекті з 2 додатковими \"крилами\""
    b = stilci.check_description()
    print 'description = ' + b
    assert stilci.check_description() == description

def test_check_feedback_count(): 
    driver = set_stilci_page()
    stilci = StilciRyslingePage(driver)    
    feedback_count = "4 відгуків"
    c = stilci.check_feedback_count()
    print 'feedback_count = ' + c
    assert stilci.check_feedback_count() == feedback_count

def test_check_feedback_count_feedback_tab(): 
    driver = set_stilci_page()
    stilci = StilciRyslingePage(driver)   
    sleep(1)    
    stilci.click_feedback_tab()   
    feedback_count = "4 відгуків"
    sleep(1)
    c = stilci.feedback_count_feedback_tab()
    print 'feedback_count = ' + c
    assert feedback_count in stilci.feedback_count_feedback_tab()
    sleep(3)

	
def test_check_text_color(): 
    driver = set_stilci_page()
    stilci = StilciRyslingePage(driver)   
    sleep(1)    
    stilci.click_feedback_tab()   
    sleep(1)
    stilci.click_write_feedback()
    sleep(1)
    stilci.set_rating()
    stilci.set_title("test title")
    stilci.set_feedback("It is test feedback")
    stilci.set_name("Myroslava")
    stilci.set_age("25-34")
    stilci.set_sex("Жінка")
    stilci.set_city("Chernivtsi")
    stilci.set_email("mail@gmail.com")
    sleep(1)	
    stilci.click_send_feedback()
    sleep(1)
    stilci.check_color()
    assert stilci.check_color() == True
    sleep(5)	

def test_check_window_isnot_closed(): 
    driver = set_stilci_page()
    stilci = StilciRyslingePage(driver)   
    sleep(1)    
    stilci.click_feedback_tab()   
    sleep(1)
    stilci.click_write_feedback()
    sleep(1)
    stilci.set_rating()
    stilci.set_title("test title")
    stilci.set_feedback("It is test feedback")
    stilci.set_name("Myroslava")
    stilci.set_age("25-34")
    stilci.set_sex("Жінка")
    stilci.set_city("Chernivtsi")
    stilci.set_email("mail@gmail.com")
    sleep(1)	
    stilci.click_send_feedback()
    sleep(1)
    stilci.check_color()
    assert stilci.feedback_window() == True
    sleep(5)	
    
    

def tearDown(self):
    self.driver.close()

def set_driver():
    driver = webdriver.Chrome()
    driver.get("http://www.jysk.ua")
    return driver
    
def set_stilci_page():   
    driver = webdriver.Chrome()
    driver.get("https://jysk.ua/vitalnya-stolova/obidniy-nabir/stil-ryslinge-4-stilci-ryslinge")
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
        
    def check_description(self):
        xpathResult = self.driver.find_element_by_xpath("//div[@class = 'product-specs']/table/tbody/tr/td[@class = 'value']")
        result = xpathResult.text.encode("utf-8")
        return result

    def check_feedback_count(self):
        xpathResult = self.driver.find_element_by_xpath("//div[@class = 'review-count']")
        result = xpathResult.text.encode("utf-8")
        return result 
    def click_feedback_tab(self):
		element = self.driver.find_element_by_xpath("//div[@class = 'col-xs-12']/ul/li/a[@class = 'tab-rating']")
		self.driver.execute_script("return arguments[0].scrollIntoView(true);", element)
		element.click()
        
    def feedback_count_feedback_tab(self):
        xpathResult = self.driver.find_element_by_xpath("//div[@class = 'stars']/div[@class = 'product-score']")
        result = xpathResult.text.encode("utf-8")
        return result

    def set_rating(self):
        select = self.driver.find_element_by_xpath("//div[@class = 'rating']/div/span[@class = 'star-3 none']")
        select.click()          
        
    def click_write_feedback(self):
        self.driver.find_element_by_link_text("Залишити відгук").click()
        
    def set_title(self, text):
        inputElement = self.driver.find_element_by_name("title")
        inputElement.send_keys(text)
        
    def set_feedback(self, text):
        inputElement = self.driver.find_element_by_name("body")
        inputElement.send_keys(text)        
        
    def set_name(self, text):
        inputElement = self.driver.find_element_by_name("author")
        inputElement.send_keys(text) 

    def set_age(self, text):
        select = Select(self.driver.find_element_by_name("age"))       
        select.select_by_visible_text(text)        
        
    def set_sex(self, text):
        select = Select(self.driver.find_element_by_name("sex"))       
        select.select_by_visible_text(text)    

    def set_city(self, text):
        inputElement = self.driver.find_element_by_name("city")
        inputElement.send_keys(text)   

    def set_email(self, text):
		inputElement = self.driver.find_element_by_id("edit-email")
		inputElement.send_keys(text)
		
    def click_send_feedback(self):
		self.driver.find_element_by_id("edit-submit--4").click()
        
    def feedback_window(self):
        try:
            self.driver.find_elements_by_class_name("modal-content")
        except NoSuchElementException:
            return False
        return True
        
    def check_color(self):
        try:
            self.driver.find_element_by_xpath("//*[@id=\"jysk-reviews-add-review-form\"]/div/div/div[9]")
        except NoSuchElementException:
            return False
        return True

     
        
    
#if __name__ == "__main__":
#    test_search_in__jysk_ua()
