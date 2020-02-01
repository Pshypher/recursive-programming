# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 04:56:07 2020

@author: Pshypher
"""

def f(x, a):
    return x * x - a

def df(x):
    return 2 * x

def newton_raphson_linear(a, x, n):
    if n <= 1:
        return x
    else:
        z = newton_raphson_linear(a, x, n - 1)
        return z + (-1 * f(z, a)) / df(z)
    
def newton_raphson_tail(a, x, n):
    if n <= 1:
        return x
    else:
        z = x + (-1 * f(x, a)) / df(x)
        return newton_raphson_tail(a, z, n - 1)
        
# Test
print(newton_raphson_linear(2, 1, 0))
print(newton_raphson_linear(2, 1, 1))        
print(newton_raphson_linear(2, 1, 2))
print(newton_raphson_linear(2, 1, 3))
print(newton_raphson_linear(2, 1, 5))
print(newton_raphson_linear(2, 1, 10))

print()

print(newton_raphson_tail(2, 1, 0))
print(newton_raphson_tail(2, 1, 1))        
print(newton_raphson_tail(2, 1, 2))
print(newton_raphson_tail(2, 1, 3))
print(newton_raphson_tail(2, 1, 5))
print(newton_raphson_tail(2, 1, 10)) 