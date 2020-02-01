# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 07:40:06 2019

@author: Pshypher
"""
# Decomposition: s(a, n) => s(a[0:n-1], n-1), a[n-1] 
def sum_list_size_1(a, n):
    if n == 0:
        return 0
    else:
        return (sum_list_size_1(a[0:n - 1], n - 1)
                + a[n - 1])
        
# Decomposition: s(a, n) => s(a[1:n], n-1), a[0]
def sum_list_size_2(a, n):
    if n == 0:
        return 0;
    else:
        return (sum_list_size_2(a[1:n], n - 1) +
                a[0])
        
# Decomposition: s(a) => s(a[0:n//2], n//2), s(a[n//2:n], n//2) if n is even
#                s(a) => s(a[0:n//2], n//2), s(a[n//2:n], (n+1)//2) if n is odd
def sum_list_size_3(a, n):
    if n == 0:
        return 0;
    elif n == 1:
        return a[0];
    else:
        if n % 2:
            return (sum_list_size_3(a[0:n//2], n//2) + 
                    sum_list_size_3(a[n//2:n], (n + 1)//2))
        else:
            return (sum_list_size_3(a[0:n//2], n//2) + 
                    sum_list_size_3(a[n//2:n], n//2))                    
        
        
# Some lists
a = [5, -1, 3, 2, 4, -3]
b = [5, -1, 4, 10, 3, 2, -3]

# Function calls
print(sum_list_size_1(a, 6))
print(sum_list_size_2(a, 6))
print(sum_list_size_3(a, 6))
print(sum_list_size_1(b, 7))
print(sum_list_size_2(b, 7))
print(sum_list_size_3(b, 7))
      