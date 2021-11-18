#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:字符串与数字互转.py
@time:2021/11/17
@software:PyCharm
"""

def printchar():
    chara='a'
    print(ord(chara))
    for i in range(ord('a'),ord('z')+1):
        print(i,chr(i),chr(i).upper())

def main():
    pass


if __name__ == '__main__':
    main()
    printchar()
