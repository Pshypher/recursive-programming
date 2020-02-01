# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:56:52 2019

@author: Pshypher
"""

def cube(x):
    return x ** 3

def sigma(m, n, f):
    if m > n:
        return 0;
    else:
        return sigma(m, n - 1, f) + f(n)
    
# Test
for i in range(0, 4):
    print(sigma(1, i, cube))        