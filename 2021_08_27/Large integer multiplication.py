# -*- coding = utf-8 -*-
# @Time : 2021/8/27 9:33
# @Author : 陈凡亮
# @File : Large integer multiplication.py
# @Software : PyCharm

def main():
    while True:
        try:
            a, b = input().split()
            s=int(a[-1])*int(b[-1])
            print(str(s)[-1])
        except:
            break


if __name__ == "__main__":
    main()
