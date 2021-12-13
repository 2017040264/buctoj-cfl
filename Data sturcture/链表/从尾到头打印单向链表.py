#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:从尾到头打印单向链表.py
@time:2021/12/13
@software:PyCharm
"""

from slinklist import SlinkList

def revdispay(node):

    if node.next!=None:
        revdispay(node.next)
    print(node.data)


def main():
    sll=SlinkList()
    for i in range(10):
        sll.appendtail(i)

    print("\n 从头到尾打印")
    print(sll.display())

    print('\n 从尾到头打印')
    node=sll.phead
    revdispay(node)

if __name__ == '__main__':
    main()
