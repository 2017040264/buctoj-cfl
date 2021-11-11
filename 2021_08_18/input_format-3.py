# -*- coding = utf-8 -*-
# @Time : 2021/8/18 8:16
# @Author : 陈凡亮
# @File : input_format-3.py
# @Software : PyCharm

def main():
    n = int(input())
    for i in range(n):
        a, b = input().split()
        print(int(a) + int(b))


if __name__ == "__main__":
    main()
