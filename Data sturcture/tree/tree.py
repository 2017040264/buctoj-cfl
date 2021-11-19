#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:tree.py
@time:2021/11/18
@software:PyCharm
"""
from graphviz import  Digraph
import uuid
from random import  sample

class TreeNode(object):

    # 初始化节点
    def __init__(self,data=None,left=None,right=None):
        self.data= data
        self.left=left
        self.right=right
        #self.dot=Digraph(comment='Binary Tree')


class BTree(object):

    def __init__(self,root=None):
        self.root=root

    def add(self,data):
        node=TreeNode(data)
        # 如果树是空的，则对根节点赋值
        if self.root==None:
            self.root=node
        else:
            queue=[]
            queue.append(self.root)
            # 对已有的节点进行层次遍历
            while queue:
                # 弹出队列的第一个元素
                cur=queue.pop(0)
                if cur.left==None:
                    cur.left=node
                    return
                elif cur.right==None:
                    cur.right=node
                    return
                else:
                    # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.left)
                    queue.append(cur.right)

    # 前序遍历
    def preorder(self, root):
        if root == None:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    # 中序遍历
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    # 后续遍历
    def postorder(self,root):
        if root==None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)

    # 层序遍历
    def bfs(self,root):
        if root==None:
            return
        queue=[]
        queue.append(root)
        while queue:
            node=queue.pop(0)
            print(node.data)
            if node.left!=None:
                queue.append(node.left)
            if node.right!=None:
                queue.append(node.right)


def main():
    tree = BTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    print('先序遍历\n')
    tree.preorder(tree.root)
    print('中序遍历\n')
    tree.inorder(tree.root)
    print('后序遍历\n')
    tree.postorder(tree.root)
    print('层序遍历\n')
    tree.bfs(tree.root)


if __name__ == '__main__':
    main()
