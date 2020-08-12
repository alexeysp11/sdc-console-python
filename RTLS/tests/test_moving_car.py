"""
Here I am going to test moving car with constant velocity. 

Is median of medians equal to overall median? 
"""

import sys
sys.path.append('../')
import moving_car
import unittest

class TestMovingCarKF(unittest.TestCase): 
    def test_calc(self):
        self.assertEqual(try_catch.calc('6'), 0.06)

if __name__ == '__main__':
    unittest.main()