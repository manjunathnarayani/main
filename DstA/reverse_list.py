# -*- coding: utf-8 -*-
"""
Created on Fri May 14 10:52:54 2021

@author: manju

Algorithm to reverse the list - by swaping the numbers.
"""

def reverse_list(nums):
    """
    
    Parameters
    ----------
    nums : list
        num list which is to be reversed

    Returns
    -------
    nums : list
        num list which has been reversed.

    """
    start_index=0
    last_index = len(nums)-1
    
    while last_index >start_index:
        nums[start_index],nums[last_index] = nums[last_index],nums[start_index]
        
        start_index = start_index+1
        last_index = last_index-1
    
    return nums

if __name__ == '__main__':
    
    n= [1,2,3,4,5,6,7,8,9,0]
    reverse_list(n)
    print(n)