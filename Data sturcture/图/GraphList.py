#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:GraphList.py
@time:2022/01/06
@software:PyCharm
"""

class graphList:
    def __init__(self):
        self.dict={}  # 顶点名为键，链表为值，链表中存储其它节点的名称和距离

    def addVertex(self,key):
        self.dict[key]=[]

    # 添加无向边
    def addNoDirectLine(self,start,ends):
        for row in ends:
            key=row[0]

            # 1. 在start的邻接表中追加新的边和权值
            lst=self.dict[start]

            flag=True  # 如果在此顶点的邻接表中找到此节点(已经存在)，flag将变为false,也可以用新的进行更新
            for k in lst:
                if k[0]==key:
                    flag=False

            if flag:
                self.dict[start].append(row) # 在邻接表中添加[顶点名称，距离]

            # 2. 在start顶点对应的key节点的邻接表中追加边和权值
            lst=self.dict[key]
            flag=True
            for k in lst:
                if k[0]==start:
                    flag=False
            if flag:
                weight=row[1]
                self.dict[key].append([start,weight])

    # 添加有向边
    def addDirectLine(self,start,ends):
        for row in ends:
            key=row[0]

            # 1.在start的邻接表中追加新的边和权值
            lst=self.dict[start]
            flag=True

            for k in lst:
                if k[0]==key:
                    flag=False

            if flag:
                self.dict[start].append(row)


def main():
    lst=['北京','天津','郑州','青岛']

    statr1='北京'
    ends1=[['天津',138],['郑州',689]]

    statr2='天津'
    ends2=[['郑州',700],['青岛',597]]

    statr3='郑州'
    ends3=[['青岛',725]]

    gl=graphList()
    for k in lst:
        gl.addVertex(k)

    print(gl.dict)

    gl.addNoDirectLine(statr1,ends1)
    gl.addNoDirectLine(statr2, ends2)
    gl.addNoDirectLine(statr3, ends3)

    print('\n')
    for key in gl.dict:
        print(key,'-->',gl.dict[key])


if __name__ == '__main__':
    main()
