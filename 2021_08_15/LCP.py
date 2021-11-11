# -*- coding = utf-8 -*-
# @Time : 2021/7/1 14:39
# @Author : 陈凡亮
# @File : LCP.py
# @Software : PyCharm

def findpath(n, relation, k, path, lista):
    print('k=',k)
    if k == 0:
        return 0

    start = path[-1]
    for rela in relation:

        if rela[0] == start:
            print(rela)
            path.append(rela[-1])
            if rela[1] == n - 1 and len(path) == k + 1:
                lista.append(path)
            else:
                findpath(n, relation, k - 1, path, lista)

def numWays(n, relation, k):

    lista = []  # 存储所有的路径方案
    listb = [0]  # 单条路径方案，中间存储器

    # 从指定点0到指定点n-1，并且可以有环，限定步数为k
    findpath(n, relation, k, listb, lista)
    print(lista)
    return len(lista)

def main():
    n = 5
    relation=[[0,2],[2,1],[3,4],[2,3],[1,4],[2,0],[0,4]]
    k = 3
    lenth=numWays(n,relation,k)
    print(lenth)


if __name__ == "__main__":
    main()
