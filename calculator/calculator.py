# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 10:06:52 2018

@author: Chenhao
"""

class Calculator(object):
#####
#3.5 red-green-refactoring
########
    def add(self, x, y):
        return x+y
#        
#####
##3.6 different input for testing
#######  
#        
        number_types = (int,  float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else:
            raise ValueError

#############
#Section 4.1 debugging code while testing - add error
################

    def add(self, x, y):
        
        number_types = (int,  float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            return x - y
        else:
            raise ValueError
            
#############
#Section 4.2 debugging code while testing - add inline debug
################
           
            

    def add(self, x, y):
        
        number_types = (int,  float, complex)
 
        if isinstance(x, number_types) and isinstance(y, number_types):
            
            import pdb; pdb.set_trace() # new debugging technique
            
            result =  x - y
        
            print ('Result is: {}'.format(result))
            
            return result

        else:
            raise ValueError