# -*- coding = utf-8 -*-
# @Time : 2021/8/30 9:22
# @Author : 陈凡亮
# @File : Count down.py
# @Software : PyCharm

def main():
    n=int(input())
    lista=input().split()
    lista=lista[:n]
    number=[0,1,6,8,9]

    # 1. look beckward
    for i in range(n):
        aa=lista[i]
        listb=[]
        for a in aa:
            if a=='6':
                listb.append('9')
            elif a=='9':
                listb.append('6')
            else:
                listb.append(a)
        listb.reverse()
        ls=''
        for j in range(len(listb)):
            ls+=listb[j]
        lista[i]=int(ls)

    # 2. 确定 单调性, flag=1表示单调增
    flag=0
    if lista[0]<lista[-1]:
        flag=1

    # 3. 确定下一位数
    # 单调增
    if flag==1:
        # 一位数
        if len(str(lista[-1]))==1:
            listc=[]
            for p in [0,1,6,8,9]:
                if p>lista[-1]:
                    listc.append(p)
            if len(listc)==0:
                print("01")
            else:
                re=min(listc)
                if re==6:
                    print(9)
                elif re==9:
                    print(6)
                else:print(re)
        else:
            a=lista[-1]//10
            b=lista[-1]%10
            if number.index(b)==4: # 末尾是9
                re=number[number.index(a)+1]
                if re==6:
                    print('09')
                elif re==9:
                    print('06')
                else:
                    print('0'+str(re))
            else:
                aa=a*10+number[number.index(b)+1]
                listb = []

                for a in str(aa):
                    if a == '6':
                        listb.append('9')
                    elif a == '9':
                        listb.append('6')
                    else:
                        listb.append(a)
                listb.reverse()
                ls = ''
                for j in range(len(listb)):
                    ls += listb[j]
                print(int(ls))
    # 单调递减
    else:
        if len(str(lista[-1]))==1:
            re=number[number.index(lista[-1])-1]
            if re==6:
                print(9)
            else:
                print(re)
        else:
            a=lista[-1]//10
            b=lista[-1]%10
            if number.index(b)==0:
                a=number[number.index(a)-1]
                if a==6:
                    print('69')
                else:
                    print('6'+str(a))
            else:
                aa=a*10+number[number.index(b)-1]
                listb = []
                for a in str(aa):
                    if a == '6':
                        listb.append('9')
                    elif a == '9':
                        listb.append('6')
                    else:
                        listb.append(a)
                listb.reverse()
                ls = ''
                for j in range(len(listb)):
                    ls += listb[j]
                print(int(ls))


if __name__ == "__main__":
    main()


