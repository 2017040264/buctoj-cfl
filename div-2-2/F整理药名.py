#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:F整理药名.py
@time:2021/12/28
@software:PyCharm
"""


def main():
    n=int(input())
    for i in range(n):
        strss=input()
        strs=[]
        for ss in strss:
            strs.append(ss)
        if strs[0].isalpha():

            strs[0]=strs[0].upper()
        for i in range(1,len(strs)):
            if strs[i].isalpha():
                strs[i]=strs[i].lower()
        re=''
        for s in strs:
            re+=s
        print(re)


if __name__ == '__main__':
    main()
