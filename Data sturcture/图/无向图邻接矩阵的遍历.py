#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:无向图邻接矩阵的遍历.py
@time:2022/01/07
@software:PyCharm
"""


class graphMatrix:
    def __init__(self):
        self.dict = {}  # 结点对应矩阵下标的字典
        self.length = 0  # 矩阵的长度
        self.matrix = []

    # 添加节点
    def addVertex(self, key):
        self.dict[key] = self.length  # 键(顶点名称)->值(在矩阵中的下标)
        self.dict[self.length] = key  # 键(在矩阵中的下标)->值(顶点名称)

        lst = []
        for i in range(self.length):  # 创建一行长度为self.length,全是0的列表
            lst.append(0)
        self.matrix.append(lst)

        for row in self.matrix:  # 为矩阵中每行添加新的一个单元，单元中值为0
            row.append(0)

        self.length += 1

    # 添加无向边
    def addNoDirectLine(self, start, ends):  # 起始字符，终点(字符+权值)数组
        startIndex = self.dict[start]  # 起点在二维矩阵中的下标
        for row in ends:  # 遍历终点数组
            endKey = row[0]
            endIndex = self.dict[endKey]  # 终点在二维矩阵中的下标
            weight = row[1]
            self.matrix[startIndex][endIndex] = weight  # 权值赋值
            self.matrix[endIndex][startIndex] = weight

    # 无向图的深度优先遍历
    def DFS(self, index, lst, keyList=None):
        '''
        :param index: 邻接矩阵中的索引
        :param lst: 存储遍历结果的列表
        :param keyList: 已被遍历过的索引的集合
        :return: 无返回值，lst是目标结果
        '''
        # 1、如果当前已被遍历过的索引集合为空，那么创建一个空列表
        if keyList == None:
            keyList = []

        # 2、如果当前遍历到的索引未被遍历过，则：
        if index not in keyList:
            # 2.1 将当前索引加入被遍历索引集合，索引的值加入遍历结果列表
            keyList.append(index)
            lst.append(self.dict[index])
            # 2.2 深度遍历，递归方式
            for i in range(self.length):
                if self.matrix[index][i] != 0 and i not in keyList:
                    self.DFS(i, lst, keyList)

    # 无向图的广度优先遍历子方法
    def cBFS(self,index,lst,keyList):
        childList = []
        for i in range(self.length):
            if self.matrix[index][i] != 0 and i not in keyList:
                keyList.append(i)
                lst.append(self.dict[i])
                childList.append(i)
        for j in childList:
            self.cBFS(j,lst,keyList)

    # 无向图的广度优先遍历
    def BFS(self, index, lst, keyList=None):
        if keyList == None:
            keyList = []

        if index not in keyList:
            keyList.append(index)
            lst.append(self.dict[index])
            self.cBFS(index,lst,keyList)




def main():
    lst = ['A', 'B', 'C', 'D','E','F','G']

    lsta=[['C',1],['D',1],['B',1]]

    lstc=[['E',1],['F',1]]
    lstd=[['G',1]]

    gm = graphMatrix()
    for k in lst:
        gm.addVertex(k)

    print(gm.dict)
    #print(gm.matrix)

    gm.addNoDirectLine(lst[0], lsta)
    gm.addNoDirectLine(lst[2], lstc)
    gm.addNoDirectLine(lst[3], lstd)
    print('\n')
    for i in range(len(gm.matrix)):
        if i == 0:
            print('    ', end='')
            for k in lst:
                print(k, end=' ')
            print('')
        print(gm.dict[i], gm.matrix[i])

    red=[]
    gm.DFS(0,red)
    print('DFS:',red)

    reb=[]
    gm.BFS(0,reb)
    print('BFS:',reb)



if __name__ == '__main__':
    main()
