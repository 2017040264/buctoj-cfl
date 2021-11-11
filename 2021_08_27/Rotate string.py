# -*- coding = utf-8 -*-
# @Time : 2021/8/27 10:46
# @Author : 陈凡亮
# @File : Rotate string.py
# @Software : PyCharm

def main():
    while True:
        try:
            a,b=input().split()
            if len(a)!=len(b):
                print("No")
            else:

                lista=[]
                listb=[]

                for i in a:
                    lista.append(i)
                for i in b:
                    listb.append(i)
                flag=0
                for i in range(len(lista)+1):
                    if lista==listb:
                        flag=1
                        break
                    else:
                        temp=listb[0]
                        for j in range(len(listb)-1):
                            listb[j]=listb[j+1]
                        listb[-1]=temp

                if flag==1:
                    print("Yes")
                else:print('No')


        except:
            break


if __name__ == "__main__":
    main()
