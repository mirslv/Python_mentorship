#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pytest
from time import sleep
from behave import *


@given('website "{url}"')
def step(context, url):
    context.browser = webdriver.Chrome()
    context.browser.get("http://www.jysk.ua")
    
@given('website page Stilci')
def step(context):
    context.browser = webdriver.Chrome()
    context.browser.get("https://jysk.ua/vitalnya-stolova/obidniy-nabir/stil-ryslinge-4-stilci-ryslinge")    
    
@then("set text for search '{text}'")
def step(context, text):    
    inputElement = context.browser.find_element_by_name("query")
    inputElement.send_keys(text)   

@then("push search button")
def step(context):
    clickElement = context.browser.find_element_by_name("op")
    clickElement.click()

@then("check count of results = '{text}'")
def check_results(context, text):
    WebDriverWait(context.browser, 20).until(EC.title_contains("JYSK"))
    xpathResult = context.browser.find_element_by_xpath("//div[@class = 'view-header']/h1/span")
    result = xpathResult.text
    assert result == text

@then("click first search item")
def step(context):
    searchElement = context.browser.find_elements_by_class_name("product-name")[0]
    searchElement.click()
        
@then("check if header equals clicked search item '{text}'")
def step(context, text):
    xpathResult = context.browser.find_element_by_xpath("//div[@class = 'product-name-sku']/h1")
    result = xpathResult.text 
    assert result == text

@then("check that description text equals '{text}'")
def step(context, text):
    xpathResult = context.browser.find_element_by_xpath("//div[@class = 'product-specs']/table/tbody/tr/td[@class = 'value']")
    result = xpathResult.text
    assert result == text

@then("check feedback count equals '{text}'")
def step(context, text):
    xpathResult = context.browser.find_element_by_xpath("//div[@class = 'review-count']")
    result = xpathResult.text
    assert result == text

@when("I click Feedback tab")
def step(context):
    element = context.browser.find_element_by_xpath("//div[@class = 'col-xs-12']/ul/li/a[@class = 'tab-rating']")
    context.browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    element.click()   

@then("feedback count should also equal '{text}'")
def step(context, text):  
    xpathResult = context.browser.find_element_by_xpath("//div[@class = 'stars']/div[@class = 'product-score']")
    result = xpathResult.text
    assert text in result  

@then("I want to send feedback")
def step(context):    
    context.browser.find_element_by_link_text("Залишити відгук").click()
    
@then("I set rating")
def step(context):
    sleep(2)
    rating = context.browser.find_element_by_xpath("//div[@class = 'rating']/div/span[@class = 'star-3 none']")
    rating.click()

@then("I set title '{text}'")
def step(context, text):
    titleElement = context.browser.find_element_by_name("title")
    titleElement.send_keys(text)     
    
@then("I set feedback '{text}'")
def step(context, text):  
    inputElement = context.browser.find_element_by_name("body")
    inputElement.send_keys(text) 

@then("I set my name '{text}'")
def step(context, text):
    inputElement = context.browser.find_element_by_name("author")
    inputElement.send_keys(text)  

@then("I set my age '{text}'")
def step(context, text):   
    select = Select(context.browser.find_element_by_name("age"))       
    select.select_by_visible_text(text)

@then("I set my sex '{text}'")
def step(context, text):    
    select = Select(context.browser.find_element_by_name("sex"))       
    select.select_by_visible_text(text)  

@then("I set City '{text}'")
def step(context, text):     
    inputElement = context.browser.find_element_by_name("city")
    inputElement.send_keys(text)

@then("I set my email '{text}'")
def step(context, text):     
    inputElement = context.browser.find_element_by_id("edit-email")
    inputElement.send_keys(text)  

@when("all fields are filled I click button Send Feedback")  
def step(context):  
    context.browser.find_element_by_id("edit-submit--4").click()

@then("I need to check that Feedback window is not closed")
def step(context):     
    element = context.browser.find_elements_by_class_name("modal-content")  
    assert element[0].is_displayed()

@then("required checkbox for agreements is red")
def step(context):     
    element = context.browser.find_element_by_xpath("//*[@id=\"jysk-reviews-add-review-form\"]/div/div/div[9]") 
    assert element.is_displayed()    