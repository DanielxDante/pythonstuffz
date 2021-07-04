def giveChange(amount):
    a=amount//100
    b=(amount%100)//50
    c=((amount%100)%50)//20
    d=(((amount%100)%50)%20)//10
    e=((((amount%100)%50)%20)%10)//5
    if amount%5!=0:
        return("Error")
    return(str(a)+" X $1, "+str(b)+" X 50 cents, " +str(c)+" X 20 cents, " +str(d)+ " X 10 cents, " + str(e)+" X 5 cents")
print(giveChange(1005))

def cc(n,no_deno,i=0):
    deno=[50,20,10,5,1]
    if n==0:
        return 1
    elif n<0:
        return 0
    else:
        ways=0
        for i in range(i,no_deno): #why use i as the temp variable?
            coin=deno[i] 
            if n-coin<coin:
                way=cc(n-coin,no_deno,i+1) #No need to change no_deno because if upper limit of lst exceeds len(lst), no_deno=lst[:]
            else:
                way=cc(n-coin,no_deno,i)
            if way:
                ways+=way
        return ways
    
            
#DO NOT EDIT THE FOLLOWING CODE
#==============================
def count_change(amount):
    if amount == 0:
        return 0
    else:
        return cc(amount,5) #amount, starting number of denominations
print(count_change(100))
