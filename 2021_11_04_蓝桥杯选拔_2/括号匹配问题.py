while True:
    try:
        ss=input()
        lista=[]
        
        for s in ss:
            
            if s=='(':
               lista.append(s)
               
            elif s==')' :
                if len(lista)==0:
                    lista.append(s)
                elif lista[-1]=='(':
                    lista.pop()
                else:
                    lista.append(s)
        
        if len(lista)!=0:
            print('NO')
        else:
            print("YES")
    except:
        break