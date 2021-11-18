#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:分数拆分.py
@time:2021/11/11
@software:PyCharm
"""


def main():
    while True:
        try:
            k=int(input())
            y=k+1
            for i in range(y,2*y):
                x=int((i*k)/(i-k))
                #print(x)
                if k==(x*i)/(x+i):
                    print("1/{}=1/{}+1/{}".format(k,x,i))
        except:
            break


if __name__ == '__main__':
    main()
