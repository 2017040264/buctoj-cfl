# -*- coding = utf-8 -*-
# @Time : 2021/8/24 8:08
# @Author : 陈凡亮
# @File : Is prime.py
# @Software : PyCharm

def main():
    n=int(input())
    flag=1
    for i in range(2,n//2):
        if n%i==0:
            flag=0
            break
    if flag==1:
        print("prime")
    else:
        print("not prime")



if __name__ == "__main__":
    main()
