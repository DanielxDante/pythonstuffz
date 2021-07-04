##Pointer points to another node
class Node:
    def __init__(self):
        self.data=" "
        self.previous=None
        self.next=None

class DoublyLinkedList:
    def __init__(self):
        self.start=None
        self.last=None

    def isEmpty(self):
        if self.start==None:
            return True
        return False

    def addNode(self, data):
        node=Node()
        node.data=data
        if self.isEmpty()==True:
            self.start=node
            self.last=node
        else:
            Current=self.start
            while Current!=None:
                Previous=Current
                Current=Current.next
            node.previous=Previous
            Previous.next=node
            self.last=node

    def traverseForward(self):
        if self.isEmpty()==True:
            return "List empty"
        else:
            Current=self.start
            while Current!=None:
                Previous=Current
                print(Previous.data)
                Current=Current.next
            return None

    def traverseBackward(self):
        if self.isEmpty()==True:
            return "List Empty"
        else:
            Current=self.last
            while Current!=None:
                Following=Current
                print(Following.data)
                Current=Current.previous
            return None

    def deleteLastNode(self):
        if self.isEmpty()==True:
            return "List Empty. Request unable to resolve."
        elif self.start.next==None:
            self.start=None
            self.last=None
        else:
            self.last.previous.next=None
            self.last=None
              
#Do not delete or amend the following code
#=========================================
lst = DoublyLinkedList()
##a = lst.isEmpty()
##lst.addNode("liuweiling@jjc.edu.sg")
##lst.addNode("h2computing@gmail.com")
##b = lst.isEmpty()
##c = (lst.start).data
##lst.deleteLastNode()
##d = (lst.Start).Pointer
##e = lst.isEmpty()
##lst.deleteLastNode()
##f = lst.isEmpty()
##g=lst.traverseForward()
##h=lst.traverseBackward()
##print(a)
##print(b)
##print(c)
##print(d)
##print(e)
##print(f)
##print(g)
##print(h)
    
            
