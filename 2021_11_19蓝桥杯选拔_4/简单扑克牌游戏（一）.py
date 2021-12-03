#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:简单扑克牌游戏（一）.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    while True:
        try:
            a,b,c,d=map(int,input().split())
            if a==b:
                if c!=d:
                    print("A")
                else:
                    if a>c:
                        print('A')
                    elif a==c:
                        print('N')
                    else:
                        print('B')
            else:
                if c==d:
                    print('B')
                else:
                    a=(a+b)%10
                    c=(c+d)%10
                    if a>c:
                        print('A')
                    elif a==c:
                        print('N')
                    else:
                        print('B')

        except:
            break



if __name__ == '__main__':
    main()
