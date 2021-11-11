n,k=input().split()
n=int(n)
k=int(k)

lista=input().split()
lista=lista[:n]
for i in range(len(lista)):
    lista[i]=int(lista[i])

count=0
left=0
right=0
sum=lista[0]

while(right<n):
    
    if sum>=k:
        sum-=lista[left]
        left+=1
        count+=n-right
        #print(left,right)
    else:
        right+=1
        if right>=n:
            break
        sum+=lista[right]

print(count)

'''
4 10
6 1 2 7

'''
