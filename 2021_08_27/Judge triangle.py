# -*- coding = utf-8 -*-
# @Time : 2021/8/27 8:01
# @Author : 陈凡亮
# @File : Judge triangle.py
# @Software : PyCharm

def main():
    while True:
        try:
            lista=input().split()
            for i in range(len(lista)):
                lista[i]=int(lista[i])
            lista.sort()
            a=lista[0]
            b=lista[1]
            c=lista[2]
            if a+b<=c:
                print('ERROR')
            elif a==b==c:
                print("DB")
            elif a==b  or b==c:
                print("DY")
            elif a*a+b*b==c*c:
                print("ZJ")
            elif a+b>c:
                print("PT")

        except:
            break


if __name__ == "__main__":
    main()
