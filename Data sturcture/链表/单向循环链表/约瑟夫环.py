#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:约瑟夫环.py
@time:2021/12/29
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
        self.forpoint=None # 约瑟夫环计数指针
        self.prepoint=None # 约瑟夫环计数前一个指针

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

    # 约瑟夫环的转动方法
    def ysfNext(self):
        if self.length>2:
            if self.forpoint!=None:
                self.prepoint=self.forpoint     # 当前指针赋值给前结点指针
                self.forpoint=self.forpoint.next # 当前指针指向下一个结点
            else:
                self.forpoint=self.phead # 刚开始转动，当前指针指向头结点
            return True
        else:
            return False

    # 约瑟夫环出队方法
    def ysfRemove(self):
        node=self.forpoint
        if node==self.phead:   # 如果出队的是头指针
            self.phead=node.next
        self.forpoint=self.forpoint.next  # 当前指针后移
        self.prepoint.next=node.next    # 前一个节点next指向当前结点的下一个结点

        node.next=None  # 当前结点出队，指针为空
        self.length-=1
        print(node.data,'出队')

    def sc_display(self):
        lst = []
        node = self.phead
        lst.append(node.data)
        while node.next != self.phead:
            node = node.next
            lst.append(node.data)
        return lst

def main():
    scll=scLinkList()
    n=41 # 总人数
    m=3  # 报数第m个人被kill掉
    for i in range(1,n+1):
        scll.sc_append(i)
    print(scll.sc_display())
    print('开始约瑟夫循环：\n')
    ii=0
    while scll.ysfNext():
        ii+=1
        if ii==m:
            scll.ysfRemove()
            ii=1
    print('\n约瑟夫循环结束：')
    print(scll.sc_display())


if __name__ == '__main__':
    main()
