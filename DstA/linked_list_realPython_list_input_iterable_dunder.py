# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:50:17 2021

@author: manju
"""

"""
linked list from Real Python
"""

class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    

class LinkedList():

    def __init__(self,nodelist=None):
        self.head  = None
        self.nodelist = nodelist
        
        if nodelist is not None:
            # Get the first element of list-nodelist
            node = Node(data = nodelist.pop(0))
            # and assign it to self.head
            self.head= node
            
            # iterate thorugh remaining elements of list - nodelist
            for elem in nodelist:
                node.next = Node(data=elem)
                node = node.next
    
    def __iter__(self):
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
            
        
    

    def __repr__(self):
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')

        return "-> ".join(nodes)  





