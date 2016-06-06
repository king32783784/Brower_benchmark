import logging
import runtest
from subprocess import call
from selenium import webdriver

# create logger with 'spam_application'
logger = logging.getLogger('browser-test')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('browser.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

css4 = {'name':'css4', 'url':'http://css4-selectors.com/browser-selector-test/',
      'click':'start-browser-selector-test', 'result':'diagram'}
#do_type2test
acid3 = {'name': 'acid3', 'url': 'http://acid3.acidtests.org/', 'result': 'result'}
v8test = {'name': 'v8test', 'url': 'http://chrome.360.cn/test/v8/run.html', 'result': 'status'}
octane = {'name': 'octane', 'url': 'http://chrome.2345.com/labs/test/octanebenchmark.htm', 'result': 'main-banner'}
#do_type3test
html5 = {'name': 'html5', 'url': 'http://html5test.com/', 'result': '//*[@id=\"score\"]/div[1]/h2/strong'}
#do_type4test
dromaeo = {'name': 'dromaeo', 'url': 'http://dromaeo.com/', 'result': '//*[@id=\'timebar\']/span/strong',
         'testxpath': '//*[@id=\"tests\"]/li[8]/a', 'runid': 'pause', 'resultid': 'left'}


def chrome():
    try:
        retcode = call("which chromium-browser", shell=True)
        if retcode > 0:
            pass
        else:
            test = runtest.Do_type2test(css4)
            test.do_test(webdriver.Chrome())
            test = runtest.Do_type1test(acid3)
            test.do_test(webdriver.Chrome())
            test = runtest.Do_type1test(v8test)
            test.do_test(webdriver.Chrome())
            test = runtest.Do_type1test(octane)
            test.do_test(webdriver.Chrome())
            test = runtest.Do_type3test(html5)
            test.do_test(webdriver.Chrome())
            test = runtest.Do_type4test(dromaeo)
            test.do_test(webdriver.Chrome())
    except OSError as e:
        logger.ERROR("Execution failed:%s" % e)


def firefox():
    try:
        retcode = call("which firefox", shell=True)
        if retcode > 0:
            pass
        else:
            test = runtest.Do_type2test(css4)
            test.do_test(webdriver.Firefox())
            test = runtest.Do_type1test(acid3)
            test.do_test(webdriver.Firefox())
            test = runtest.Do_type1test(v8test)
            test.do_test(webdriver.Firefox())
            test = runtest.Do_type1test(octane)
            test.do_test(webdriver.Firefox())
            test = runtest.Do_type3test(html5)
            test.do_test(webdriver.Firefox())
            test = runtest.Do_type4test(dromaeo)
            test.do_test(webdriver.Firefox())
    except OSError as e:
        logger.ERROR("Execution failed:%s" % e)
if __name__ == "__main__":
    chrome()
    firefox()
