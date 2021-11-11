# -*- coding = utf-8 -*-
# @Time : 2021/8/30 8:43
# @Author : 陈凡亮
# @File : factorial 0s number.py
# @Software : PyCharm

def main():
    while True:
        try:
            n=int(input())
            if n==0:
                print(0)
            else:
                jc = 1
                for i in range(1,n+1):
                    jc=jc*i
                print(jc)
                st= str(jc)
                lista=[]
                for s in st:
                    lista.append(int(s))
                lista.reverse()
                count=0
                for li in lista:
                    if li!=0:
                        break
                    else:
                        count+=1
                print(count)

        except:
            break

def getn():
    while True:
        try:
            n=int(input())
            re=0
            while n>=5:

                n=n//5
                re+=n

            print(re)

        except:
            break

if __name__ == "__main__":
    #main()
    getn()
