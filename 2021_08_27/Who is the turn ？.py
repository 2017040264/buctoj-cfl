# -*- coding = utf-8 -*-
# @Time : 2021/8/27 9:08
# @Author : 陈凡亮
# @File : Who is the turn ？.py
# @Software : PyCharm

def main():
    while True:
        try:
            a,b=input().split()
            a,b=max(int(a),int(b)),min(int(a),int(b))

            if a<=10 and b <10:

                if (a+b)//2%2==0:
                    print("A")
                else:
                    print("B")

            else:
                if a-b>=2:
                    print("Game Over")
                else:
                    if (a+b)%2==0:
                        print("A")
                    else: print("B")

        except:
            break


if __name__ == "__main__":
    main()
