#!/usr/bin/python
import sys

def main():
    argCount = len(sys.argv)
    if argCount < 2 :
        print "Wrong arg"
    else:
        print "Correct"
        print "Hello " + sys.argv[1]
    print helloName()

def helloName(name="Sanku"):
    return "Hello " + name

if __name__ == '__main__':
    main()
    

