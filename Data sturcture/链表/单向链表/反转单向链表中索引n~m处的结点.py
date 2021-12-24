#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:反转单向链表中索引n~m处的结点.py
@time:2021/12/14
@software:PyCharm
"""
from slinklist import SlinkList


# 反转链表第n-m位
def passrev(sll, n, m):
    p1 = sll.phead
    ii = 0
    if n > 0:

        while ii < (n - 1):
            p1 = p1.next
            ii += 1

        # 要反转的结点的起始节点
        startNode = p1.next

    else:
        startNode = sll.phead
        ii -= 1

    def reversal(node, ii):
        ii += 1
        if ii < m:
            nextNode = node.next
            reversal(nextNode, ii)
            nextNode.next = node
        else:
            startNode.next = node.next
            if n > 0:
                p1.next = node
            else:
                sll.phead = node

    reversal(startNode, ii)


def main():

    sll=SlinkList()
    for i in range(10):
        sll.appendtail(i)
    print(sll.display())

    # 反转链表
    passrev(sll,0,7)
    print(sll.display())


if __name__ == '__main__':
    main()
