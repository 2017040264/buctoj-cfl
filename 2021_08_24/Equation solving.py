# -*- coding = utf-8 -*-
# @Time : 2021/8/24 8:15
# @Author : 陈凡亮
# @File : Equation solving.py
# @Software : PyCharm
import math


def main():
    a,b,c=input().split()
    a,b,c=int(a),int(b),int(c)
    dert=b*b-4*a*c
    if dert>=0:
        print("x1=",((-b)+math.sqrt(dert))/(2*a),"x2=",((-b)-math.sqrt(dert))/(2*a))
    else:
        aa=(-b)/(2*a)
        bb=math.sqrt(-dert)/(2*a)

        print("x1={:.3f}+{:.3f}i x2={:.3f}-{:.3f}i".format(aa,bb,aa,bb))




if __name__ == "__main__":
    main()
