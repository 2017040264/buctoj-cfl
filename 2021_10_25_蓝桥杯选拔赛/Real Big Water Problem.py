import math

def funct(x,n):
    if x==0:
        return math.cos(n)
    return math.cos(funct(x-1,n))

while True:
    try:
        n=int(input())
        if n >50:
            print("0.739085")
        else:
            print("{:.6f}".format(funct(n,n)))
    except:
        break
