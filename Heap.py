#WEEK 3.4
#HEAP HEAP HOORAY
#================
#maintain the properties of a heap data structure
#heap is an binary tree displayed as an array
'''
def helper():
    if leaf!=0: #excluding 0
            if leaf%2==1:
                parent=leaf//2
            else:
                parent=(leaf//2)-1

            child=leaf
    #if element larger than parent do a swap
            while i>heap[parent]:
                heap[child]=heap[parent]#swap
                heap[parent]=i
    #continue to compare element with new parent...
                child=parent#bottom up
                if child%2==1:
                    parent=child//2
                else:
                    parent=(child//2)-1
    #until it is smaller than parent
    #or it becomes the root of heap
                    if parent<0:
                        parent=0
'''        
def buildheap(seq, size): #build tree
    heap = [0] * size #initialise array for heap
    leaf = 0
    parent=0
    child=0
    #store element as leaf
    for i in seq:
        heap[leaf]=i
    #compare element with parent
        if leaf!=0: #excluding 0
            if leaf%2==1:
                parent=leaf//2
            else:
                parent=(leaf//2)-1

            child=leaf
    #if element larger than parent do a swap
            while i>heap[parent]:
                heap[child]=heap[parent]#swap
                heap[parent]=i
    #continue to compare element with new parent...
                child=parent#bottom up
                if child%2==1:
                    parent=child//2
                else:
                    parent=(child//2)-1
    #until it is smaller than parent
    #or it becomes the root of heap
                    if parent<0:
                        parent=0
        leaf+=1
                
    return heap 

def addNode(heap, item):
    leaf=0
    for i in heap:
        if i==0:
            break
        else:
            leaf+=1

    heap[leaf]=item
    
    if leaf!=0: #excluding 0
            if leaf%2==1:
                parent=leaf//2
            else:
                parent=(leaf//2)-1

            child=leaf
    #if element larger than parent do a swap
            while item>heap[parent]:
                heap[child]=heap[parent]#swap
                heap[parent]=item
    #continue to compare element with new parent...
                child=parent#bottom up
                if child%2==1:
                    parent=child//2
                else:
                    parent=(child//2)-1
    #until it is smaller than parent
    #or it becomes the root of heap
                    if parent<0:
                        parent=0
                
        
    return heap


def deleteHead(heap):
    del heap[0]

    for i in range(1,len(heap)):
        if heap[-i]!=0:
            leaf=heap[-i]
            heap[-i]=0
            break


       
h = buildheap([3,2,10,1,20],7)
print(h) 
print(addNode(h, -2))
print(addNode(h, 50))
