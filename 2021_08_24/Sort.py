# -*- coding = utf-8 -*-
# @Time : 2021/8/24 8:11
# @Author : 陈凡亮
# @File : Sort.py
# @Software : PyCharm

def main():
    lista=input().split()

    for i in range(len(lista)):
        lista[i]=int(lista[i])
    lista.sort()
    for i in range(len(lista)):
        print(lista[i])


if __name__ == "__main__":
    main()
