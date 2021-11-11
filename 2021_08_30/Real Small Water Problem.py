# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:26
# @Author : 陈凡亮
# @File : Real Small Water Problem.py
# @Software : PyCharm
import math

def func(n,x):
    if n==0:
        return math.sin(x)
    else:
        return math.sin(func(n-1,x))

def main():
    while True:
        try:
            n=int(input())

            print("{:.6f}".format(func(n,n)))
        except:
            break


if __name__ == "__main__":
    main()
    #print(func(2,2))
