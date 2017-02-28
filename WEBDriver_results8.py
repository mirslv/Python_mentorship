import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# go to the jysk.ua
driver.get("http://www.jysk.ua")

# find the element that's name attribute is query (the jysk search box)
inputElement = driver.find_element_by_name("query")

# type in the search
inputElement.send_keys("RYSLINGE")

# submit the form
driver.find_element_by_name("op").click()

# XPath + test
xpathResult = driver.find_element_by_xpath("//div[@class = 'view-header']/h1/span")
print 'Count of RYSLINGE = ' + xpathResult.text

def test_matchCount():
    assert int(xpathResult.text) == 8















