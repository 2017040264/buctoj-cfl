#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:quence.py
@time:2021/12/08
@software:PyCharm
"""


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class Quence:
    def __init__(self):
        self.head = None
        self.rear = None
        self.length = 0

    def inque(self, v):
        node = Node(v)
        # 如果不是空的队列，先让尾结点指向新的node，然后把尾节点移动到新的node
        if self.head != None:
            self.rear.next = node
            self.rear = node
        else:
            self.head = node
            self.rear = node

        self.length += 1

    def outque(self):
        # 判断队列是不是空队列
        try:
            node = self.head

            # 如果队列结点超过一个，head后移
            if node.next != None:
                self.head = node.next
                node.next = None
            else:
                self.head = None
                self.rear = None

            self.length -= 1
            return node.value
        except:
            print('队列为空，无法进行出队操作，请检查代码')

    def isempty(self):
        return False if self.length else True


def main():
    que = Quence()
    for i in range(5):
        que.inque(i)
    for i in range(5):
        print(que.outque())

    que.outque()


if __name__ == '__main__':
    main()
