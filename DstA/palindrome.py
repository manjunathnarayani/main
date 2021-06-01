# -*- coding: utf-8 -*-
"""
Created on Fri May 14 11:48:39 2021

@author: manju

Find if the string is Palindrome by reversing using swaping letters
"""

def func_palindrome(s):
    """
    Check if the input string is a palindrome
    :param s: DESCRIPTION
    :type s: TYPE
    :return: DESCRIPTION
    :rtype: TYPE

    """
    ori_s = s
    s = list(s)
    
    start_index = 0
    last_index = len(s)-1
    
    while last_index >start_index:
        s[start_index],s[last_index] = s[last_index],s[start_index]
        
        start_index += 1
        last_index -= 1
    
    return ''.join(s) == ori_s


if __name__=='__main__':
    
    s= 'level'
    print(func_palindrome(s))
    
     