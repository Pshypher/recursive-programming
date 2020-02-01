# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:01:38 2019

@author: Pshypher
"""

def insert_num(n, x):
    if (n % 10) <= x:
        return n * 10 + x
    else:
        return (insert_num(n // 10, x) 
                * 10 + (n % 10))
        
# Test
print(insert_num(0, 0))
print(insert_num(0, 2))
print(insert_num(5, 5))
print(insert_num(256, 4))
print(insert_num(24667, 5))        