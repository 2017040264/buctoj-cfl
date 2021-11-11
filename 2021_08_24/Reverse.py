# -*- coding = utf-8 -*-
# @Time : 2021/8/24 8:14
# @Author : 陈凡亮
# @File : Reverse.py
# @Software : PyCharm

def main():
    lista=input().split()
    lista.reverse()
    s=''
    for i in range(len(lista)):
        s+=lista[i]+' '
    print(s.strip())


if __name__ == "__main__":
    main()
