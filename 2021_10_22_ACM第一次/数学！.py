n,m=input().split()
n,m=int(n),int(m)

def input_list():
    listn=input().split()
    for i in range(len(listn)):
        listn[i]=int(listn[i])
    
    return listn

listn=input_list()
listm=input_list()


print(listn,listm)


