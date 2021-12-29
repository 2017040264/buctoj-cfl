#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:G矩阵转置.py
@time:2021/12/28
@software:PyCharm
"""

def main():
    m,n=map(int,input().split())
    llist=[]

    for i in range(m):
        ll=input().split()
        llist.append(ll)

    for i in range(n):
        s=''
        for j in range(m):
            s+=llist[j][i]+' '
        print(s.strip())


if __name__ == '__main__':
    main()
