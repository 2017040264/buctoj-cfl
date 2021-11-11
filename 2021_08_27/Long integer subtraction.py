# -*- coding = utf-8 -*-
# @Time : 2021/8/27 9:40
# @Author : 陈凡亮
# @File : Long integer subtraction.py
# @Software : PyCharm

def main():
    while True:
        try:
            a,b=input().split()
            a,b=max(int(a),int(b)),min(int(a),int(b))
            print(a-b)

        except:
            break


if __name__ == "__main__":
    main()
