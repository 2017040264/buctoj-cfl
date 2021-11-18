#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:数数.py
@time:2021/11/11
@software:PyCharm
"""

from collections import  Counter

def main():
    n=int(input())
    lista=input().split()
    lista=lista[:n]
    dicta=Counter(lista)
    m=int(input())
    for i in range(m):
        qu=input()
        print(dicta[qu])

if __name__ == '__main__':
    main()
