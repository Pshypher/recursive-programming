# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:23:23 2019

@author: Pshypher
"""

def num_vowels(s):
    if s == '':
        return 0
    elif (s[0] == 'a' or s[0] == 'e' or
          s[0] == 'i' or s[0] == 'o' or
          s[0] == 'u'):
        return num_vowels(s[1:]) + 1
    else:
        return num_vowels(s[1:])
    
# Test
print(num_vowels(""))
print(num_vowels("by"))
print(num_vowels("io"))
print(num_vowels("dialog"))
print(num_vowels("rhythm"))
print(num_vowels("symphony"))
print(num_vowels("disambuigation"))
print(num_vowels("The quick brown fox jumps over the lazy dog"))