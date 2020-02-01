# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:35:33 2020

@author: Pshypher

Computes the transpose of a matrix A using a divide and conquer decomposition
that breaks up the input matrix A into four block matrices by dividing each
dimension by 2
"""

import numpy as np

def matrix_transpose(A):
    
    p = A.shape[0]
    q = A.shape[1]
    
    if p == 0 or q == 0:
        return A
    elif p == 1:
        return row_to_column(A)
    elif q == 1:
        return column_to_row(A)  
    else:
        A11 = A[:p // 2, :q // 2]
        A12 = A[:p // 2, q // 2:]
        A21 = A[p // 2:, :q // 2]
        A22 = A[p // 2:, q // 2:]
        
        AT = np.vstack((np.hstack((matrix_transpose(A11), 
                                   matrix_transpose(A21))), 
                       np.hstack((matrix_transpose(A12), 
                                  matrix_transpose(A22)))))
        
        return AT
    
def row_to_column(A):
    
    p = A.shape[0]
    q = A.shape[1]
    
    if p == 1 and q == 1:
        return A
    else:
        return np.vstack((A[:, 0:1], 
                          row_to_column(A[:, 1:])))
    
def column_to_row(A):
    
    p = A.shape[0]
    q = A.shape[1]

    if p == 1 and q == 1:
        return A
    else:
        return np.hstack((A[0:1, :], 
                          column_to_row(A[1:, :])))
    
# Test
A = np.matrix([[-2]])
print(matrix_transpose(A))
print()
A = np.matrix([[-2, 4, 5]])
print(matrix_transpose(A))
print()
A = np.matrix([[-2], 
               [4], 
               [5]])
print(matrix_transpose(A))
print()
A = np.matrix([[2, 3, 1, -3], 
               [4, -2, 1, 2]])
print(matrix_transpose(A));
print()
A = np.matrix([[2, 3, 1], 
               [4, -1, -5], 
               [0, -6, 3], 
               [1, -1, 1]])
print(matrix_transpose(A))        