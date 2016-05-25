#coding = utf-8
from selenium import webdriver
import time

class Html_test():
    '''Html5 Test'''
    def __init__(self,name):
        self.name=name
        print "%s Html5 test starting" %self.name

    def do_html5test(self,html5test=webdriver.Chrome()):
        html5test.get("http://html5test.com/")
        time.sleep(60)
        result=html5test.find_element_by_xpath("//*[@id=\"score\"]/div[1]/h2/strong").text
        html5test.quit()
        print result
        
chrome=Html_test("chrouim")
chrome.do_html5test(html5test=webdriver.Chrome())
