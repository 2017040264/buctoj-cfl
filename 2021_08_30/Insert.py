# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:03
# @Author : 陈凡亮
# @File : Insert.py
# @Software : PyCharm

def main():
    lista=input().split()
    a=int(input())
    for i in range(len(lista)):
        lista[i]=int(lista[i])


    if lista[0]<lista[-1]:
        lista.append(a)
        lista.sort()
    else:
        lista.append(a)
        lista.sort(reverse=True)

    for i in range(len(lista)):
        print(lista[i])


if __name__ == "__main__":
    main()
