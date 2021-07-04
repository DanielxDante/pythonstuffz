##def is_palindrome(string): #helper function
##    reverse_string=string[::-1]
##    if string.upper()==reverse_string.upper():
##        return True
##    return False

import math

def isPalindrome(num):
    whole, decimal = str(num).split(".")

    if decimal == "0":
        return whole == whole[::-1]

def numberpalindrome():
    largest=0
    temp_largest=0
    for num1 in range (100, 1000):
        for num2 in range(100, 1000):
            temp_largest=num1*num2
            if is_palindrome(str(temp_largest))==True and temp_largest>largest:
                largest=temp_largest
    return largest


def recur_palindrome(string):
    n=0
    if string=="" or len(string)==1:
        return True
    else:
        first=string[0]
        last=string[-1]
        if first==last:
            return recur_palindrome(string[1:-1])
        else:
            return False

def main1(): #Print fair and square numbers that are palindromes
    count = 0
    numbers = input("Enter two integers: ")
    a, b = numbers.split(" ")
    a = int(a)
    b = int(b)

    for i in range(a,b+1):
        if isPalindrome(float(i)):
            if isPalindrome((math.sqrt(i))):
                count += 1
                print(i)

def main2():
    count = 0
    i = 1
    while count < 10:
        if isPalindrome(float(i)):
            if isPalindrome(math.sqrt(i)):
                count += 1
                print(i)

        i += 1

main1()
print()
main2()

