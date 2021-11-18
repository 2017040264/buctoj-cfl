#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:销售排行榜.py
@time:2021/11/11
@software:PyCharm
"""
import sys

def main():
    dicta = dict()
    listb=[]
    for line in sys.stdin:
        listc=line.split()
        listb.append(listc)
    #print(listb)

    for lista in listb:
        if lista[0] not in dicta.keys():
            dicta[lista[0]]=[int(lista[1]),int(lista[1])*int(lista[2])]
        else:
            out=dicta[lista[0]]
            out[0]+=int(lista[1])
            out[1]+=int(lista[1])*int(lista[2])
            dicta[lista[0]]=out
    #print(dicta)
    listb=[(v[0],k,v[1]) for k,v in dicta.items()]
    #print(listb)

    listb.sort(key=lambda x :(-x[0],x[1]))
    for li in listb:
        print(li[1],li[0],li[2])

"""
apple 1 20 2014-4-2 
basketball 1 20 2014-4-2
computer 4 20 2014-4-2
shoe 1 20 2014-4-2
tv 1 20 2014-4-2
apple 1 18 2014-4-3 
"""



if __name__ == '__main__':
    main()
