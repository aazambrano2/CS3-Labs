'''
Course: CS 2302 Data Structures

@author: Aaron Zambrano

Assignment: Exercise 3 - B Trees

Instructor: Dr. Olac Fuentes

T.A: Oscar Galindo

Last Modified on Wed March 11, 2020

Purpose of the program is to implement functions to practice and observe the behaviors of B-Trees
'''
import btree
import matplotlib.pyplot as plt
import math

def largestAtDepthD(T,d):    
    if type(T) == btree.BTree:
        T = T.root
#    #Base Case    
#    if T.data == []:
#        return -math.inf
        
    #Base Case    
    if d == 0 and T.data != []:
            return T.data[-1]
    if not T.is_leaf:
        return largestAtDepthD(T.child[-1],d-1)
    else:
        return -math.inf # depth does not exist in T
    
def findDepth(T,k):
    if type(T) == btree.BTree:
        T = T.root    
    i = 0
    while i < len(T.data) and k > T.data[i]: #iterate keys
        i += 1    
    #Base Case    
    if k in T.data:
        return 0
    #Base Case    
    if T.is_leaf:
        return -1
    else:
        d = findDepth(T.child[i],k) 
        if d == -1:
            return -1
        else:
            return d+1
        
def printAtDepthD(T,d): 
    if type(T) == btree.BTree:
        T = T.root
    #Base Case    
    if d == 0:
        for i in range(len(T.data)): #prints keys at d
            print(T.data[i],'',end='') 
    if not T.is_leaf: 
        for i in range(len(T.child)): #goes to children of T
            printAtDepthD(T.child[i],d-1)
            
def numLeaves(T):
    if type(T) == btree.BTree:
        T = T.root
    count = 0
    #Base Case    
    if T.is_leaf:
        return 1
    for i in range(len(T.child)): #counts all children
        count += numLeaves(T.child[i])
    return count

def fullNodesAtDepthD(T,d):
    if type(T) == btree.BTree:
        T = T.root
    count = 0
    #Base Case    
    if d ==0:
        if T.is_full():
            return 1
    for i in range(len(T.child)): #counts all the nodes that are full
        count += fullNodesAtDepthD(T.child[i],d-1)
    return count
        
def printDescending(T):
    if type(T) == btree.BTree:
        T = T.root
    #Base Case    
    if T.is_leaf:
        rev = T.data[::-1]
        for i in range(len(rev)): #print keys in reverse
            print(rev[i],'',end='')
    else:
        for i in range(len(T.child)-1,0,-1): #go to the last child
            printDescending(T.child[i])
            print(T.data[i-1],'',end='') # children - 1 keys
         #print first child
        printDescending(T.child[0])  
    
def printItemsInNode(T,k): 
    if type(T) == btree.BTree:
        T = T.root    
    i = 0
    while i < len(T.data) and k > T.data[i]: #iterate keys
        i += 1    
    #Base Case    
    if k in T.data:
        for i in range(len(T.data)):
            print(T.data[i],'',end='') #print keys
    if not T.is_leaf:
        printItemsInNode(T.child[i],k)  
        
if __name__ == "__main__":
    plt.close('all')
    
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T2 = btree.BTree()   
    for num in [32,12,58,7,43]:
        T2.insert(num)
        
    T_empty = btree.BTree()
    
    T.draw()
    T2.draw()

    print(largestAtDepthD(T,0)) # 17
    print(largestAtDepthD(T,1)) # 27
    print(largestAtDepthD(T,2)) # 30
    print(largestAtDepthD(T,3)) # -inf
    
    print(largestAtDepthD(T2,0)) # 58
    print(largestAtDepthD(T2,1)) # -inf
    
    print(largestAtDepthD(T_empty,0)) # -inf 
    print(largestAtDepthD(T_empty,1)) # -inf
    
    print(findDepth(T,17)) # 0
    print(findDepth(T,11)) # 1
    print(findDepth(T,18)) # 2
    print(findDepth(T,31)) # -1
    
    print(findDepth(T2,7)) # 0
    print(findDepth(T2,61)) # -1
    print(findDepth(T_empty,0)) # -1
    
    printAtDepthD(T,0) # 17
    print()
    printAtDepthD(T,1) # 6 11 23 27
    print()
    
    #Added test case - Aaron Zambrano
#    printAtDepthD(T_empty,1) # 
#    print()
    
    print(numLeaves(T))         # 6
    print(numLeaves(T2))        # 1
    print(numLeaves(T_empty))   # 1
    
    print(fullNodesAtDepthD(T,0)) # 0
    print(fullNodesAtDepthD(T,1)) # 0
    print(fullNodesAtDepthD(T,2)) # 3
    print(fullNodesAtDepthD(T,3)) # 0
    
    print(fullNodesAtDepthD(T2,0)) # 1
    print(fullNodesAtDepthD(T2,1)) # 0
    
    print(fullNodesAtDepthD(T_empty,0)) # 0
    print(fullNodesAtDepthD(T_empty,1)) # 0
    
    printDescending(T)  # 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 
    print()
    printDescending(T2) # 58 43 32 12 7 
    print()
    
    #Added test case - Aaron Zambrano
#    printDescending(T_empty) # 
#    print()
    
    printItemsInNode(T,3)   # 1 2 3 4 5
    print()
    printItemsInNode(T,32)  #
    print()
    printItemsInNode(T2,43) # 7 12 32 43 58 
    print()
    printItemsInNode(T2,20) #

    
    # Added test case - Aaron Zambrano
#    printItemsInNode(T_empty,32)  #
#    print()