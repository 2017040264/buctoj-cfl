#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:二叉排序树的按层遍历.py
@time:2022/01/04
@software:PyCharm
"""

from treeNode import sortTree

def main():

    # 二叉排序树
    sTree=sortTree()
    for i in [10, 6, 15, 9, 3, 13, 7, 16, 8]:
        sTree.add(i)

    root=sTree.root
    lst1=[root]
    lst2=[]
    for i in range(sTree.length):
        for item in lst1:
            print(item.data,end=' ')
            if item.left!=None:
                lst2.append(item.left)
            if item.right!=None:
                lst2.append(item.right)
        print('')

        if len(lst2)>0:
            lst1.clear()
            lst1=lst2.copy()
            lst2.clear()
        else:
            break


if __name__ == '__main__':
    main()
