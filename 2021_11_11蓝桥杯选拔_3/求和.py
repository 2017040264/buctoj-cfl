#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:求和.py
@time:2021/11/11
@software:PyCharm
"""


def main():
    t=int(input())
    for i in range(t):
        n,m=input().split()
        n,m=int(n),int(m)

        lista=input().split()
        for j in range(len(lista)):
            lista[j]=int(lista[j])

        maxsum=sum(lista[:m])
        suma=maxsum
        for j in range(1,len(lista)-m+1):
            #print(maxsum,suma)
            suma=suma-lista[j-1]+lista[j+m-1]
            maxsum=max(maxsum,suma)

        print(maxsum)



if __name__ == '__main__':
    main()
