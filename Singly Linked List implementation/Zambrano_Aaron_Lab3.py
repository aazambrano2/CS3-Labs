"""
Created on Mon Feb 17 4:34:47 2020

Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Lab 3 - Singly Linked List

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Mon Feb 28, 2020

Purpose of the program is to implement functions within the List class to create and observe the behavior of linked lists
and how they can be modified. Efficiecy of each function depends on the size of the list and the order of the items.

"""

import matplotlib.pyplot as plt
import numpy as np
import math

class ListNode:
    # Constructor. Creates list node
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:
    # Constructor. Creates empty list
    def __init__(self):
        self.head = None
        self.tail = None
        
    '''Prints the contents of a list
    Assumptions: Will print a list of any size n including empty lists'''
    def print(self):
        t = self.head
        print('[',end ='')
        while t is not None:
            print(t.data,end='')
            t = t.next
            if t!= None:
                print(', ',end='')
        print(']')
            
    '''Appends list node given an item
    Assumptions: Item can be any type'''
    def append(self,x):
        if self.head is None: #List is empty
            self.head = ListNode(x)
            self.tail = self.head
        else:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next
            
    '''Extends the linked list given a python list of size n >= 0
    Assumptions: Items in list can be of any type'''
    def extend(self,python_list):
        for d in python_list:
            self.append(d)
            
    '''Inserts an ListNode at a specific index in the list given the position (i) and the item (x) 
    Assumptions: Will insert an item if the position is not out of bound of the list'''
    def insert(self,i,x): 
        if i < 0:
            print('Index out of bound of list')
            return
        #if the list is empty, then the list becomes filled with one element
        if self.head is None: 
            self.head = ListNode(x)
            self.tail = self.head
        # new element in the front of the list
        elif i == 0:
            new_node = ListNode(x)
            new_node.next = self.head
            self.head = new_node
            
        # insert at i in list 
        else:                   
            previous = None 
            current = self.head
            index = 0            
            new_node = ListNode(x)
            while current is not None and index != i:
                previous = current
                current = current.next
                index += 1
            
            #append new node if index is in end of the list 
            if previous.next == None: 
                self.tail = new_node
                
            previous.next = new_node
            new_node.next = current
                
            #update tail
            current = self.head
            prev = None
            while current is not None:
                prev = current
                current = current.next
            self.tail = prev
            return
                
    '''Removes an an item from a ListNode given an item that exist in the list 
    Assumptions: Item in a ListNode will be removed if it exist otherwise it will print an error'''
    def remove(self,x):
        try:
            if self.head == None:
                raise ValueError('Value Error: No such item in List' )
        except ValueError as error:
            print(error)
            return
        
        #if list contains one item and the item is x
        if self.head.data == x and self.head.next == None: 
            self.head = None
            self.tail = None
            return
        
        #rest of list
        temp = self.head
        prev = None
        while temp is not None and temp.data != x: 
            prev = temp
            temp = temp.next
            
        #if item was not found    
        try:
            if temp == None:
                raise ValueError('Value Error: No such item in List' )
        except ValueError as error:
            print(error)
            return
        
        #remove item
        prev.next = temp.next 
        temp.next = None
        
        #update tail
        current = self.head
        prev = None
        while current is not None:
            prev = current
            current = current.next
        self.tail = prev
        
    '''Returns an item from a popped ListNode of a list given the position (i)
    Assumptions: Item will be popped if the position is wihin  the range of the list'''   
    def pop(self,i = math.inf):
        if i < 0:
            print('Index out of bound of list')
            return
        
        #default value
        if i == math.inf:  
            temp = self.head
            prev = None
            while temp.next is not None:
                prev = temp
                temp = temp.next
            item = temp.data
            
            #tail updated
            self.tail = prev 
            prev.next = temp.next
            return item
        #pops head
        if i == 0:  
            item = self.head.data
            self.head = self.head.next
            
            #update tail
            current = self.head
            prev = None
            while current is not None:
                prev = current
                current = current.next
            self.tail = prev
            return item
        
        #pops item in list
        if i > 0:   
            temp = self.head
            prev = None
            while temp is not None and i >0:
                prev = temp
                temp = temp.next
                i -= 1
            
            #if index is out of bound
            if temp == None: 
                return -1
            
            item = temp.data
            prev.next = temp.next
            temp.next = None  
            
            #update tail
            current = self.head
            prev = None
            while current is not None:
                prev = current
                current = current.next
            self.tail = prev
            

            return item
        
    '''Clears all items in the list creating an empty list
    Assumptions: Will work in any sized list'''    
    def clear(self):
        self.head = self.tail = None
        return
    
    '''Returns a zero-based index in the list of the first item found given an item, a start position and
        end position. If no item exists, function will return -1
    Assumptions: Start and end positions must be within range of list otherwise the function will print errors and return -1'''
    def index(self,x,start,end):
        start_node = end_node = self.head 
        index = 0
        
        if start < 0: 
            print('Start Index out of bound of list')
            return -1
        
        if self.head == None:
            print('List is Empty')
            return -1
        
        #finding start
        while start_node is not None and start > 0: 
            start_node = start_node.next
            index += 1
            start -= 1
    
        if start_node == None:
            print('Start Index out of bound of list')
            return -1 
        #finding end
        while end_node is not None and end > 0: 
            end_node = end_node.next
            end -= 1
 
        if end_node == None:
            print('End Index out of bound of list')
            return -1
        
        #finding x between start and end index
        location = start_node
        while location is not None and location is not end_node: 
            if location.data == x:
                break
            location = location.next
            index += 1
        
        try:
            if location == None or location == end_node: #no item found in scope
                raise ValueError('Value Error: No such Item in list')
        except ValueError as error:
            print(error)
            return -1
    
        return index
    
    '''Returns the number of times an item appears in a list given the item of interest
    Assumptions: Will return 0 if no item exist in list'''
    def count(self,x):
        if self.head == None:
            return -math.inf 
        temp = self.head
        count = 0
        while temp is not None:
            if temp.data == x:
                count +=1
            temp = temp.next
        return count
    
    '''Sorts the items in the list in acending order using a bubble sort algorithm
    Assumptions: Only works if list items are intergers'''
    def sort(self): 
        if self.head == None:
            return
        
        temp = self.head
        while temp.next is not None:
            swap = temp.next
            while swap is not None:
                if temp.data > swap.data:
                    temp.data,swap.data = swap.data,temp.data
                swap = swap.next
            temp = temp.next
        return
    '''Reverses the order of the list items
    Assumptions: A list with one item will reverse itself '''
    def reverse(self):
        prev = next_n =  None
        curr = self.head
        self.tail = self.head 
        if curr == None: # list is empty
            return
        while curr is not None: 
            #reverses order
            next_n = curr.next
            curr.next = prev 
            prev = curr 
            curr = next_n
        self.head = prev
        
    '''Returns the address of a list that that is the head of the copy of another list
    Assumptions: If desired list to be copy is none, an empty list will be created'''
    def copy(self):
        new_list = List()
        copy = self.head
        while copy is not None:
            new_list.append(copy.data)
            copy = copy.next
        return new_list
    #################################################################################################   
    def _rectangle(self,x0,y0,dx,dy):
        # Returns the coordinates of the corners of a rectangle
        # with bottom-left corner (x0,y0), dx width and dy height
        x = [x0,x0+dx,x0+dx,x0,x0]
        y = [y0,y0,y0+dy,y0+dy,y0]
        return x,y
    '''Draws a linked list'''
    def draw(self,figure_name=' '):
        # Assumes the list contains no loops
        fig, ax = plt.subplots()
        x, y = self._rectangle(0,0,20,20)
        ax.plot(x,y,linewidth=1,color='k')
        ax.plot([0,20],[10,10],linewidth=1,color='k')
        ax.text(-2,15, 'head', size=10,ha="right", va="center")
        ax.text(-2,5, 'tail', size=10,ha="right", va="center")
        t = self.head
        x0 = 40
        while t !=None:
            x, y = self._rectangle(x0,0,30,20)
            ax.plot(x,y,linewidth=1,color='k')
            ax.plot([x0+15,x0+15],[0,20],linewidth=1,color='k')
            ax.text(x0+7,10, str(t.data), size=10,ha="center", va="center")
            if t.next == None:
                ax.text(x0+22,10, '/', size=15,ha="center", va="center")
            else:
                ax.plot([x0+22,x0+40],[10,10],linewidth=1,color='k')
                ax.plot([x0+37,x0+40,x0+37],[7,10,13],linewidth=1,color='k')
            t = t.next
            x0 = x0+40
        if self.head == None:
            ax.text(12,15, '/', size=10,ha="center", va="center")
        else:
            ax.plot([10,40],[15,15],linewidth=1,color='k')
            ax.plot([37,40,37],[12,15,18],linewidth=1,color='k')

        if self.tail == None:
            ax.text(12,5, '/', size=10,ha="center", va="center")
        else:
            xt = 40
            t = self.head
            while t!= self.tail:
                t = t.next
                xt+=40
            ax.plot([10,10,xt+15,xt+15],[5,-10,-10,0],linewidth=1,color='k')
            ax.plot([xt+12,xt+15,xt+18],[-3,0,-3],linewidth=1,color='k')

        ax.set_title(figure_name)
        ax.set_aspect(1.0)
        ax.axis('off')
        fig.set_size_inches(1.2*(x0+200)/fig.get_dpi(),100/fig.get_dpi())
        plt.show()

    # It won't execute when this file is imported

if __name__ == "__main__":
    plt.close('all')




