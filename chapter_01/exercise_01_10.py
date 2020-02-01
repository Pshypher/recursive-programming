# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 09:43:07 2019

@author: Pshypher
"""
import math

# Relationship: F(n) => f(n)
def fibonacci_linear(n):
    if n == 1 or n == 2:
        return 1
    else:
        GOLDEN_RATIO = (1 + math.sqrt(5)) / 2
        return math.floor(GOLDEN_RATIO * fibonacci_linear(n - 1) 
                          + 1 / 2)
    
# Relationship: F(n) => f(n,1,1)
def fibonacci_wrapper_tail(n):
    
    def fibonacci_tail(n, a, b):
        if n == 1:
            return b
        else:
            return fibonacci_tail(n - 1, a + b, a)
        
    return fibonacci_tail(n, 1, 1)

# Relationship: F(n) => f(n)
def fibonacci_mult(n):
    if n == 1 or n == 2:
        return 1
    elif not (n % 2):
        return (fibonacci_mult(n//2 + 1) ** 2 - 
                fibonacci_mult(n//2 - 1) ** 2)
    else:
        return (fibonacci_mult((n + 1) // 2) ** 2 +
                fibonacci_mult((n - 1) // 2) ** 2)

# Relationship: F(n) => B(n) + A(n)
def fibonacci_wrapper_mutual(n):
    
    def fibonacci_mutual_a(n):
        if n == 1:
            return 0
        else:
            return (fibonacci_mutual_a(n - 1) +
                    fibonacci_mutual_b(n - 1))
            
    def fibonacci_mutual_b(n):
        if n == 1:
            return 1
        else:
            return fibonacci_mutual_a(n - 1)
        
    return (fibonacci_mutual_b(n) + fibonacci_mutual_a(n))

# Relationship: F(n) = f(n, 0)
def fibonacci_wrapper_nested(n):
    
    def fibonacci_nested(n, s):
        if n == 1 or n == 2:
            return 1 + s;
        else:
            return fibonacci_nested(n - 1, s + 
                                    fibonacci_nested(n - 2, 0))
            
    return fibonacci_nested(n, 0)            
        

# Function calls (n=1)
print(fibonacci_linear(1))
print(fibonacci_wrapper_tail(1))
print(fibonacci_mult(1))
print(fibonacci_wrapper_mutual(1))
print(fibonacci_wrapper_nested(1))
print()

# Function calls (n=2)  
print(fibonacci_linear(2))
print(fibonacci_wrapper_tail(2))
print(fibonacci_mult(2))
print(fibonacci_wrapper_mutual(2))
print(fibonacci_wrapper_nested(2))
print()

# Function calls (n=3)
print(fibonacci_linear(3))
print(fibonacci_wrapper_tail(3))
print(fibonacci_mult(3))
print(fibonacci_wrapper_mutual(3))
print(fibonacci_wrapper_nested(3))
print()

# Function calls (n=4)
print(fibonacci_linear(4))
print(fibonacci_wrapper_tail(4))
print(fibonacci_mult(4))
print(fibonacci_wrapper_mutual(4))
print(fibonacci_wrapper_nested(4))
print()

# Function calls (n=5)
print(fibonacci_linear(5))
print(fibonacci_wrapper_tail(5))
print(fibonacci_mult(5))
print(fibonacci_wrapper_mutual(5))
print(fibonacci_wrapper_nested(5))
print()

# Function calls (n=6)
print(fibonacci_linear(6))
print(fibonacci_wrapper_tail(6))
print(fibonacci_mult(6))
print(fibonacci_wrapper_mutual(6))
print(fibonacci_wrapper_nested(6))
print()

# Function calls (n=7)
print(fibonacci_linear(7))
print(fibonacci_wrapper_tail(7))
print(fibonacci_mult(7))
print(fibonacci_wrapper_mutual(7))
print(fibonacci_wrapper_nested(7))
print()

# Function calls (n=8)
print(fibonacci_linear(8))
print(fibonacci_wrapper_tail(8))
print(fibonacci_mult(8))
print(fibonacci_wrapper_mutual(8))
print(fibonacci_wrapper_nested(8))
print()
            
# Function calls (n=9)
print(fibonacci_linear(9))
print(fibonacci_wrapper_tail(9))
print(fibonacci_mult(9))
print(fibonacci_wrapper_mutual(9))
print(fibonacci_wrapper_nested(9))
print()

# Function calls (n=10)
print(fibonacci_linear(10))
print(fibonacci_wrapper_tail(10))
print(fibonacci_mult(10))
print(fibonacci_wrapper_mutual(10))
print(fibonacci_wrapper_nested(10))