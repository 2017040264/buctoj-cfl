#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:递归与栈实现汉诺塔.py
@time:2021/12/10
@software:PyCharm
"""
class Node:
    def __init__(self, value):
        self.value = value  # 栈结点的值
        self.pre = None  # 指向前一个节点的指针


class Stack:
    # 初始化栈
    def __init__(self,name):
        self.point = None
        self.length = 0
        self.name=name

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

def move(n,s1,s2,s3):
    if n!=1:
        move(n-1,s1,s3,s2)
        move(1,s1,s2,s3)
        move(n-1,s2,s1,s3)
    else:
        # s1->s3
        temp=s1.pop()
        s3.push(temp)
        print(s1.name,'->',s3.name,'value=',temp)

def main():
    a=Stack('A')
    b=Stack('B')
    c=Stack('C')

    # a中压栈4个元素，[4,3,2,1]
    for i in range(4,0,-1):
        a.push(i)
    length=a.length


    print('转移过程')
    move(length,a,b,c)

    print('最终结果：')
    for i in range(length):
        print(c.pop())



if __name__ == '__main__':
    main()
