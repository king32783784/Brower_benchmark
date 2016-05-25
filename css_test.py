#coding = utf-8
from selenium import webdriver
import time


class Css_test():
    ''' Browser CSS-Selector-Test'''
    def __init__(self,name):
        self.name=name
        print "%s test starting" %self.name

    def do_csstest(self,csstest=webdriver.Chrome()):
        csstest.get("http://css4-selectors.com/browser-selector-test/")
        csstest.find_element_by_id("start-browser-selector-test").click()
        time.sleep(10)
        csstest_result=csstest.find_element_by_id("diagram").text
        csstest.quit()
        print csstest_result

        
chrome=Css_test("chrouim")
chrome.do_csstest()
firefox=Css_test("Firefox")
firefox.do_csstest(csstest=webdriver.Firefox())       
