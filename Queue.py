#Simple Qn utilising list Queue
##def make_queue():
##    q=[]
##    return q
##
##def enqueue(q,item):
##    q.append(item)
##    return q
##
##def size(q):
##    return len(q)
##
##def dequeue(q):
##    q.pop(0)
##    return q
##
##def getqueue(q):
##    return q[0]
##
##def patient():
##    print("                       MENU                       ")
##    print("================================")
##    print("1. Create new empty queue")
##    print("2. Add patient to queue")
##    print("3. Remove patient at front of queue")
##    print("4. Check number of patients in queue")
##    print("5. Check patient at front of queue")
##    print(" ")
##
##    choice=input("Please enter a respective number : ")
##
##    if choice=="1":
##        file=open("Patients.txt","w")
##        file.close()
##
##    if choice=="2":
##        name=input("Please enter your name : ")
##        lst=[]
##        file1=open("Patients.txt","r")
##
##        for line in file1:
##            lst.append(line)
##
##        file=open("Patients.txt","w")
##
##        for a in lst:
##            file.write(a+"/n")
##
##        file.write(name+"\n")
##        file.close()
##
##    if choice=="3":
##        file1=open("Patients.txt","r")
##        lst=[]
##
##        for line in file1:
##            lst.append(line)
##
##        file=open("Patients.txt","w")
##
##        for a in lst[1:]:
##            file.write(a)
##        file.close()
##
##    if choice=="4":
##        counter=0
##        file=open("Patients.txt","r")
##
##        for line in file:
##            counter+=1
##        print(counter)
##
##    if choice=="5":
##        file=open("Patients.txt","r")
##        for line in file:
##            print(line)
##            break#exits from loop
##
##    end=input("Press e to return to Menu\n")
##    if end=="e":
##        print("\n")
##        patient()
##    else:
##        print("Program terminated")
##
##patient()
##
###DISPLAY USER MENU AND ALLOW USER TO INPUT CHOICE
###HANDLE USER CHOICE ACCORDINGLY
##test=True
##print(test)
########################################################
#Array Queue with Head and Tail
class Queue:
    def __init__(self,size):
        self.size=size #3
        self.Head=0
        self.Tail=1
        self.QueueArray=[None]*(size+1)
    
    def enqueue(self,item):
        if self.Head==0:
            self.Head=1
            self.QueueArray[self.Tail]=item
            self.Tail+=1
        elif self.Tail<=self.size:#<3
            if self.Tail==self.Head:
                return "Queue Full"
            else:
                self.QueueArray[self.Tail]=item
                self.Tail+=1
        elif self.Tail>self.size:
            self.Tail=1
            counter=self.Tail
            if self.Tail==self.Head:
                print("Queue Full!")
            else:
                self.QueueArray[self.Tail]=item
                self.Tail+=1
            

    def dequeue(self):
        if self.Head==0:
            print("Queue Empty!")
        elif self.Head<=self.size:
            removed=self.QueueArray[self.Head]
            self.QueueArray[self.Head]=None
            print(removed)
            self.Head+=1
            if self.Head==self.Tail:
                self.Head=0
                self.Tail=1
        elif self.Head>self.size:
            self.Head=1
            if self.Head==self.Tail:
                self.Head=0
                self.Tail=1
                return "Queue Empty!"
            else:
                removed=self.QueueArray[self.Head]
                self.QueueArray[self.Head]=None
                print(removed)
                self.Head+=1
                
            

#DO NOT DELETE OR MODIFY THE FOLLOWING CODE
#==========================================
q = Queue(3) 
q.enqueue("Mac")
q.enqueue("Ben")
q.enqueue("Dog") #Tail=1 Head=1
q.dequeue() #Tail=1 Head=2
q.enqueue("Can")#Tail=2 Head=2
a = (q.QueueArray[1] == "Can")
b = (q.Head == 2)
c = (q.Tail == 2)
q.enqueue("Yog") #Tail=2 Head=2
d = ("Yog" in q.QueueArray)
e = ("Can" in q.QueueArray)

p = Queue(3) 
p.enqueue("Mac")
p.enqueue("Ben")
p.enqueue("Dog") 
p.enqueue("Can")
p.enqueue("Mat") #Tail=1 Head=1
p.dequeue()
p.dequeue()
p.dequeue()#Tail=1 Head=0
f = (p.Head == 0)
g = (p.Tail == 1)
p.enqueue("Mat")
h = (p.QueueArray[1]=="Mat")

r = Queue(3) 
r.enqueue("Matt")
r.dequeue()
i = (r.Head == 0)
r.enqueue("Damon")
j = (r.QueueArray[r.Head]=="Damon")



#Linear Queue - memory dequeued will not be reused
class LiQueue:
    def __init__(self):
        self.data=[""]*20
        for i in range(20):
            self.data[i]=""
        self.front=1
        self.rear=0

    def IsEmpty(self):
        for el in self.data[1:]:
            if el!="":
                return True
        return False

    def IsFull(self):
        for el in self.data[1:]:
            if el=="":
                return True
        return False

    def enQueue(self,item):
        if self.IsFull()==True:
            return "Queue is full!"
        else:
            self.rear+=1
            self.data[self.rear]=item
            return "Item added"
            
    def deQueue(self):
        if self.IsEmpty()==True:
            return "Queue is empty!"
        else:
            temp=self.data[self.front]
            self.data[self.front]=""
            self.front+=1
            return temp

    def Peek(self):
        if self.IsEmpty()==True:
            return "Queue is empty!"
        else:
            return self.data[self.front]

    def Size(self):
        if self.IsEmpty()==True:
            return 0
        elif self.IsFull()==True:
            return 19
        else:
            return (self.rear-self.front)+1

    def Display(self):
        print("Front")
        for el in self.data[1:]:
            if el!="":
                print(el)

#Circular Queue - memory dequeued will be reused
class CiQueue:
    def __init__(self):
        self.data=[""]*20
        for i in range(20): #data starts from index 1
            self.data[i]=""
        self.front=1 #removing
        self.rear=1 #adding,never 0

    def IsEmpty(self):
        for el in self.data[1:]:
            if el!="":
                return False 
        return True

    def IsFull(self):
        for el in self.data[1:]:
            if el=="":
                return False
        return True

    def enQueue(self,item):
        if self.IsFull()==True:
            print("Queue is full!")
        else:
            self.data[self.rear]=item
            self.rear=(self.rear%20)+1 #never adding at index 0
            
    def deQueue(self):
        if self.IsEmpty()==True:
            print("Queue is empty!")
        else:
            self.data[self.front]=""
            self.front=(self.front%20)+1
            
    def Peek(self):
        if self.IsEmpty()==True:
            print("Queue is empty!")
        else:
            return self.data[self.front]

    def Size(self):
        if self.IsEmpty()==True:
            print(0)
        elif self.IsFull()==True:
            print(19)
        else:
            count=0
            for el in self.data[1:]:
                if el!="":
                    count+=1
            print(count)

    def Display(self):
        temp=self.front
        for el in self.data[1:temp]:
            if el!="":
                print(el)
        print(self.data[temp] + " Front")
        for el in self.data[temp+1:]:
            if el!="":
                print(el)
    
        

    































