# -*- coding = utf-8 -*-
# @Time : 2021/8/21 8:37
# @Author : 陈凡亮
# @File : Daffodil number.py
# @Software : PyCharm
import math


def main():

    for i in range(100,999):
        if i == int(math.pow(i//100,3)+math.pow(i%10,3)+math.pow(i%100//10,3)):
            print(i)



if __name__ == "__main__":
    main()
