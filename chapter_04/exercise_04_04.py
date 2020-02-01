# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 06:15:32 2019

@author: Pshypher
"""

def product(m, n):
    if m == 0 or n == 0:
        return 0
    elif n == 1:
        return m
    elif m == 1:
        return n
    else:
        return (product(m - 1, n - 1) + m + n - 1)
    
    
# Test
for x in range(0, 5):
    for y in range(0, 5):
        print(product(x, y), "=", x * y)
    print()        