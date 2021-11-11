# -*- coding = utf-8 -*-
# @Time : 2021/8/27 8:17
# @Author : 陈凡亮
# @File : Division.py
# @Software : PyCharm

def main():

    while True:
        try:
            a, b = input().split()
            a, b = int(a),int(b)
            if b==0:
                print("error")
            else:
                re=a/b*10//1/10
                # print(a/b*10//1/10)

                st=str(re)
                index=st.index('.')
                aa=st[:index]
                bb=st[index+1:]
                # print('aa=',aa)
                # print('bb=',bb)
                aa,bb=int(aa),int(bb)
                if bb>=5:
                    print(aa+1)
                else:print(aa)

                # lista=str(re).split('.')
                # lista.reverse()
                # print(lista)
                #
                # if int(lista[1])>=5:
                #     print(int(lista[0])+1)
                # else:
                #     print(int(lista[0]))


        except:
            break

if __name__ == "__main__":
    main()
