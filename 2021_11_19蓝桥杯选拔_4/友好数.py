#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:友好数.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    m,n=map(int,input().split())
    summ=0
    sumn=0
    for i in range(1,m//2+1):
        if m%i==0:
            summ+=i
    for i in range(1,n//2+1):
        if n%i==0:
            sumn+=i
    if sumn==m and n==summ:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
