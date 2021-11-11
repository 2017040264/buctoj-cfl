# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:37
# @Author : 陈凡亮
# @File : Minimum currency payment problem.py
# @Software : PyCharm

def main():
    n=int(input())
    for i in range(n):
        money=int(input())
        lista=[]

        temp=money//100
        lista.append(temp)
        money=money-temp*100

        temp=money//50
        lista.append(temp)
        money=money-temp*50

        temp=money//20
        lista.append(temp)
        money=money-temp*20

        temp=money//10
        lista.append(temp)
        money=money-temp*10

        temp=money//5
        lista.append(temp)
        money=money-temp*5

        temp=money//2
        lista.append(temp)
        money=money-temp*2

        lista.append(money)

        lista.reverse()

        s=''
        for li in lista:
            s+=str(li)+' '
        print(s.strip())


if __name__ == "__main__":
    main()
