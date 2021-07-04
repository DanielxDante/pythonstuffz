def is_Fibonacci(n):
    temp=0
    a=1
    b=1
    num=2

    if n==0:
        return False
    elif n==1:
        return True
    while num<=n:
        if num==n:
            return True
        else:
            a=b
            temp=b
            b=num
            num+=temp
    return False
print(is_Fibonacci(6))
