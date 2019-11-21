#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 14:24:47 2019

@author: chenwu
"""

import unittest
import random
from fizzbuzz import *

class TestFizzBuzz(unittest.TestCase):
############# 1. test return num ###########
    
#    def test_it_returns_2(self):
#        self.assertEqual(fizzbuzz(2),2)
    
    def test_if_no_rule_apply_returns_num(self):
        num  = random.randint(1, 1000)
        rule = False
        self.assertEqual(fizzbuzz(num,rule),num)
        
#############################

############# 2. test return word ###########
        
#    def test_rule_true_returns_abc(self):
#        num  = random.randint(1, 1000)
#        rule = True
#        self.assertEqual(fizzbuzz(num, 'abc', rule),'abc')
    
#    def test_rule_true_returns_words(self):
#        num  = random.randint(1, 1000)
#        rule = True
#        words = 'abc'
#        self.assertEqual(fizzbuzz(num, words, rule),words)
        
#############################

############# 3. test return fizz ###########
#    
##    def test_it_returns_fizz(self):
##        self.assertEqual(fizzbuzz(3),'fizz')
#        
#    def test_multiple_of_3_fizz(self):
#        num  = random.randint(1, 1000)
#        if num %3 == 0:
#            self.assertEqual(fizzbuzz(num, 0),'fizz')
#        
    def test_multiple_of_3_fizz(self):
        num  = random.randint(1, 1000)
        words = 'fizz'
        rule = lambda num : num%3 ==0
        self.assertEqual(fizzbuzz(num,  words, rule),words)
        
#############################

############# 4. test return buzz ###########

##    
##    def test_it_returns_buzz(self):
##        self.assertEqual(fizzbuzz(5),'buzz')
#
#    def test_multiple_of_5_buzz(self):
#        num  = random.randint(1, 1000)
#        if num %5 == 0:
#            self.assertEqual(fizzbuzz(num, 1),'buzz')
        
    def test_multiple_of_5_fizz(self):
        num  = random.randint(1, 1000)
        words = 'buzz'
        rule = lambda num : num%5 ==0
        self.assertEqual(fizzbuzz(num,  words, rule),words)

#############################

############# 5. test return fizzbuzz ###########
##    
##    def test_it_returns_fizzbuzz(self):
##        self.assertEqual(fizzbuzz(15),'fizzbuzz')
#    
#    def test_multiple_of_3_and_5_fizzbuzz(self):
#        num  = random.randint(1, 1000)
#            
#        if num % 15 == 0:
#            self.assertEqual(fizzbuzz(num, 2),'fizzbuzz')
#        
    def test_multiple_of_3_and_5_fizz(self):
        num  = random.randint(1, 1000)
        words = 'fizzbuzz'
        rule = lambda num : num%3 ==0 and num%5 ==0
        self.assertEqual(fizzbuzz(num,  words, rule),words)
            
##        
        
if __name__ == '__main__':
    unittest.main()