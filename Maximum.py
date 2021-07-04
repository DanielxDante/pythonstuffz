def maximum():
    file=open("NUMBERS.txt","r")
    for line in file:
        num=line
        lst=[]
        lst.append(num.split(" "))
        lst=lst[0]
        
        maximum=0
        for e in lst:
            if int(e)>maximum:
                maximum=int(e)
        return maximum
        
print(maximum())
