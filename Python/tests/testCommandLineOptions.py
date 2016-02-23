import unittest
import sys
import time
import argparse

sys.path.append("../src")
import commandLineOptions as code


class TestCommandLineOptions(unittest.TestCase):
    def setUP(self):
        pass
        
    def tearDown(self):
        pass
    
    def testCommandLineOptionDateDefault(self):
        self.assertEqual(time.strftime("%Y%m%d"), code.defaultDate())
    


#suite = unittest.TestLoader().loadTestsFromTestCase(TestCommandLineOptions)
#unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__' :
    unittest_args = ["-d", time.strftime("%Y%m%d")]
    args = [sys.argv[0]] + unittest_args 
    unittest.main(argv=args)
    
