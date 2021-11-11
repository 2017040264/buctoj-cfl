# -*- coding = utf-8 -*-
# @Time : 2021/8/30 10:17
# @Author : 陈凡亮
# @File : Full Permutation.py
# @Software : PyCharm

def printfunc(lista):
    s=''
    for i in range(len(lista)):
        s+=str(lista[i])+' '
    print(s.strip())


def main():
    while True:

        n=int(input())
        if n==0:
            break
        elif n==1:
            print(1)
        else:
            lista=[i for i in range(1,n+1)]


            # 结果的个数
            fc=1
            for i in range(1,n+1):
                fc*=i

            for i in range(fc):
                printfunc(lista)
                a,b=-1,-1  # 从后向前查找的(a,b)升序

                for j in range(n-1,0,-1):
                    if lista[j]>lista[j-1]:
                        a,b=j-1,j
                        break
                # 从b开始找大于lista[a]的最小的位置
                c=-1
                for j in range(b,n):
                    if lista[j]>lista[a]:
                        if c==-1:
                            c=j
                        elif lista[j]<lista[c]:
                            c=j

                temp=lista[c]
                lista[c]=lista[a]
                lista[a]=temp

                lista,listb=lista[:b],lista[b:]
                listb.reverse()
                lista.extend(listb)





if __name__ == "__main__":
   main()
   #  lista=[1,2,3,5,4]
   #  b=3
   #  lista, listb = lista[:b], lista[b:]
   #  listb.reverse()
   #  print(listb)
   #  lista.extend(listb)
   #  print(lista)
