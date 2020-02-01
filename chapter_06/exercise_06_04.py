# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:17:11 2020

@author: Pshypher

Fast polynomial multiplication algorithm based on the divide and conquer 
decomposition analoguous to the one used in Karatsuba's algorithm
"""
def distribute(n, p):
    
    if len(p) == 1:
        return [p[0] * n]
    else:
        return [p[0] * n] + distribute(n, p[1:])
    
def add_polynomial(p, q):
    
    if q == []:
        return p
    elif p == []:
        return q
    else:
        return (add_polynomial(p[0:len(p)-1], q[0:len(q)-1]) +
                [p[len(p)-1] + q[len(q)-1]])
    
def subtract_polynomial(p, q):

    if q == []:
        return p
    else:
        return (subtract_polynomial(p[0:len(p)-1], q[0:len(q)-1]) + 
                [p[len(p)-1] - q[len(q)-1]])
    
def polynomial_multiplication(p, q):
    if p == [] or q == []:
        return []
    elif len(p) == 1:
        return distribute(p[0], q)
    elif len(q) == 1:
        return distribute(q[0], p)
    else:
         m = min(len(p) // 2, len(q) // 2)
         a = p[0:len(p) - m]
         b = p[len(p) - m:]
         c = q[0:len(q) - m]
         d = q[len(q) - m:]
         
         ac = polynomial_multiplication(a, c)
         bd = polynomial_multiplication(b, d)
         i = add_polynomial(a, b)
         j = add_polynomial(c, d)
         r = polynomial_multiplication(i, j)
         s = subtract_polynomial(r, ac)
         t = subtract_polynomial(s, bd) + ([0] * m)
         
         return add_polynomial(
             add_polynomial((ac + ([0] * 2 * m)), t), bd)

# Test
print(polynomial_multiplication([-2, 1], [2, 1]))
print(polynomial_multiplication([3, -5, 0, 1], [-4, 0, 1]))