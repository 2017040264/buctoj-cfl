# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:14
# @Author : 陈凡亮
# @File : Big Dipper.py
# @Software : PyCharm
import math


def main():
    while True:
        try:
            n=int(input())
            a1=n//1000000
            a2=n//100000%10
            a3=n//10000%10
            a4=n//1000%10
            a5=n//100%10
            a6=n//10%10
            a7=n%10
            if math.pow(a1,7)+math.pow(a2,7)+math.pow(a3,7)+math.pow(a4,7)+math.pow(a5,7)+math.pow(a6,7)+math.pow(a7,7)==n:
                print("Y")
            else:
                print("N")
        except:
            break


if __name__ == "__main__":
    main()
