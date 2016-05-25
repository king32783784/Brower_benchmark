#coding = utf-8
from selenium import webdriver
import time


class Acid3_test():
    ''' Browser Acdi3-Test'''
    def __init__(self,name):
        self.name=name
        print "%s test starting" %self.name

    def do_acid3test(self,acid3test=webdriver.Chrome()):
        acid3test.get("http://acid3.acidtests.org/")
        time.sleep(10)
        acid3test_result=acid3test.find_element_by_id("result").text
        acid3test.quit()
        print acid3test_result

        
chrome=Acid3_test("chrouim")
chrome.do_acid3test()
firefox=Acid3_test("Firefox")
firefox.do_acid3test(acid3test=webdriver.Firefox())       
