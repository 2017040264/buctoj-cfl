#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:a+b+c=1000.py
@time:2021/11/19
@software:PyCharm
"""

import time

def main():
    start=time.time()
    for i in range(1001):
        for j in range(1001):
            for k in range(1001):
                if i+j+k==1000 and i*i+j*j==k*k:
                    print(i,j,k)
    end1=time.time()
    print('运行时间',end1-start)

    s1=time.time()
    for i in range(1001):
        for j in range(1001):
            if i*i+j*j==(1000-i-j)**2:
                print(i,j,1000-i-j)
    e1=time.time()
    print('运行时间',e1-s1)

    s1=time.time()
    for i in range(501):
        for j in range(1000-i):
            if i*i+j*j==(1000-i-j)**2:
                print(i,j,1000-i-j)
    e1=time.time()
    print('运行时间',e1-s1)

    s1=time.time()
    for i in range(501):
        for j in range(501):
            if i*i+j*j==(1000-i-j)**2:
                print(i,j,1000-i-j)
    e1=time.time()
    print('运行时间',e1-s1)





if __name__ == '__main__':
    main()
