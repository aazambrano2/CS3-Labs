'''
Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Lab 4 - Binary Search Trees

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Tues March 19, 2020

Purpose of the program is to implement functions to the bst_list program provided
by Dr. Fuentes where each has functionality of binary search trees using list implementation
and as well to observe the run times of each function.
'''

# Implementation of binary search trees using lists
import matplotlib.pyplot as plt
import time as t
import math

''' Returns a List representing a node of a BST containing an item, 
    left address to a child list, and a right address to a child list
RUNTIME: O(log(n))'''
def insert(T,newItem): # Insert newItem to BST T
    if T == None:  # T is empty
        T = [newItem,None,None]
    else:
        if newItem< T[0]:
            T[1] = insert(T[1],newItem) # Insert newItem in left subtree
        else:
            T[2] = insert(T[2],newItem) # Insert newItem in right subtree
    return T

'''Returns a count of all the data items of a binary search tree given a list of lists that represents a BST
RUNTIME: O(1)'''
def size(T):
    if T != None:
        #Count the root plus all the nodes of the left and right subtrees
        return 1 + size(T[1]) + size(T[2])
    return 0   

'''Returns the minimum data item of a tree given a list of lists that represents a BST
RUNTIME: O(1)'''
def minimum(T):   
    if T != None:
        if T[1] is None:
            return T[0]
        return minimum(T[1])
    return -math.inf #tree is empty

'''Returns the maximum data item of a tree given a list of lists that represents a BST
RUNTIME: O(1)'''
def maximum(T):
    if T != None:
        if T[2] is None:
            return T[0]
        return maximum(T[2])
    return -math.inf #tree is empty

'''Returns the height of a tree given a list of lists that represent a BST
RUNTIME: O(n)'''
def height(T):
    if T is None:
        return -1
    left = height(T[1])
    right = height(T[2])
    return 1 + max(left,right)

'''Returns a boolean if a data item exists in the tree given a list of lists that represent a BST
RUNTIME: O(1)'''
def inTree(T,i): 
    if T is None:
        return False
    if T[0] == i:
        return True
    elif i < T[0]: #Go to left child
        return inTree(T[1],i)
    else:#Go to right child
        return inTree(T[2],i)
    
'''Prints the contents of a tree by level order
RUNTIME: O(n)'''     
def printByLevel(T):
    if T is None:
        print('No Items in Tree')
    else:    
        Q = []
        Q.append(T)
        while len(Q)>0:
            print(Q[0][0],'',end='')
            T = Q.pop(0)
            
            #left
            if T[1] != None:
                Q.append(T[1])
            #right
            if T[2] != None:
                Q.append(T[2])
        print()       
        
'''Returns a sorted list containig all the data items of a tree in acending order
     given a list of lists that represent a BST
RUNTIME: O(n)'''        
def tree2List(T):
    if T == None:
        return []
    #In order traversal
    return tree2List(T[1]) + [T[0]] + tree2List(T[2])

'''Returns a list of items in a tree that are stored in leaf nodes given a list of lists that represent a BST
RUNTIME: O(n)'''
def leaves(T): 
    if T == None:
        return []
    # Node is a leaf
    if T[1] == None and T[2] == None:
        return [T[0]]
    #check left and right sub trees
    return leaves(T[1]) + leaves(T[2])

'''Returns a list of items in a tree stored at a depth given a list of lists that represent a BST
RUNTIME: O(n)'''
def itemsAtDepthD(T,d): 
   if T is None:
       return []
   if d == 0:
       return [T[0]]       
   return itemsAtDepthD(T[1],d-1) + itemsAtDepthD(T[2],d-1)

'''Returns the depth of an item given a list of lists that representt a BST
RUNTIME: O(1)'''
def depthOfK(T,k): 
    if T==None:
        return -math.inf
    if T[0]==k:
        return 0
    c = T[1] #go to left child
    if T[0] < k: #go to right child
        c = T[2]
    d = depthOfK(c,k)
    if d>=0:
        d+=1
    return d

'''Draws the Binary search tree given a list of lists that represent a BST
RUNTIME: O(n)'''
def draw(T):
    if T != None:
        fig, ax = plt.subplots()
        draw_n(T,ax, 0, 0, 1000, 120)
        ax.axis('off')
        plt.show()
'''auxilary function for draw'''
def draw_n(T, ax, x0, y0, delta_x, delta_y):
    delta_x = max([20,delta_x])
    if T[1] is not None:
        ax.plot([x0-delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw_n(T[1],ax, x0-delta_x, y0-delta_y, delta_x/2, delta_y)
    if T[2] is not None:
        ax.plot([x0+delta_x,x0],[y0-delta_y,y0],linewidth=1,color='k')
        draw_n(T[2],ax, x0+delta_x, y0-delta_y, delta_x/2, delta_y)
    ax.text(x0,y0, str(T[0]), size=14,ha="center", va="center",
        bbox=dict(facecolor='w',boxstyle="circle"))     
       
'''Prints items in order given a list of lists that represent a BST
RUNTIME: O(n)'''
def inOrder(T):
    if T!=None:
        inOrder(T[1])
        print(T[0],end=' ')
        inOrder(T[2])
        
############################TESTING PURPOSES ONLY#######################      
'''Returns a list that contains items in an order that will generate a balanced BST given a list of integers'''
def balanced_list(A):
    b = []
    A.sort()
    if A == []:
        return []
    mid = len(A) // 2
    b.insert(0,A[mid])
    return b + balanced_list(A[:mid]) + balanced_list(A[mid+1:])

if __name__ == "__main__":
    plt.close('all')
    '''Lists for Testing different trees'''
    A = [11, 6, 7, 16, 17, 2, 4, 18, 14, 8, 15, 1, 20, 13]   
    B = [2,0]
    C = [2,0,5,6]
    D = [2,0,5,4,6,7]
    E = [2,0,1,5,4,6,7,3]
    
    T = None #empty #A list
    T2 = None #one Node
    T3 = None
    T4 = None
    T5 = None
    T6 = None

    for a in A:
        T = insert(T,a)   
    start2 = t.time_ns()    
    for b in B:
        T2 = insert(T2,b)
    for c in C:
        T3 = insert(T3,c)
    for d in D:
        T4 = insert(T4,d)        
        
    for e in E:
        T5 = insert(T5,e)
#    
#    inOrder(T)
#    print(T)
#    
    
    '''TESTING DIFFERENT TREES'''
    print(T2)
    print('Testing size')
    print(size(T)) #14
    print(size(T2)) #2
    print(size(T3)) #4
    print(size(T4)) #6
    print(size(T5)) #8
    print(size(T6)) #0  
    print('Testing minimum')
    print(minimum(T)) #1
    print(minimum(T2)) #0
    print(minimum(T3)) #0
    print(minimum(T4)) #0
    print(minimum(T5)) #0
    print(minimum(T6)) #-math.inf    
    print('Testing maximum')
    print(maximum(T)) #20
    print(maximum(T2)) #2
    print(maximum(T3)) #6
    print(maximum(T4)) #7
    print(maximum(T5)) #7
    print(maximum(T6)) #-math.inf   
    print('Testing height')
    print(height(T)) #4
    print(height(T2)) #1
    print(height(T3)) #2
    print(height(T4)) #3
    print(height(T5)) #3
    print(height(T6)) #-1
    
    print('Testing inTree')   
    print(inTree(T,14)) #True
    print(inTree(T,0)) #False
    print(inTree(T2,0))#True
    print(inTree(T6,0))#False
    
    print('Testing printByLevel')    
    printByLevel(T)#11 6 16 2 7 14 17 1 4 8 13 15 18 20 
    printByLevel(T2)#2 0 
    printByLevel(T3)#2 0 5 6 
    printByLevel(T4)#2 0 5 4 6 7
    printByLevel(T5)#2 0 5 1 4 6 3 7 
    printByLevel(T6)#No Items in Tree  
    print('Testing tree2list') 
    print(tree2List(T))#[1, 2, 4, 6, 7, 8, 11, 13, 14, 15, 16, 17, 18, 20]
    print(tree2List(T2))#[0, 2]
    print(tree2List(T3))#[0, 2, 5, 6]
    print(tree2List(T4))#[0, 2, 4, 5, 6, 7]
    print(tree2List(T5))#[0, 1, 2, 3, 4, 5, 6, 7]
    print(tree2List(T6))#[]
    
    print('Testing leaves') 
    print(leaves(T))#[1, 4, 8, 13, 15, 20]
    print(leaves(T2))#[0]
    print(leaves(T3))#[0, 6]
    print(leaves(T4))#[0, 4, 7]
    print(leaves(T5))#[1, 3, 7]
    print(leaves(T6))#[]
    
    print('Testing itemsAtDepthD') 
    print(itemsAtDepthD(T,2))#[2, 7, 14, 17]
    print(itemsAtDepthD(T2,2))#[]
    print(itemsAtDepthD(T3,2))#[6]
    print(itemsAtDepthD(T4,2))#[4, 6]
    print(itemsAtDepthD(T5,2))#[1, 4, 6]
    print(itemsAtDepthD(T6,2))#[]
    
    print('Testing depthOfK')
    print(depthOfK(T,6))  #1
    print(depthOfK(T2,6)) #-math.inf
    print(depthOfK(T3,6)) #2
    print(depthOfK(T4,7)) #3
    print(depthOfK(T5,3)) #3
    print(depthOfK(T6,3)) #-math.inf
    print('Testing draw')
    draw(T)
    draw(T2)
    draw(T3)
    draw(T4)
    draw(T5)
    draw(T6) #draws nothing
    
    
    
      
    
    
    
    
