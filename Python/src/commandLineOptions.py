#!/usr/bin/python
# This demonstrates how to read command line options
from optparse import OptionParser
import time

def init():
    parser = OptionParser()
    parser.add_option("-c", "--config", dest="configFile", help="config file path")
    parser.add_option("-d", "--date", dest="tradeDate" , default=time.strftime("%Y%m%d"), help="TradeDate as YYYYMMDD")
    parser.add_option("-e", "--email", dest="sendEmail", action="store_true", default=False, help="option to send email")
    
    return parser

def main():
    
    parser = init()
    (options, args) = parser.parse_args()
    print "You selected configFile = " + str(options.configFile)
    print "You selected date = " + options.tradeDate
    if (options.sendEmail):
        print "You selected sendEmail = " + str(options.sendEmail)
    

if __name__ == '__main__' :
    main()



    
    