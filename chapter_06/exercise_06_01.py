# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 05:38:09 2020

@author: Pshypher
"""

def search(a, x):
    n = len(a)
    
    if n == 0:
        return False
    elif n == 1:
        return a[0] == x
    else:
        return (search(a[0:n//2], x) or
                search(a[n//2:], x))
        
# Test
print(search([], 2))
print(search([0], 1))
print(search([2], 2))
print(search([5, 2, 7], 3))
print(search([3, 7, 5], 3))
print(search([2, 3, 7, 2, 11], 2))
print(search([7, 5, 1, 13, 2, 17, 3, 11, 9], 10))
print(search([7, 5, 1, 11, 3, 17, 2, 13], 17))        