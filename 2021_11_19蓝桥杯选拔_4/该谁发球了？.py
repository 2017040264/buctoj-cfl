#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:该谁发球了？.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    while True:
        try:
            a,b=map(int,input().split())
            if a<b:
                c=a
                a=b
                b=c
            # 总是让a>=b

            if a<11:
                if a==10 and b==10:
                    print("A")
                else:
                    a=a+b
                    if a//2%2==0:
                        print("A")
                    else:print("B")
            else :
                if a-b>=2:
                    print('Game Over')
                else:
                    a=a+b-20
                    if a%2==0:
                        print('A')
                    else:
                        print('B')
        except:
            break





if __name__ == '__main__':
    main()
