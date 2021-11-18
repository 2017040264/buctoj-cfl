#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:最大乘积.py
@time:2021/11/11
@software:PyCharm
"""


def main():
    while True:
        try:
            n=int(input())
            lista=input().split()

            listc=[] # 存储负数的位置
            for i in range(len(lista)):
                lista[i]=int(lista[i])
                if lista[i]< 0 :
                    listc.append(i)
            maxre=1
            listb = []

            if len(listc)%2==0:# 偶数个负数
                #print('偶数个负数')
                for li in lista:
                    if li == 0:
                        listb.append(maxre)
                        maxre=1
                    else:
                        maxre=maxre*li
                listb.append(maxre)
            else: # 奇数个负数
                if len(lista)==1:
                    print(-1)
                    continue
                # 求第一个负数位置和最后一个负数位置
                fist_index=listc[0]
                last_index=listc[-1]
                maxre=1
                for i in range(last_index):
                    if lista[i]==0:
                        listb.append(maxre)
                        maxre=1
                    else:
                        maxre=maxre*lista[i]
                listb.append(maxre)

                maxre=1
                for i in range(fist_index+1,len(lista)):
                    if lista[i]==0:
                        listb.append(maxre)
                        maxre=1
                    else:
                        maxre=maxre*lista[i]
                listb.append(maxre)

            print(max(listb))

        except:
            break


if __name__ == '__main__':
    main()
