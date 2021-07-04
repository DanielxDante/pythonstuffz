##Pointer points to another node
class Node:
    def __init__(self):
        self.Data=""
        self.Pointer=None
    
class LinkedList:
    def __init__(self): #Initialise method
        self.Start=None
    
    def IsEmpty(self):
        if self.Start==None:
            return True
        return False
    
    def AddNode(self, Data):
        node=Node()
        node.Data=Data
        if self.IsEmpty()==True:
            self.Start=node
        else:
            Current=self.Start
            while Current!=None:
                Previous=Current
                Current=Current.Pointer
            Previous.Pointer=node
                
    def DeleteNode(self,Data):
        if self.IsEmpty()==True:
            return None
        else:
            Current=self.Start
            if Current.Data==Data:
                if Current.Pointer==None:
                    self.Start=None
                    return None
                else:
                    self.Start=Current.Pointer
                    return None
            while Current.Pointer!=None:
                nextnode=Current.Pointer
                if nextnode.Data==Data:
                    if nextnode.Pointer==None:
                        Current.Pointer=None
                        return None
                    else:
                        Current.Pointer=nextnode.Pointer
                        return None
    
#Do not delete or amend the following code
#=========================================
lst = LinkedList()
a = lst.IsEmpty()
lst.AddNode("liuweiling@jjc.edu.sg")
lst.AddNode("h2computing@gmail.com")
b = lst.IsEmpty()
c = (lst.Start).Data
lst.DeleteNode("h2computing@gmail.com")
d = (lst.Start).Pointer
lst.DeleteNode("fakenews@yahoo.com")
e = lst.IsEmpty()
lst.DeleteNode("liuweiling@jjc.edu.sg")
f = lst.IsEmpty()
##print(a)
##print(b)
##print(c)
##print(d)
##print(e)
##print(f)

##Pointer points to next index
class Node:
    def __init__(self):
        self.Data=""
        self.Pointer=0
    
class LinkedList:
    def __init__(self): #Initialise method
        self.Start=0
        self.NextFree=1
        self.Nodes=[Node()]*11
        for i in range(1,10):
            self.Nodes[i]=Node()
            self.Nodes[i].Pointer=i+1
        self.Nodes[0].Data=""
    
    def IsEmpty(self):
        for node in self.Nodes[1:]:
            if node.Data!="":
                return False
            return True
    
    def AddNode(self, Data):
        if self.IsEmpty()==True:
            self.Start=self.NextFree #1
            self.Nodes[self.Start].Data=Data
            self.NextFree=self.Nodes[self.Start].Pointer #2
            self.Nodes[self.Start].Pointer=0
        else: #self.Start=1
            Current=self.Start #1
            while Current!=0:
                Previous=Current #1
                Current=self.Nodes[Previous].Pointer #0
            self.Nodes[self.NextFree].Data=Data
            temp=self.Nodes[self.NextFree].Pointer
            self.Nodes[self.NextFree].Pointer=0
            self.Nodes[Previous].Pointer=self.NextFree
            self.NextFree=temp
            
    def DeleteNode(self, Data):
        if self.IsEmpty()==True:
            return None
        else:
            current=self.Start
            if self.Nodes[current].Data==Data:
                if self.Nodes[current].Pointer==0:
                    self.Start=self.NextFree
                    return None
                else:
                    self.Start=self.Nodes[current].Pointer
                    return None
            while self.Nodes[current].Pointer!=0:
                nextnode=self.Nodes[current].Pointer
                if self.Nodes[nextnode].Data==Data:
                    if self.Nodes[nextnode].Pointer==0:
                        self.Nodes[current].Pointer=0
                    else:
                        self.Nodes[current].Pointer=self.Nodes[nextnode].Pointer
                        return None
    
#Do not delete or amend the following code
#=========================================
lst = LinkedList()
a = len(lst.Nodes)
b = lst.Start 
c = lst.IsEmpty()
lst.AddNode("liuweiling@jjc.edu.sg")
lst.AddNode("h2computing@gmail.com")
d = lst.IsEmpty()
e = (lst.Nodes[1]).Data
f = (lst.Nodes[2]).Data
g = (lst.Nodes[1]).Pointer
h = (lst.Nodes[2]).Pointer
lst.DeleteNode("liuweiling@jjc.edu.sg")
i = lst.Start
##print(a)
##print(b)
##print(c)
##print(d)
##print(e)
##print(f)
##print(g)
##print(h)
##print(i)

##Classless linked list
#Initialize Data, Ptr arrays and StartPtr, NextFree pointers.
#Index 0 of Data not used
#Index 0 of Ptr used as Start
# StartPtr, NextFree and Current are indexes of Ptr
size=3001
Data=[""]*size
Ptr=[0]*size
for i in range(1,size):
    Ptr[i]=i+1
StartPtr=0
NextFree=1
def InsertListItem(surname):
    global Data, Ptr, StartPtr, NextFree
    
    Data[NextFree]=surname #Data[1] : First index of Data
    Ptr[NextFree]=0 #Ptr[1]=2=0 : Because there is no next item
    if StartPtr==0: #Empty initially, now after inserting 1 item
        StartPtr=NextFree #StartPtr=1 : New first item
        NextFree+=1 
    else:
        Current=StartPtr 
        while Ptr[Current]!=0: #searching for Ptr=0
            Current=Ptr[Current]
        Ptr[Current]=NextFree #
        NextFree+=1
def DeleteListItem(surname):
    global Data, Ptr, StartPtr, NextFree
    if StartPtr==0:
        return None
    else:
        Current=StartPtr
        if Data[Current]==surname:
            if Ptr[Current]==0:
                StartPtr=0
                return None
            else:
                StartPtr=Ptr[Current]
                return None
        while Current!=0:
            Previous=Current
            Current=Ptr[Current]
            if Data[Current]==surname:
                Ptr[Previous]=Ptr[Current]
    
#Do not delete or amend the following code
#=========================================
d = len(Data)
p = len(Ptr)
s = StartPtr
nf = NextFree
InsertListItem("Liu")
InsertListItem("Wong")
InsertListItem("Sandhu")
s1 = StartPtr
nf1 = NextFree
surname = Data[2]
pointer = Ptr[1]
pointer2 = Ptr[3]
DeleteListItem("Wong")
pointer1 = Ptr[1]
DeleteListItem("Liu")
s2 = StartPtr
DeleteListItem("Sandhu")
s3 = StartPtr
##print(d)
##print(p)
##print(s)
##print(nf)
##print(s1)
##print(nf1)
##print(surname)
##print(pointer)
##print(pointer2)
##print(pointer1)
##print(s2)
##print(s3)
