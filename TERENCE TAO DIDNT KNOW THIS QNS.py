import math
def qns6():
    for integer in range(1,1000):
        for a in range(1000):
            for b in range(1000):
                if (a**2+b**2)%(a*b+1)==0 and math.sqrt((a**2+b**2)//(a*b+1))==integer:
                    print(integer)
qns6()
