# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:28:06 2018

@author: Chen
"""

###############
# Section 3.6
#####################

import unittest
from primes import is_prime

###############
# Section 3.6 -13 run twince, one error done, one correct 
#####################
#
class PrimesTestCase(unittest.TestCase):
    """Tests for `primes.py`."""

    def test_is_five_prime(self):
        """Is five successfully determined to be prime?"""
        self.assertTrue(is_prime(5))



###############
# Section 3.15
#####################
#
    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertTrue(is_prime(4), msg='four is not prime!')
        
##********************test with input as 4

    def test_is_four_non_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='four is not prime!')
#        
################
## Section 5.1 0
######################     
    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))

###############
# Section 5.2 negtive number
#####################   
    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))
    ###############
# Section 5.3
##################### 
            
    def test_negative_number(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index), msg='{} should not be determined to be prime'.format(index))
            
    

if __name__ == '__main__':
    unittest.main()