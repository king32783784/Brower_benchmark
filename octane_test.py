#coding=utf-8
'''
  This moudle is used for  goole v8 test of autotest.
'''
import time
from selenium import webdriver

class Octane_test():
    '''Goole v8 test'''
    def __init__(self,name):
        self.name=name
        print '%s Octane test starting' %self.name
    def do_octanetest(self,octanetest=webdriver.Chrome()):
        octanetest.get("http://chrome.2345.com/labs/test/octanebenchmark.htm")
        time.sleep(30)
        octanetest_result=octanetest.find_element_by_id("main-banner").text
        octanetest.quit()       
        print octanetest_result


Chromium_octane=Octane_test('Chromium')
Chromium_octane.do_octanetest() 
Firefox_v8=Octane_test('Firefox')
Firefox_v8.do_octanetest(octanetest=webdriver.Firefox())          
 




       
    
