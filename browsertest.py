#coding:utf-8

import time
import logging
import re
from selenium import webdriver
from subprocess import call
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

weblogger = logging.getLogger('browser-test')
TIMEOUT = 10

class TestBrowser(object):

    # 等待指定id的元素出现
    def wait_byid(self, driver, checkid):
        try:
            element = WebDriverWait(driver, TIMEOUT).until(
                  EC.presence_of_element_located((By.ID, checkid))
                  )
            weblogger.info("Wait for %s sucessfull" % checkid)
            return "TRUE"
        except:
            weblogger.warning("Wait for %s failed" % checkid)

    # 模拟鼠标点击元素
    def doclick(self, driver, elem):
        actions = ActionChains(driver)
        actions.move_to_element(elem)
        actions.click(elem)
        actions.perform()

    # 等待指定id的元素可以点击
    def wait_byclickable(self, driver, elem):
        try:
            element = WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable((By.ID, elem)))
            weblogger.info("Wait for %s sucessfull" % elem)
            return "TRUE"
        except:
            weblogger.warning("Wait for %s Faild" % elem)

    # 等待指定xpath的元素可以点击
    def wait_byclickable_xpath(self, driver, xpath):
         try:
             element = WebDriverWait(driver, TIMEOUT).until(
             EC.element_to_be_clickable((By.XPATH, xpath)))
             weblogger.info("Wait for %s sucessfull" % xpath)
             return "TRUE"
         except:
             weblogger.warning("Wait fo %s Faild" % xpath)

    # 等待指定xpath的元素可见
    def wait_byxpath(self, driver, xpath):
        elem = driver.find_element_by_xpath(xpath)
        try:
            element = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of(elem))
            weblogger.info("Wait by %s sucessfull" % xpath)
            return "TRUE"
        except:
            weblogger.warning("Wait by %s failed" % xpath)

    # 等待对应id的指定文本出现
    def wait_bytext(self, driver, elem, text):
        try:
            element = WebDriverWait(driver, TIMEOUT).until(
            EC.text_to_be_present_in_element((By.ID, elem), text))
            weblogger.info("Wait by %s sucessfull" % text)
            return "TRUE"
        except:
            weblogger.warning("Wait by %s faild" % text)

    # 查找结果中的数字部分
    def find_result(self, result):
        findresult = re.compile(r'\d+')
        try:
            data = findresult.findall(result)
            return data
        except:
            return 0
    
    # 关闭浏览器
    def tearDown(self, driver):
        driver.close()

class TestCss(TestBrowser):
    """ css4-test"""
    css4 = {'name': 'css4',
            'url': "http://css4-selectors.com/browser-selector-test/",
            'click': "start-browser-selector-test",
            'result': 'diagram'}
    def __init__(self, browsertype, browsername):
        self.browser = browsertype
        self.browsername  = browsername

    def dotest(self, starttest):
        waittime = 0
        while waittime < 10:
            self.doclick(self.browser, starttest)
            teststatus = self.wait_bytext(self.browser, "diagram","Browser-Support:")
            if teststatus == "TRUE":
                self.result = self.browser.find_element_by_id(self.css4['result']).text
                break
            else:
                self.result = "css test result: error"
                waittime += 1
              
    def run(self):
        self.browser.get(self.css4['url'])
        self.wait_byclickable(self.browser, self.css4['click'])
        try:
            starttest = self.browser.find_element_by_id(self.css4['click'])
            status = "RIGHT"
        except:
            status = "ERROR"
        if status == "ERROR":
            self.result = "css test result: error"
        else:
            try:
                print("hello")
                self.dotest(starttest)
            except:
                self.result = "css test result: error"
        if "error" not in self.result:
            data = self.find_result(self.result)[3]
            weblogger.warning("%s css result: %s" % (self.browsername,data))
        else:
            weblogger.warning("%s css result: 0" % self.browsername)
        self.tearDown(self.browser)
 

class TestAcid(TestBrowser):
    """ acid3 test"""
    acid3 = {'name': 'acid3',
             'url': "http://acid3.acidtests.org/",
             'result': 'score'}

    def __init__(self, webdriver, browsername ):
        self.browser = webdriver
        self.browsername = browsername

    def run(self):
        self.browser.get(self.acid3["url"])
        testtime = 0
        while testtime < 3:
            time.sleep(10)
            try:
                result = self.browser.find_element_by_id(self.acid3['result']).text
            except:
                result = "error"
            if result == 100:
                break
            testtime += 1
        if result.isdigit():
            weblogger.warning("%s acid result: %s" % (self.browsername, result))
        else:
            weblogger.warning("%s acid result: 0" % self.browsername)
        self.tearDown(self.browser)


class TestV8(TestBrowser):
    """ V8test"""
    v8test = {'name': 'v8test',
              'url': "http://chrome.360.cn/test/v8/run.html",
              'result': 'status'}

    def __init__(self, webdriver, browsername):
        self.browser = webdriver
        self.browsername = browsername

    def run(self):
        self.browser.get(self.v8test["url"])
        time = 0
        while time < 6:
            status = self.wait_bytext(self.browser, self.v8test['result'],
                                      u"总成绩")
            if status == "TRUE":
                break
            else:
                time += 1
        try:
            result = self.browser.find_element_by_id(self.v8test['result']).text
        except:
            result = "error"
        result = self.find_result(result)
        if len(result) > 0:
            weblogger.warning("%s v8 result: %s" % 
                              (self.browsername, result[0]))
        else:
            weblogger.warning("%s v8 result: 0" % self.browsername) 
        self.tearDown(self.browser)

    
class TestOctane(TestBrowser):
    """Octane"""
    octane = {'name': 'octane',
              'url': "http://chrome.2345.com/labs/test/octanebenchmark.htm",
              'result': 'main-banner'}
    def __init__(self, webdriver, browsername):
        self.browser = webdriver
        self.browsername = browsername

    def run(self):
        self.browser.get(self.octane['url'])  
        time = 0
        while time < 12:
            status = self.wait_bytext(self.browser, self.octane['result'],
                                      u'您的浏览器得分:')
            if status == "TRUE":
                break
            else:
                time += 1
        try:
            result = self.browser.find_element_by_id(self.octane['result']).text
        except:
            result = "octane test : error"
        result = self.find_result(result)
        if len(result) > 0:
            weblogger.warning("%s octane result: %s" % (self.browsername, result[0]))
        else:
            weblogger.warning("%s octane result: 0" % self.browsername)
        self.tearDown(self.browser)       
        

class TestHtml(TestBrowser):
    """HTML5"""
    html5 = {'name': 'html5',
             'url': 'http://html5test.com/',
             'result': 'score'}
    def __init__(self, webdriver, browsername):
        self.browser = webdriver
        self.browsername = browsername

    def run(self):
        self.browser.get(self.html5['url'])
        time = 0
        while time < 6:
            status = self.wait_bytext(self.browser, self.html5['result'],
                                      'YOUR BROWSER SCORES')
            if status == "TRUE":
                break
            else:
                time += 1
        try:
            result = self.browser.find_element_by_id('score').text
            data = re.findall(r"YOUR BROWSER SCORES (.*?) OUT OF 555 POINTS", result, re.S)
        except:
            data = "html test error"
        if len(data) > 0:
            data = data[0]
            if data.isdigit():
                weblogger.warning("%s html5 result: %s" % (self.browsername, data))
            else:
                weblogger.warning("%s html5 result: 0" % self.browsername)
        else:
            weblogger.warning("%s html5 result: 0" % self.browsername)
        self.tearDown(self.browser)


class TestDromaeo(TestBrowser):
    """dromaeo"""
    dromaeo = {'name':'dromaeo',
               'url': 'http://dromaeo.com/',
               'result':'//*[@id=\'timebar\']/span/strong',
               'testxpath': '//*[@id=\"tests\"]/li[8]/a', 
               'runid': 'pause', 
               'resultid': 'timebar'}
    def __init__(self, webdriver, browsername):
        self.browser = webdriver
        self.browsername = browsername

    def run(self):
        self.browser.get(self.dromaeo['url'])
        waittime = 0
        while waittime < 3:
            status = self.wait_byclickable_xpath(self.browser,
                                                 self.dromaeo['testxpath'])
            if status == "TRUE":
                runpage = self.browser.find_element_by_xpath\
                          (self.dromaeo['testxpath'])    
                self.doclick(self.browser, runpage)
                RUNPAGE="TRUE"
                break
            else:
                waittime += 1
                RUNPAGE="FAIL"
        if RUNPAGE == "FAIL":
            weblogger.warning("%s dromaeo result: 0" % self.browsername)
        else:
            try:
                status = self.wait_byid(self.browser, self.dromaeo['runid'])
                if status == "TRUE":
                    WAITRUN = "TRUE"
                else:
                    WAITRUN = "FAIL"
            except:
                WAITRUN = "FAIL"
            if WAITRUN == "FAIL":
                weblogger.warning("%s dromaeo result: 0" % self.browsername)
            else:
                waittime = 0
                while waittime < 3:
                    texta = self.browser.find_element_by_id(self.dromaeo\
                            ['runid']).get_attribute("value")
                    if texta == "Run":
                        weblogger.info("wait for Run sucessfull")
                        dotest = self.browser.find_element_by_id\
                                 (self.dromaeo['runid'])
                        self.doclick(self.browser, dotest)
                        waittime = 0
                        while waittime < 15:
                            status = self.wait_bytext(self.browser, 
                                     "timebar", "runs/s (Total)")
                            if status == "TRUE":
                                weblogger.info("test finish")
                                result=self.browser.find_element_by_id\
                                       (self.dromaeo["resultid"]).text
                                result = self.find_result(result)[0]
                                weblogger.warning("%s dromaeo result: %s" %
                                                  (self.browsername,result))
                                break
                            else:
                                waittime += 1
                        break
                    else:
                        time.sleep(TIMEOUT)
                        waittime += 1
        self.tearDown(self.browser)

test_item_list = {"css": TestCss, "acid": TestAcid, 
                 "v8" : TestV8, "octane": TestOctane,
                 "html": TestHtml, "dromaeo": TestDromaeo}
def dotest(args):
    weblogger.info(args)
    if "firefox" in args["type"]:
        for testitem in args["item"]:
            runtest = test_item_list[testitem](webdriver.Firefox(), "firefox")
            runtest.run()
    elif "chrome" in args["type"]:
        for testitem in args["item"]:
            runtest = test_item_list[testitem](webdriver.Chrome(), "chrome")
            runtest.run()
