# -*- coding = utf-8 -*-
# @Time : 2021/8/18 8:34
# @Author : 陈凡亮
# @File : Score Conversion.py
# @Software : PyCharm

def main():
    n=int(input())
    if n>89:
        print("A")
    elif n>79:
        print("B")
    elif n>69:
        print("C")
    elif n>59:
        print("D")
    else:
        print('E')


if __name__ == "__main__":
    main()
