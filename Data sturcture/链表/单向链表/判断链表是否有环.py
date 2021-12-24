#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:判断链表是否有环.py
@time:2021/12/24
@software:PyCharm
"""
import ssl

from slinklist import SlinkList

def judgecircle(ssl):
    fast=ssl.phead
    slow=ssl.phead
    while fast!=None and fast.next!=None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            print('有环,第一次相遇节点值为{}'.format(fast.data))
            break
    if fast==None or fast.next==None:
        print('无环')
    else: # 找出闭合结点
        slow=ssl.phead
        while slow!=fast:
            fast=fast.next
            slow=slow.next
        print('闭合点：',slow.data)


def main():

    ssl=SlinkList()
    for i in range(10):
        ssl.appendtail(i*i)
    print(ssl.display())

    judgecircle(ssl)

    ssl.setCricle(6)

    judgecircle(ssl)

if __name__ == '__main__':
    main()
