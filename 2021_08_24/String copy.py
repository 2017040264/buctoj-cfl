# -*- coding = utf-8 -*-
# @Time : 2021/8/24 8:28
# @Author : 陈凡亮
# @File : String copy.py
# @Software : PyCharm

def main():
    s1=input()
    s2=''
    for s in s1:
        if str(s) in ['a','e','i','o','u']:
            s2+=str(s)
    print(s2)



if __name__ == "__main__":
    main()
