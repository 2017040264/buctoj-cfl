#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:Cleaning Shifts.py
@time:2021/11/19
@software:PyCharm
"""


def main():

    m,n=map(int,input().split())
    dicta={}
    for i in range(m):
        a,b=map(int,input().split())
        if a not in dicta.keys():
            dicta[a]=0
        dicta[a]=max(dicta[a],b)

    xli=list(dicta.keys())

    xli.sort()

    if xli[0]!=1:
        print(-1)
    else:
        count=1
        t1 = xli[0]
        t2 = dicta[t1]
        flag=1
        #print(xli.index(t1),'t1=',t1,'t2=',t2)
        while t2<n:
            #print('t1=',t1,'t2=',t2)
            maxs=0
            newt1=0
            for i in range(xli.index(t1)+1,len(xli)):
                if xli[i]>t2+1:
                    break
                if dicta[xli[i]]>maxs:
                    maxs=dicta[xli[i]]
                    newt1=xli[i]
            if newt1==0:
                flag=0
                break
            t1=newt1
            t2=dicta[t1]
            count+=1

        if flag==1:
            print(count)
        else:print(-1)


if __name__ == '__main__':
    main()
