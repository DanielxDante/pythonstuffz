#Q1
#####################################################
##def hit(lyrics,magic_word,repetitions):
##    final_lyrics=[]
##    song=""
##    length=len(lyrics)
##    for i in range(length):
##        if lyrics[i]==magic_word:
##            final_lyrics+=(magic_word + " ")*repetitions
##        else:
##            final_lyrics+=lyrics[i] + " "
##    for lyric in final_lyrics:
##        song+=lyric
##    return song.strip()
##print(hit(["op", "oppa", "gangnam", "style"], "op", 4))

######################################################
#Q2
#######################################################
##def mega_hit(lyrics,magic_words_dict):
##    final_lyrics=[]
##    song=""
##    length=len(lyrics)
##    for i in range(length):
##        for x in magic_words_dict:
##            if x==lyrics[i]:
##                final_lyrics+=(x + " ")*magic_words_dict[x]
##            else:
##                final_lyrics+=lyrics[i] + " "
##    for lyric in final_lyrics:
##        song+=lyric
##    return song.strip()
##print(mega_hit (["op", "oppa", "gangnam", "style"], {"op": 4}))

#######################################################
#Q3
########################################################
##def triangle(a,b,c):
##    if (a>b+c or b>a+c or c>a+b):
##        return("Not a triangle")
##    if a==b and b==c:
##        return("Equilateral")
##    if (a==b or b==c or a==c) and not(a==b and b==c):
##        return("Isoceles")
##    if not(a>b+c or b>a+c or c>a+b) and (a!=b and a!=c and b!=c):
##        return("Scalene")

#####################################################
#Q4
#####################################################
##def prime(a):
##    a=int(a)
##    if a==1:
##        return False
##    for b in range(2,a):
##        if a%b==0:
##            return False
##        else:
##            return True

#####################################################
#Q5
###################################################
##def legendre_n(n):
##    n=int(n)
##    c=0
##    for i in range(n**2,(n+1)**2+1):
##        if prime(i):
##            c+=1
##    return c
##        
##print(legendre_n(1))

#####################################################
#Q6
###################################################





















