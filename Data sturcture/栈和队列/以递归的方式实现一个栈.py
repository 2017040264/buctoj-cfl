#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:以递归的方式实现一个栈.py
@time:2021/12/10
@software:PyCharm
"""
from stack import Node,Stack

stack1=Stack()

def rev(node):
    global stack1
    preNode=node.pre
    if preNode!=None:
        rev(preNode)
        preNode.pre=node
    else:
        stack1.point=node

def main():
    for i in range(5):
        stack1.push(i)

    node=stack1.point
    rev(node)
    node.pre=None

    for i in range(5):
        print(stack1.pop())


if __name__ == '__main__':
    main()
