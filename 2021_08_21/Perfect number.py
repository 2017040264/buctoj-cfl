# -*- coding = utf-8 -*-
# @Time : 2021/8/21 8:47
# @Author : 陈凡亮
# @File : Perfect number.py
# @Software : PyCharm

def main():
    n= int(input())
    for i in range(1,n+1):
        sum=0
        lista=[]
        for j in range(1,i):
            if i%j==0:
                sum+=j
                lista.append(j)

        if sum==i:
            result=str(i)+" its factors are"
            for li in lista:
                result+=" "+str(li)
            print(result)



if __name__ == "__main__":
    main()
