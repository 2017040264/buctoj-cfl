#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:栈做十进制与二进制的转换.py
@time:2021/12/09
@software:PyCharm
"""

import math
from stack import Stack

def tenTotwo(n):
    if n>1:
        satck=Stack()
        temp=n
        while(temp>0):
            mod=temp%2
            satck.push(mod)
            # 向下取整
            temp=math.floor(temp/2)

        r=satck.pop()
        while satck.length:
            r=r*10+satck.pop()
        return r

    else:
        return n


def main():
    # 限制输入应该大于0
    print('5 的二进制 ',tenTotwo(5))
    print('10 的二进制 ',tenTotwo(10))


if __name__ == '__main__':
    main()
