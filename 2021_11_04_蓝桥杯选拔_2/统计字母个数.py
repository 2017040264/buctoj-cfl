from collections import Counter


a=1
re=['a','b','c',"d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
dicta={}
for r in re:
    dicta[r]=0

while a==1:

    s=input()
    if len(s)==0:
        continue
    
    if s[-1]=='#':
        s=s[:-1]
        a=0
    
    for ss in s:
        if ss.islower():
            dicta[ss]+=1




for rr in re:
    print(rr,dicta[rr])


    

  
