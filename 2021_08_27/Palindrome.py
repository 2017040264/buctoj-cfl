# -*- coding = utf-8 -*-
# @Time : 2021/8/27 8:12
# @Author : 陈凡亮
# @File : Palindrome.py
# @Software : PyCharm

def main():
    n=int(input())
    for i in range(n):
        st=input()
        flag=0
        for j in range(len(st)//2):
            if st[j]!=st[len(st)-1-j]:
                flag=1
                break
        if flag==1:
            print("NO")
        else:
            print("YES")



if __name__ == "__main__":
    main()
