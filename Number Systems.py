#Any base n to Denary(Iterative)
def get_index(my_list, key):
    for i in range(len(my_list)):
            if my_list[i] == key:
                    return i
    return None
def base_n_to_denary(value_str, n):
    key = "0123456789ABCDEF"
    denary_value = 0
    for i in range(len(value_str)):
            index = get_index(key, value_str[i])
            if index != None:
                    denary_value += index * n ** (len(value_str) - 1 - i)
            else:
                    print("Unexpected symbol in value string parameter!")
                    return None
    return denary_value

#Denary to Binary (Iterative)
def d2b(num):
    n=0
    remainder=0
    lst=[]

    while num>0:
        remainder=num%2
        lst.append(str(remainder))
        num=(num-remainder)//2
    

    binary=""
    for i in lst[::-1]:
        binary+=str(i)

    return binary

#Denary to Binary (Recursive)           
def d2b(num):
    if num==0:
        return 0
    else:
        remainder=num%2
        quotient=num//2
    return str(d2b(quotient))+str(remainder)

#Denary to Hexadecimal (Recursive)
def DenaryToHexadecimal(n):
    HexDigits="0123456789ABCDEF" #16
    if n<16:
        TempString=HexDigits[n]
    else:
        # "+" is the concatenation operator
        TempString=DenaryToHexadecimal(n//16)+HexDigits[n%16]
    return TempString

def hexa_to_denary(num):
    hexdigits="0123456789ABCDEF"
    total=0
    count=0
    num=num[::-1]
    for char in num:
        if char=="A":
            char=10
        elif char=="B":
            char=11
        elif char=="C":
            char=12
        elif char=="D":
            char=13
        elif char=="E":
            char=14
        elif char=="F":
            char=15
        char=int(char)
        total+=char*(16**count)
        count+=1
    return total
    
#Denary to Octal (Recursive)
def DenaryToOctal(n):
    OctalDigits="01234567"
    if n<8:
        TempString=OctalDigits[n:n+1]
    else:
        # "+" is the concatenation operator
        TempString=DenaryToOctal(n//8)+OctalDigits[(n%8):(n%8)+1]
    return TempString





























