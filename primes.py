# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 11:28:47 2018

@author: Chen
"""
###############
# Section 3.3 errorful code
#####################
def is_prime(number):
    """Return True if *number* is prime."""
    for element in range(number):
        if number % element == 0:
            return False
    return True

def print_next_prime(number):
    """Print the closest prime number larger than *number*."""
    index = number
    while True:
        index += 1
        if is_prime(index):
            print(index)

###############
# Section 3.11 exception corrected
#####################

def is_prime(number):
    """Return True if *number* is prime."""
    if number > 1:
        for element in range(2, number):
            print(number, element)
            if number % element == 0:
                return False

    return True

################
## Section 3.15 continue testing
######################
#
import math

def is_prime(number):
    """
    is_prime returns True or False indicating whether x is prime or not.
    """
    if number > 1:
        for element in range(2, int(math.sqrt(number))):
            if number % element == 0:
                return False
    return True

###############
# Section 5.1 edge cases 0 
#####################
#
def is_prime(number):
    
    if number in (0, 1):
        return False
    
    """Return True if *number* is prime."""
    if number > 1:
        for element in range(2, number):
            print(number, element)
            if number % element == 0:
                return False

    return True
##############
# Section 5.2 edge cases negtive
#####################
#
def is_prime(number):
    
#    if number in (0, 1):
#        return False
#    
    if number <= 1:
        return False
    
    """Return True if *number* is prime."""
    if number > 1:
        for element in range(2, number):
            print(number, element)
            if number % element == 0:
                return False

    return True
