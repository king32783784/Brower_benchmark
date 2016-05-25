#coding=utf-8
'''
  This moudle is used for  goole v8 test of autotest.
'''
import time
from selenium import webdriver

class Goole_V8test():
    '''Goole v8 test'''
    def __init__(self,name):
        self.name=name
        print '%s Goole V8 test starting' %self.name
    def do_v8test(self,v8test=webdriver.Chrome()):
        v8test.get("http://chrome.360.cn/test/v8/run.html")
        time.sleep(30)
        v8test_result=v8test.find_element_by_id("status").text
        v8test.quit()       
        print v8test_result


Chromium_v8=Goole_V8test('Chromium')
Chromium_v8.do_v8test() 
Firefox_v8=Goole_V8test('Firefox')
Firefox_v8.do_v8test(v8test=webdriver.Firefox())          
 




       
    
