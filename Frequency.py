def most_frequent(file_input):
    file_size=0
    file=open(file_input,"r")
    for line in file:
        file_size+=1
    
    array_terms=[""]*int(file_size/2)
    array_occurrences=[0]*int(file_size/2)

    file.seek(0)
    #OR:file=open(file_input,"r")
    
    i=0
    s=0
    for line in file:
        if "\n" in line:
            line=line[:-1]
        if line.isnumeric():
            array_occurrences[i]=int(line)
            i+=1
        else:
            array_terms[s]=line
            s+=1
            
    most_occurrences=0
    term=""
    for i in range(int(file_size/2)):
        if array_occurrences[i]>most_occurrences:
            most_occurrences=array_occurrences[i]
            term=array_terms[i]
    return term

print(most_frequent("WORDS1.txt"))
    
    
        
    


    

            
            
        

    
    
"""
print(most_frequent("WORDS1.txt"))
"""
        
    
