'''
Created on Mon Feb 17 4:34:47 2020

Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Exercise 1 - B Trees

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Mon March 9, 2020

Purpose of the program is to implement functions 
'''

import matplotlib.pyplot as plt
import numpy as np 
import btree

if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()
    nums = [6, 3, 23, 16, 11, 25, 7, 17, 27, 30, 21, 14, 26, 8, 29, 22, 28, 5,
            19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
    
    for num in nums:
        T.insert(num)
        print(T.root.data)
        
    T.draw()
    
    print(T.max_items)
    print(T.root.data)
    print(len(T.root.child))
    print(T.root.is_leaf)
    print(len(T.root.child[0].data))
    print(sum(T.root.child[0].child[1].data))
    print(T.root.child[1].child[0].data[0])
    print(T.root.child[0].child[2].is_leaf)
    t = T.find(4)
    print(t.data)
    
    
#    print(T.root.child[0].child[2].data[0])
#    print(T.root.child[0].child[2].data[-1])

    
    #[0] means left
    #[1] means middle
    #[2] means right