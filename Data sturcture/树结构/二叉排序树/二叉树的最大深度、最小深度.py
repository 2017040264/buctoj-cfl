#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:二叉树的最大深度、最小深度.py
@time:2022/01/05
@software:PyCharm
"""
from treeNode import sortTree

def main():
    # 二叉排序树
    sTree = sortTree()
    for i in [10, 6, 15, 9, 3, 13, 7, 16, 8]:
        sTree.add(i)

    root = sTree.root
    lst1=[root]
    lst2=[]

    minLayer=0
    maxLayer=0
    k=1

    for i in range(sTree.length):
        flga=0  # flga=0表示node无后续结点（叶子结点）
        for node in lst1:
            if node.left!=None:
                flga=1
                lst2.append(node.left)
            if node.right!=None:
                flga=1
                lst2.append(node.right)

            if minLayer==0 and flga==0: # 最小深度
                minLayer=k

        if len(lst2)==0: # 最大深度
            maxLayer=k
            break

        k+=1
        lst1.clear()
        lst1=lst2.copy()
        lst2.clear()
    print('最小深度：',minLayer)
    print('最大深度：',maxLayer)


if __name__ == '__main__':
    main()
