#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:长整数减法.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    while True:
        try:
            a,b=map(int,input().split())
            print(a-b)
        except:
            break



if __name__ == '__main__':
    main()
