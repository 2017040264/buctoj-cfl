# -*- coding = utf-8 -*-
# @Time : 2021/8/27 9:42
# @Author : 陈凡亮
# @File : ACM penalty time.py
# @Software : PyCharm

def main():
    while True:
        try:
            n=int(input())
            rea=0
            reb=0
            dicta={}
            lista=[]
            for i in range(n):
                a=input().split()
                lista.append(a)

            for i in range(len(lista)):
                if lista[i][1] in dicta.keys():
                    li=dicta.get(lista[i][1])
                else:
                    li=["18:00",0,0] # 第一个表示AC的时间，第二个表示是否AC,第三个表示第几次AC
                if li[1]==1: # 假设AC后再次提交不会罚时
                    continue
                if lista[i][2]=='AC':
                    li[0]=lista[i][0]
                    li[1]=1
                else:
                    li[2]+=1
                dicta[lista[i][1]]=li

            for xx,b in dicta.items():

                if b[1]==1:
                    ta,tb=b[0].split(":")
                    ta=int(ta)
                    tb=int(tb)

                    reb+=tb+b[2]*20
                    if reb>=60:
                        rea+=reb//60
                        reb-=reb//60*60
                    rea+=ta-18



            sa=''
            sb=''
            if reb<10:
                sb='0'+str(reb)
            else:
                sb=str(reb)

            if rea<10:
                sa='0'+str(rea)
            else:
                sa=str(rea)

            print(sa+':'+sb)




        except:
            break


if __name__ == "__main__":
    main()
