# -*- coding = utf-8 -*-
# @Time : 2021/8/21 8:55
# @Author : 陈凡亮
# @File : Sequence summation.py
# @Software : PyCharm

def main():
    n= int(input())
    fenzi=2
    fenmu=1
    sum=0
    for i in range(n):
        sum+=fenzi/fenmu
        fenmu,fenzi=fenzi,fenzi+fenmu
    print("{:.2f}".format(sum))


if __name__ == "__main__":
    main()
