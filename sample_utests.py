import unittest
import calc

# Create a class that inherits from unittest.TestCase
class TestCalc(unittest.TestCase):

    # as any method of class, takes self as first arg
    def test_add_success(self):
        self.assertEqual(calc.add(5, 7), 12)
        self.assertEqual(calc.add(-5, -7), -12)
        self.assertEqual(calc.add(5, -7), -2)
        
    def test_add_fail(self):    
        self.assertEqual(TypeError, calc.add(5, "hi"))


    def test_subtr_success(self):
        self.assertEqual(calc.subtr(2, 2), 0)
        self.assertEqual(calc.subtr(12, 2), 10)
        self.assertEqual(calc.subtr(2, 12), -10)


# run tests: python3 -m unittest sample_utests.py
# or: set module to run the unittest main if this code is ran directly
# now tests can be run by running this file
if __name__ == '__main__':
    unittest.main()



