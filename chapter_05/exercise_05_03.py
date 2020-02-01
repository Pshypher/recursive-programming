# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:31:44 2020

@author: Pshypher
"""

def count(a, b):
    n = len(a)
    if n > 0:
        index = a[0]
        b[index] = b[index] + 1
        return count(a[1:], b)
    
def translate_count(b):
    n = len(b)
    
    if n == 0:
        return []
    else:
        count = b[n - 1]
        aux = [n - 1] * count    
        return translate_count(b[0 : n - 1]) + aux

def count_sort_wrapper(a):
    
    if len(a) == 0:
        return a
    
    k = max(a)            
    b = [0] * (k + 1)  
            
    count(a, b)
    c = translate_count(b)
    
    return c

# Test
print(count_sort_wrapper([]))
print(count_sort_wrapper([0]))
print(count_sort_wrapper([1, 2, 3]))
print(count_sort_wrapper([1, 3, 2]))
print(count_sort_wrapper([2, 1, 3]))
print(count_sort_wrapper([2, 3, 1]))
print(count_sort_wrapper([3, 2, 1]))
print(count_sort_wrapper([3, 1, 2]))
print(count_sort_wrapper([2, 2, 3, 2, 0, 1, 3, 2, 0, 0, 4]))   
        