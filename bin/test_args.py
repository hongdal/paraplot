#!/usr/bin/env python3
# coding=utf-8
#---------------------------------------------------------------
# This script is used to test whether pylib can receive 
# parameters that passed by the user correctly.
#
# By shashibici (shashibici@gmail.com)
#   11/02/2015
#---------------------------------------------------------------

import sys
import os

if __name__ == '__main__':
    argc = len(sys.argv)
    if argc < 3:
        print("Usage: " + sys.argv[0] + " <arg1> <arg2> [arg3] [arg4] ... ")
        exit(1)
    
    for index in range(0,argc):
        print("arg[" + str(index) + "]: " + sys.argv[index])
    
