# -*- coding = utf-8 -*-
# @Time : 2021/8/27 8:45
# @Author : 陈凡亮
# @File : Basketball game.py
# @Software : PyCharm

def main():
    while True:
        try:
            st= input()
            score=0
            r_number=0
            a_number=0
            s_number=0
            b_number=0
            t_number=0
            shot_number=0
            succ_shot_number=0
            free_number=0
            succ_free_number=0
            temp=0
            for s in st:
                if s=="Y":
                    score += temp
                    if temp==2 or temp==3:
                        succ_shot_number+=1
                    elif temp==1:
                        succ_free_number += 1

                elif s=='N':
                    continue
                elif s=='1':
                    free_number+=1
                    temp=1
                elif s=='2':
                    shot_number+=1
                    temp=2
                elif s=='3':
                    shot_number+=1
                    temp=3
                elif s=='R':
                    r_number+=1
                elif s=='A':
                    a_number+=1
                elif s=='S':
                    s_number+=1
                elif s=='B':
                    b_number+=1
                elif s=='T':
                    t_number+=1

            print(score+r_number+a_number+s_number+b_number-(shot_number-succ_shot_number)-(free_number-succ_free_number)-t_number)

        except:
            break


if __name__ == "__main__":
    main()
