n=int(input())
for i in range(n):
    a,b=input().split()
    x,y=input().split()
    a,b,x,y=int(a),int(b),int(x),int(y)

    if x>b and y>b:
        print(b-a+1)
    elif x>b and y<=b:
        dy=0
        for j in range(a,b+1):
            if j%y==0:
                dy=j
                break
        dy=(b-dy)//y+1
        print(b-a+1-dy)
    elif x<=b and y>b:
        dx=0
        for j in range(a,b+1):
            if j%x==0:
                dx=j
                break
        dx=(b-dx)//x+1
        print(b-a+1-dx)
    else:
        count=0
        dx=0
        dy=0
        # 分别找出第一个可以整除x,y的数
        for j in range(a,b+1):
            if dx!=0 and dy!=0:
                break
            if j%x==0 :
                dx=j
            if j%y==0:
                dy=j
        
        # 分别计算可以整除x，y的个数
        dx=(b-dx)//x+1
        dy=(b-dy)//y+1

        minb=0
        # 计算x，y的最小公倍数
        for j in range(min(x,y),x*y+1):
            if j%x==0 and j%y==0:
                minb=j
                break
        
        db=0
        # 计算即可整除x也可整除y的数的个数
        if b>minb:
            db=(b-minb)//minb+1
        
        print(b-a+1-dx-dy+db)
        #print('最终结果：',b-a+1-dx-dy+db)