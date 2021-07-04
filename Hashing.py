##Linear Probing
hta=[(0,0)]*71

def hashkey(key):
    total=0
    for char in key:
        total+=ord(char)
    return total%71

file=open("SALES.txt","r")
for line in file:
    date,sale=line.split(",")
    index=hashkey(date)

    while hta[index]!=(0,0):
        index+=1
        index=index%71
    hta[index]=(date,sale[:-1])

def saleSearch(hta,date):
    index=hashkey(date)
    while hta[index]!=(0,0):
        if hta[index][0]==date:
            return hta[index][1]
        else:
            index+=1
            index=index%71
    return "No Sale Registered"

def no_Comparisons(hta,date):
    index=hashkey(date)
    comparisons=1
    while hta[index][0]!=date:
        comparisons+=1
        index+=1
        index=index%71
    return comparisons

#Chaining
from Node import*
from LinkedList import*

hta=[0]*23
for i in range(23):
    hta[i]=LinkedList()

def hashkey(key):
    total=0
    for char in key:
        total+=ord(char)
    return total%23

file=open("SALES.txt","r")
for line in file:
    date,sale=line.split(",")
    index=hashkey(date)
    hta[index].addLast((date,sale[:-1]))

def saleSearch(hta,date):
    index=hashkey(date)
    linkedlist=hta[index]

    for node in linkedlist.nodes:
        if node.value[0]==date:
            return node.value[1]
    return "No Sale Registered"

def no_Comparisons(hta,date):
    index=hashkey(date)
    comparisons=1
    linkedlist=hta[index]
    for node in linkedlist.nodes:
        if node.value[0]==date:
            return comparisons
        comparisons+=1
    return comparisons

#Hashing-Pickle
import pickle

def hashfunction(key): 
    index=0
    index=ord(key[0])
    return index%5

def storepair(hashtable,index,key,value):
    lst=[key,value]
    while hashtable[index]!=["None","None"]:
         index+=1
         index=index%5
    hashtable[index]=lst
    return hashtable

def update_pantry():
    #Display menu
    print("                                 MENU                                ")
    print("===========================================")
    print("1. Input type of item and its quantity.")
    print("2. Increase quantity of item.")
    print("3. Decrease quantity of item.")
    print("4. Display all items and their respective quantities.")
    print("5. Create an empty pantry.")
    #User input choice
    choice=input("Please enter a respective number : ")
    #Handle user choice
    if choice=="1":
        item=input("Please enter item name : ")
        quantity=input("Please enter quantity of item : ")
        if int(quantity)<0:
            print("Error in updating quantity of " + str(item) + ". Please re-run program and enter 1 to update pantry.")
        else:
            index=hashfunction(item)
            
            file = open("pantry.p","rb")
            hta = pickle.load(file)
            file.close()
            
            hta1=storepair(hta,index,item,quantity)

            file = open("pantry.p","wb")
            pickle.dump(hta1, file)
            file.close()

            print("Pantry updated")

    if choice=="2":
        item=input("Please enter item name : ")
        quantity=input("Please enter quantity of item you would like to increase to : ")

        file = open("pantry.p","rb")
        hta = pickle.load(file)
        file.close()

        item_list=[]
        for i in range(6):
            item_list.append(hta[i][0])
        if item not in item_list:
            print("Item not found. Re-run program and enter 1 to update pantry.")
            
        for i in range(6):
            if hta[i][0]==item:
                hta[i][1]=quantity
                print("Quantity of " + str(item) + " updated")
            
        file = open("pantry.p","wb")
        pickle.dump(hta, file)
        file.close()
            
    if choice=="3":
        item=input("Please enter item name : ")
        quantity=input("Please enter quantity of item you would like to decrease to : ")
        
        file = open("pantry.p","rb")
        hta = pickle.load(file)
        file.close()

        item_list=[]
        for i in range(6):
            item_list.append(hta[i][0])
        if item not in item_list:
            print("Item not found. Re-run program and enter 1 to update pantry.")

        for i in range(6):
            if hta[i][0]==item:
                if int(hta[i][1])==0:
                    print("Quantity of " +  str(item) + " is 0. Cannot decrease further.")
                else:
                    hta[i][1]=quantity
                    print("Quantity of " + str(item) + " updated")

        file = open("pantry.p","wb")
        pickle.dump(hta, file)
        file.close()
        
    if choice=="4":
        file = open("pantry.p","rb")
        hta = pickle.load(file)
        file.close()

        print("Item Name" + "\t" + "Quantity")
        print("===========================")
        for i in range(6):
            print(str(hta[i][0]) + "\t\t" + str(hta[i][1]))
            
    if choice=="5":
        hta=[["None","None"]]*6
        file = open("pantry.p","wb")
        pickle.dump(hta, file)
        file.close()
        print("Empty pantry created")

    update_pantry()

update_pantry()
test = True



#Hashing-Class

































    
