#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:sclink.py
@time:2021/12/28
@software:PyCharm
"""


class scNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class scLinkList:
    def __init__(self):
        self.phead = None
        self.length = 0

    def sc_append(self, data):
        newnode = scNode(data)
        if self.phead != None:
            p1 = self.phead
            while p1.next != self.phead:
                p1 = p1.next
            newnode.next = self.phead
            p1.next = newnode
        else:
            self.phead = newnode
            # 这里需要注意，newnode.next也可指向self.phead
            newnode.next = newnode

        self.length += 1

    def sc_display(self):
        lst = []
        node = self.phead
        lst.append(node.data)
        while node.next != self.phead:
            node = node.next
            lst.append(node.data)
        return lst


def main():
    scll = scLinkList()
    for i in range(10):
        scll.sc_append(i * i)
    print(scll.sc_display())


if __name__ == '__main__':
    main()
