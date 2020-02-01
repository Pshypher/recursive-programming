# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:14:29 2019

@author: Pshypher
"""

def binary_to_decimal(n):
    if n <= 1:
        return n
    else:
        return (binary_to_decimal(n // 10)
                * 2 + (n % 10))
        
# Test
print(binary_to_decimal(0))
print(binary_to_decimal(1))
print(binary_to_decimal(10))
print(binary_to_decimal(1010))
print(binary_to_decimal(1011))
print(binary_to_decimal(10110))        