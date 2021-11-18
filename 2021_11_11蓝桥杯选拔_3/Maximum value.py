#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:Maximum value.py
@time:2021/11/11
@software:PyCharm
"""


def main():
    lista=input().split()
    for i in range(len(lista)):
        lista[i]=int(lista[i])
    print(max(lista))


if __name__ == '__main__':
    main()
