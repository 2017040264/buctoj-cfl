#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:E输出亲朋字符串.py
@time:2021/12/28
@software:PyCharm
"""


def main():
    strs=input()
    result=''
    for i in range(len(strs)-1):
        result+=chr(ord(strs[i])+ord(strs[i+1]))
    result += chr(ord(strs[0]) + ord(strs[-1]))
    print(result)


if __name__ == '__main__':
    main()
