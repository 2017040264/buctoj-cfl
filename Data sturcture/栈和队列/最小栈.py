#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:最小栈.py
@time:2021/12/09
@software:PyCharm
"""

"""
最小栈的意思是当前（在有元素入栈的过程中）栈顶元素始终是最小值
"""

class Node:
    def __init__(self,v):
        self.value=v   # 栈结点的值
        self.pre=None


class minStack:
    def __init__(self):
        self.point=None
        self.length=0

    def push(self,v):
        node=Node(v)
        if self.point!=None:
            # 如果新结点值大于栈顶元素值，则将栈顶结点出栈，入栈新结点，之后再入栈原栈顶结点
            # 否则直接入栈新结点
            if node.value>self.point.value:
                # 栈顶元素出栈
                temp=self.pop()
                # 新结点入栈
                node.pre=self.point
                self.point=node
                # 原栈顶结点入栈
                newnode=Node(temp)
                newnode.pre=self.point
                self.point=newnode
                self.length+=1
            else:
                node.pre=self.point
                self.point=node
        else:
            self.point=node
        self.length+=1

    def pop(self):
        if self.point!=None:
            node=self.point
            self.point=node.pre
            node.pre=None
            self.length-=1
            return node.value

        else:
            return None

    def isempty(self):
        return False if self.length else True



def main():
    minstk=minStack()
    test=[9,1,2,4,5,6,7,11,34,56,33]
    for i in range(len(test)):
        minstk.push(test[i])

    print(minstk.pop())

    #print(minstk.pop())



if __name__ == '__main__':
    main()
