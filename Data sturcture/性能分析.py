#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:性能分析.py
@time:2021/11/19
@software:PyCharm
"""
from timeit import Timer


def test1():
    l = []
    for i in range(100000):
        l += [i]


def test2():
    l = []
    for i in range(100000):
        l.append(i)





def main():
    pass


if __name__ == '__main__':
    main()
    t1 = Timer('test1()', 'from __main__ import test1')
    print('concat', t1.timeit(number=1000), 'seconds')

    t2 = Timer('test2()', 'from __main__ import test2')
    print('append', t2.timeit(number=1000), 'seconds')
