def EuclidAlgo(x,y):
    if y==0:
        return x
    else:
        return EuclidAlgo(y,x%y)
print(EuclidAlgo(9,3))
