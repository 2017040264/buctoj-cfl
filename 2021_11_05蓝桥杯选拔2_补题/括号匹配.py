#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:括号匹配.py
@time:2021/11/10
@software:PyCharm
"""
def main():
    n=int(input())
    for i in range(n):
        strs=input()

        que=[strs]
        result=[]

        while len(que)>0:
            #print(que)
            q=que.pop(0)
            #print('que.pop',q)
            if len(q)>1:
                left=0
                leftbr=0
                rigtbr=0
                #print('长度大于1',q[left])
                if q[left]==')' or q[left]==']':
                   # print('右括号直接进列表')
                    que.append(q[left])
                    que.append(q[1:])
                elif q[left]=='(':
                    leftbr=1
                    #print('等于(')
                    left=1
                    while left<len(q):

                        if q[left]=='(':
                            leftbr+=1
                        elif q[left]==')':
                            rigtbr+=1

                        if leftbr==rigtbr:
                            break


                        left+=1
                    #print('( left=',left)
                    if left==len(q):
                        que.append(q[0])
                        que.append(q[1:])
                    elif left+1!=len(q):  # ([)
                        que.append(q[:left+1])
                        que.append(q[left+1:])
                    elif left+1==len(q):
                        #print("最右边")
                        if len(q)>2:
                            que.append(q[1:left])
                elif q[left]=='[':
                    #print("等于[")
                    left=1
                    leftbr = 1
                    while left<len(q):
                        if q[left] == '[':
                            leftbr += 1
                        elif q[left] == ']':
                            rigtbr += 1

                        if leftbr == rigtbr:
                            break
                        left+=1
                    #print('left=',left)
                    if left==len(q):
                        que.append(q[0])
                        que.append(q[1:])
                    elif left!=len(q)-1:
                        que.append(q[:left+1])
                        que.append(q[left+1:])
                    elif left+1==len(q):
                        if len(q)>2:
                            que.append(q[1:left])
            else:
                result.append(q)
        print(len(result))


if __name__ == '__main__':
    main()
