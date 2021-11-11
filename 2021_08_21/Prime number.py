# -*- coding = utf-8 -*-
# @Time : 2021/8/21 9:34
# @Author : 陈凡亮
# @File : Prime number.py
# @Software : PyCharm

def main():
    n= int(input())
    lista=[2,3,5,7]

    for i in range(10,n+1):
        flag=0
        for li in lista:
            if i%li==0:
                flag=1
                break
        if flag==0:
            lista.append(i)

    for li in lista:
        print(li)


if __name__ == "__main__":
    main()
