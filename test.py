#!/usr/bin/env python
#coding = utf-8
from selenium import webdriver
import time
from subprocess import call

def check_xpath(testname='dromaetest', checkxpath="//*[@id='tests']/li[3]/b/a"):
    '''check the xpath ready or not'''
    while True:
        try:
            drop = testname.find_element_by_xpath("%s" %checkxpath)
            break
        except:
            print "not ok"

def check_idon(testname='dromaeotest', checkid='pause'):
    while True:
        try:
            drop = testname.find_element_by_id("%s" %checkid)
            break
        except:
            time.sleep(1)

def check_idoff(testname='dromaeotest', checkid='left'):
    while True:
        try:
            drop = testname.find_element_by_id("%s" %checkid)
            time.sleep(1)
        except:
            break

class Do_type1test(object):
    def __init__(self, testcmds):
        self.cmds = testcmds
        print ("%s test startting " % self.cmds['name'])

    def do_test(self, test):
        test.get(self.cmds['url'])
        time.sleep(60)
        while True:
            try:
                drop = test.find_element_by_id(self.cmds['result'])
                break
            except:
                print ("There are some errors about this test")
                test.quit()
                exit()
        result = test.find_element_by_id(self.cmds['result']).text
        test.quit()
        print result


class Do_type2test(Do_type1test):
    def do_test(self, test):
        time.sleep(3)
        test.get(self.cmds['url'])
        test.find_element_by_id(self.cmds['click']).click()
        time.sleep(20)
        result = test.find_element_by_id(self.cmds['result']).text
        test.quit()
        print result

class Do_type3test(Do_type1test):
    def do_test(self, test):
        test.get(self.cmds['url'])
        time.sleep(60)
        result=test.find_element_by_xpath(self.cmds['result']).text
        test.quit()
        print result

class Do_type4test(Do_type1test):
    def do_test(self, test):
        test.get(self.cmds['url'])
        time.sleep(30)
        check_xpath(testname=test, checkxpath=self.cmds['testxpath'])
        test.find_element_by_xpath(self.cmds['testxpath']).click()
        time.sleep(30)
        check_idon(testname=test, checkid=self.cmds['runid'])
        test.find_element_by_id(self.cmds['runid']).click()
        check_idoff(testname=test, checkid=self.cmds['resultid'])
        result = test.find_element_by_xpath(self.cmds['result']).text
        test.quit()
        print result

css4={'name':'css4', 'url':'http://css4-selectors.com/browser-selector-test/',
      'click':'start-browser-selector-test', 'result':'diagram'}
#do_type2test
acid3={'name':'acid3', 'url':'http://acid3.acidtests.org/', 'result':'result'}
v8test={'name':'v8test', 'url':'http://chrome.360.cn/test/v8/run.html', 'result':'status'}
octane={'name':'octane', 'url':'http://chrome.2345.com/labs/test/octanebenchmark.htm', 'result':'main-banner'}
#do_type3test
html5={'name':'html5', 'url':'http://html5test.com/', 'result':'//*[@id=\"score\"]/div[1]/h2/strong'}
#do_type4test
dromaeo={'name':'dromaeo', 'url':'http://dromaeo.com/', 'result':'//*[@id=\'timebar\']/span/strong',
         'testxpath':'//*[@id=\"tests\"]/li[8]/a', 'runid':'pause', 'resultid':'left'}

def chrome():    
    try:
        retcode = call("which chromium-browser", shell=True)
        if retcode > 0:
            pass
        else:
            test=Do_type2test(css4)
            test.do_test(webdriver.Chrome())
            test=Do_type1test(acid3)
            test.do_test(webdriver.Chrome())
            test=Do_type1test(v8test)
            test.do_test(webdriver.Chrome())
            test=Do_type1test(octane)
            test.do_test(webdriver.Chrome())
            test=Do_type3test(html5)
            test.do_test(webdriver.Chrome())
            test=Do_type4test(dromaeo)
            test.do_test(webdriver.Chrome())
    except OSError as e:
        print "Execution failed:%s" %e

def firefox():
    try:
        retcode = call("which firefox", shell=True)
        if retcode > 0:
            pass
        else:
            test=Do_type2test(css4)
            test.do_test(webdriver.Firefox())
            test=Do_type1test(acid3)
            test.do_test(webdriver.Firefox())
            test=Do_type1test(v8test)
            test.do_test(webdriver.Firefox())
            test=Do_type1test(octane)
            test.do_test(webdriver.Firefox())
            test=Do_type3test(html5)
            test.do_test(webdriver.Firefox())
            test=Do_type4test(dromaeo)
            test.do_test(webdriver.Firefox())
    except OSError as e:
        print "Execution failed:%s" %e
    
if __name__ ==  "__main__":
 #   chrome()
    firefox()
