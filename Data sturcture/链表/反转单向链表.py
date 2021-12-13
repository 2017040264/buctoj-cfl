#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:反转单向链表.py
@time:2021/12/13
@software:PyCharm
"""

from slinklist import SlinkList,Node

def rev(sll):
    def reversal(node):
        if node.next!=None:
            nextNode=node.next
            reversal(nextNode)
            nextNode.next=node
        else:
            sll.phead.next=None
            sll.phead=node
    reversal(sll.phead)


def main():
     sll=SlinkList()
     for i in range(10):
         sll.appendtail(i)

     print('未反转前的链表：')
     print(sll.display())

     print('\n 反转后的链表：')
     rev(sll)
     print(sll.display())

if __name__ == '__main__':
    main()
