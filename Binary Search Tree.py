# BINARY SEARCH TREE TEMPLATE
#============================
class TreeNode: 
    def __init__(self, value): 
        self.entry=value
        self.left=None
        self.right=None

    def getNodeValue(self):     #optional
        return self.entry

    def getLeftValue(self):     #optional
        return self.left

    def getRightValue(self):    #optional
        return self.right

class BST:
    def __init__(self): #creates empty tree
        self.root = None

    def setRoot(self, value):
        self.root=TreeNode(value)

    def insert(self, value):
        if self.root == None:   #if BST is empty
            self.setRoot(value)
        else:                   #if BST is not empty
            self.insertNode(self.root, value)

    def insertNode(self, currentNode, value): #None output
        if value<=currentNode.entry:
            if currentNode.left==None:
                currentNode.left=TreeNode(value)
            else:
                self.insertNode(currentNode.left, value)

        elif value>currentNode.entry:
            if currentNode.right==None:
                currentNode.right=TreeNode(value)
            else:
                self.insertNode(currentNode.right, value)
        
    def find(self, value):
        return self.findNode(self.root, value)

    def findNode(self, currentNode, value): #boolean output
        if currentNode==None:
            return False
        elif currentNode.entry==value:
            return True
        elif value<currentNode.entry: #compare right branch
            return self.findNode(currentNode.left, value)
        elif value>currentNode.entry: #compare left branch
            return self.findNode(currentNode.right, value)
    
#UNCOMMENT BELOW TO TEST YOUR CODE
#=================================            
bst1 = BST()
bst1.setRoot(10)
bst1.insert(5)
bst1.insert(20)
print(bst1.root.getNodeValue())
print(bst1.find(5))
print(bst1.find(10))
print(bst1.find(15))
###################################################
Node points to another node
global lst
lst=[]

class Node:
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None

    def set_data(self,data):
        self.data=data
        return "Node data set!"

    def get_data(self):
        return self.data

    def set_left(self,node):
        self.left=node
        return "Left node set!"

    def get_left(self):
        return self.left #returns data on left

    def set_right(self,node):
        self.right=node

    def get_right(self):
        return self.right #returns data on right

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def set_root(self,node):
        self.root=node
        return "Root set!"

    def get_root(self):
        return self.root

    def addNode(self,data): #string
        node=Node()
        node.set_data(data)
        if self.root==None:
            self.set_root(node)
        else:
            currentNode=self.root
            if data<=currentNode.data:
                while currentNode.left!=None:
                    temp=currentNode.left
                    currentNode=temp
                    if data>currentNode.data:
                        currentNode.right=node
                        return "Node added!"
                    else:
                        pass
                currentNode.left=node
                return "Node added!"
            elif data>currentNode.data:
                while currentNode.right!=None:
                    temp=currentNode.right
                    currentNode=temp
                    if data<=currentNode.data:
                        currentNode.left=node
                        return "Node added"
                    else:
                        pass
                currentNode.right=node
                return "Node added!"

    def inorder(self, node):
        global lst
        if node.left!=None:
            self.inorder(node.left)
        lst.append(str(node.data))
        if node.right!=None:
            self.inorder(node.right)
    
    def inOrderTraversal(self): #left, center, right
        self.inorder(self.root)
        return lst
        
DO NOT DELETE OR EDIT THE FOLLOWING CODE
========================================
bst = BinarySearchTree()
bst.addNode("mango")
bst.addNode("pineapple")
bst.addNode("banana")
bst.addNode("cucumber")

a = (bst.get_root().data == "mango")
b = (bst.get_root().left.data == "banana")
c = (bst.get_root().right.data == "pineapple")
lst = bst.inOrderTraversal()

############################################
#Parent points to index of child, stored in a list
class Node:
    def __init__(self):
        self.data=""
        self.left=0
        self.right=0

    def set_data(self,data):
        self.data=data

    def get_data(self):
        return self.data

    def set_left(self,index):
        self.left=index

    def get_left(self):
        return self.left

    def set_right(self,index):
        self.right=index

    def get_right(self):
        return self.right

class BinarySearchTree:
    def __init__(self):
        self.root=0
        self.nodes=[Node()]*8
        for i in range(8):
            self.nodes[i]=Node()
        self.nextFree=1

    def set_root(self,index):
        self.root=index

    def get_root(self):
        return self.root

    def addNode(self,data):
        if self.root==0:
            self.root=1
            self.nodes[self.nextFree].set_data(data)
            self.nextFree=2
            print("Node Added!")
        else:
            if self.nextFree>7:
                print("Tree Full!")
            else:
                currentNode=self.nodes[self.root]
                previousNode=None
                while currentNode.get_data()!="":
                    if data>currentNode.get_data():
                        previousNode=currentNode
                        currentNode=self.nodes[currentNode.get_right()]
                    elif data<=currentNode.get_data():
                        previousNode=currentNode
                        currentNode=self.nodes[currentNode.get_left()]
                if data>previousNode.get_data():
                    previousNode.set_right(self.nextFree)
                    self.nodes[self.nextFree].set_data(data)
                    print("Node Added!")
                elif data<=previousNode.get_data():
                    previousNode.set_left(self.nextFree)
                    self.nodes[self.nextFree].set_data(data)
                    print("Node Added!")
                self.nextFree+=1
###########################################################
Pointer points to node
def insertionsort(lst): #in descending order
    for i in range(1,len(lst)):
        for j in range(i):
            if lst[i-j] > lst[i-j-1]:
                lst[i-j],lst[i-j-1] = lst[i-j-1],lst[i-j]
            else:
                break
    return lst

size = 0

file = open("FRUITS.txt","r")
for line in file:
    size += 1

array = [""] * size

file.seek(0)
index  = 0

for line in file:
    array[index] = line.strip()
    index += 1

insertionsort(array)
print(array)

class Node:
    def __init__(self):
        self.data = None #String
        self.left = None #Node object
        self.right = None #Node object

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self,node):
        self.left = node

    def get_left(self):
        return self.left

    def set_right(self, node):
        self.right = node

    def get_right(self):
        return self.right


class BinarySearchTree:    
    def __init__(self):
        self.root = None #Node object

    def set_root(self, node):
        self.root = node

    def get_root(self):
        return self.root


    def addNodeTraverse(self, current, node):
        data = node.get_data()
        
        if current.get_data() > data and current.get_left() == None:
            current.left = node
        elif current.get_data() <= data and current.get_right() == None:
            current.right = node
        else:
            if current.get_data() > data:
                self.addNodeTraverse(current.get_left(), node)
            else:
                self.addNodeTraverse(current.get_right(), node)
            
    def addNode(self, data):
        node = Node()
        node.set_data(data)
        
        if self.get_root() == None: #empty BST
            self.set_root(node)
            return None

        self.addNodeTraverse(self.get_root(), node)

    def inorder(self, root):
        if root.get_left() != None:
            self.inorder(root.get_left())
        print(root.get_data())
        if root.get_right() != None:
            self.inorder(root.get_right())

    def preorder(self, root):
        print(root.get_data())
        if root.get_left() != None:
            self.inorder(root.get_left())
        if root.get_right() != None:
            self.inorder(root.get_right())

    def postorder(self, root):
        if root.get_left() != None:
            self.inorder(root.get_left())
        if root.get_right() != None:
            self.inorder(root.get_right())
        print(root.get_data())
            

bst = BinarySearchTree()
file = open("FRUITS.txt","r")
for line in file:
    line = line.strip()
    bst.addNode(line)
    
print()
print("in-order traversal")
print("==================")
bst.inorder(bst.root)

print()
print("pre-order traversal")
print("===================")
bst.preorder(bst.root)

print()
print("post-order traversal")
print("====================")
bst.postorder(bst.root)

##########################################################
global num_terms
num_terms=1

class Node:
    def __init__(self):
        self.data="" #string
        self.leftPtr=-1 #integer
        self.rightPtr=-1 #integer

    def setData(self,s): #s is string
        self.data=s

    def setLeftPtr(self,x):#x is integer
        self.leftPtr=int(x)

    def setRightPtr(self,y): #y is integer
        self.rightPtr=int(y)

    def getData(self):
        return self.data

    def getLeftPtr(self):
        return self.leftPtr

    def getRightPtr(self):
        return self.rightPtr

class Tree:
    global num_terms

    def __init__(self): #Constructor method
        self.tree=[Node()]*32
        for i in range(32):
            self.tree[i]=Node()
        self.root=-1 #integer

    def add(self,newItem):
        global num_terms
        
        if self.root==-1:
            self.root=0
            self.tree[self.root].setData(newItem)
        else:
            current=self.root
            previous=-1
            while current!=-1:
                if newItem>self.tree[current].getData():
                    previous=current
                    current=self.tree[previous].getRightPtr()
                elif newItem<=self.tree[current].getData():
                    previous=current
                    current=self.tree[previous].getLeftPtr()
            if newItem>=self.tree[previous].getData():
                self.tree[previous].setRightPtr(num_terms)
                self.tree[num_terms].setData(newItem)
                num_terms+=1
            elif newItem<self.tree[previous].getData():
                self.tree[previous].setLeftPtr(num_terms)
                self.tree[num_terms].setData(newItem)
                num_terms+=1

    def print_tree(self):
        print("==================================")
        print("{0:6}{1:10}{2:10}{3:10}".format("Index","Data","LeftPtr","RightPtr"))
        for i in range(11):
            print("{0:6}{1:10}{2:10}{3:10}".format(str(i),str(self.tree[i].getData()),str(self.tree[i].getLeftPtr()),str(self.tree[i].getRightPtr())))

    def postOrderTraversalHelper(self,root): #left right node
        if self.tree[root].getLeftPtr()!=-1:
            self.postOrderTraversal(self.tree[root].getLeftPtr())
        if self.tree[root].getRightPtr()!=-1:
            self.postOrderTraversal(self.tree[root].getRightPtr())
        print(self.tree[root].getData())

    def postOrderTraversal(self):
        if self.root==-1:
            print("Tree is empty!")
        else:
            self.postOrderTraversalHelper(self.root)

    def smallerNodesHelper(self,data,root,count):
        if self.tree[root].getLeftPtr() != -1:
            count = self.smallerNodesHelper(data,self.tree[root].getLeftPtr(),count)
            
        if self.tree[root].getData() < data:
            count += 1
        else:
            return count #stop traversing if node is larger than data
        
        if self.tree[root].getRightPtr() != -1:
            count = self.smallerNodesHelper(data,self.tree[root].getRightPtr(),count)
            
        return count

    def smallerNodes(self,data):
        if self.root==-1:
            print("Tree is empty!")
        else:
            return self.smallerNodesHelper(data,self.root,0)

    def getHeightHelper(self, root):
        left_depth, right_depth = 0, 0
        
        # Compute the depth of each subtree
        if self.tree[root].getLeftPtr() != -1:
            left_depth = self.getHeightHelper(self.tree[root].getLeftPtr())

        if self.tree[root].getRightPtr() != -1:
            right_depth = self.getHeightHelper(self.tree[root].getRightPtr())

        # Use the longer path
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1
        
    def getHeight(self):
        if self.root == -1:
            return 0
        else:
            return self.getHeightHelper(self.root) -1
        
your code here

DO NOT DELETE THE FOLLOWING CODE
================================

t = Tree()

t.add("Cat")
t.add("Ant")
t.add("Dog")
t.add("Bat")

a = t.getHeight() == 2
print(a)
       





































