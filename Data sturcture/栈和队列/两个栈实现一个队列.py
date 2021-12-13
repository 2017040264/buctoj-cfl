#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:两个栈实现一个队列.py
@time:2021/12/10
@software:PyCharm
"""
from stack import Stack

class StackQue:
    def __init__(self):
        self.a=Stack()
        self.b=Stack()
    def appendtail(self,v):
        if self.b.is_empty()==False:
            lenb=self.b.length
            for i in range(lenb):
                self.a.push(self.b.pop())
        self.a.push(v)
    def deletehead(self):
        if self.b.is_empty():
            lena=self.a.length
            for i in range(lena):
                self.b.push(self.a.pop())
        return self.b.pop()

def main():
    stackque=StackQue()

    for i in range(4):
        stackque.appendtail(i)

    for i in range(3):
        stackque.deletehead()

    for i in range(7,10):
        stackque.appendtail(i)

    for i in range(7):
        print(stackque.deletehead())


if __name__ == '__main__':
    main()
