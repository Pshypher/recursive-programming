# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 07:09:39 2019

@author: Pshypher
"""
# Decomposition: f(n) => n, f(n-1)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
    
# Test
print(factorial(0))
print(factorial(1))
print(factorial(5))
print(factorial(9))