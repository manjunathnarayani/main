# -*- coding: utf-8 -*-
"""
Created on Fri May 14 18:26:50 2021

@author: manju
"""

def anagram(str_1,str_2):
    """
    Check if two strings are anagram
    :param str_1: DESCRIPTION
    :type str_1: TYPE
    :param str_2: DESCRIPTION
    :type str_2: TYPE
    :return: DESCRIPTION
    :rtype: TYPE

    """
    
    str_1 = sorted(str_1)
    str_2 = sorted(str_2)
    
    if ''.join(str_1) == ''.join(str_2):
        return True
    else:
        return False

if __name__ == '__main__':
    str_1 = "restful"
    str_2 = "fluster"
    
    print(anagram(str_1, str_2))
