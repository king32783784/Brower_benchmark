#!/usr/bin/env python
# *-*coding=utf-8*-*
'''
   Name: Browser test
   Function: Browser performance test, support css4/acid3/v8test/octane/html5test/dromaeotest
   Author:peng.li@i-soft.com.cn
   Time:2017.1.12
'''
import os
import sys
import logging
import re
import sys
from optparse import OptionParser
from browsertest import *

def setloger():
    logger = logging.getLogger('browser-test')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('browser.log')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)
    formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    logger.addHandler(fh)
    logger.addHandler(ch)

def recive_args():
    parser = OptionParser()
    parser.add_option("-t", "--type", dest="browsertype",
                      help="browser type, support firefox and chrome")
    parser.add_option("-i", "--item", dest="testitem",
                      help="test item, support css/acid/v8/octane/\
                            html/dromaeo")
    (options, args) = parser.parse_args()
    test_args = {}
    test_args["type"] = options.browsertype
    test_args["item"] = options.testitem
    return test_args

if __name__ == "__main__":
    setloger()
    args = recive_args()
    for key, value in args.iteritems():
        args[key] = value.split(",")
    dotest(args)
                      

