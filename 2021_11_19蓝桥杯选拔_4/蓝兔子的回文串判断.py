#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:蓝兔子的回文串判断.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    n=int(input())
    for i in range(n):
        s1=input()
        lens=len(s1)
        flag=0
        for i in range(lens//2):
            if s1[i]!=s1[lens-1-i]:
                flag=1
                break
        if flag==0:
            print("YES")
        else:
            print("NO")





if __name__ == '__main__':
    main()
