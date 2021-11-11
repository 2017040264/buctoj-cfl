# -*- coding = utf-8 -*-
# @Time : 2021/8/21 8:58
# @Author : 陈凡亮
# @File : Free fall.py
# @Software : PyCharm

def main():
    m,n=input().split()
    m=float(m)
    n=int(n)
    temp=m
    sum=0
    for i in range(n):
        if i==0:
            sum+=temp
        else:
            sum+=m*2
        m=m/2
        #print(m)

    # ss=0
    # while(m<temp):
    #     m*=2
    #     ss+=m
    # print(ss+temp)


    print("{:.2f} {:.2f}".format(m,sum))


if __name__ == "__main__":
    main()
