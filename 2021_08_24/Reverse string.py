# -*- coding = utf-8 -*-
# @Time : 2021/8/24 8:24
# @Author : 陈凡亮
# @File : Reverse string.py
# @Software : PyCharm

def main():
    ss= input()
    lista=[]
    for s in ss:
        lista.append(str(s))
    lista.reverse()
    #print(lista)
    rs = ''
    for i in range(len(lista)):
        rs += lista[i]
    print(rs.strip())


if __name__ == "__main__":
    main()
