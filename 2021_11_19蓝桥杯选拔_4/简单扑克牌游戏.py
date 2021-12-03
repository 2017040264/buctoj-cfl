#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:简单扑克牌游戏.py
@time:2021/11/19
@software:PyCharm
"""


def main():

    # 同色返回1 ；
    def color(lista):

        for i in range(2):
            if lista[1][i]!=lista[1][i+1]:
                return 0
        return 1

    # 数字连续返回-1;3张牌数字相同返回-2;2张相同返回相同的数；其他返回0
    def dig(lista):
        listb=lista[0]
        listb.sort()

        if listb[0]+1==listb[1] and listb[1]+1==listb[2]:
            return -1
        elif listb[0]==listb[1]==listb[2]:
            return -2
        elif listb[0]==listb[1] or listb[0]==listb[2]:
            return listb[0]
        elif listb[1]==listb[2]:
            return listb[1]
        else:
            return 0


    while True:
        try:
            lista=input().split()
            la=lista[:3]
            lb=lista[3:]
            laa=[[],[]]
            lbb=[[],[]]
            for i in range(3):
                laa[0].append(int(la[i][0]))
                laa[1].append(la[i][1])
                lbb[0].append(int(lb[i][0]))
                lbb[1].append(lb[i][1])
                # la[i]=[la[i][0],la[i][1]]
                # lb[i] = [lb[i][0], lb[i][1]]
            #print(laa,lbb)

            coa,cob=color(laa),color(lbb)
            #print(coa,cob)

            dia,dib=dig(laa),dig(lbb)
            #print(dia,dib)

            # 同花顺
            if color(laa)==1 and dig(laa)==-1:
                if color(lbb)==1 and dig(lbb)==-1:
                    if max(laa[0])>max(lbb[0]):
                        print('zhangsan')
                    elif max(laa[0])==max(lbb[0]):
                        print('tie')
                    else:
                        print('lisi')
                else:
                    print('zhangsan')
            # 顺子
            elif dig(laa)==-1 and color(laa)==0:
                if color(lbb)==1 and dig(lbb)==-1:
                    print('lisi')
                elif dig(lbb)==-1 and color(lbb)==0:
                    if max(laa[0])>max(lbb[0]):
                        print('zhangsan')
                    elif max(laa[0])==max(lbb[0]):
                        print('tie')
                    else:
                        print('lisi')
                else:
                    print('zhangsan')
            # 飞机
            elif dig(laa)==-2:
                if color(lbb)==1 and dig(lbb)==-1:
                    print('lisi')
                elif dig(lbb)==-1 and color(lbb)==0:
                    print('lisi')
                elif dig(lbb)==-2:
                    if max(laa[0])>max(lbb[0]):
                        print('zhangsan')
                    elif max(laa[0])==max(lbb[0]):
                        print('tie')
                    else:
                        print('lisi')
                else:
                    print('zhangsan')
            # 同花
            elif color(laa)==1:
                if color(lbb)==1 and dig(lbb)==-1:
                    print('lisi')
                elif dig(lbb)==-1 and color(lbb)==0:
                    print('lisi')
                elif dig(lbb)==-2:
                    print('lisi')
                elif color(lbb)==1:
                    if max(laa[0])>max(lbb[0]):
                        print('zhangsan')
                    elif max(laa[0])==max(lbb[0]):
                        print('tie')
                    else:
                        print('lisi')
                else:
                    print('zhangsan')
            # 对子
            elif 0<dig(laa)<=9:
                if color(lbb)==1 and dig(lbb)==-1:
                    print('lisi')
                elif dig(lbb)==-1 and color(lbb)==0:
                    print('lisi')
                elif dig(lbb)==-2:
                    print('lisi')
                elif color(lbb)==1:
                    print('lisi')
                elif 0<dig(lbb)<10:
                    if dig(laa)>dig(lbb):
                        print("zahngsan")
                    elif dig(lbb)==dig(laa):
                        print('tie')
                    else:
                        print('lisi')
                else:
                    print('zhangsan')
            # 杂牌
            else:
                if max(laa[0]) > max(lbb[0]):
                    print('zhangsan')
                elif max(laa[0]) == max(lbb[0]):
                    print('tie')
                else:
                    print('lisi')

        except:
            break




if __name__ == '__main__':
    main()
