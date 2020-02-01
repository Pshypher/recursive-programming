# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:57:56 2019

@author: Pshypher
"""

def print_digits_vertically(n):
    if n < 10:
        print(n)
    else:
        print_digits_vertically(n // 10)
        print(n % 10)
        
# Test
print_digits_vertically(0)
print()
print_digits_vertically(5)
print()
print_digits_vertically(879)
print()
print_digits_vertically(2743)
        