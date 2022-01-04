#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@author:cfl
@file:treeNode.py
@time:2021/12/29
@software:PyCharm
"""
from collections import deque

# 二叉排序树结点
class treeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# 二叉排序树
class sortTree:
    def __init__(self):
        self.root = None
        self.length = 0  # 结点的数量

    def addNode(self, oldnode,node):
        if node.data < oldnode.data:
            if oldnode.left != None:
               self.addNode(oldnode.left,node)
            else:
                oldnode.left = node
        else:
            if oldnode.right != None:
                self.addNode(oldnode.right,node)
            else:
                oldnode.right = node

    def add(self, data):
        tnode = treeNode(data)
        if self.root != None:
            self.addNode(self.root,tnode)
        else:
            self.root = tnode

        self.length += 1

    def recursivePreOrder(self, node, lst):
        lst.append(node.data)
        if node.left != None:
            self.recursivePreOrder(node.left, lst)
        if node.right != None:
            self.recursivePreOrder(node.right, lst)

    def recursiveInOrder(self, node, lst):
        if node.left != None:
            self.recursiveInOrder(node.left, lst)
        lst.append(node.data)
        if node.right != None:
            self.recursiveInOrder(node.right, lst)

    def recursivePostOrder(self, node, lst):
        if node.left != None:
            self.recursivePostOrder(node.left, lst)

        if node.right != None:
            self.recursivePostOrder(node.right, lst)
        lst.append(node.data)

    def Preorder(self):
        lst = []
        node = self.root
        self.recursivePreOrder(node, lst)
        return lst

    def InOrder(self):
        lst = []
        node = self.root
        self.recursiveInOrder(node,lst)
        return lst

    def PostOrder(self):
        lst = []
        node = self.root
        self.recursivePostOrder(node,lst)
        return lst

    def levelTraverse(self):
        lst=[]
        nodeList=deque()

        if self.root!=None:
            nodeList.append(self.root)

        while nodeList:
            popnode=nodeList.popleft()
            lst.append(popnode.data)
            if popnode.left!=None:
                nodeList.append(popnode.left)
            if popnode.right!=None:
                nodeList.append(popnode.right)
        return lst


def main():
    sTree = sortTree()
    for i in [10, 6, 15, 9, 3, 13, 7, 16, 8]:
        sTree.add(i)
    # 前序遍历
    print('\n 二叉树的深度优先遍历：')
    print('***************************')
    print('\n 先序遍历:')
    print(sTree.Preorder())

    print('\n 中序遍历')
    print(sTree.InOrder())

    print('\n 后序遍历')
    print(sTree.PostOrder())
    print('***************************')
    print('\n 二叉树的广度优先遍历')
    print(sTree.levelTraverse())


if __name__ == '__main__':
    main()
