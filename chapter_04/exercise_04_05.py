# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:05:54 2019

@author: Pshypher
"""

def product_alt(m, n):
    if m == 0 or n == 0:
        return 0
    elif m == 1:
        return n
    elif n == 1:
        return m
    elif m % 2 == 0 and n % 2 == 0:
        return product_alt(m // 2, n // 2) << 2
    elif m % 2 == 1 and n % 2 == 1:
        return ((product_alt((m - 1) // 2, (n - 1) // 2) << 2)
                + m + n - 1)
    elif m % 2 == 1:
        return (product_alt((m - 1) // 2, n // 2) << 2) + n
    else:
        return (product_alt(m // 2, (n - 1) // 2) << 2) + m
    
# Test
for x in range(1, 10):
    for y in range(1, 10):
        print(product_alt(x, y), "=", x * y)
    print()        