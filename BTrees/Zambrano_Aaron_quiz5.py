import btree

#def largestAtDepthD(T,d):
#    temp = T.root
#    
#    if temp == None:
#        return -math.inf
#    if d == 0:
#        return temp.data[-1]
#    
#    c = btree.BTree(max_items = len(temp.child[-1].data))
#    c.root = temp.child[-1]
#    return largestAtDepthD(c,d-1) 
def nodeRange(t):
    if t.data ==[]:
        return 0
    return t.data[-1] - t.data[0]

def countNodes(t):
    count = 0
    if t.is_leaf:
        return 1
    for i in range(len(t.child)):
        count += countNodes(t.child[i])
    return count + 1

def countItemsAtDepthD(t,d):
    count = 0
    if d == 0:
        return len(t.data)
    if not t.is_leaf:
        for c in t.child:
            count += countItemsAtDepthD(c,d-1)
    return count 

'''extra btree ascend'''      
#def printAscend(T):
#    return printAscend_wrap(T.root)
#
#def printAscend_wrap(t):
#    if t.is_leaf:
#        for i in t.data:
#            print(i,'',end='')
#    else:
#        for i in range(len(t.child)-1): #keys -1
#            printDescending_wrap(t.child[i])
#            print(t.data[i],'',end='')
#        printDescending_wrap(t.child[-1])    #print last child
#    return
'''exercise btrees 3 find depth vers 1'''    
#def findDepth(T,k):
#    i = 0
#    while i < len(T.data) and k > T.data[i]: #iterate keys
#        i += 1
#    if i == len(T.data) or k < T.data[i]: # k is not in node
#        if T.is_leaf: #k is not in BTree
#            return -1
#        else:
#            d = findDepth(T.child[i],k)
#            if d == -1: #k is not in sub-tree
#                return -1
#            else:
#                return d + 1
#    else: 
#        return 0 #k is in node
if __name__ == "__main__":
    plt.close('all')
    T = btree.BTree()

    nums = [6, 3, 23,16, 11, 25, 7, 17,27, 30, 21, 14, 26, 8, 29, 
            22, 28, 5, 19, 24, 15, 1, 2, 4, 18, 13, 9, 20, 10, 12]
  
    t = T.find(4)
    for num in nums:
        T.insert(num)
        
    T.draw()
    
    print(nodeRange(T.root))  # 0
    t = T.find(4)
    print(nodeRange(t))       # 4
    t = T.find(25)
    print(nodeRange(t))       # 2
    
    print(countNodes(T.root))  # 9
    
    print(countItemsAtDepthD(T.root,0))   # 1
    print(countItemsAtDepthD(T.root,1))   # 4
    print(countItemsAtDepthD(T.root,2))   # 25
    print(countItemsAtDepthD(T.root,3))   # 0
    