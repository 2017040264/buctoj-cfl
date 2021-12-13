#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author:cfl
@file:slinklist.py
@time:2021/12/13
@software:PyCharm
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SlinkList:
    def __init__(self):
        self.phead = None  # 头指针
        self.length = 0

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


def main():
    singleLinkList = SlinkList()
    n=7
    getindex=[-2,5,9]
    insertindex=0
    removeindex=5
    for i in range(n):
        singleLinkList.appendtail(i)
    lst = singleLinkList.display()
    print('\n头插法插入{}个结点：'.format(n))
    print(lst)
    for i in range(len(getindex)):
        print('\n获取指定位置{}的节点值：'.format(getindex[i]))
        print(singleLinkList.getData(getindex[i]))

    print('\n在指定位置{}插入新结点(前插)'.format(insertindex))
    singleLinkList.insert(28, insertindex)
    print(singleLinkList.display())

    print('\n删除指定位置{}的结点，并返回结点值'.format(removeindex))
    removerdata=singleLinkList.remove(removeindex)
    print('删除的结点值为：{}'.format(removerdata))
    print(singleLinkList.display())


if __name__ == '__main__':
    main()
