#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:Graphmatrix.py
@time:2022/01/06
@software:PyCharm
"""

class graphMatrix:
    def __init__(self):
        self.dict={}  # 结点对应矩阵下标的字典
        self.length=0 # 矩阵的长度
        self.matrix=[]

    # 添加节点
    def addVertex(self,key):
        self.dict[key]=self.length # 键(顶点名称)->值(在矩阵中的下标)
        self.dict[self.length]=key # 键(在矩阵中的下标)->值(顶点名称)


        lst=[]
        for i in range(self.length):  # 创建一行长度为self.length,全是0的列表
            lst.append(0)
        self.matrix.append(lst)

        for row in self.matrix:  # 为矩阵中每行添加新的一个单元，单元中值为0
            row.append(0)

        self.length += 1

    # 添加无向边
    def addNoDirectLine(self,start,ends): #起始字符，终点(字符+权值)数组
        startIndex=self.dict[start] # 起点在二维矩阵中的下标
        for row in ends:  # 遍历终点数组
            endKey=row[0]
            endIndex=self.dict[endKey]  # 终点在二维矩阵中的下标
            weight=row[1]
            self.matrix[startIndex][endIndex]=weight  # 权值赋值
            self.matrix[endIndex][startIndex]=weight

    # 添加有向边
    def addDirectLine(self,start,ends):
        startIndex=self.dict[start] # 起点在二维矩阵中的下标
        for row in ends:  # 遍历终点数组
            endKey=row[0]
            endIndex=self.dict[endKey]  # 终点在二维矩阵中的下标
            weight=row[1]
            self.matrix[startIndex][endIndex]=weight  # 权值赋值




def main():

    lst=['北京','天津','郑州','青岛']

    statr1='北京'
    ends1=[['天津',138],['郑州',689]]

    statr2='天津'
    ends2=[['郑州',700],['青岛',597]]

    statr3='郑州'
    ends3=[['青岛',725]]

    gm=graphMatrix()
    for k in lst:
        gm.addVertex(k)

    print(gm.dict)
    print(gm.matrix)

    gm.addNoDirectLine(statr1,ends1)
    gm.addNoDirectLine(statr2, ends2)
    gm.addNoDirectLine(statr3, ends3)
    print('\n')
    for i in range(len(gm.matrix)):
        if i==0:
            print('    ',end='')
            for k in lst:
                print(k,end=' ')
            print('')
        print(gm.dict[i],gm.matrix[i])



if __name__ == '__main__':
    main()
