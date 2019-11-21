# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 09:45:05 2018

@author: Chenhao
"""

import unittest

from calculator import Calculator

############
#3.5 red-green-refactoring
############

class TddInPythonExample1(unittest.TestCase):
     def test_calculator_add_method_returns_correct_result(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)

####
#3.6 different input for testing
######      
class TddInPythonExample2(unittest.TestCase):
    
    def setUp(self):  # for initialise things used for all test method
        self.calc = Calculator()
 
    def test_calculator_add_method_returns_correct_result(self):
        result = self.calc.add(2, 2)
        self.assertEqual(4, result)
 
    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 'three')
        
####
#3.7 recall edge cases
######     
    
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 'two', 3)
 
    def test_calculator_returns_error_message_if_y_arg_not_number(self):
        self.assertRaises(ValueError, self.calc.add, 2, 'three')



if __name__ == '__main__':
    unittest.main()
