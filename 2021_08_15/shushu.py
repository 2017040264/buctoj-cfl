# -*- coding = utf-8 -*-
# @Time : 2021/6/29 14:54
# @Author : 陈凡亮
# @File : shushu.py
# @Software : PyCharm

def main():
    m=int(input())

    lista=input().split()

    n=int(input())
    for i in range(n):
        number=input()
        print(lista.count(number))

if __name__ == "__main__":
    main()

# 66051
# 1e5
