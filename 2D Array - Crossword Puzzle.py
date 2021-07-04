array = [["+"]*10 ] * 12 #row X col; 12 X 10

for row in range(12):
    array[row] = ["+"]*10 

array[6][0] = "-"
array[6][1] = "-"
array[6][2] = "-"
array[6][3] = "-"
array[6][4] = "-"
array[6][5] = "-"
array[6][6] = "-"

array[1][2] = "-"
array[2][2] = "-"
array[3][2] = "-"
array[4][2] = "-"
array[5][2] = "-"

array[5][6] = "-"
array[7][6] = "-"
array[8][6] = "-"

def generateCrossword():
    words=[]
    file=open("Word.txt","r")
    for word in file:
        words.append(word)
    return words
    
##    return array
print(generateCrossword())

#####################################################
#End Result
array2 = [["+"]*10 ] * 12 #row X col; 12 X 10

for row in range(12):
    array2[row] = ["+"]*10 

array2[6][0] = "c"
array2[6][1] = "o"
array2[6][2] = "n"
array2[6][3] = "q"
array2[6][4] = "u"
array2[6][5] = "e"
array2[6][6] = "r"

array2[1][2] = "w"
array2[2][2] = "i"
array2[3][2] = "t"
array2[4][2] = "h"
array2[5][2] = "i"

array2[5][6] = "f"
array2[7][6] = "o"
array2[8][6] = "m"

for row in array2:
    print(str(row)+"\n")
