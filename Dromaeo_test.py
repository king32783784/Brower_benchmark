#coding = utf-8
from selenium import webdriver
import time

def check_xpath(browser='dromaeotest',checkxpath="//*[@id='tests']/li[3]/b/a"):
    '''Check the xpath ready or not'''
    while True:
        try:
            drop=browser.find_element_by_xpath("%s" %checkxpath)
            break
        except:
            pass
            print "not ok"

def check_id(browser='dromaeotest',checkid="pause"):
    '''Check the ID ready or not'''
    while True:
        try:
            drop=browser.find_element_by_id("%s" %checkid)
            break
        except:
            pass
            print "not ok"

class Dromaeo_test():
    '''Dromaeo Test'''
    def __init__(self,name):
        self.name=name
        print "%s Dromaeo test starting" %self.name


    def do_dromaeotest(self,dromaeotest="webdriver.Chrome()",testxpath="//*[@id='tests']/li[3]/b/a"):
        dromaeotest.get("http://dromaeo.com/")
        time.sleep(30)
        check_xpath(browser=dromaeotest,checkxpath=testxpath)
        dromaeotest.find_element_by_xpath("%s" %testxpath).click()
        time.sleep(60)
        check_id(browser=dromaeotest,checkid="pause")
        print "ok"
        dromaeotest.find_element_by_id("pause").click()
        check_id(browser=dromaeotest,checkid="timebar")
        print "oK"
        result=dromaeotest.find_element_by_xpath("//*[@id='timebar']/span/strong").text
        print result
       # csstest.quit()
       # print csstest_result

SunSpider_JS_xpath="//*[@id='tests']/li[5]/a[1]"
Run_SunSpider_JS_xpath="pause"
Dromaeo_JS_xpath="//*[@id='tests']/li[3]/b/a"
V8_JS_xpath="//*[@id='tests']/li[6]/a[1]"
        
chrome=Dromaeo_test("chrouim")
chrome.do_dromaeotest(dromaeotest=webdriver.Chrome(),testxpath=SunSpider_JS_xpath)
