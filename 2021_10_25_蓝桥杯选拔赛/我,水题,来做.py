n=int(input())
lista=[0]*n 
for i in range(2,n):
    if lista[i]==0:
        print(i)
        if i*i>n:
            continue
        for j in range(i*i,n,i):
            lista[j]=1
# Consolas
# times