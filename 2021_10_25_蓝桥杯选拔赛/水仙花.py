
a=int(input())
b=a
sum=0
for i in range(3):
    last=a%10
    sum+=last**3
    #print(last)
    a=a//10
if sum==b:
    print("YES")
else:
    print("NO")
