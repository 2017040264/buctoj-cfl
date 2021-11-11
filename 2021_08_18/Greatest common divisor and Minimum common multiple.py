# -*- coding = utf-8 -*-
# @Time : 2021/8/18 9:15
# @Author : 陈凡亮
# @File : Greatest common divisor and Minimum common multiple.py
# @Software : PyCharm

def main():
    a,b=input().split()
    a,b=max(int(a),int(b)),min(int(a),int(b))

    minnumber=a
    # 找最小公约数
    while(minnumber):
        if a%minnumber==0 and b%minnumber==0:
            break
        else:
            minnumber-=1

    maxnumber=b
    # 找最大公倍数
    while(maxnumber):
        if maxnumber%a==0 and maxnumber%b==0:
            break
        else:
            maxnumber+=1

    print(minnumber,maxnumber)




if __name__ == "__main__":
    main()
