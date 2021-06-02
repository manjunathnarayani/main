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
        """
        

        Parameters
        ----------
        nodelist : list, optional
            DESCRIPTION. list as input to create a linkedlist
            
            
        Returns
        -------
        None.

        """
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
    
    
    def add_first(self,node):
        """
        

        Parameters
        ----------
        node : string type
            DESCRIPTION. - add string at the start of the node

        Returns
        -------
        None.

        """
        node.next = self.head
        self.head = node
        
    def add_last(self,node):
        """
        

        Parameters
        ----------
        node : class object
            DESCRIPTION. - Add node at the end of the linked list

        Returns
        -------
        None.

        """
        # if there is no node/ if linked list is empty
        if self.head is None:
            self.head = Node
            return
            
        # this trick will traverse the linkedlist to the end 
        # and will assign the last node to current_node
        # so do nothing in the for loop
        for current_node in self:
            pass
        
        # assin the input node refernece to current node.next
        current_node.next = node
        
            
    def add_in_btween(self,target_data,new_node):
        """
        

        Parameters
        ----------
        target_data : string 
            DESCRIPTION. Add new node after the target data being provided
        new_node : object
            DESCRIPTION. Add new node after the target data being provided

        Raises
        ------
        Exception
            DESCRIPTION.

        Returns
        -------
        None.

        """
        # Raise and error if the the list if empty
        if not self.head:
            raise Exception("The List is empty")
        
        #find the node data equivalent to target data and change the refrences.
        for current_node in self:
            if current_node.data == target_data:
                new_node.next = current_node.next
                current_node.next  = new_node
    
    
    
    
    def __iter__(self):
        """
        
        __iter__ : this is dunder function used to iterate the the linked list.
        This is more pythonic way to iterate.
        Yields
        ------
        node : TYPE
            DESCRIPTION. Yield works as Return, except it doesnt stop the loop

        """
        node = self.head
        
        while node is not None:
            yield node
            node = node.next
            
        
    

    def __repr__(self):
        """
        __repr__ : This dunder function is used to print the class object 
        attribute without using the print function while runnint the code.
        This is a pythonic way to print , more for developer analysis

        Returns
        -------
        TYPE
            DESCRIPTION - returns the list of string.

        """
        node = self.head
        nodes = []

        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')

        return "-> ".join(nodes)  





