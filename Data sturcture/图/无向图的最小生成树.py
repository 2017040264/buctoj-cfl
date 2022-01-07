#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:无向图的最小生成树.py
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

    # 无向图的最小生成树（需是连通图）
    def Prim(self,index,reachedVertexList=None,parents=None):
        '''
        :param index: 开始结点
        :param reachedVertexList: 已到达顶点列表
        :param parents: 每个已到达顶点列表的父顶点
        :return: reachedVertexList,parents
        '''
        if reachedVertexList==None:
            reachedVertexList=[]
            parents=[]
            # 把邻接矩阵中第0个顶点放入到已到达顶点列表，由于第0个顶点没有父顶点，parents放-1
            reachedVertexList.append(index)
            parents.append(-1)

        minweigt=0   # 最小权重
        minIndex=None # 最小权重对应的顶点在邻接矩阵中的下标
        pindex=None # 最小权重对应的顶点的父顶点

        # 寻找：从已到顶点出发，到未到顶点结束的最小权值的（边、出发顶点、到达顶点）
        for rindex in reachedVertexList:
            for i in range(self.length):
                if i not in reachedVertexList:
                    v=self.matrix[rindex][i]
                    if v>0:
                        if minweigt>0:
                            if minweigt>v:
                                minweigt=v
                                minIndex=i
                                pindex=rindex
                        else:
                            minweigt=v
                            minIndex=i
                            pindex=rindex
        if minIndex!=None:
            reachedVertexList.append(minIndex)
            parents.append(pindex)
            self.Prim(minIndex,reachedVertexList,parents)
        return reachedVertexList,parents

def main():
    lst = ['A', 'B', 'C', 'D', 'E']

    lsta = [['B', 3], ['E', 4]]
    lstb = [['C',1],['E',8]]
    lstc = [['D', 9]]
    lstd = [['E', 7]]

    gm = graphMatrix()
    for k in lst:
        gm.addVertex(k)

    print(gm.dict)
    # print(gm.matrix)

    gm.addNoDirectLine(lst[0], lsta)
    gm.addNoDirectLine(lst[1], lstb)
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

    print('************************')
    reach,pa=gm.Prim(0)
    print(pa)
    print(reach)

    for i in range(1,len(pa)):
        print('%s 连 %s '%(gm.dict[pa[i]],gm.dict[reach[i]]))


if __name__ == '__main__':
    main()
