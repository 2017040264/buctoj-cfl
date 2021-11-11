# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:10
# @Author : 陈凡亮
# @File : Daffodil.py
# @Software : PyCharm

def main():
    n=int(input())

    a=n//100
    b=n//10%10
    c=n%10

    if a*a*a+b*b*b+c*c*c==n:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
