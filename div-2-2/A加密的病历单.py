#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:A加密的病历单.py
@time:2021/12/28
@software:PyCharm
"""


def main():
    strs=input()
    lists=[]
    for s in strs:
        if s.isupper():
            lists.append(chr(ord('A')+(ord(s)+3-ord('A'))%26))
        else:
            #print(1)
            #print(ord('a'))
            #print(ord(s)+3-ord('a'))
            #print(chr(100))
            lists.append(chr(ord('a')+(ord(s)+3-ord('a'))%26))
    #print(lists)
    lists.reverse()
    #print(lists)

    result=''
    for i in range(len(lists)):
        if lists[i].isupper():
            result+=lists[i].lower()
        else:
            result+=lists[i].upper()
    print(result)


if __name__ == '__main__':
    main()
