def make_stack(seq):
    stack = []
    for i in seq:
        stack.append(i)
    return stack
    
def make_empty_stack():
    return make_stack([])
    
def is_empty_stack(stack):
    if stack == []:
        return True
    return False
    
def push_stack(stack, item):
    stack.append(item)
       
def pop_stack(stack):
    if len(stack)==0:
        return None
    stack.pop()
    return stack

############################################
###       Do not modify test code          #              
############################################
##s = make_empty_stack()                   #
##first = pop_stack(s)                     #
##                                         #
##push_stack(s, 1)                         #
##push_stack(s, 2)                         #
##push_stack(s, 3)                         #
##                                         #
##s1 = pop_stack(s)                        #
##
############################################

def top(stack):
    if stack==[]:
        return None
    else:
        return stack[-1]
    
    
def topandpop(stack):
    if stack==[]:
        return None
    else:
        return stack.pop()
    
############################################
###       Do not modify test code          #              
############################################
##s = make_empty_stack()                   #
##first = top(s)                           #
##second = topandpop(s)                    #
##push_stack(s, 1)                         #
##push_stack(s, 2)                         #
##push_stack(s, 3)                         #
##                                         #
##third = top(s)                           #
##fourth = topandpop(s)                    #
############################################

def clear_stack(stack):
    while stack!=[]:
        stack.pop()
    return stack


#Do not delete or modify the following code
s = make_empty_stack()                   #
                                         #
push_stack(s, 1)                         #
push_stack(s, 2)                         #
push_stack(s, 3)                         #

clear_stack(s)
print(s)

class Stack: #FILO
    def __init__(self,size):
        self.size=size
        self.pointer=-1 #-1 as null value
        self.array=[-1]*size
        for i in range(0,size):
            self.array[i]=-1

    def isEmpty(self):
        if self.pointer==-1:
            return True
        return False

    def isFull(self):
        if self.pointer==self.size-1:
            return True
        return False

    def push(self,number):
        if self.pointer<self.size:
            self.array[self.pointer+1]=number
            self.pointer+=1
            return None

    def pop(self):
        if self.isEmpty()==True:
            return None
        else:
            popped=self.array[self.pointer]
            self.array[self.pointer]=-1 #Return back to empty/null
            self.pointer-=1
            return popped

    def peek(self):
        if self.isEmpty()==True:
            return None
        else:
            peeked=self.array[self.pointer]
            return peeked

    def display(self):
        for i in range(0,self.size):
            print(self.array[i])




   
   
   
    
    
