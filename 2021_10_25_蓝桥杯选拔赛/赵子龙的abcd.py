n=int(input())
for i in range(n):
    a,b,c,d=input().split()
    a,b,c,d,=int(a),int(b),int(c),int(d)
    #a,b,c,d,=bin(a),bin(b),bin(c),bin(d)
    #print(a,b,c,d)
    sum=a+b+c+d
    print(sum)
    