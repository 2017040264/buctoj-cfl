# -*- coding = utf-8 -*-
# @Time : 2021/8/18 9:21
# @Author : 陈凡亮
# @File : the sum of factorials.py
# @Software : PyCharm

def main():
    n=int(input())
    sum=0
    for i in range(1,n+1):
        temp=1
        for j in range(1,i+1):
            temp*=j

        sum+=temp
    print(sum)



if __name__ == "__main__":
    main()
