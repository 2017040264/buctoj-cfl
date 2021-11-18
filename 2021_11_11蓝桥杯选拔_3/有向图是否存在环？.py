#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:有向图是否存在环？.py
@time:2021/11/11
@software:PyCharm
"""

# 拓扑排序

def main():
    while True:
        n,m=map(int,input().split())
        if m==0 and n==0:
            return 0


        lista_in=[0]*(n+1) # 入度

        # 所有的边
        listb=[]

        # 用列表表示队列
        listc=[]

        for i in range(m):
            u,v=map(int,input().split())
            lista_in[v]+=1

            listb.append([u,v])

        # 将所有 度为0 的节点入队列
        for i in range(1,len(lista_in)):
            if lista_in[i]==0:
                listc.append(i)

        seta=set(listc)

        while len(listc):

            #print(listc,seta)

            first=listc.pop(0)
            lista_in = [0 for i in range(n + 1)]  # 入度
            for i in range(len(listb)):
                if listb[i][0]==first:
                    listb[i]=[0,0]
                lista_in[listb[i][1]]+=1

            # 将所有 度为 0 的节点入队列
            for i in range(1, len(lista_in)):
                if lista_in[i] == 0 and i not in seta:
                    listc.append(i)
                    seta.add(i)




        if len(seta)<n:
            print("YES")
        else:print("NO")

"""
11 10
1 2
2 3
4 3
5 4
6 5
3 9
10 9
9 11
7 8
8 11
"""

if __name__ == '__main__':
    main()
