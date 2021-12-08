#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:stack.py
@time:2021/12/08
@software:PyCharm
"""


class Node:
    def __init__(self, value):
        self.value = value  # 栈结点的值
        self.pre = None  # 指向前一个节点的指针


class Stack:
    # 初始化栈
    def __init__(self):
        self.point = None
        self.length = 0

    # 压栈操作
    def push(self, value):
        node = Node(value)
        if self.point != None:
            node.pre = self.point
            self.point = node
        else:
            self.point = node

        self.length += 1

    # 出栈操作
    def pop(self):
        if self.point != None:
            node = self.point
            self.point = node.pre
            node.pre = None

            self.length -= 1
            return node.value
        else:
            return None

    # 判断栈是否为空
    def is_empty(self):
        return False if self.length else True


def main():
    stack=Stack()
    for i in range(5):
        print(i)
        stack.push(i)
    print(stack.is_empty())
    print('*****************')
    for i in range(5):
        print(stack.pop())
    print(stack.is_empty())

if __name__ == '__main__':
    main()
