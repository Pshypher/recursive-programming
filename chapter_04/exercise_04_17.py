# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:38:56 2019

@author: Pshypher
"""

def insert(a, x):
    if len(a) == 0:
        return [x]
    elif a[0] > x:
        return [x] + a
    else:
        return [a[0]] + insert(a[1:], x)
    
def insertion_sort(a):
    if len(a) <= 1:
        return a
    else:
        sorted_list = insertion_sort(a[1:])
        return insert(sorted_list, a[0])
        
# Test
print(insertion_sort([1]))
print(insertion_sort([1, 2, 3]))
print(insertion_sort([1, 3, 2]))
print(insertion_sort([2, 1, 3]))
print(insertion_sort([2, 3, 1]))
print(insertion_sort([3, 2, 1]))
print(insertion_sort([1, 3, 4, 5, 5, 6]))
print(insertion_sort([2, 8, 1, 9, 3, 7, 8]))
print(insertion_sort([1, 3, 4, 5, 5, 6, 2, 8, 1, 9, 3, 7, 8]))        