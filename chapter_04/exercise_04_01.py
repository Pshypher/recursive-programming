# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 18:07:31 2019

@author: Pshypher
"""

def is_even_alt(n):
    if n == 0:
        return True
    else:
        return not(is_even_alt(n - 1))
    
for n in range(10):
    print(n, end=' ')
    print("is even?", is_even_alt(n))
        