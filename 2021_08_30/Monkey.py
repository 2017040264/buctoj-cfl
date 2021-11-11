# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:00
# @Author : 陈凡亮
# @File : Monkey.py
# @Software : PyCharm

def main():
    n=int(input())
    re=1
    for i in range(n-1):
        re=(re+1)*2
    print(re)


if __name__ == "__main__":
    main()
