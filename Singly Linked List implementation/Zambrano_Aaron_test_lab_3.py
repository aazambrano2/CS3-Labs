# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 16:42:55 2020

Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Lab 3 - Singly Linked List

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Mon Feb 17, 2020

Purpose of the program is implement functions within the List class to observe the behavior how linked list 
can be modified and how efficient each function are depending the size of the list and how they are sorted.

"""
import Zambrano_Aaron_Lab3 as sll
import numpy as np
import math

if __name__ == "__main__":
    L = sll.List()
    L.draw("L")
    L.extend(list(np.arange(10)))
    L.draw('L extended')
    #testing insert and length
    L.insert(0,23) #inserts at i = 0
    L.insert(7,-99) #inserts at i=7
    L.insert(12,15)  #inserts
    L.insert(-1,2) #print index out of bound
    L.draw('L inserted')
    
    
#    test remove()
    L1 = sll.List()
    L1.draw('created1')
    L1.remove(30)                #value error
    L1.extend(list(np.arange(1))) #empty list
    L1.draw('created2')
    L1.print()
    L1.remove(0) 
    L1.draw('created3')
    L1.print()
    L1.extend(list(np.arange(10))) 
    L1.draw('created4')
    L1.print()
    L1.remove(5)#removes first item that is equal to x
    L1.print()
    L1.remove(898) #value error
    L1.print()
    L1.draw('L1 removed')
    
#    test pop()
    print(L1.pop())  #default
    L1.print()
    L1.draw('created5')
    print(L1.pop(0)) #pops the first item
    L1.print()
    L1.draw('created6')
    print(L1.pop(3)) #pops any item within the list
    L1.print()
    L1.draw('created7')
    print(L1.pop(10)) #does not pop any item if the index is out of bound #-1
    L1.print()
    L1.draw('created8')
    print(L1.pop(5)) #list does not change 
    L1.print()
    
    L1.draw('L1 poped')

    
#    testing clear
#    L.clear()  #testing clear
    
#    test index() :TODO
    print(L1.index(6,0,4)) #3
    print(L1.index(6,0,2)) #print range error -1
    print(L1.index(6,1,4)) #3
    print(L1.index(6,-1,4)) #print start error -1
    print(L1.index(6,0,5)) # print  end error -1
    print(L1.pop(3))
    L1.print()
    print(L1.index(6,0,3)) # value error 
    print(L1.index(6,0,3)) # value error -1
    
    L1.draw('L1 FINAL')
    
    
    #test copy()
    L2 = L.copy() 
    L5 = sll.List()
    L6 = L5.copy()
    L6.draw('L6')
    L2.draw('COPY OF L')
    
    #test count
    L.insert(3,1)
    L.draw('L modified')
    L2.draw('L2 not modified')
    print('Test Count',L.count(1))
    
    #testing sort() :TODO()
    L3 = sll.List()
    L3.extend([4,2,7,5,3,9,53,6,45,7,3])
    L3.sort()
    L3.draw('L sorted')
    
    
    
    #testing reverse()
    L.reverse()
    
    L.draw('L reverse')
    L4 = sll.List()
    L4.extend([1,2])
    L4.reverse()
    L4.draw('L4')

    
    
    