# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:25:59 2021

@author: manju

Algorithm - Reverse the given number using mod and divide
"""

def rev_int(num):
    """
    
    :param num: DESCRIPTION
    :type num: TYPE
    :return: DESCRIPTION
    :rtype: TYPE

    """
    rev_num = 0
    
    while num>0:
        remainder = num%10
        rev_num = rev_num *10 + remainder
        num = num // 10
    
    return rev_num

if __name__ == '__main__':
    num  = 123450
    print(rev_int(num))

    