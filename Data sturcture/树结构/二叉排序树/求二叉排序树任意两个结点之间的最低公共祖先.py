#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:求二叉排序树任意两个结点之间的最低公共祖先.py
@time:2022/01/05
@software:PyCharm
"""

from treeNode import sortTree

# 寻找值对应的结点，把途径的结点值放到列表中
def lookup(tree,v):
    lst=[]
    node=tree.root
    for i in range(tree.length):
        lst.append(node)
        if v<node.data:           # 向左查找
            if node.left!=None:
                node=node.left
            else:
                return None
        elif v>node.data:
            if node.right!=None:
                node=node.right
            else:
                return None
        else:
            return lst

def main():
    sTree=sortTree()
    for i in [10, 6, 15, 9, 3, 13, 7, 16, 8]:
        sTree.add(i)

    lst1=lookup(sTree,8)
    lst2=lookup(sTree,13)
    try:
        commonNode=None
        for i in range(min(len(lst1),len(lst2))):
            if lst1[i]!=lst2[i]:
                break
            commonNode=lst1[i]
        if commonNode!=None:
            print('最低共同祖先：',commonNode.data)
        else:
            # 不在同一个树上才会找不到最低共同祖先
            print('找不到最低共同祖先')
    except:
        print('请确认要查找的值是否在二叉排序树中')


if __name__ == '__main__':
    main()
