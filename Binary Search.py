lst=[1,2,4,9]
length=len(lst)
start=0
end=length
def finditem(lst,num,start,end):
    if start>end:
        return "Not Found"
    else:
        middle=(start+end)//2
        if lst[middle]==num:
            return middle
        elif lst[middle]<num:
            return finditem(lst,num,middle+1,end)
        else:
            return finditem(lst,num,start,middle-1)
print(finditem(lst,1,start,end))
