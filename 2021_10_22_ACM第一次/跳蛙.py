n,x=input().split()
n=int(n)
x=int(x)

sum=0
count=1
lista=input().split()
for i in range(len(lista)):
    sum+=int(lista[i])
    
    if sum>x:
        break
    count+=1

print(count)
