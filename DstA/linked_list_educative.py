# -*- coding: utf-8 -*-
"""
Created on Tue May 25 21:52:49 2021

@author: manju
"""

class Node:
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    
    def __init__(self,head = None):
        self.head = head
    

    
ll  = LinkedList
ll.head = Node(1)
print(ll.head.data)