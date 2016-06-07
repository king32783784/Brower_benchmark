import time
import logging
from selenium import webdriver
from subprocess import call

module_logger = logging.getLogger('browser-test.runtest')

def check_xpath(testname='dromaetest', checkxpath="//*[@id='tests']/li[3]/b/a"):
    '''check the xpath ready or not'''
    while True:
        try:
            drop = testname.find_element_by_xpath("%s" % checkxpath)
            break
        except:
            module_logger.info("%s is  not ok" % checkxpath)


def check_idon(testname='dromaeotest', checkid='pause'):
    while True:
        try:
            drop = testname.find_element_by_id("%s" % checkid)
            break
        except:
            time.sleep(1)


def check_idoff(testname='dromaeotest', checkid='left'):
    while True:
        try:
            drop = testname.find_element_by_id("%s" % checkid)
            time.sleep(1)
        except:
            break


class Do_type1test(object):
    def __init__(self, testcmds):
        self.logger = logging.getLogger('browser-test.runtest.Do_type1test')
        self.cmds = testcmds
        self.logger.info("%s test startting " % self.cmds['name'])

    def do_test(self, test):
        test.get(self.cmds['url'])
        time.sleep(60)
        while True:
            try:
                drop = test.find_element_by_id(self.cmds['result'])
                break
            except:
                self.logger.info("There are some errors about this test")
                test.quit()
                exit()
        result = test.find_element_by_id(self.cmds['result']).text
        test.quit()
        return result


class Do_type2test(object):
    def __init__(self, testcmds):
        self.logger = logging.getLogger('browser-test.runtest.Do_type2test')
        self.cmds = testcmds
        self.logger.info("%s test startting " % self.cmds['name'])

    def do_test(self, test):
        test.get(self.cmds['url'])
        test.find_element_by_id(self.cmds['click']).click()
        time.sleep(20)
        result = test.find_element_by_id(self.cmds['result']).text
        test.quit()
        return result


class Do_type3test(object):
    def __init__(self, testcmds):
        self.logger = logging.getLogger('browser-test.runtest.Do_type3test')
        self.cmds = testcmds
        self.logger.info("%s test startting " % self.cmds['name'])

    def do_test(self, test):
        test.get(self.cmds['url'])
        time.sleep(60)
        result = test.find_element_by_xpath(self.cmds['result']).text
        test.quit()
        return result


class Do_type4test(object):
    def __init__(self, testcmds):
        self.logger = logging.getLogger('browser-test.runtest.Do_type4test')
        self.cmds = testcmds
        self.logger.info("%s test startting " % self.cmds['name'])

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
        return result
