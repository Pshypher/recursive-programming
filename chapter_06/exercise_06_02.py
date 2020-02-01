# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 06:25:22 2020

@author: Pshypher
"""

def common_digits(a):
    n = len(a)
    
    if n == 1:
        return digits(a[0])
    else:
        s = common_digits(a[0:n//2])
        t = common_digits(a[n//2:])
        return intersection(s, t)
    
# Test
def digits(v):
    if v < 10:
        return {v}
    else:
        s = digits(v//10)
        s.add(v % 10)
        return s
    
def intersection(s, t):
    n = len(s)
    
    if n == 0:
        return set()
    else:
        d = s.pop()
        c = intersection(s, t)
        if d in t:
            c.add(d)
            
        return c
    
print(common_digits([2]))
print(common_digits([35]))
print(common_digits([13, 29]))
print(common_digits([295, 1801]))
print(common_digits([1996, 1846]))
print(common_digits([7523, 3502]))
print(common_digits([2348, 1349, 7523, 3215]))