#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:简单除法.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    while True:
        try:
            m,n=map(int,input().split())
            if n==0:
                print('error')
            else:
                if m/n-m//n>=0.5:
                    print(m//n+1)
                else:
                    print(m//n)
        except:
            break


if __name__ == '__main__':
    main()
