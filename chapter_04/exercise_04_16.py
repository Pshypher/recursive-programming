# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:13:27 2019

@author: Pshypher
"""

def insert(a, x):
    if len(a) == 0:
        return [x]
    elif a[0] > x:
        return [x] + a
    else:
        first = a[0]
        rem = a[1:]
        return [first] + insert(rem, x)
    
# Test
print(insert([], 0))
print(insert([5], 5))
print(insert([2, 5, 6], 4))
print(insert([2, 4, 6, 6, 7], 5))        