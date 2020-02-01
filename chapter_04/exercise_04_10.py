# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:53:05 2019

@author: Pshypher
"""

def least_significant_bit(x):
    if x == 0:
        return 0
    elif x == 1 or (x % 10) == 1:
        return 1
    else:
        return least_significant_bit(x // 10) + 1
    
# Test
print(least_significant_bit(0))
print(least_significant_bit(1))
print(least_significant_bit(10))
print(least_significant_bit(0000))
print(least_significant_bit(1100))
print(least_significant_bit(1110100))