# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:03:38 2020

@author: Pshypher
"""

def contains_odd_digit_linear(n):
    if n < 10:
        return n % 2 == 1
    else:
        digit = n % 10
        return contains_odd_digit_linear(n // 10) or digit % 2 == 1
    
def contains_odd_digit_tail(n):
    if n < 10:
        return n % 2 == 1
    elif (n % 10) % 2 == 1:
        return True;
    else:
        return contains_odd_digit_tail(n // 10)
    
# Test
print(contains_odd_digit_linear(0))
print(contains_odd_digit_linear(2))
print(contains_odd_digit_linear(3))
print(contains_odd_digit_linear(64))
print(contains_odd_digit_linear(70))
print(contains_odd_digit_linear(256))
print(contains_odd_digit_linear(1024))
print(contains_odd_digit_linear(2048))
print()

print(contains_odd_digit_tail(0))
print(contains_odd_digit_tail(2))
print(contains_odd_digit_tail(3))
print(contains_odd_digit_tail(64))
print(contains_odd_digit_tail(70))
print(contains_odd_digit_tail(256))
print(contains_odd_digit_tail(1024))
print(contains_odd_digit_tail(2048))