def bubbleSort(array): #Time : O(n^2) Space : O(1)
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
                       
def insertionSort(array): #Time : Worst - O(n^2)  Best - O(n) Space : O(1) 
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0:
            if array[j]>key:
                array[j+1],array[j]=array[j],key
                j-=1
            else:
                break
    return array

def insertionSort(array):
    for i in range(1,len(array)):
        while i>0 and array[i]<array[i-1]:
            array[i],array[i-1]=array[i-1],array[i]
            i-=1
    return array

def quickSort(array):  #Recursive 1
    if len(array) < 2:
            return array
    pivot = array[-1]
    less_than_pivot = []
    greater_than_pivot = []
    for i in range(len(array) - 1): # exclude the pivot
            if array[i][2] > pivot[2]:
                less_than_pivot.append(array[i])
            else:
                greater_than_pivot.append(array[i])
    return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)
print(insertionSort([9,2,4,3,8,1]))

def partition(alist,first,last): 
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last
   done = False
   while done!=True:
       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while leftmark <= rightmark and alist[rightmark] > pivotvalue:
           rightmark = rightmark -1
       if leftmark >= rightmark:
           done = True
       else:
           temp = alist[leftmark] #swap numbers at pointers
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp
   temp = alist[first] #place pivot at position where numbers in left subarray are smaller
   alist[first] = alist[rightmark]
   alist[rightmark] = temp
   return rightmark

def quicksort(alist): #Recursive 2
   quickSortHelper(alist,0,len(alist)-1) #seq, left, right
   return alist
   
def quickSortHelper(alist,first,last):
    if first<last: #left < right; at least two numbers in seq
       splitpoint = partition(alist,first,last)
       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)
