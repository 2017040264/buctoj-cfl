#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:合并两个有序链表.py
@time:2021/12/21
@software:PyCharm
"""

# 合并有序链表，经典问题
# 将两个有序链表合并成一个，让新链表依然是有序的
from slinklist import SlinkList

def orderconcat(a,b):
    pa=a.phead
    pb=b.phead
    c=SlinkList()
    while pa!=None and pb!=None:
        if pa.data<pb.data:
            c.appendtail(pa.data)
            pa=pa.next
        else:
            c.appendtail(pb.data)
            pb=pb.next

    while pa!=None:
        c.appendtail(pa.data)
        pa=pa.next

    while pb!=None:
        c.appendtail(pb.data)
        pb=pb.next

    return c


def main():
    a=SlinkList()
    b=SlinkList()

    for i in [1,3,16,27,49]:
        a.appendtail(i)

    for i in [4,7,22,45,90]:
        b.appendtail(i)

    neworderlinklist=orderconcat(a,b)
    print(neworderlinklist.display())


if __name__ == '__main__':
    main()
