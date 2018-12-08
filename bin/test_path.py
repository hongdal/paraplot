#!/usr/bin/env python3
# coding=utf-8
#---------------------------------------------------------------
# This script is used to test whether pylib work appropriately.
# It prints basic informations and current work directory for
# the user. 
#
# By shashibici (shashibici@gmail.com)
#   11/02/2015
#---------------------------------------------------------------

import sys 
import os

print ("+--------------------------------+")
print ("|   Testing for python path ...  |")
print ("+--------------------------------+")
print (sys.version)
print ("<================================>")
print ("Your current work directory: ")
print (os.getcwd())

