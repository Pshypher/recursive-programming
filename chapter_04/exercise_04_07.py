# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:15:32 2019

@author: Pshypher
"""

def num_digits(n):
    if n < 10:
        return 1;
    else:
        return num_digits(n // 10) + 1
    
    
# Test
print(num_digits(0))
print(num_digits(1))
print(num_digits(2))
print(num_digits(64))
print(num_digits(192))
print(num_digits(1024))
print(num_digits(65536))