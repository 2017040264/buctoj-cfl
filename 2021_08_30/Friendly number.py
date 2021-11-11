# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:21
# @Author : 陈凡亮
# @File : Friendly number.py
# @Software : PyCharm

def main():
    a,b=input().split()
    a,b=int(a),int(b)
    suma=1
    sumb=1
    for i in range(2,a//2+1):
        if a%i==0:
           # print(i)
            suma+=i
    #print("BBBBBBBBB")
    for i in range(2,b//2+1):
        if b%i==0:
            #print(i)
            sumb+=i

    if suma==b and sumb==a:
        print("yes")
    else:
        print('no')


if __name__ == "__main__":
    main()
