
n=int(input())
llst=[]
for i in range(n):
    s=input()

    
    left=0
    rigth=len(s)-1
    count=0
    while(left<=rigth):
        if s[left]!=s[rigth] :
            count+=1
        elif count==0 and left==rigth:
            count+=1
        
        left+=1
        rigth-=1

    if count==1:
        llst.append("YES")
        print("YES")
    else:
        llst.append("NO")
        print('NO')
#print(llst)
    


