#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:相交链表.py
@time:2021/12/21
@software:PyCharm
"""


# 两个单向链表中的结点发生next指针指向同一结点的情况

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SlinkList:
    def __init__(self):
        self.phead = None  # 头指针
        self.length = 0
        self.other = None  # 对另一链表的引用

    # 尾插法
    def appendtail(self, data):
        node = Node(data)

        # 头结点为空，说明该链表还没有元素
        if self.phead != None:
            pl = self.phead
            while pl.next != None:
                pl = pl.next
            pl.next = node
        else:
            self.phead = node

        self.length += 1

        # 如果有相交链表，另一个链表长度加1
        if self.other != None:
            self.other.length += 1

    # 获取指定位置的结点值
    def getData(self, index):
        if index >= self.length:
            print('越界，上界')
            return None
        elif index < 0:
            print('越界，下界')
            return None

        p1 = self.phead
        n = 0
        while n < index:
            n += 1
            p1 = p1.next

        return p1.data

    # 单向链表的随机插入，按位置插入，插入到指定位置的前端
    def insert(self, data, index):

        # 针对位置越界的情况进行判定
        if index > self.length:
            print('越界，上界')
            index = self.length
        elif index < 0:
            print('越界，下界')
            index = 0

        node = Node(data)
        if index > 0:
            p1 = self.phead
            n = 0
            while n < (index - 1):
                p1 = p1.next
                n += 1
            node.next = p1.next
            p1.next = node
        else:
            # 插在头部，也就是index=0
            node.next = self.phead
            self.phead = node

        self.length += 1

    # 单向链表按位置删除
    def remove(self, index):
        if index >= self.length:
            print('越界，上界')
            return None
        elif index < 0:
            print('越界，下界')
            return None
        else:
            node = None
            if index > 0:
                p1 = self.phead
                n = 0
                while n < (index - 1):
                    p1 = p1.next
                    n += 1
                node = p1.next
                p1.next = node.next
                node.next = None
            else:
                node = self.phead
                self.phead = node.next
                node.next = None

            self.length -= 1

            return node.data

    # 返回结点列表
    def display(self):
        lst = []
        node = self.phead
        while node != None:
            lst.append(node.data)
            node = node.next
        return lst

    # 通过结点追加链表，appendtail是通过值的方式追加结点
    def appendNode(self, node):
        if self.phead != None:  # 如果已经存在头结点
            p1 = self.phead
            while p1.next != None:
                p1 = p1.next
            p1.next = node
        else:
            self.phead = node
        self.length += 1

        # 为相交链表增加长度
        if self.other != None:
            self.other.length += 1

    # 创建相交方法
    def cross(self, other, data):
        node = Node(data)
        if self.other == None:
            self.appendNode(node)
            other.appendNode(node)
            self.other = other
            self.other.other = self


def main():
    a = SlinkList()
    b = SlinkList()

    a.appendtail(2)
    a.appendtail(3)
    a.appendtail(8)
    a.appendtail(1)

    b.appendtail(5)
    b.appendtail(6)

    a.cross(b, 10)

    a.appendtail(100)

    b.appendtail(99)

    print(a.display())
    print(b.display())


if __name__ == '__main__':
    main()
