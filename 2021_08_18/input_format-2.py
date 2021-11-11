# -*- coding = utf-8 -*-
# @Time : 2021/8/18 8:13
# @Author : 陈凡亮
# @File : input_format-2.py
# @Software : PyCharm

def main():
    while True:
        try:
            a,b=input().split()
            print(int(a)+int(b))
        except:
            break


if __name__ == "__main__":
    main()
