# -*- coding = utf-8 -*-
# @Time : 2021/8/18 8:19
# @Author : 陈凡亮
# @File : input_format-4.py
# @Software : PyCharm

def main():
    n=int(input())
    for i in range(n):

        s = input().split()
        sum=0
        for j in range(1,int(s[0])+1):
            sum+=int(s[j])
        print(sum)




if __name__ == "__main__":
    main()
