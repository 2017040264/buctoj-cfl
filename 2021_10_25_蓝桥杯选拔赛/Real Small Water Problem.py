import math

def funct(x,n):
    if x==0:
        return math.sin(n)
    return math.sin(funct(x-1,n))

while True:
    try:
        n=int(input())
        
        print("{:.6f}".format(funct(n,n)))
    except:
        break