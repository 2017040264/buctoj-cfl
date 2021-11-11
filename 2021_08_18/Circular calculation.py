# -*- coding = utf-8 -*-
# @Time : 2021/8/18 8:37
# @Author : 陈凡亮
# @File : Circular calculation.py
# @Software : PyCharm
import math

def main():
    # pi=math.pi
    pi=3.14
    print(pi)
    a,b=input().split()
    a=float(a)
    b=float(b)
    print(a,b)

    c1=2*pi*a
    sa=a*a*pi
    sb=4*a*a*pi
    va=4.0/3*a*a*a*pi
    vb=pi*a*a*b



    print("C1=",2*pi*a*100//1/100)
    print("Sa=",pi*a*a*100//1/100)
    print("Sb=",4*pi*a*a*100//1/100)
    print("Va=",4*pi*a*a*a/3*100//1/100)
    print("Vb=",pi*a*a*b*100//1/100)
    print("\n%%%%%%%%%%%%%%%%%%%\n")
    print("C1=",c1)
    print("Sa=",sa)
    print("Sb=",sb)
    print("Va=",va)
    print("Vb=",vb)



if __name__ == "__main__":
    main()
