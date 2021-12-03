#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:cfl
@file:单词分析.py
@time:2021/12/03
@software:PyCharm
"""


import os
import sys
from collections import Counter
# 请在此输入您的代码

aa=input()
lista=[]
for a in aa:
  lista.append(a)

dita=Counter(lista)

re=sorted(dita.items(),key=lambda x: (x[1],-ord(x[0])))

print(re[-1][0])
print(re[-1][1])
