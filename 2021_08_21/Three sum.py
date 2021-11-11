# -*- coding = utf-8 -*-
# @Time : 2021/8/21 8:33
# @Author : 陈凡亮
# @File : Three sum.py
# @Software : PyCharm

def main():
    a,b,c=input().split()
    a=int(a)
    b=int(b)
    c=int(c)
    sum=0
    for i in range(1,a+1):
        sum+=i
    for i in range(1,b+1):
        sum+=i*i
    for i in range(1,c+1):
        sum+=1/i
    print("{:.2f}".format(sum))


if __name__ == "__main__":
    main()
