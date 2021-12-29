#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:D最长最短单词.py
@time:2021/12/28
@software:PyCharm
"""


def main():
    strs=input()

    word=''
    maxlenword=''
    minlenword='sssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss'

    for s in strs:
        if s in [' ',',']:
            if len(word)>len(maxlenword):
                maxlenword=word
            if len(word)<len(minlenword):
                minlenword=word
            word=''
        else:
            word+=s
    print(maxlenword)
    print(minlenword)





if __name__ == '__main__':
    main()
