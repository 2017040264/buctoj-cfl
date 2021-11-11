n=int(input())
for i in range(n):
    strs=input()
    lista=[strs]
    
    #1print(lista)

    a=1
    while a==1:
        a=0
        
        for i in range(len(lista)):
            if len(lista[0]>1):
            strs=lista.pop(0)
            
            
            if len(strs)>1:
                left=0
                while(left<len(strs)):
                    if strs[left]==')' or strs[left]==']':
                        
                        lista.append(strs[:left])
                        left+=1
                        
                    elif strs[left]=='(':
                        loca=left+1
                        while(loca<len(strs)):
                            if strs[loca]==')' and left+1!=loca:
                                lista.append(strs[left,loca+1])
                                a=1
                                left=loca+1
                                break
                            loca+=1
                            
                        if loca==len(strs):
                            lista.append(strs[left])
                            left+=1 
                    
    #                 elif strs[left]=='[':
    #                     loca=left+1
    #                     while(loca<len(strs)):
    #                         if strs[loca]==']' and left+1!=loca:
    #                             lista.append(strs[left,loca+1])
    #                             a=1
    #                             left=loca+1
    #                             break
    #                         loca+=1
                            
    #                     if loca==len(strs):
    #                         lista.append(strs[left]) 
    #                         a=1
    #                         left+=1

    #     print(lista)
    
    print('\n')


    

            
