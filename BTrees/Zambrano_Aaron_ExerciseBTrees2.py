'''
Created on Mon Feb 17 4:34:47 2020

Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Exercise 2 - B Trees

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Mon March 9, 2020

Purpose of the program is to implement functions 
'''
import btree
import matplotlib.pyplot as plt

'''while loop version'''
def smallest(T):
    temp = T.root
    #assuming the BTree can be empty (have a single node with no items or children)
    while not temp.is_leaf:
        temp = temp.child[0]
    if temp.data == []:
        return 0
    return temp.data[0]

def largest(T):   
    temp = T.root
    #assuming the BTree can be empty (have a single node with no items or children)
    while not temp.is_leaf:
        temp = temp.child[-1]
    if temp.data == []:
        return 0
    return temp.data[-1]

'''wrapper version'''  
def numItems(T):
    return numItems_n(T.root) #wrapper function

def numItems_n(T):
    num = 0
    temp = T
    #assuming the BTree can be empty (have a single node with no items or children)
    if temp.is_leaf:
        return len(temp.data) 
    
    for i in range(len(temp.child)):
        num += numItems_n(temp.child[i])
#    num += len(temp.data)
    return num + len(temp.data)
        
if __name__ == "__main__":
    nums = [6, 3, 23, 16, 11, 25, 7, 17, 27, 30, 21, 14, 26, 8, 29, 22, 28, 5,
            19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
    plt.close('all')
    T = btree.BTree()
    for num in nums:
        T.insert(num)    
        
    print(smallest(T)) #1
    print(largest(T)) #30
    print(numItems(T)) #30
    
    #'empty' BTree
#    t2 = btree.BTree()
#    t2.root = btree.BTreeNode(data=[])
#    
#    print(smallest(t2)) #0
#    print(largest(t2)) #0
#    print(numItems(t2)) #0
#    
    
    T.draw()

    
    
    

