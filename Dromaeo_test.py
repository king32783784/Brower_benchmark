#coding = utf-8
from selenium import webdriver
import time

def check_xpath(browser='dromaeotest', checkxpath="//*[@id='tests']/li[3]/b/a"):
    '''Check the xpath ready or not'''
    while True:
        try:
            drop=browser.find_element_by_xpath("%s" %checkxpath)
            break
        except:
            pass
            print "not ok"

def check_idon(browser='dromaeotest', checkid="pause"):
    '''Check the ID on or off'''
    while True:
        try:
            drop=browser.find_element_by_id("%s" %checkid)
            break
        except:
            time.sleep(1)

def check_idoff(browser='dromaeotest', checkid='left'):
    while True:
        try:
            drop=browser.find_element_by_id("%s" %checkid)
            time.sleep(1)
        except:
            break


class Dromaeo_test(object):
    '''Dromaeo Test'''
    def __init__(self,name):
        self.name=name
        print "%s Dromaeo test starting" %self.name


    def do_dromaeotest(self,dromaeotest="webdriver.Chrome()",testxpath="//*[@id='tests']/li[3]/b/a"):
        dromaeotest.get("http://dromaeo.com/")
        time.sleep(30)
        check_xpath(browser=dromaeotest,checkxpath=testxpath)
        dromaeotest.find_element_by_xpath("%s" %testxpath).click()
        time.sleep(30)
        check_idon(browser=dromaeotest,checkid="pause")
        dromaeotest.find_element_by_id("pause").click()
        check_idoff(browser=dromaeotest,checkid="left")
        result=dromaeotest.find_element_by_xpath("//*[@id='timebar']/span/strong").text
        print result

# test type
# DOM Core test
Domtest_xpath="//*[@id=\"tests\"]/li[8]/a"

chrome=Dromaeo_test("chrouim")
chrome.do_dromaeotest(dromaeotest=webdriver.Chrome(),testxpath=Domtest_xpath)
