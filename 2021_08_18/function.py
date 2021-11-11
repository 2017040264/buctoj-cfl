# -*- coding = utf-8 -*-
# @Time : 2021/8/18 8:32
# @Author : 陈凡亮
# @File : function.py
# @Software : PyCharm

def main():
    x=int(input())
    if x<1:
        print(x)
    elif x<10:
        print(2*x-1)
    else:
        print(3*x-11)


if __name__ == "__main__":
    main()
