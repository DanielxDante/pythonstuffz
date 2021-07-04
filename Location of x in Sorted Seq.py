def search(x,seq): 
    status=True
    length=len(seq)
    counter=1
    if x<seq[0]: #If x lesser than smallest element in sequence, x will be inserted first. Hence, 0
        return 0
    elif x>seq[length-1]:
        return length
    while status==True:
        for i in range(1,length):
            if x>seq[i]:
                counter+=1
            elif x<seq[i]:
                status=False
                return counter
print(search (42 , (-5, 1, 3, 5, 7, 10 )))

        
            
