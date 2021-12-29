#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:C图像旋转.py
@time:2021/12/28
@software:PyCharm
"""


def main():
    n,m=map(int,input().split())
    llist=[]
    for i in range(n):
        st=input().split()
        llist.append(st)
    for i in range(m):
        s=''
        for j in range(n):
            s+=llist[n-1-j][i]+' '
        print(s.strip())


if __name__ == '__main__':
    main()
