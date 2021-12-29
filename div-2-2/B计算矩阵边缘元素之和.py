#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:B计算矩阵边缘元素之和.py
@time:2021/12/28
@software:PyCharm
"""


def main():
    n,m=map(int,input().split())
    sum=0

    if m==1:
        lista = input().split()[:n]
        for i in range(len(lista)):
            sum+=int(lista[i])

    elif n==1:
        for i in range(m):
            sum+=int(input())
    else:
        for i in range(m):
            lista=input().split()[:n]
            if i==0 or i==m-1:
                for ll in lista:
                    sum+=int(ll)
            else:
                sum+=(int(lista[0])+int(lista[-1]))
    print(sum)


if __name__ == '__main__':
    main()
