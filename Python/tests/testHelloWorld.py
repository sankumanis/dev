import unittest
import sys
sys.path.append("../src")
import HelloWorld as code


class TestHelloWorld(unittest.TestCase):
    def setUP(self):
        pass
    
    def tearDown(self):
        pass
    
    def testHelloNameEquals(self):
        self.assertEqual("Hello Amit", code.helloName("Amit"))
        
    def testHelloNameNotEquals(self):
        self.assertNotEqual("Hello Amit", code.helloName("Abhi"))
    
    def testHelloNameDefault(self):
        self.assertEqual("Hello Sanku", code.helloName())
    


suite = unittest.TestLoader().loadTestsFromTestCase(TestHelloWorld)
unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__' :
    unittest.main()
    
