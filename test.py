#!/usr/bin/python 
#coding=utf-8
from subprocess import call, PIPE, Popen
import subprocess

test = Popen("python Run.py -i 'css' -t 'chrome'", stdout=PIPE, stderr=PIPE, shell=True)
stdout, stderr = test.communicate()
print stdout,stderr

