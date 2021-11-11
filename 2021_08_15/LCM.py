# -*- coding = utf-8 -*-
# @Time : 2021/6/29 16:20
# @Author : 陈凡亮
# @File : LCM.py
# @Software : PyCharm

def main():
    m=int(input())

    lista=input().split()
    listb=[]

    for i in range(m):
        listb.append(int(lista[i]))

    samll=min(listb)
    listb.remove(samll)
    #print(listb,'最小值为：',samll)
    lcm=samll*listb[0]
    s=lcm
    # print('lcm=',lcm,'s=',s)
    for b in listb:
        if b==samll:
            pass
           # print(b,'等于最小值，忽略')

        elif b%samll==0:
           # print(b,'是最小值的倍数，最小公倍数为s=',b)
            s = b
        else :

            s = samll*b
            #print(b, '不等于b,也不能整除b，s=',s)

        if s < lcm:
            lcm=s


    print(lcm)

if __name__ == "__main__":
    main()
