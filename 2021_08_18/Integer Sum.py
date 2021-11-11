# -*- coding = utf-8 -*-
# @Time : 2021/8/18 9:10
# @Author : 陈凡亮
# @File : Integer Sum.py
# @Software : PyCharm

def main():
    n=int(input())
    sum=0
    for i in range(1,n+1):
        temp=2
        for j in range(1,i):
            temp=temp*10+2
        sum+=temp
    print(sum)


if __name__ == "__main__":
    main()
