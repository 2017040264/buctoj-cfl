#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:H字符串p型编码.py
@time:2021/12/29
@software:PyCharm
"""


def main():
    strs=input()
    re=''
    count=1
    lastchar=strs[0]
    for i in range(1,len(strs)):
        if strs[i]==lastchar:
            count+=1
        else:
            re=re+str(count)+lastchar
            lastchar=strs[i]
            count=1

    print(re+str(count)+lastchar)


if __name__ == '__main__':
    main()
