#Hash NRIC (eg : S8123456I, T9900001J) {T or S format, 7 numbers, 1 random alphabet at the back}
#Table size 131, storing 60 keys
#Linear Probing, function returns index
#Range of decimals for uppercase alphabets : 65-90
#Range of decimals for lowercase alphabets : 97-122
#Range of decimals for numbers : 48-57 (0 included)
def hashfunction(key): 
    total=0
    index=0
    for character in key:
        total+=ord(character)
    index=total%131
    return index
print(hashfunction("S8123456I"))
