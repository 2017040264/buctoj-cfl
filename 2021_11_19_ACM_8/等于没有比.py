#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:等于没有比.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    m,n=map(int,input().split())
    if m%(2*n+1)==0:
        print(m//(2*n+1))
    else:
        print(m//(2*n+1)+1)


if __name__ == '__main__':
    main()
