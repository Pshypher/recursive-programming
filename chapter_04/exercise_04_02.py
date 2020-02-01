# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 20:18:34 2019

@author: Pshypher
"""

import random

def power(b, n):
    if n == 0:
        return 1
    elif not n % 2:     # n is even
        return power(b, n// 2) ** 2
    elif n < 0:         # n is odd and n < 0
        return (power(b, (n + 1) // 2)
                ** 2 / b)
    else:               # n is odd and n > 0
        return (power(b, (n - 1) // 2)
                ** 2 * b)

# Test      
for x in range(1, 5):
    for y in range(0, 5):
        operators = ("+", "-")
        sym = random.choice(operators)
        y = -y if sym == "-" else y
        print(power(x, y), "=", x ** y)