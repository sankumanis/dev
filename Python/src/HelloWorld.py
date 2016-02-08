#!/usr/bin/python
import sys

argCount = len(sys.argv)
if argCount < 2 :
    print "Wrong arg"
else:
    print "Correct"
    print "Hello " + sys.argv[1]
    

