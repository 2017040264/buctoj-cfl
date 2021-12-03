#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:Poker Game.py
@time:2021/11/19
@software:PyCharm
"""

from collections import  Counter

# 字母相同返回1
def color(lista):
    for i in range(4):
        if lista[1][i] != lista[1][i + 1]:
            return 0
    return 1

# 数字连续返回-1
# 4个数字相同返回-2
# 有1对，返回-3
def diglian(lista):
     listb=lista[0]
     listb.sort()
     dicta=Counter(listb)
     difflen=len(dicta)
     # 5个各不同
     if difflen==5:
         if listb[0]+4==listb[-1]:
             return -1
         else:
             return -10
     # 有1对
     elif difflen==4:
         return -3
     elif difflen=3:



     return 1

#




def main():

    while True:
        try:
            lista=input().split()
            la=lista[:5]
            lb=lista[5:]
            laa=[[],[]]
            lbb=[[],[]]
            for i in range(5):
                if la[i][0]=='T':
                    laa[0].append(10)
                elif la[i][0]=='J':
                    laa[0].append(11)
                elif la[i][0]=='Q':
                    laa[0].append(12)
                elif la[i][0]=='K':
                    laa[0].append(13)
                elif la[i][0]=='A':
                    laa[0].append(14)
                else:
                    laa[0].append(int(la[i][0]))

                if lb[i][0]=='T':
                    lbb[0].append(10)
                elif lb[i][0]=='J':
                    lbb[0].append(11)
                elif lb[i][0]=='Q':
                    lbb[0].append(12)
                elif lb[i][0]=='K':
                    lbb[0].append(13)
                elif lb[i][0]=='A':
                    lbb[0].append(14)
                else:
                    lbb[0].append(int(lb[i][0]))

                #laa[0].append(la[i][0])
                laa[1].append(la[i][1])
                #lbb[0].append(lb[i][0])
                lbb[1].append(lb[i][1])

            print(laa,lbb)
        except:
            break


if __name__ == '__main__':
    main()
