# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:42:49 2020

@author: Pshypher
"""

def format_polynomial(p, s):
    
    n = len(p)
    
    if n == 1:
        if p[0] > 0:
            s = s + "+ " + str(p[0])
        elif p[0] < 0:
            s = s + "- " + str(abs(p[0]))
        else:
            s = s + str(0)
            
        return s            
                        
    else:
        coefficient = p[n - 1]
        degree = n - 1
        
        if coefficient > 0:
            s = s + "+ " + str(coefficient) + "x^" + str(degree) + " "
        elif coefficient < 0:
            coefficient = abs(coefficient)
            s = s + "- " + str(coefficient) + "x^" + str(degree) + " "
                      
        return format_polynomial(p[0:n - 1], s)

def format_polynomial_wrapper(p):
    out = format_polynomial(p, '')
    return out       
    
# Test
print(format_polynomial_wrapper([0]))
print(format_polynomial_wrapper([-1, 2]))
print(format_polynomial_wrapper([-5, 0, 1]))
print(format_polynomial_wrapper([9, -6, 1]))
print(format_polynomial_wrapper([3, -5, 0, 1]))    