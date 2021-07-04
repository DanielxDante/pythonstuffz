#Format Method 1 : Simplest, most useless method ever
#Inserts 8 spaces
+ "\t" 

#Format Method 2 : Best for me so far
#Must use courier (and a few other fonts) to obtain optimal format
#{item number:Size allocated}
print("{0:10}{1:10}{2:10}".format(str(item1),str(item2),str(item3)))

#Format Method 3 : Similar to Method 2, just shorter syntax
#item.ljust(size allocated) + 
print(item1.ljust(20) + item2.ljust(15) + item3.ljust(10))

#Format Method 4 : Effectiveness is dependant on situation
#Inserts whatever inside "" between each item
lst=["a","b","c"]
" ".join(lst) ==> "a b c"
"$$$".join(lst) ==> "a$$$b$$$c"

#Format Method 5 : Only if built-in functions are not allowed
#Hard-coding by adding to line
line=""
lst=["a","b","c"]
for char in lst:
    line+=char
line ==> abc


