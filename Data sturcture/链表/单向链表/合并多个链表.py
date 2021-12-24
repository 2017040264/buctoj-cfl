#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:合并多个链表.py
@time:2021/12/21
@software:PyCharm
"""

# 这里的链表并不是有序的，

from slinklist import SlinkList


def concat(lista):
    slink = SlinkList()
    for ll in lista:
        sllv = ll.display()
        for v in sllv:
            slink.appendtail(v)
    return slink


def main():
    sll1 = SlinkList()
    sll2 = SlinkList()
    for i in range(1, 6):
        sll1.appendtail(i)
        sll2.appendtail(i * i)
    lst = [sll1, sll2]

    newlinklist = concat(lst)
    print(newlinklist.display())


if __name__ == '__main__':
    main()
