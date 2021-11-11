# -*- coding = utf-8 -*-
# @Time : 2021/8/24 8:18
# @Author : 陈凡亮
# @File : Matrix transpose.py
# @Software : PyCharm

def main():
    lista=input().split()
    listb = input().split()
    listc = input().split()
    a=[]
    b=[]
    c=[]

    a.append(lista[0])
    a.append(listb[0])
    a.append(listc[0])

    b.append(lista[1])
    b.append(listb[1])
    b.append(listc[1])

    c.append(lista[2])
    c.append(listb[2])
    c.append(listc[2])

    s=''
    ss=''
    sss=''
    for i in range(3):
        s+=a[i]+' '
        ss+=b[i]+' '
        sss+=c[i]+' '
    print(s.strip())
    print(ss.strip())
    print(sss.strip())


if __name__ == "__main__":
    main()
