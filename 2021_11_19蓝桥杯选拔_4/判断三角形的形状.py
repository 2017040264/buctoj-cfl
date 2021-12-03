#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:判断三角形的形状.py
@time:2021/11/19
@software:PyCharm
"""


def main():
    while True:
        try:

            a,b,c=map(int,input().split())
            lista = [a, b, c]
            lista.sort()
            if lista[2]-lista[0]<lista[1] and lista[0]+lista[1]>lista[2]:
                if a==b==c:
                    print("DB")
                elif a==b or a==c or b==c:
                    print('DY')
                else:
                    if lista[0]**2+lista[1]**2==lista[2]**2:
                        print('ZJ')
                    else:
                        print("PT")
            else:
                print('ERROR')
        except:
            break




if __name__ == '__main__':
    main()
