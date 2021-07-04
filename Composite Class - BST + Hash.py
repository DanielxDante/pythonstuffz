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

class HashTable:
    def __init__(self,size):
        self.size=size
        self.HashTableArray=[BinarySearchTree()]*(size)
        for i in range(0,size):
            self.HashTableArray[i]=BinarySearchTree()

    def Hash(self,key):
        total=0
        for digit in key:
            total+=int(digit)
        index=total%self.size
        return index
    
    
#DO NOT DELETE OR EDIT THE FOLLOWING CODE
#========================================
hta = HashTable(5)

a = (hta.Hash("344166") == 4)
b = (hta.Hash("680462") == 1)
c = (hta.Hash("120517") == 1)
d = (hta.Hash("010001") == 2)

hta.HashTableArray[1].addNode("Tan Liang Soon")
hta.HashTableArray[1].addNode("Bruno Mars")
hta.HashTableArray[1].addNode("Shawn Sandhu")
hta.HashTableArray[1].addNode("Joyce Ng")
hta.HashTableArray[1].addNode("Jean Koh")
hta.HashTableArray[1].addNode("Tan Si Jie")
hta.HashTableArray[1].addNode("Haz Awang")
hta.HashTableArray[1].addNode("Liu Weiling")

hta.HashTableArray[2].addNode("Liu Weiling")
hta.HashTableArray[2].addNode("Yasmine Sim")
hta.HashTableArray[2].addNode("Monish Chandra")
hta.HashTableArray[2].addNode("Seah Hon Hui")
hta.HashTableArray[2].addNode("Felicia Lee")

hta.HashTableArray[4].addNode("Sandra Chelvan")
hta.HashTableArray[4].addNode("Lee Juan Juan")
hta.HashTableArray[4].addNode("Amoy Chew")

e = (hta.HashTableArray[1].get_root().get_data() == "Tan Liang Soon")
f = (hta.HashTableArray[2].inOrderTraversal() == ['Felicia Lee', 'Liu Weiling', 'Monish Chandra', 'Seah Hon Hui', 'Yasmine Sim'])
print(test)










